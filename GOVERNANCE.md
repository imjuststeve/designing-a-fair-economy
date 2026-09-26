# Contribution governance

Working process v0.1 — September 26, 2026.

The owner has requested third-party review and a system for evaluating, voting on, and integrating contributions. The procedure below is an initial operational design. Review windows and participation targets are provisional defaults to test. The existing authority remains: Steve Smith makes final project-position decisions. Binding voting rights, elected stewards, and a transfer of authority are open governance proposals, not adopted changes.

The governance of this repository should itself be open to criticism. Current owner authority is explicit; this small research project does not claim already to implement the distributed governance it studies.

## Roles

- Contributor: submits ideas, evidence, reviews, or edits. No degree, financial contribution, or write permission is required to participate.
- Reviewer: evaluates a defined proposal using the contribution criteria and discloses relevant interests. Expertise informs reasons, not extra ballots.
- Facilitator: the owner or a publicly named delegate who tracks status, prepares a neutral review summary, opens a vote, and records the tally. This role does not independently confer adoption authority.
- Decision owner: Steve, until an explicit governance decision delegates authority. Records acceptance, revision requests, deferral, or rejection and the reasons.
- Integrator: prepares and merges the accepted wording after review. Write access is a technical permission, not independent authority to adopt project positions.

## Contribution paths

Editorial fixes, broken links, and faithful synchronization of an already adopted position may use a short pull-request review without a ballot. A disputed correction or any change to meaning enters substantive review. Standalone evidence can be added as evidence without adopting the policy it favors, provided source and claim checks are recorded.

Substantive mechanisms, changes to goals, conclusions, obligations, or governance follow the full process. The owner's own substantive proposals follow it as well once contributor review is open. Routine maintenance and this initial process setup are not retroactively subject to a ballot. Any urgent departure must be identified and explained; it must not be described as community approval.

## Workflow

1. Draft: open an issue with the proposal template. Use its issue number as the proposal ID. Explain what changes, why, and how it affects the whole framework.
2. Triage: a facilitator checks scope, duplicates, missing context, and the appropriate path. Target an initial response within seven days of active maintenance; if capacity is unavailable, leave it visibly pending.
3. Review: allow at least seven calendar days for substantive comments. Seek evidence, an assessment of affected people, and at least one review independent of the author. Record missing perspectives instead of inventing reviewers.
4. Revision: the author or integrator addresses objections. Preserve earlier versions and summarize changes. A proposal may remain exploratory or be deferred when evidence is inadequate.
5. Ballot: freeze an exact version in a linked commit or immutable pull-request commit. A facilitator posts the voting notice, unresolved concerns, and opening and closing times in UTC. Default duration is seven full days. Do not change the version during the vote.
6. Decision: publish the tally and an evidence-based explanation. Owner chooses accept, revise, defer, or reject. Explain any departure from the majority recommendation. An unresolved severe concern about evidence, rights, or feasibility can justify deferral despite support.
7. Integration: prepare or finalize a pull request containing the accepted changes, the relevant plan sections, references, decisions, changelog, and generated editions. Review the final diff against the voted version. Owner approval must refer to that final commit; a later substantive edit requires renewed review and a new ballot.
8. Closeout: merge, verify the published files, record the merge commit, and close the issue as integrated. Track review triggers and reopen when new evidence materially changes the decision.

Record stage in the issue's opening status block; labels are optional and are not required for this process to work. Accepted awaiting integration and integrated are distinct states. An open pull request does not imply adoption.

## Ballots

During the announced window, post a new top-level comment in the proposal issue:

    Ballot: SUPPORT / OPPOSE / ABSTAIN
    Proposal version: <commit SHA>
    Reason: <brief explanation>
    Relevant interests: <disclosure or none>
    Supersedes: <earlier ballot link, if changing a vote>

Anyone participating as an individual may cast one ballot. Use one GitHub account per person; pseudonyms are allowed and identity documents are not required. Organizations and automated accounts do not get separate ballots. The author may vote and must disclose authorship. Affiliations do not automatically invalidate a person's vote, but relevant ties must be disclosed.

The most recent valid new ballot comment submitted by that account before closing counts. Do not edit an old ballot to change it; post a replacement that links to it. Capture comment links, account names, timestamps, version, choices, and disclosed interests in the closing record. Flag edits affecting a ballot after the deadline instead of silently counting changed content. Manual review and public records are the initial mechanism; there is no automatic vote bot or identity verification.

Count support, oppose, and abstain separately. Report support divided by support plus oppose; if that denominator is zero, report no expressed preference. Strictly more than half of non-abstaining ballots means a favorable advisory tally. A tie is no majority. Neither result automatically authorizes a merge.

The provisional participation target is three valid non-author ballots and at least one substantive review independent of the author. If either is missing, mark participation limited; never describe a small turnout as community consensus. The owner may defer, extend the window before it closes, or make a clearly labeled owner decision with the participation limitation recorded. Do not change thresholds mid-vote. No universal quorum for binding decisions is established.

Exclusions require a stated reason such as duplicate ballots, wrong version, lateness, automated activity, or evidenced manipulation. A new account or an unpopular view alone is not a sufficient reason. Preserve an exclusion log and a route to challenge it; do not publicly expose private data. If integrity cannot be established, mark the tally disputed and defer or rerun it. Open account voting cannot reliably prove one person per account; it remains advisory for that reason as well.

Material changes require a new version and a fresh ballot. New decisive evidence discovered during voting should pause the process with reasons recorded. Restart with a new full window when ready. Cosmetic corrections can proceed only if they do not alter meaning and are explicitly documented.

## Decisions and reconsideration

Use docs/templates/DECISION_RECORD.md and add adopted decisions to docs/DECISIONS.md. Preserve the strongest dissent and why it did or did not change the outcome. Record when the result should be revisited. A request for reconsideration must identify new evidence, a changed condition, or a process error and link the earlier decision.

Governance amendments use this same substantive process and apply prospectively. Changes to owner authority, voter eligibility, binding thresholds, or institutional roles require an explicit owner decision. Review this initial procedure after three completed proposals or the first 30 days of active participation, whichever occurs first; that review is a checkpoint, not an automatically scheduled task.

## GitHub controls and current limits

Issues and pull-request templates in this repository support submissions, review, and integration. A vote is recorded manually in the linked issue. No automatic merge, ballot counting, account validation, invitations, or background processing has been installed.

Branch protection should be considered when maintainers are appointed: require pull requests, review of final changes, resolution of conversations, and renewed approval after substantive edits. Do not impose a reviewer requirement that the current staffing cannot meet. Protection settings and available reviewers must be verified before claiming technical enforcement; this documentation does not enable those settings. Until configured, compliance depends on maintainers following this process.

Implementation references: [GitHub issue and pull request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates) and [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches). These describe platform capabilities, not adopted economic policy or a completed security configuration.
