"""Bounded reference-model adapters, never product or hardware acceptance.

No eval, generated code, shell, compiler or network execution. All parameter
values come from a reviewed plan. These routines are trusted model calculations,
not a universal theorem prover and not executions of the project's C binary.
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction


class ModelError(ValueError):
    pass


def integer(value, name, low=0, high=1000000):
    if type(value) is not int or not low <= value <= high:
        raise ModelError(f"{name}: integer outside [{low}, {high}]")
    return value


def quantity(spec, dimension):
    units = {"bytes": ("bytes", 1), "bytes/s": ("rate", 1),
             "s": ("time", 1), "ms": ("time", Fraction(1, 1000))}
    if not isinstance(spec, dict) or spec.get("unit") not in units:
        raise ModelError("Quantity needs an explicit supported unit")
    dim, scale = units[spec["unit"]]
    value = spec.get("value")
    if dim != dimension or type(value) not in (int, str):
        raise ModelError("Quantity dimension/type mismatch")
    if len(str(value)) > 80:
        raise ModelError("Quantity too large")
    try:
        result = Fraction(value) * scale
    except (ValueError, ZeroDivisionError) as exc:
        raise ModelError("Invalid rational quantity") from exc
    if result < 0 or result > 10**12:
        raise ModelError("Quantity outside model range")
    return result


def result(kind, details, *, counterexample=None, limitations=()):
    return {"execution_status": "COMPLETED", "evidence_kind": kind,
            "details": details, "counterexample": counterexample,
            "limitations": list(limitations), "product_verified": False}


def window_bound(p, budget):
    n = integer(p.get("window"), "window", 1)
    m = integer(p.get("max_sample"), "max_sample", 0, 2**32 - 1)
    bits = integer(p.get("bits"), "bits", 1, 64)
    capacity = (1 << bits) - 1
    final, transient = n * m * m, (n + 1) * m * m
    return result("CONDITIONAL_INTEGER_BOUND", {
        "max_square": m*m, "max_final": final,
        "add_first_max": transient, "capacity": capacity,
        "final_fits": final <= capacity,
        "add_first_fits": transient <= capacity,
        "premise": "valid sum-of-squares state; legal unsigned inputs",
    }, limitations=["Mathematical integer bound only; no compiler correspondence or memory evidence."])


def ring_finite(p, budget):
    n = integer(p.get("window"), "window", 1, 64)
    m = integer(p.get("max_sample"), "max_sample", 0, 4095)
    bits = integer(p.get("bits", 32), "bits", 1, 64)
    mutation = p.get("mutation", "none")
    if mutation not in ("none", "wrong_eviction", "omit_eviction", "old_result", "narrow"):
        raise ModelError("Unsupported ring variant")
    count = (m + 1)**n * n * (m + 1)
    if count > budget:
        return {"execution_status": "BUDGET_LIMIT", "evidence_kind": "NOT_ESTABLISHED",
                "details": {"required_cases": count, "budget": budget},
                "counterexample": None, "limitations": ["Enumeration was not run."],
                "product_verified": False}
    mismatches, witness = 0, None
    for slots in itertools.product(range(m + 1), repeat=n):
        for i in range(n):
            history = slots[i:] + slots[:i]
            total = sum(v*v for v in slots)
            for x in range(m + 1):
                expected_history = history[1:] + (x,)
                expected = sum(v*v for v in expected_history)
                old = slots[(i+1) % n] if mutation == "wrong_eviction" else slots[i]
                updated = total + x*x - (0 if mutation == "omit_eviction" else old*old)
                if mutation == "narrow":
                    updated %= (1 << bits)
                actual_return = total if mutation == "old_result" else updated
                new_slots = list(slots)
                new_slots[i] = x
                new_i = (i+1) % n
                actual_history = tuple(new_slots[new_i:] + new_slots[:new_i])
                if actual_return != expected or updated != expected or actual_history != expected_history:
                    mismatches += 1
                    if witness is None:
                        # i leading zero samples then one full history reaches this encoding.
                        witness = {"prefix_from_reset": [0]*i + list(history),
                                   "input": x, "oldest": i, "slots": list(slots),
                                   "expected": expected, "actual": actual_return}
    return result("FINITE_MODEL_COUNTEREXAMPLE" if mismatches else "FINITE_MODEL_CHECK",
                  {"cases": count, "mismatches": mismatches,
                   "model": "ring-reference-transition/v1", "variant": mutation,
                   "oracle": "chronological shift queue with recomputed sum",
                   "quantifier": "all enumerated model transitions",
                   "domain": {"window": n, "max_sample": m}},
                  counterexample=witness,
                  limitations=["Not an execution or proof of project C; no extrapolation to other domains."])


def queue_values(p):
    return (quantity(p.get("initial"), "bytes"), quantity(p.get("burst"), "bytes"),
            quantity(p.get("rate"), "rate"), quantity(p.get("service"), "rate"),
            quantity(p.get("latency"), "time"), quantity(p.get("capacity"), "bytes"))


def queue_bound(p, budget):
    q0, b, r, mu, t, cap = queue_values(p)
    if cap <= 0 or mu <= 0:
        raise ModelError("Queue capacity and service must be positive")
    if r > mu:
        return result("ENVELOPE_BOUND_UNBOUNDED", {"rate_exceeds_service": True},
                      limitations=["Unbounded eligible horizon and valid arrival/service envelopes assumed."])
    bound = q0 + b + r*t
    return result("CONDITIONAL_QUEUE_BOUND", {
        "bound_bytes": str(bound), "margin_bytes": str(cap-bound),
        "bound_fits": bound <= cap,
        "formula": "q0 + b + r*T, under rate <= service",
        "mixed_rate_latency_derivative_of_margin": "-1",
        "units": "bytes", "horizon": "unbounded model busy period",
    }, limitations=["A bound above capacity is not itself an overflow witness.",
                    "Arrival and service envelopes and initial-state bound are assumed, not measured."])


def queue_witness(p, budget):
    q0, b, r, mu, t, cap = queue_values(p)
    dt = quantity(p.get("tick"), "time")
    if cap <= 0 or mu <= 0 or dt <= 0 or r > mu or t <= 0:
        raise ModelError("Witness needs positive tick/latency/capacity and stable-rate model")
    quantum = r*dt
    if any(x.denominator != 1 for x in (q0, b, quantum)) or quantum > b:
        raise ModelError("This discrete witness needs integral bytes and per-tick batch <= burst")
    steps = math.ceil(t/dt)
    if steps > budget:
        return {"execution_status": "BUDGET_LIMIT", "evidence_kind": "NOT_ESTABLISHED",
                "details": {"required_steps": steps}, "counterexample": None,
                "limitations": ["No trace was evaluated."], "product_verified": False}
    witness = None
    peak = q0+b
    checked = 0
    for k in range(steps):  # Strictly before service latency; no departure is admissible.
        timestamp = k*dt
        if timestamp >= t:
            break
        occupancy = q0+b+k*quantum
        checked += 1
        peak = max(peak, occupancy)
        if occupancy > cap:
            witness = {"initial_bytes": str(q0), "batch_at_zero_bytes": str(b),
                       "bytes_per_tick": str(quantum), "tick_seconds": str(dt),
                       "failure_tick": k, "time_seconds": str(timestamp),
                       "required_bytes": str(occupancy), "capacity_bytes": str(cap),
                       "departures_before_failure": 0}
            break
    return result("MODEL_TRACE_COUNTEREXAMPLE" if witness else "NO_WITNESS_IN_CHECKED_PREFIX",
                  {"checked_instants": checked, "peak_required_bytes": str(peak),
                   "boundary": "batch enqueue after packet assembly"},
                  counterexample=witness,
                  limitations=["Not a physical UART witness without packetization/model correspondence.",
                               "No witness in a prefix does not establish universal safety."])


def zero_failures(p, budget):
    if not isinstance(p.get("estimand"), str) or not p["estimand"]:
        raise ModelError("Statistical estimand required")
    observations = p.get("observations")
    if not isinstance(observations, list) or not observations or len(observations) > budget:
        raise ModelError("Nonempty bounded observations required")
    unique = {}
    for row in observations:
        if not isinstance(row, dict) or not isinstance(row.get("unit_id"), str) or not row["unit_id"]:
            raise ModelError("Missing sampling-unit identity")
        if type(row.get("failed")) is not bool:
            raise ModelError("A trial needs a Boolean failure outcome")
        if row["unit_id"] in unique and unique[row["unit_id"]] != row["failed"]:
            raise ModelError("Conflicting outcomes for one sampling unit")
        unique[row["unit_id"]] = row["failed"]
    protocol = p.get("protocol", {})
    if (protocol.get("design") != "fixed_sample" or protocol.get("units") != "iid_assumed"
            or protocol.get("candidate") != "frozen" or protocol.get("selection") != "unselected"):
        return result("INCONCLUSIVE_SAMPLING_PROTOCOL", {"unique_units": len(unique)},
                      limitations=["No calibrated statistical bound is justified by this protocol."])
    if any(unique.values()):
        return result("UNSUPPORTED_NONZERO_FAILURE_CASE", {"unique_units": len(unique)},
                      limitations=["This adapter implements only the zero-failure formula."])
    alpha = p.get("alpha", "0.05")
    if type(alpha) not in (str, int):
        raise ModelError("alpha must be an exact decimal/rational string")
    try:
        a = Fraction(alpha)
    except (ValueError, ZeroDivisionError) as exc:
        raise ModelError("Invalid alpha") from exc
    if not 0 < a < 1:
        raise ModelError("alpha must be between zero and one")
    n = len(unique)
    upper = -math.expm1(math.log(float(a))/n)
    return result("CONDITIONAL_STATISTICAL_BOUND", {
        "unique_units": n, "rows": len(observations),
        "duplicate_rows_not_counted": len(observations)-n,
        "failures": 0, "one_sided_error_probability": str(a),
        "upper_failure_probability_float": upper,
        "formula": "1 - alpha**(1/n)",
        "estimand": p.get("estimand", "UNSPECIFIED"),
    }, limitations=["Floating evaluation of fixed-sample formula, conditional on iid units and frozen selection.",
                    "Declared independence and deployment representativeness are not verified by this calculation."])


ADAPTERS = {
    "window_integer_bound/v1": window_bound,
    "ring_finite/v1": ring_finite,
    "queue_envelope/v1": queue_bound,
    "queue_trace/v1": queue_witness,
    "zero_failures/v1": zero_failures,
}


def evaluate(method, parameters, budget):
    integer(budget, "max_cases", 1, 1000000)
    if method not in ADAPTERS:
        return {"execution_status": "UNSUPPORTED", "evidence_kind": "NOT_ESTABLISHED",
                "details": {"method": method}, "counterexample": None,
                "limitations": ["No registered adapter; no code was evaluated."],
                "product_verified": False}
    if not isinstance(parameters, dict):
        raise ModelError("Model parameters must be a mapping")
    try:
        return ADAPTERS[method](parameters, budget)
    except ModelError:
        raise
    except (KeyError, TypeError, ValueError, OverflowError, ZeroDivisionError) as exc:
        raise ModelError(f"Invalid {method} model: {exc}") from exc
