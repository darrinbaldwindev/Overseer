# Commercial Frontend — Tradie fallback wedge 002

Date: 2026-09-14 Brisbane
Owner: Commercial Frontend Overseer
Status: DISCOVERY-READY / DIRECT DEMAND UNKNOWN / NO PRODUCTION IMPLEMENTATION

## Purpose
Define the smallest second Tradie cross-system exception to validate if direct evidence shows the current Xero-paid post-payment closure wedge is too low-frequency or low-value.

This is a fallback hypothesis, not a replacement CRM, quoting system, payment chaser or invoice engine.

## Candidate wedge
**Completed job -> invoice awaiting approval -> accounting-sync exception resolution**

Core flow:
1. detect a completed ServiceM8 job whose invoice remains in `Awaiting Approval` or whose attempted accounting sync has an error/ambiguous state;
2. assemble exact job, invoice, customer and accounting-integration context;
3. identify the smallest blocking condition that prevents approval/sync;
4. prepare one recommended corrective step;
5. require human approval for any consequential invoice/accounting change;
6. perform only a bounded authorized action in a future implementation;
7. reread ServiceM8/Xero state;
8. show verified outcome or explicit unresolved/changed state.

## Why this is the next fallback
Current ServiceM8 documentation confirms:
- completed jobs flow into the Invoicing page and `Awaiting Approval` stage;
- someone must approve an invoice before it syncs to Xero/QuickBooks/MYOB;
- failed processing is visibly surfaced for resolution;
- finance/invoicing permission is required for invoice approval in the app.

This creates a concrete cross-system handoff and exception boundary rather than duplicating ServiceM8's existing invoice workflow.

Evidence rechecked 2026-09-14:
- https://support.servicem8.com/help-center/servicem8-add-ons/xero/sending-your-first-job-to-xero
- https://support.servicem8.com/questions/invoices/can-servicem8-send-invoices-automatically-to-accounting-software
- https://support.servicem8.com/help-center/app/basics/approving-an-invoice-from-the-app
- https://support.servicem8.com/help-center/desktop/basics/new-to-servicem8-start-with-a-job-walkthrough

## Systems
- ServiceM8: system of record for job/invoice operational state and approval workflow.
- Xero: accounting system of record for synchronized accounting invoice/payment state.
- AgentOS: governance/orchestration/verification/audit.
- Commercial Frontend: approval and exception visibility cockpit only.

## Manual handoff hypothesis
Current operator may need to:
- notice an invoice remains awaiting approval or a sync reports an error;
- open the job/invoice;
- inspect whether job status, invoice content or integration state is blocking progress;
- decide whether to correct, approve, defer or escalate;
- recheck whether the invoice actually reached the accounting system.

Frequency, minutes/case and consequence are UNKNOWN until direct observation/interview.

## Read feasibility
Current public evidence supports read-oriented investigation of ServiceM8 jobs/payments and current ServiceM8 invoice state through product/developer surfaces already mapped in this workstream. Exact production-safe Xero/ServiceM8 write scopes remain out of scope and must be separately evidenced before implementation.

## Approval boundary
Default first-MVP rule:
- observation/context assembly: read-only;
- recommendation/prepared correction: allowed as proposal only;
- invoice approval, invoice/accounting mutation, customer communication or any financial-state change: explicit authorized human approval required;
- ambiguous identity, conflicting state, stale evidence or post-approval change: `BLOCKED_NO_ACTION` / `CHANGED_AFTER_APPROVAL`.

No model may self-approve the accounting consequence.

## Smallest testable non-production MVP
1. synthetic completed-job/invoice fixture;
2. detect awaiting-approval or sync-error condition;
3. correlate exact job/invoice/customer/accounting identifiers;
4. render one exception card with blocking reason and proposed next step;
5. default to no action;
6. simulated approval produces a bounded action intent only;
7. reread fixture state;
8. assert replay cannot generate a second action intent;
9. stale/conflicting state invalidates the recommendation.

## Measurable direct-validation questions
Ask operators:
- How many completed jobs reach invoicing per week?
- How many sit in Awaiting Approval longer than expected?
- How often does Xero/accounting sync fail or require manual investigation?
- What are the top 3 reasons approval/sync is delayed?
- Who notices and resolves these cases?
- How many minutes does a typical exception take?
- What happens if the exception is missed for a day or a week?
- Do these delays affect cash collection, reporting, customer communication or bookkeeping workload?
- Would a single exception queue that explains the blocker and prepares the next action be useful?
- Would they trial it? What would make them pay for it?

## Success condition for prototype promotion
At least 3 independent participants/observed workflows must report materially similar approval/sync exception pain, with enough frequency and measurable burden to justify testing, plus a feasible read path and clear approval boundary.

## Rejection condition
Reject or deprioritize this wedge if:
- exceptions are rare;
- ServiceM8 already resolves the dominant cases adequately;
- the accounting sync issue is mostly one-time setup rather than recurring operations;
- there is no measurable operator burden/consequence;
- trial/WTP interest is weak.

## Non-goals
- no autonomous invoice approval;
- no autonomous accounting mutation;
- no replacement invoicing screen;
- no replacement ServiceM8/Xero integration;
- no customer contact;
- no production connector activation.

Classification: `SECONDARY TRADIE WEDGE / DISCOVERY-READY / DIRECT DEMAND UNKNOWN`.