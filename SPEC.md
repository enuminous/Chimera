# CHIMERA Specification v0.1.0

## Name
Correlation-History Identification, Measurement, Encryption, and Record Audit

## Type
EFMW Zoo classifier / sorter

## Input
A description of an observational or record-writing event and any available:
- initial-state specification
- interaction model
- resulting record
- environmental correlations
- claimed recovery procedure
- downstream feedback

## Required output
1. `object`: target whose prior state is at issue
2. `interaction`: event producing the observation/record
3. `records`: accessible persistent records
4. `correlates`: other systems carrying relevant correlation
5. `key`: demonstrated recovery-enabling correlate, or null
6. `recovery_map`: explicit recovery/reconstruction procedure, or null
7. `feedback`: whether the record changes later dynamics
8. `in_principle`: preservation/recoverability claim and assumptions
9. `operational`: demonstrated practical recoverability
10. `tags`: subset of Q/K/R/D/C/U
11. `confidence`: low/medium/high, evidence-based
12. `failure_notes`: unsupported equivalences, missing evidence, or contradictions

## Decision discipline

### Q — correlated/quantum
Use only when the event genuinely invokes quantum states/correlations or a quantum model is explicitly under test.

### K — keyed
Use when reconstruction depends on a separately identifiable correlate and a recovery map can be specified. Do not label a generic environment a "key" merely because information may reside there.

### R — recursive
Use when the produced record causally re-enters later system/environment dynamics.

### D — dispersed
Use when the relevant information has dispersed into uncontrolled degrees of freedom or no operational recovery procedure is demonstrated.

### C — classical record
Use when the central product is an ordinary persistent readable record.

### U — unresolved
Use when available evidence cannot distinguish classes.

## Hard prohibitions
- Do not infer quantum behavior from a cryptographic analogy.
- Do not infer encryption merely from correlation.
- Do not call environmental information a usable key without a recovery map.
- Do not equate theoretical reversibility with feasible reconstruction.
- Do not infer observer-caused physics from ordinary recursive feedback.
- Do not alter the classification criteria to obtain a preferred result.

## Stop rule
After classification, report the tags and evidence. Any claim of deeper physical identity requires an independent model and test outside CHIMERA.
