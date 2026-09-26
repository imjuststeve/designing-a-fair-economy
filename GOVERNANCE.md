# Contribution governance

Working process v0.2 — September 26, 2026.

## Authority and revisability

Contributors determine adoption by vote. An adopted decision directs the current project until a later valid vote changes or reverses it. Nothing in the project is permanently settled: goals, principles, mechanisms, wording, membership criteria, voting procedures, and governance itself can be revised.

Steve Smith confirmed this direction on September 26, 2026, including that contributors qualify to vote and the founder has no unilateral veto. The founder participates on the same voting terms as other contributors. Repository ownership and merge permissions are administrative capabilities; they do not grant additional policy authority.

This supersedes the initial advisory-vote and owner-approval model. It does not turn earlier proposals into adopted policies or turn previous discussion into a recorded community vote. The founding clarification is recorded as such in docs/DECISIONS.md.

## Who qualifies to vote

A person qualifies through a publicly traceable contribution to this project: a concrete proposal, substantive review or critique, relevant evidence with explanation, documented lived experience tied to an issue, analysis, editing, accessibility work, or other identifiable project work. A proposal need not be accepted, and a critique need not agree with the current position. Qualification must not depend on founder approval, ideology, credentials, donations, employment, or write access.

A reaction, star, empty endorsement, spam, or a ballot alone does not establish a contribution. A relevant first contribution made during proposal review qualifies that person for the subsequent vote. Each ballot includes a link to a contribution made before the announced voting window opened. Contributors joining after that cutoff participate in discussion and subsequent votes. This cutoff is a provisional operating rule, itself revisable.

Each person has one vote, including an author voting on their own proposal. Use one account per person. Pseudonyms are welcome; no identity documents are required. Organizations and automated accounts do not receive separate votes. Expertise informs reasons, not voting weight. Disclose relevant interests without publishing private information.

The contribution link is evidence of qualification; a maintainer's acceptance of the contribution is not required. Publish qualification disputes and reasons. A rejected proposal does not remove its author's voting rights. Open account participation cannot guarantee identity uniqueness; record credible manipulation concerns and handle them under the dispute procedure below.

## Roles

- Contributor: proposes, reviews, supplies evidence, votes, and may seek reconsideration.
- Facilitator: organizes review, posts a neutral voting notice, records eligibility and the tally, and documents the result. The initial coordinator is Steve; contributors can replace or delegate this role by vote. A facilitator cannot override a valid result.
- Integrator: prepares and merges the text that the vote adopted, checks consistency, and records the published commit. Technical discrepancies must be corrected without altering the adopted meaning.
- Reviewer: evaluates evidence, feasibility, distribution, freedom, power, and alternatives. Where possible, someone other than the author checks the final edit and tally.

No role holds a unilateral veto. Contributors can replace role holders and revise role powers by vote. A contributor may post a complete voting notice when a facilitator is unavailable; access to a formal title must not become a gate on proposals. Competing notices for the same version should be reconciled publicly before voting proceeds.

## Contribution paths

Editorial corrections, repaired links, and faithful synchronization of adopted text may use a short pull-request review without a policy ballot. Evidence may be recorded with its limitations without adopting the policy it favors. A disputed correction or change of meaning enters substantive review.

All substantive changes, including founder proposals and changes to the current goals or governance, use the voting process. Explain how a proposed revision affects the full concept; disagreement with current goals is not itself grounds to exclude it. Existing text remains operative until a valid replacement is adopted.

## Review and voting

