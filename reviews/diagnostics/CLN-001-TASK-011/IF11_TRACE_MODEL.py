#!/usr/bin/env python3
"""CLN-001 IF11: bounded original models, never a physical qualification.

No file I/O, networking, subprocesses, random source, or external provider.
Oracle histories and all Python integers are unbounded TEST instrumentation.
S = ordered synchronous consumer with explicitly retained exact rank context.
X = explicit canonical binary (sequence, ordinal) frames from a hypothetical
    association owner. Neither owner nor persistence/transport is authorized.
C uses a hypothetical pinned pre-event snapshot ONLY when provider=True.
"""

import itertools
import json
import sys


ASSUMPTIONS = {
    "S": ["single outstanding acceptance; publisher coordination assumed",
          "ordered reliable success/rejection and drain-before-reset marker",
          "consumer retains exact rank/reset context across modeled restart"],
    "X": ["hypothetical exact sequence/accepted-ordinal owner",
          "canonical binary framing and event-bound immutable response",
          "ordered exact reset-completion frames; old numeric commits fenced before reset",
          "lossless retained debt; restart preserves received-event dedup state"],
    "C": ["provider=True explicitly supplies pinned correct-event pre-tail",
          "provider=False supplies nothing; no real C-HIST/RN is present"],
    "scope": ["finite enumerations, no random seed",
              "Python arbitrary precision/list storage is not bounded MCU RAM",
              "no universal crash survival, deadline, fairness or availability"],
}


class Spec:
    """Independent oracle: full accepted histories, not a candidate tail.

    Labels are private specification instrumentation. They are NEVER injected
    into S's consumer. X must produce its own explicit wire representation.
    """

    def __init__(self):
        self.sequence = 0
        self.histories = [[]]
        self.attempts = {}
        self.events = {}
        self.resetting = False

    def step(self, action):
        op, *args = action
        if op == "attempt":
            handle, value = args
            self.attempts[handle] = value
        elif op == "accept":
            handle, = args
            value = self.attempts[handle]
            if self.resetting or not 0 <= value <= 4095:
                raise ValueError("illegal oracle acceptance")
            history = self.histories[self.sequence]
            history.append(value)
            self.events[handle] = {
                "result": (self.sequence, len(history),
                           sum(v * v for v in history[-32:])),
                "phase": "accepted",
            }
        elif op == "reject":
            if 0 <= self.attempts[args[0]] <= 4095:
                raise ValueError("valid input cannot be silently rejected")
        elif op in ("commit", "publish", "receive"):
            handle, = args
            before, after = {"commit": ("accepted", "committed"),
                             "publish": ("committed", "published"),
                             "receive": ("published", "received")}[op]
            if self.events[handle]["phase"] != before:
                raise ValueError("illegal result lifecycle")
            self.events[handle]["phase"] = after
            if op == "receive":
                return self.events[handle]["result"]
        elif op == "reset_start":
            if self.resetting:
                raise ValueError("nested reset")
            self.resetting = True
        elif op == "reset_complete":
            if not self.resetting:
                raise ValueError("no reset start")
            self.sequence += 1
            self.histories.append([])
            self.resetting = False
        elif op == "retry":
            # Bound retry refers to the original event, never another accept.
            return self.events[args[0]]["result"]
        elif op != "restart":
            raise ValueError(op)
        return None


class Numeric:
    """Candidate numeric states, deliberately unlike full-stream Spec."""

    def __init__(self, kind, provider=False):
        self.kind = kind
        self.provider = provider and kind == "C"
        self.tail = [0] * 31 if kind != "C" else None
        self.total = 0
        # Explicit hypothetical upstream-owned TEST service, not C-DET state.
        self.upstream_tail = [0] * 31 if self.provider else None

    def accept(self, value):
        if self.kind == "C":
            snapshot = tuple(self.upstream_tail) if self.provider else None
            if self.provider:
                self.upstream_tail = self.upstream_tail[1:] + [value]
            return value, snapshot
        if self.kind == "A":
            return value, tuple(self.tail)
        q = value * value
        return self.total + q, q, self.tail[0]

    def commit(self, context):
        if self.kind == "B":
            energy, q, oldest = context
            self.total = energy - oldest
            self.tail = self.tail[1:] + [q]
            return energy
        value, snapshot = context
        if snapshot is None:
            return None
        acc = value * value
        for term in snapshot:
            acc += term * term
        if self.kind == "A":
            self.tail = list(snapshot[1:]) + [value]
        return acc

    def reset(self):
        self.__init__(self.kind, self.provider)


