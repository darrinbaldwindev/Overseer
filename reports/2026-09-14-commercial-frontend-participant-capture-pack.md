# Commercial Frontend — Participant Validation Capture Pack

**Date:** 2026-09-14  
**Purpose:** make direct customer/observed-workflow evidence collection consistent across Tradie and Ecommerce candidates.  
**Target:** minimum 10 relevant conversations/observations before production-build recommendation; 3 materially similar independent cases may justify a read-only/non-production prototype step if all hard gates pass.

## Evidence rule

One completed sheet = one participant or one directly observed real workflow. Public posts, vendor documentation and portfolio fixtures do not count as direct participant sheets.

Do not infer missing numbers. Record `UNKNOWN` when the participant cannot support an estimate.

---

# PARTICIPANT SHEET

## A. Identity / context

- Participant ID:
- Date:
- Role: owner/operator / admin / finance-bookkeeper / ecommerce ops / support / other
- Business type:
- Approximate team size:
- Technical confidence: low / medium / high
- Workflow tested: Tradie post-payment closure / Ecommerce supplier-fulfilment exception / other
- Systems actually used:

## B. Last real occurrence

- Describe the most recent real case:
- Starting system:
- Other systems opened:
- What had to be copied, checked, re-entered, messaged or waited for:
- People involved:
- What signalled the case was actually finished:

## C. Frequency

- Normal cases/week or month:
- Exception percentage if relevant:
- Seasonal variation:
- Confidence in estimate: low / medium / high

## D. Time / cost / friction

- Active minutes per case:
- Waiting time per case:
- Context switches:
- Paid staff/contractor cost directly attributable, if known:
- Rework frequency, if known:
- Cash-collection / fulfilment / customer-response delay, if known:

## E. Failure consequence

Check only if participant has experienced or directly observed it:
- [ ] customer complaint
- [ ] delayed payment
- [ ] refund
- [ ] rework
- [ ] staff interruption
- [ ] wrong accounting state
- [ ] wrong fulfilment state
- [ ] missed delivery/customer promise
- [ ] trust/compliance concern
- [ ] other:

Example and consequence:

## F. Current workaround

- Current apps/automation:
- What incumbent handles well:
- Where workflow becomes manual:
- Workarounds already tried:
- Why those did not fully solve it:

## G. Authority boundary

For each action mark `AUTO_OK`, `APPROVAL_REQUIRED`, `NEVER_AUTO`, or `UNKNOWN`.

| Action | Boundary | Evidence/notes |
|---|---|---|
| Read relevant records | | |
| Match identity across systems | | |
| Draft customer communication | | |
| Send customer communication | | |
| Hold fulfilment | | |
| Release fulfilment | | |
| Update tracking | | |
| Mark job/order closed | | |
| Apply/refund/reverse money | | |
| Correct customer/accounting data | | |

## H. Trust / verification

- What evidence would make approval comfortable?
- Is an audit trail required? yes / no / unsure
- What must be re-read after action?
- What single failure would cause immediate loss of trust?

## I. Trial intent

- Would participant trial the exact workflow on real non-critical cases? yes / no / conditional
- Conditions:
- Acceptable setup burden:
- Required systems/connectors:
- Would they permit read-only first? yes / no
- Would they permit bounded writes with approval? yes / no / conditional

## J. Willingness to pay

Ask only after workflow/value discussion.

- Is money or paid staff time already spent on this problem? amount/UNKNOWN
- Expected packaging: included in current software / small add-on / separate product / usage-based / unsure
- What outcome would justify payment?
- Price range considered reasonable after value framing:
- Price objection:
- Credibility of WTP signal: none / weak / moderate / strong

---

# SCORING

Score 0–3 with one sentence of evidence for every non-zero score.

| Dimension | 0 | 1 | 2 | 3 | Score | Evidence |
|---|---|---|---|---|---:|---|
| Frequency | rare/none | occasional | regular | frequent/core | | |
| Cost/friction | trivial | noticeable | material | high | | |
| Failure impact | low | mild | material | severe | | |
| Cross-system coordination | none | limited | repeated | substantial | | |
| Integration feasibility | blocked | unclear | partial | clear | | |
| Authority safety | unsafe | ambiguous | bounded with approvals | clearly bounded | | |
| Verification feasibility | weak | partial | good | strong deterministic re-read | | |
| Trial intent | none | vague | conditional | explicit | | |
| WTP | none/unknown | weak | credible | repeated/strong | | |
| Acquisition reachability | unclear | difficult | reachable | obvious channel | | |

## Hard blockers

Any `YES` keeps the candidate from production-build recommendation regardless of score:
- [ ] identity matching unresolved
- [ ] required integration unavailable
- [ ] required write scope/permission unknown
- [ ] consequential action lacks safe approval rule
- [ ] no reliable verification re-read
- [ ] direct demand evidence insufficient
- [ ] relevant AgentOS interaction/governance primitive not proven
- [ ] critical security/privacy unknown

## Participant-level result

- Supports workflow hypothesis: yes / no / mixed
- Counts toward 3-case prototype threshold: yes / no
- Counts toward 10-case production evidence set: yes / no
- Follow-up evidence required:

---

# AGGREGATE DASHBOARD TEMPLATE

| ID | Segment | Workflow | Frequency | Min/case | Failure impact | Trial | WTP | Hard blocker | Counts to prototype |
|---|---|---|---:|---:|---|---|---|---|---|
| P01 | | | | | | | | | |
| P02 | | | | | | | | | |
| P03 | | | | | | | | | |
| P04 | | | | | | | | | |
| P05 | | | | | | | | | |
| P06 | | | | | | | | | |
| P07 | | | | | | | | | |
| P08 | | | | | | | | | |
| P09 | | | | | | | | | |
| P10 | | | | | | | | | |

## Gate calculation

### Read-only prototype may be recommended only when
- at least 3 independent materially similar direct cases;
- pain occurs often enough to matter;
- incumbent gap is real;
- read path is feasible;
- approval boundary is explicit;
- measurable outcome exists;
- no hard blocker above vetoes the step.

### Production build may be recommended only when
- evidence set reaches approximately 10 relevant cases or equivalent observed workflows;
- repeated trial interest is present;
- several credible WTP signals are present;
- exact required permissions/write actions are understood;
- fail-closed and verification behavior is specified;
- relevant AgentOS Wave-0 primitives are proven;
- no critical authority/security unknown remains.