1. Draft: open a proposal issue. State the exact change, reasons, evidence, uncertainties, alternatives, affected people, and connections to the full project. Its issue number is the proposal ID.
2. Review: allow at least seven calendar days for substantive comments and seek a review independent of the author. Record missing evidence and objections. The author revises the proposal with a visible change history.
3. Freeze: link the exact proposal to a commit. Publish opening and closing timestamps in UTC, the contribution cutoff, qualification criteria, rule version, unresolved concerns, and ballot format. The voting window lasts seven full days. Do not change the rules or proposal mid-vote.
4. Vote: eligible contributors post SUPPORT, OPPOSE, or ABSTAIN in a new top-level issue comment, with the frozen commit, contribution link, reasons, relevant interests, and any superseded ballot link. Reactions do not count.
5. Tally: count each person's last valid new ballot posted within the window. Preserve comment links, timestamps, choices, contribution links, disclosed interests, and exclusions. A replacement ballot must be a new comment; flag edits made after closing.
6. Determine the result under the rules below. Record evidence, dissent, and the outcome. A maintainer reports the result rather than choosing whether to honor it.
7. Integrate accepted text through a linked pull request. Check the final diff against the voted version, update affected documentation and references, regenerate editions, and record the merge commit. Material changes require another review and vote; faithful editorial integration does not.
8. Reconsider whenever a contributor proposes a revision. Earlier decisions remain traceable in history; none is immune to replacement.

## Provisional operating rules for results

The voting authority and universal revisability above are founder-confirmed. The following mechanics are initial implementation defaults, subject to contributor revision rather than claims of separately approved founder preferences:

- Require at least three eligible contributors to cast valid ballots and at least one substantive review by someone other than the author. Authors count toward participation; no special voting weight applies.
- Abstentions count toward participation but not the approval denominator. Adopt if SUPPORT is strictly more than half of SUPPORT plus OPPOSE and the participation and review requirements are met.
- If OPPOSE has a strict majority under those same conditions, the proposal is not adopted. A tie, no non-abstaining ballots, or unmet participation or review requirements means no decision; existing wording remains current.
- Publish the turnout and limits. With fewer than three participating contributors, a substantive proposal waits for participation or an already validly adopted change to these rules. There is no founder override or low-turnout escape that substitutes a personal decision for a vote.
- A failed or inconclusive proposal can be revised and resubmitted. Record the relationship to earlier versions.

The first contributor governance review should assess these defaults after three completed proposals or 30 days of active participation, whichever occurs first. This is a review checkpoint, not a scheduled automation. Contributors may propose changes sooner.

## Evidence, disputes, and reconsideration

Voting selects the project's current position; it does not establish empirical truth. Preserve uncertainty and contrary evidence even when contributors adopt a policy. New evidence may motivate opposition, withdrawal by the author before adoption, or a fresh revision vote. A facilitator cannot cancel an unwanted result by declaring the evidence inadequate.

Exclude ballots only for an identified rule violation such as lateness, wrong version, lack of a qualifying contribution, duplication, or evidenced automation or impersonation. Publish reasons and allow challenge; do not treat a new account or unpopular opinion as evidence of manipulation. Record disputed ballots and both possible tallies. If a dispute cannot affect the outcome, integrate the uncontested result while recording the concern. If it could change the result, pause integration and seek a contributor vote on the specific procedural question, with independent review and the disputed identities disclosed. Do not claim consensus when identity or eligibility remains unresolved.

Implementation may be paused for a concrete technical mismatch, missing rights to publish submitted material, or an outcome-changing procedural dispute. State the exact obstacle and route to resolution. Such a pause is not authority to reject or rewrite an adopted position. Document delays; contributors may replace the facilitator or integrator by vote. Technical account control can still obstruct publication in practice, so the project must not claim the social rule is technically enforced.

Any contributor may propose reconsideration for new evidence, changed circumstances, a process error, or a reasoned change of judgment. New evidence is not a prerequisite for changing values or governance. Governance changes are decided under the rules in force when their vote opens and take effect prospectively; they cannot retroactively change an existing tally. There are no permanently protected clauses.

## Integration and platform limits

Use docs/templates/DECISION_RECORD.md and add adopted decisions to docs/DECISIONS.md. Keep accepted awaiting integration distinct from integrated. The record connects the proposal, frozen version, rules, qualification evidence, ballots, dissent, pull request, verification, and merge commit.

Issue and pull-request templates support the process. Voting, qualification review, and tallying are manual. No automatic merge, identity verification, background monitoring, or branch-protection configuration is installed by these documents. Technical write permissions remain separate from voting rights. Consider branch protections and distributed maintainer access through contributor governance when staffing permits.

Platform references: [GitHub issue and pull request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates) and [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches). These describe capabilities, not completed configuration.