def bits(value):
    return format(value, "b")


def parse_bits(word):
    if not word or any(c not in "01" for c in word):
        raise ValueError("malformed binary")
    if len(word) > 1 and word[0] == "0":
        raise ValueError("noncanonical binary")
    return int(word, 2)


class OrderedConsumer:
    """S-visible data: success(E), reject, ordered reset marker, restart.

    No handle, oracle rank, publisher attempt count, or oracle sequence enters
    the decoder. sequence/rank are consumer-owned exact Python integers.
    """

    def __init__(self, retain=True):
        self.sequence = 0
        self.rank = 0
        self.retain = retain

    def receive(self, energy):
        self.rank += 1
        return self.sequence, self.rank, energy

    def marker(self):
        self.sequence += 1
        self.rank = 0

    def restart(self):
        if not self.retain:
            self.sequence = self.rank = 0


class TaggedConsumer:
    """X-visible frame alone supplies sequence/rank. seen is retained state.

    Frame boundaries are a hypothetical transport capability. Exactly-once
    logical receipt is modeled by seen; this is not exactly-once transport.
    """

    def __init__(self):
        self.seen = set()
        self.latest_sequence = 0

    def marker(self, sequence_word):
        sequence = parse_bits(sequence_word)
        if sequence != self.latest_sequence + 1:
            raise ValueError("reset marker gap/order fault")
        self.latest_sequence = sequence

    def receive(self, frame):
        seq, rank, energy = frame
        result = parse_bits(seq), parse_bits(rank), energy
        if result[1] < 1:
            raise ValueError("rank must be positive")
        if result[0] > self.latest_sequence:
            raise ValueError("result precedes its reset marker")
        identity = result[:2]
        if identity in self.seen:
            return None
        self.seen.add(identity)
        return result


class Candidate:
    """Prospective acceptance staging, distinct commit/pub/receipt events.

    S reset requires old received debt drained. X retains old contexts/frames
    through reset and may deliver old/new in either order. attempts includes
    publisher-owned test staging, not a claimed constant detector allocation.
    """

    def __init__(self, kind, contract, provider=False, retain=True):
        self.numeric = Numeric(kind, provider)
        self.contract = contract
        self.sequence = 0 if contract == "X" else None
        self.rank = 0 if contract == "X" else None
        self.attempts = {}
        self.pending = {}
        self.frames = {}
        self.received = set()
        self.consumer = (OrderedConsumer(retain) if contract == "S"
                         else TaggedConsumer())

    def step(self, action):
        op, *args = action
        if op == "attempt":
            self.attempts[args[0]] = args[1]
        elif op == "accept":
            handle, = args
            value = self.attempts[handle]
            if not 0 <= value <= 4095:
                raise ValueError("invalid acceptance")
            if self.contract == "S" and len(self.pending) != len(self.received):
                raise ValueError("S rendezvous not available")
            if self.contract == "X":
                self.rank += 1
            self.pending[handle] = (self.sequence, self.rank,
                                    self.numeric.accept(value))
        elif op == "commit":
            handle, = args
            seq, rank, context = self.pending[handle]
            energy = self.numeric.commit(context)
            self.frames[handle] = ((bits(seq), bits(rank), energy)
                                   if self.contract == "X" else energy)
        elif op == "receive":
            handle, = args
            frame = self.frames[handle]
            energy = frame[2] if self.contract == "X" else frame
            if energy is None:
                return None  # service fault, NO receipt and NO debt discharge
            self.received.add(handle)
            return self.consumer.receive(frame)
        elif op == "reset_complete":
            if self.contract == "S":
                if len(self.pending) != len(self.received):
                    raise ValueError("S reset not drained")
                self.consumer.marker()
            self.numeric.reset()
            if self.contract == "X":
                self.sequence += 1
                self.rank = 0
                self.consumer.marker(bits(self.sequence))
        elif op == "restart" and self.contract == "S":
            self.consumer.restart()
        elif op == "retry":
            handle, = args
            return self.frames[handle]
        # reject/publish/reset_start carry ordering but no numeric mutation.
        return None


