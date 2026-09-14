# Commercial Frontend — Tradie Wedge Comparison Scorecard

**Date:** 2026-09-14 Brisbane  
**Status:** DIRECT-EVIDENCE INTERPRETATION CONTRACT / NO WINNER YET

## Purpose
Compare the two current Tradie AI Operations wedges using only direct participant or observed-workflow evidence. This scorecard must not choose a commercial winner from public documentation, synthetic fixtures, portfolio examples or guessed economics.

## Wedges
**T1 — Xero-paid invoice administrative closure**  
`Xero payment sync -> ServiceM8 paid state -> context assembly -> missing closure action -> human approval -> future bounded customer communication -> verification`

**T2 — invoice approval / accounting-sync exception closure**  
`completed job -> invoice awaiting approval or accounting-sync exception -> context assembly -> human decision -> future bounded correction -> reread/verification`

## Evidence rule
Each scorecard row must be supported by a real participant interview, direct workflow observation or equivalent primary operator evidence. Unsupported fields remain `UNKNOWN`.

## Per-participant capture
For both T1 and T2 capture:
- participant/business identifier that is safe to retain;
- role performing the work;
- systems actually used;
- cases/week or month;
- percentage requiring manual intervention;
- minutes/case;
- number of handoffs/people involved;
- failure/rework/complaint consequence;
- whether customer communication is involved;
- whether money/accounting state is involved;
- current workaround;
- approval owner;
- measurable desired outcome;
- willingness to trial;
- stated willingness to pay, if volunteered or directly asked;
- integration constraints/permissions;
- confidence and evidence notes.

## Comparison dimensions

| Dimension | T1 | T2 | Rule |
|---|---|---|---|
| Direct participants reporting the problem | UNKNOWN | UNKNOWN | Count only direct evidence |
| Median/typical frequency | UNKNOWN | UNKNOWN | No platform-doc inference |
| Manual intervention rate | UNKNOWN | UNKNOWN | Participant supplied/observed only |
| Minutes per case | UNKNOWN | UNKNOWN | Direct value only |
| Estimated admin burden | UNKNOWN | UNKNOWN | Derived only when inputs are direct and complete |
| Consequence severity | UNKNOWN | UNKNOWN | Record observed/reported consequence, not imagined risk |
| Systems crossed | ServiceM8 + Xero + possible communication | ServiceM8 + accounting + exception resolution | Platform evidence may define feasibility, not demand score |
| Approval boundary clarity | customer communication requires approval-first by default | accounting/corrective action requires explicit approval | Product-policy evidence, not WTP evidence |
| Read-path feasibility | PARTIAL/VERIFIED | PARTIAL/VERIFIED | Technical evidence only |
| Write-path certainty | UNKNOWN/BLOCKED | UNKNOWN/BLOCKED | No production mutation authority |
| Measurable outcome | one closure case resolved without duplicate/ambiguity | one approval/sync exception resolved and verified | Must be validated with operators |
| Trial intent | UNKNOWN | UNKNOWN | Direct evidence only |
| Stated WTP | UNKNOWN | UNKNOWN | Never inferred from time savings |

## Selection rule
A wedge can be called the **leading prototype candidate** only when:
1. at least 3 independent direct participants/observations describe materially similar pain for that wedge;
2. frequency and manual effort are sufficiently evidenced to calculate a non-synthetic burden for those participants;
3. the approval boundary is understandable to those participants;
4. the read/integration path remains technically feasible;
5. at least one measurable outcome is accepted by participants;
6. there is repeated trial intent.

No synthetic weighting formula may override these gates.

## Tie-break rule
If both wedges meet the prototype threshold, prefer the one with the stronger combination of:
- higher repeated direct frequency;
- larger directly evidenced manual burden;
- clearer measurable outcome;
- lower authority/write complexity;
- fewer systems/identities required to resolve a case;
- stronger repeated trial intent;
- clearer stated WTP signal.

The tie-break is comparative, not a fixed numeric score. If evidence is mixed, label `NO CLEAR WINNER` and continue direct validation.

## Stop rules
- If a wedge is reported by fewer than 3 materially similar direct cases after a reasonable sample, do not broaden it into a generic assistant to rescue the hypothesis.
- If manual burden is trivial or already handled satisfactorily by incumbent workflows, downgrade the wedge.
- If write/authority boundaries are disproportionate to the value, prefer a read/prepare/approval-only MVP or move to the other wedge.
- Public reviews, vendor pages, synthetic fixtures and internal portfolio experience remain supporting context only.

## Current disposition
- T1: `HYPOTHESIS / DIRECT DEMAND UNKNOWN`
- T2: `HYPOTHESIS / DIRECT DEMAND UNKNOWN`
- Winner: `NONE — DIRECT EVIDENCE REQUIRED`

This report does not duplicate PR #50's Tradie value-threshold calculator. PR #50 owns interpretation utility implementation; this report only defines direct-evidence comparison and selection semantics.
