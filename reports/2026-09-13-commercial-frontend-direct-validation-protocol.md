# Commercial Frontend Direct Validation Protocol — 2026-09-13

**Purpose:** Convert the remaining UNKNOWN commercial evidence in Issues #20/#21 into a repeatable validation process without fabricating customer proof or starting production implementation.

## Scope

Priority workflows:

1. **Tradie AI Operations — post-payment / exception administrative closure**
2. **Ecommerce AI Operations — supplier / fulfilment exception handling**

Property Maintenance remains out of scope until authoritative integration evidence is established.

## Validation rule

A workflow does not pass the Commercial Frontend Build Gate because it sounds useful or is technically possible.

It must demonstrate:
- repeated real occurrence;
- measurable friction/cost/risk;
- cross-system coordination that is not already adequately solved;
- feasible read/write boundaries;
- a safe approval model;
- a measurable outcome;
- willingness to trial and, separately, willingness to pay.

## Evidence classes

Record every finding as one of:

- **VERIFIED CUSTOMER EVIDENCE** — direct statement or observed workflow from an identified participant.
- **VERIFIED PLATFORM EVIDENCE** — authoritative current product/API documentation.
- **PORTFOLIO EVIDENCE** — current repository/test/runtime evidence.
- **INFERENCE** — reasoned interpretation of evidence.
- **HYPOTHESIS** — unproven proposition requiring testing.
- **UNKNOWN** — not evidenced.

Do not silently promote inference or public research to customer proof.

## Minimum sample before implementation recommendation

Target at least **10 relevant operator/business conversations or equivalent observed workflows** across the top candidate before recommending production build.

Prefer diversity over volume alone:
- owner/operator;
- office/admin person;
- finance/bookkeeping role where relevant;
- technically confident and non-technical users;
- small and somewhat larger operations.

A smaller sample may justify a prototype/discovery step, but not broad commercial conclusions.

## Interview / observation script

### 1. Establish the real workflow

Ask:
- Walk me through the last time this happened.
- What system did you start in?
- What other systems did you have to open?
- What did you copy, check, re-enter, message or wait for?
- Who else had to be involved?
- What tells you the job is actually finished?

Record exact systems and handoffs rather than labels such as “admin” or “follow-up.”

### 2. Frequency

Ask:
- How often does this happen in a normal week/month?
- Is it every job/order or only exceptions?
- What percentage become exceptions?
- Are there seasonal spikes?

Capture an estimate and confidence level.

### 3. Cost / friction

Ask:
- Roughly how many minutes does one case take?
- How much waiting or context switching is involved?
- Does work get repeated because information is missing or stale?
- Does this delay cash collection, fulfilment, customer response or job closure?

Do not calculate ROI from assumptions if participant cannot support the inputs.

### 4. Failure consequence

Ask:
- What goes wrong when this is missed or handled late?
- Customer complaint?
- Delayed payment?
- Refund?
- Rework?
- Staff interruption?
- Incorrect accounting or fulfilment state?
- Compliance or trust concern?

Record actual examples where available.

### 5. Current workaround

Ask:
- How do you solve it today?
- Which automations/apps have you already tried?
- What does ServiceM8/Shopify/Xero/etc already handle well?
- Where does the workflow still leave the system and become manual?

This is essential to avoid rebuilding incumbent functionality.

### 6. Authority boundary

Ask:
- Which actions would you trust software to do automatically?
- Which actions must a person approve?
- What information would you need to see before approving?
- What actions should never be automatic?

Record separately for communications, finance, refunds, booking/scheduling, fulfilment changes and data corrections.

### 7. Trust / verification

Ask:
- How would you know the automation got it right?
- Would you want a receipt/audit trail?
- What evidence would make you comfortable approving an action?
- What failure would cause you to stop using it?

### 8. Trial signal

Ask:
- If a tool handled this exact workflow with the controls described, would you try it on real non-critical cases?
- What would stop you?
- What setup burden would be acceptable?

Record willingness to trial separately from enthusiasm.

### 9. Willingness-to-pay

Do not start with “Would you pay $X?”

First ask:
- Is this painful enough that you currently spend money or staff time on it?
- If it reliably removed most of that coordination, how would you evaluate whether it was worth paying for?
- Would you expect it to be included in an existing tool, a small add-on, or a separate operations product?

Only after value framing, test bounded price ranges or packaging concepts. Record objections verbatim.

## Tradie-specific evidence fields

For each case capture:
- ServiceM8 or alternative job system;
- accounting system (Xero/QBO/MYOB/other);
- payment method/system;
- invoice approval process;
- payment sync behavior;
- receipt/paid-invoice communication process;
- closure checklist;
- exceptions: partial payment, overpayment, duplicate customer, mismatched invoice, failed sync, disputed work;
- customer communication channel;
- who is authorised to approve/send/correct;
- current weekly case volume;
- minutes per case;
- current failure examples;
- trial/WTP signal.

## Ecommerce-specific evidence fields

For each case capture:
- Shopify plan/store context;
- supplier/dropship systems;
- fulfilment/shipping system;
- marketplace channels if any;
- customer support system;
- accounting/finance system;
- supplier stock/ETA visibility;
- tracking update path;
- exception types: out of stock, late dispatch, split shipment, bad tracking, damaged item, supplier substitution, refund/return;
- customer promise decision maker;
- actions that can be automatic vs approval-required;
- current weekly exception volume;
- minutes per exception;
- current cost/refund/complaint examples;
- trial/WTP signal.

## Scoring rubric

Score each candidate workflow 0–3 on each dimension after evidence collection:

1. **Frequency** — rare to frequent.
2. **Cost/friction** — trivial to material.
3. **Failure impact** — low to high.
4. **Cross-system manual coordination** — little to substantial.
5. **Integration feasibility** — unknown/blocked to clear.
6. **Authority safety** — unsafe/ambiguous to clearly bounded.
7. **Verification feasibility** — weak to strong re-read/evidence path.
8. **Trial intent** — none to strong.
9. **Willingness-to-pay** — none/unknown to repeated credible signal.
10. **Acquisition reachability** — unclear to accessible target channel.

Do not use the total score alone. A hard blocker in integration, safety, verification or demand can veto a high numeric total.

## Prototype threshold

A workflow may advance to a non-production prototype/read-only proof when:
- at least 3 independent participants describe materially similar pain;
- the workflow occurs often enough to matter;
- the incumbent does not already solve the cross-system handoff adequately;
- read access is feasible;
- the approval boundary can be stated clearly;
- a measurable outcome is defined.

## Production-build threshold

Recommend production implementation only when:
- direct evidence reaches the minimum sample target or comparably strong observed workflow evidence;
- repeated trial interest exists;
- at least several credible willingness-to-pay signals exist;
- exact permissions/write actions are understood;
- fail-closed and verification behavior is specified;
- the reusable AgentOS interaction primitives have passed the relevant Wave 0 gate;
- no critical authority/security unknown remains.

## Current state

No direct customer interviews are recorded in this report.

Therefore:
- Tradie wedge: **HYPOTHESIS / DISCOVERY READY**
- Ecommerce wedge: **HYPOTHESIS / DISCOVERY READY**
- Property wedge: **BLOCKED ON INTEGRATION EVIDENCE**
- Production Commercial Frontend: **HOLD**