def lifecycle(handle, value):
    return [("attempt", handle, value), ("accept", handle),
            ("commit", handle), ("publish", handle), ("receive", handle)]


def replay(actions, kind, contract, provider=False, retain=True):
    oracle = Spec()
    candidate = Candidate(kind, contract, provider, retain)
    expected, observed = [], []
    for action in actions:
        wanted = oracle.step(action)
        got = candidate.step(action)
        if action[0] == "receive":
            expected.append(wanted)
            observed.append(got)
    debts = sum(e["phase"] != "received" for e in oracle.events.values())
    debts += sum(wanted != got for wanted, got in zip(expected, observed))
    return expected, observed, debts


def shuffles(left, right):
    if not left:
        yield right
    elif not right:
        yield left
    else:
        for rest in shuffles(left[1:], right):
            yield left[:1] + rest
        for rest in shuffles(left, right[1:]):
            yield right[:1] + rest


class Suite:
    def __init__(self):
        self.groups = {}
        self.failures = []
        self.witnesses = {}

    def check(self, group, expected, observed):
        row = self.groups.setdefault(group, {"cases": 0, "discrepancies": 0})
        row["cases"] += 1
        if expected != observed:
            row["discrepancies"] += 1
            self.failures.append({"group": group, "expected": expected,
                                  "observed": observed})

    def witness(self, name, data):
        self.witnesses[name] = data


