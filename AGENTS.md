# Project maintenance requirements

These instructions apply throughout the repository.

## Authorization and scope

Routine documentation maintenance and publication are authorized during project work sessions. Integrate approved requirements, maintain the full framework, and ask only when ambiguity materially changes meaning or adoption. Do not convert tentative ideas into adopted policy. This authorization does not cover unrelated outreach, spending, enrollment, or live policy implementation.

## Documentation standard

Follow DOCUMENTATION_STANDARD.md. Present current proposals in formal scholarly style with nearby numbered citations and a matching References section at the end of each standalone document. Exclude internal conversations, revision narratives, and accounts of why earlier provisions were replaced. Explain current provisions analytically. Clearly identify proposals, sourced findings, assumptions, inferences, and unresolved questions. Never fabricate citations or claim verification that did not occur.

## Maintenance workflow

1. Fetch the current branch and read README.md, docs/PROJECT_PLAN.md, docs/DECISIONS.md, REFERENCES.md, CONTRIBUTING.md, GOVERNANCE.md, and DOCUMENTATION_STANDARD.md.
2. Preserve the complete relationship among security, practical freedom, diverse outcomes, ownership, contestable power, and a survivable transition.
3. Update affected documents together. docs/DECISIONS.md contains current requirements and open questions. Historical discussion, ballots, and procedural audit records belong in platform records and Git history, not the substantive documents. Do not add revision narratives to CHANGELOG.md.
4. Preserve stable source identifiers and URLs. Disclose mismatched support, unavailable sources, missing metadata, counterevidence, and verification limits. Synchronize the reference appendix in the README and plan from REFERENCES.md.
5. Run scripts/build_documents.py when the plan or references change. Verify PDF and text consistency; render and inspect every PDF page.
6. Check links, citations, definitions, proposal status, and governance consistency. Publish authorized changes without force-pushing over intervening work and verify the remote commit.

## Contributor authority

Apply GOVERNANCE.md. Every goal and rule is revisable; the founder has one vote and no unilateral veto. Editorial maintenance requires no substantive ballot. Ordinary substantive changes require 60 percent approval when at least three contributors are eligible; fewer than three use strict majority. Governance and purpose changes require two-thirds. Abstentions count toward participation, not approval. Quorum is max(3, ceiling(C/2)) for C >= 3, and one for C = 1 or 2. No expressed preferences means no decision.

When exactly one human contributor is eligible, explicit approval permits immediate adoption and publication without separate waiting periods, issue ballots, or independent PR review. Record the approval scope and tally in the publication audit trail without reproducing private conversation. Automated drafting does not create additional voters. With more contributors, apply the published review, voting, and fidelity-check procedures. Retain dissent and qualification evidence in platform audit records.

## References

[P1] Designing a Fair Economy. DOCUMENTATION_STANDARD.md. September 27, 2026. Project documentation requirements.

[P2] Designing a Fair Economy. GOVERNANCE.md. Current repository policy.