def run():
    s = Suite()
    for kind in ("A", "B", "C"):
        for contract in ("S", "X"):
            for bad in (-1, 4096, 65536):
                candidate = Candidate(kind, contract, provider=kind == "C")
                for action in lifecycle("valid", 1):
                    candidate.step(action)
                def sequence_state():
                    return repr((candidate.numeric.__dict__, candidate.sequence,
                                 candidate.rank, candidate.pending, candidate.frames,
                                 candidate.received, candidate.consumer.__dict__))
                before = sequence_state()
                candidate.step(("attempt", "invalid", bad))
                candidate.step(("reject", "invalid"))
                s.check("G01_rejection_state_invariance", before, sequence_state())
    # G01: real decoders exercised, invalid attempts between valid accepts;
    # reject cannot increment consumer or provider accepted rank.
    for values in itertools.product((0, 1, 4095), repeat=4):
        for bad in (-1, 4096, 65536):
            actions = []
            for i, value in enumerate(values):
                actions += lifecycle("v" + str(i), value)
                actions += [("attempt", "bad" + str(i), bad),
                            ("reject", "bad" + str(i))]
            for kind in ("A", "B", "C"):
                for contract in ("S", "X"):
                    e, o, debt = replay(actions, kind, contract, kind == "C")
                    s.check("G01_valid_invalid_decoders", (e, 0), (o, debt))

    # G02: tail expiry, boundary values and multiple explicit resets;
    # commits are independently recomputed by the full-history oracle.
    for values in ([1] * 65, [4095] * 65, [4095] + [0] * 65,
                   list(range(70)), [0, 4095] * 33):
        actions = []
        for i, value in enumerate(values):
            if i in (31, 33):
                actions += [("reset_start",), ("reset_complete",)]
            actions += lifecycle(str(i), value)
        for kind in ("A", "B", "C"):
            for contract in ("S", "X"):
                e, o, debt = replay(actions, kind, contract, kind == "C")
                s.check("G02_numeric_reset_controls", (e, 0), (o, debt))
    # Separate uninterrupted boundary crossing, not hidden by the resets above.
    for kind in ("A", "B", "C"):
        actions = sum((lifecycle(str(i), 4095 if i == 0 else 0)
                       for i in range(66)), [])
        e, o, debt = replay(actions, kind, "X", kind == "C")
        s.check("G02_numeric_reset_controls", (e, 0), (o, debt))

    # G03: X old/new debt across reset, delayed receipt, every restart cut.
    # Old numeric commit precedes reset here, publication need not do so.
    schedules = 0
    for old, new in itertools.product((0, 1, 2), repeat=2):
        left = lifecycle("old", old)
        right = [("reset_start",), ("reset_complete",)] + lifecycle("new", new)
        for actions in shuffles(left, right):
            if actions.index(("commit", "old")) > actions.index(("reset_start",)):
                continue
            schedules += 1
            for cut in range(len(actions) + 1):
                trace = actions[:cut] + [("restart",)] + actions[cut:]
                for kind in ("A", "B", "C"):
                    e, o, debt = replay(trace, kind, "X", kind == "C")
                    s.check("G03_X_lifecycle_schedules", (e, 0), (o, debt))
    s.witness("schedule_domain", {"base_schedules": schedules,
                                 "restart_positions_per_schedule": 13})

    # G04: S drain/reset marker is sufficient without a separate reset ACK,
    # under S's proposed coordination and retained consumer context.
    actions = lifecycle("old", 1) + [("reset_start",), ("reset_complete",)]
    actions += lifecycle("new", 1)
    for cut in range(len(actions) + 1):
        for kind in ("A", "B", "C"):
            trace = actions[:cut] + [("restart",)] + actions[cut:]
            e, o, debt = replay(trace, kind, "S", kind == "C")
            s.check("G04_S_drained_no_ACK", (e, 0), (o, debt))

    # G05: counterexample at the actual energy-only restarted boundary.
    observations, needs = [], []
    for prefix in (0, 1):
        actions = lifecycle("hidden", 0) if prefix else []
        actions += [("restart",)] + lifecycle("visible", 0)
        e, o, _ = replay(actions, "A", "S", retain=False)
        observations.append(o[-1][2])
        needs.append(e[-1][1])
    s.check("G05_restart_ambiguity_negative", (True, True),
            (observations[0] == observations[1], needs[0] != needs[1]))
    s.witness("restart_energy_only", {"consumer_view": ["restart", ["success", 0]],
                                      "required_ranks": needs,
                                      "lost_context_decoder_ranks": [1, 1]})
    for retain in (True, False):
        trace = lifecycle("one", 0) + [("restart",)] + lifecycle("two", 0)
        e, o, _ = replay(trace, "A", "S", retain=retain)
        s.check("G05_restart_retention_control", retain, e == o)

    # G06: old/new equal index AND energy, acknowledgment has no binding.
    # Same ACK and payload view permits two publication orders; labels below
    # belong only to the oracle. X's fields or S's drain remove ambiguity.
    for acknowledgment in (False, True):
        views, required = [], []
        for order in (("old", "new"), ("new", "old")):
            oracle = Spec()
            trace = lifecycle("old", 1)[:3]
            trace += [("reset_start",), ("reset_complete",)]
            trace += lifecycle("new", 1)[:3]
            trace += sum(([('publish', h), ('receive', h)] for h in order), [])
            view, results = [], []
            for action in trace:
                result = oracle.step(action)
                if action[0] == "reset_complete" and acknowledgment:
                    view.append("ACK")
                if action[0] == "receive":
                    view.append(list(result[1:]))
                    results.append(result)
            views.append(view)
            required.append(results)
        s.check("G06_ACK_only_negative", (True, True),
                (required[0] != required[1], views[0] == views[1]))
    for old_first in (False, True):
        c = TaggedConsumer()
        c.marker(bits(1))
        frames = [(bits(0), bits(1), 1), (bits(1), bits(1), 1)]
        if not old_first:
            frames.reverse()
        s.check("G06_explicit_sequence_positive", [(parse_bits(a), parse_bits(b), e)
                for a, b, e in frames], [c.receive(frame) for frame in frames])
    s.witness("equal_old_new", {"n_E": [1, 1], "sequences": [0, 1],
                                "ACK_alone_resolves": False})

    # G07: finite tags alias if reused with old response live. Retirement can
    # bound live tags, but cannot supply arbitrary rank or force valid pauses.
    for modulus in (1, 2, 4, 8):
        old = (0, 1, 0)
        new = (modulus, 1, 0)
        wire = lambda r: (r[0] % modulus, r[1], r[2])
        s.check("G07_tag_reuse_negative", (True, True),
                (wire(old) == wire(new), old != new))
        live = set()
        safe = True
        for seq in range(3 * modulus + 1):
            tag = seq % modulus
            safe = safe and tag not in live
            live.add(tag)
            live.remove(tag)  # assumed proven no buffered/retry copy remains
        s.check("G07_retirement_positive", True, safe and not live)

    # G08: slot-model capacity falsifier. Accepted, committed but unpublished
    # results occupy one indivisible slot each; no replay/compression/other
    # memory, output channel or coordinated admission allowed in the negative.
    for capacity in range(1, 9):
        oracle = Spec()
        queue = []
        overflow = 0
        for i in range(capacity + 1):
            for action in lifecycle(str(i), i + 1)[:3]:
                oracle.step(action)
            if len(queue) < capacity:
                queue.append(str(i))
            else:
                overflow += 1
        owed = sum(e["phase"] != "received" for e in oracle.events.values())
        s.check("G08_Q_plus_1_negative", (capacity + 1, capacity, 1),
                (owed, len(queue), overflow))
        # Positive storage control supplies a distinct (Q+1)th slot, honestly.
        extra_store = queue + [str(capacity)]
        s.check("G08_extra_storage_positive", owed, len(extra_store))
        # Positive coordination control is a different prospective schedule:
        # every result is received before the next publisher attempt.
        trace = sum((lifecycle(str(i), i + 1) for i in range(capacity + 1)), [])
        e, o, debt = replay(trace, "A", "S")
        s.check("G08_rendezvous_positive", (e, 0), (o, debt))
    s.witness("Q2_capacity", {"accepted_unpublished": 3, "retained_slots": 2,
                              "missing_slots": 1, "assumption": "entry_only"})

    # G09: retry is either a reference to an original event, or a NEW accept.
    for value in (0, 1, 2, 4095):
        oracle = Spec()
        candidate = Candidate("B", "X")
        for action in lifecycle("original", value):
            oracle.step(action)
            candidate.step(action)
        reference = oracle.step(("retry", "original"))
        frame = candidate.step(("retry", "original"))
        s.check("G09_bound_retry_positive", reference,
                (parse_bits(frame[0]), parse_bits(frame[1]), frame[2]))
        s.check("G09_duplicate_frame_dedup", None, candidate.consumer.receive(frame))
        trace = lifecycle("original", value) + lifecycle("fresh_retry", value)
        e, o, _ = replay(trace, "B", "X")
        s.check("G09_new_accept_is_not_recovery", (2, True),
                (len(e), e[0][:2] != e[1][:2]))
        s.check("G09_new_accept_numeric_control", e, o)
    s.witness("retry_value_1", {"original": [0, 1, 1],
                                "fresh_accept": [0, 2, 2],
                                "bound_retry": [0, 1, 1]})

    # G10: provider absence never converted to a zero or valid result.
    for kind in ("A", "B", "C"):
        for available in (False, True):
            actions = lifecycle("a", 1) + lifecycle("b", 2)
            e, o, debt = replay(actions, kind, "X", provider=available)
            s.check("G10_provider_availability", kind != "C" or available, e == o)
            if kind == "C" and not available:
                s.check("G10_C_absence_retains_unmet_obligation", [None, None],
                        o)
                s.check("G10_C_absence_debt_count", 2, debt)
    s.witness("provider_matrix", {"A": [True, True], "B": [True, True],
                                  "C": [False, True],
                                  "availability_columns": [False, True]})

    # G11: coherent WRONG-event snapshot; range validation cannot fix it.
    correct_pre = [0] * 30 + [1]
    wrong_post = [0] * 29 + [1, 2]
    n = Numeric("C", provider=True)
    good = n.commit((2, tuple(correct_pre)))
    bad = n.commit((2, tuple(wrong_post)))
    s.check("G11_snapshot_event_binding_negative", (5, 9, True),
            (good, bad, all(0 <= x <= 4095 for x in wrong_post)))
    s.witness("coherent_wrong_event", {"correct": good, "wrong": bad})

    # G12: growing representations, not a proof of arbitrary rank. Values well
    # beyond machine words check the decoder has no accidental finite wrap.
    for power in (1, 8, 16, 32, 64, 127, 256):
        rank = (1 << power) + 1
        consumer = TaggedConsumer()
        got = consumer.receive((bits(0), bits(rank), 0))
        s.check("G12_large_rank_representation", ((0, rank, 0), power + 1),
                (got, len(bits(rank))))
    for word in ("", "01", "2", "1x"):
        rejected = False
        try:
            parse_bits(word)
        except ValueError:
            rejected = True
        s.check("G12_malformed_binary", True, rejected)

    # G13: one reset-independent current tail cannot preserve older debts.
    tails, first_debts = [], []
    for first in (1, 2):
        num = Numeric("A")
        first_debts.append(num.commit(num.accept(first)))
        for _ in range(32):
            last = num.commit(num.accept(0))
        tails.append((tuple(num.tail), last))
    s.check("G13_numeric_tail_not_debt", (True, [1, 4]),
            (tails[0] == tails[1], first_debts))

    # G14: distinct old debts at the SAME accepted length, numeric tail and
    # latest energy. Each block is (1 or 2), then 32 zeros, all unpublished.
    # The finite enumeration illustrates, but does not prove, the general
    # 2**m distinguishability argument stated in the dossier.
    for blocks in range(1, 6):
        final_numeric = set()
        debt_transcripts = set()
        for choices in itertools.product((1, 2), repeat=blocks):
            oracle = Spec()
            numeric = Numeric("A")
            outputs = []
            agreed = True
            for block, value in enumerate(choices):
                for offset, sample in enumerate([value] + [0] * 32):
                    handle = str(block * 33 + offset)
                    oracle.step(("attempt", handle, sample))
                    oracle.step(("accept", handle))
                    energy = numeric.commit(numeric.accept(sample))
                    oracle.step(("commit", handle))
                    agreed = agreed and energy == oracle.events[handle]["result"][2]
                    outputs.append(energy)
            s.check("G14_debt_family_numeric_control", True, agreed)
            final_numeric.add((tuple(numeric.tail), outputs[-1]))
            debt_transcripts.add(tuple(outputs))
        s.check("G14_debt_family_distinctions", (1, 1 << blocks),
                (len(final_numeric), len(debt_transcripts)))
    s.witness("debt_family", {"blocks_tested": [1, 2, 3, 4, 5],
                               "distinct_debt_transcripts": [2, 4, 8, 16, 32],
                               "numeric_final_states_per_length": 1})

    summary = {
        "study_id": "CLN-001-IF11",
        "seed": None,
        "assumptions": ASSUMPTIONS,
        "groups": s.groups,
        "total_cases": sum(g["cases"] for g in s.groups.values()),
        "discrepancies": len(s.failures),
        "failures": s.failures,
        "witnesses": s.witnesses,
        "AP_selected": False,
        "full_H1_H6_PASS": False,
        "physical_qualification": False,
    }
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    return 1 if s.failures else 0


if __name__ == "__main__":
    sys.exit(run())
