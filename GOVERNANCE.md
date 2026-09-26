# Contribution governance

Adopted policy v1.0 — September 26, 2026.

## Authority and revisability

Contributors determine adoption by vote. An adopted decision directs the current project until a later valid vote changes or reverses it. Nothing in the project is permanently settled: goals, principles, mechanisms, wording, membership criteria, voting procedures, and governance itself can be revised.

Steve Smith confirmed this direction on September 26, 2026, including that contributors qualify to vote and the founder has no unilateral veto. The founder participates on the same voting terms as other contributors. Repository ownership and merge permissions are administrative capabilities; they do not grant additional policy authority.

This supersedes the initial advisory-vote and owner-approval model. It does not turn earlier proposals into adopted policies or turn previous discussion into a recorded community vote. The founding clarification is recorded as such in docs/DECISIONS.md.

## Who qualifies to vote

A person qualifies through a publicly traceable contribution to this project: a concrete proposal, substantive review or critique, relevant evidence with explanation, documented lived experience tied to an issue, analysis, editing, accessibility work, or other identifiable project work. A proposal need not be accepted, and a critique need not agree with the current position. Qualification must not depend on founder approval, ideology, credentials, donations, employment, or write access.

A reaction, star, empty endorsement, spam, or a ballot alone does not establish a contribution. A relevant first contribution made during proposal review qualifies that person for the subsequent vote. Each ballot includes a link to a contribution made before the announced voting window opened. Contributors joining after that cutoff participate in discussion and subsequent votes. This cutoff is an adopted operating rule, itself revisable.

Each person has one vote, including an author voting on their own proposal. Use one account per person. Pseudonyms are welcome; no identity documents are required. Organizations and automated accounts do not receive separate votes. Expertise informs reasons, not voting weight. Disclose relevant interests without publishing private information.

The contribution link is evidence of qualification; a maintainer's acceptance of the contribution is not required. Publish qualification disputes and reasons. A rejected proposal does not remove its author's voting rights. Open account participation cannot guarantee identity uniqueness; record credible manipulation concerns and handle them under the dispute procedure below.

Publish the eligible contributor list with contribution links during review and freeze it at vote opening. Count every qualifying person, including the author and founder, whether or not they are expected to vote. Allow public challenges to omissions and exclusions without requiring agreement with a maintainer. An outcome-relevant roster error requires correction and a fresh voting window, not a silent mid-vote change. Inactivity does not currently remove eligibility; any future active-member or inactivity policy requires a governance vote. Review the risk of inactive membership blocking quorum as the community grows.

## Roles

- Contributor: proposes, reviews, supplies evidence, votes, and may seek reconsideration.
- Facilitator: organizes review, posts a neutral voting notice, records eligibility and the tally, and documents the result. The initial coordinator is Steve; contributors can replace or delegate this role by vote. A facilitator cannot override a valid result.
- Integrator: prepares and merges the text that the vote adopted, checks consistency, and records the published commit. Technical discrepancies must be corrected without altering the adopted meaning.
- Reviewer: evaluates evidence, feasibility, distribution, freedom, power, and alternatives. Where possible, someone other than the author checks the final edit and tally.

No role holds a unilateral veto. Contributors can replace role holders and revise role powers by vote. A contributor may post a complete voting notice when a facilitator is unavailable; access to a formal title must not become a gate on proposals. Competing notices for the same version should be reconciled publicly before voting proceeds.

## Contribution paths and approval tiers

Classify changes by their effect, not whether they add, revise, or remove text. A new addition can change the project's purpose; a revision can simply repair a typo. These are current adopted rules, not a draft proposal.

| Contribution | Adoption path |
| --- | --- |
| Idea, evidence, critique, or alternative for consideration | Review relevance, clarity, source limits, and publication rights. Record as proposed or evidence, without a policy ballot or implying endorsement. |
| Typo, formatting, broken link, or faithful synchronization | Maintainer review without a policy ballot. A disputed change of meaning enters substantive review. |
| Substantive project position, addition, revision, or removal | At least 60 percent approval; strict majority if fewer than three contributors are eligible. |
| Voting rights, governance rules, role powers, or central purpose and guiding principles | At least two-thirds approval. These matters remain fully revisable. |

Accepting an idea for discussion is not adoption of the position it advocates. Review must not filter out disagreement with current goals. Relevance and basic quality decisions must include reasons and allow challenge. Routine appointment or replacement of a role holder under unchanged rules is a substantive decision; changing a role's powers is governance.

State the tier and its rationale before voting. Separate unrelated changes into independent proposals. A coherent proposal that changes governance or central purpose uses the higher tier in full. Resolve classification disputes before opening; use the higher tier if the disputed proposal proceeds without agreement on classification. This prevents relabeling a governance change as an ordinary addition to evade its threshold.

## Review and voting

1. Draft: open a proposal issue with one coherent decision. State the exact wording, reasons, evidence, uncertainties, alternatives, affected people, and connections to the full project. Its issue number is the proposal ID.
2. Review: allow at least seven calendar days for ordinary substantive changes and fourteen for governance or central-purpose changes. Seek review independent of the author, record objections and missing evidence, and preserve revision history. Publish the proposed tier and eligible roster for challenge.
3. Freeze: link the exact proposal to a commit. Publish the rule version, final tier, eligible roster and count, contribution cutoff, quorum, threshold, unresolved concerns, ballot format, and opening and closing timestamps in UTC. Voting lasts seven full days for ordinary changes and fourteen for governance or purpose changes. Do not change rules, eligibility, or proposal mid-vote. A material edit requires renewed review and a fresh vote.
4. Vote: eligible contributors post SUPPORT, OPPOSE, or ABSTAIN in a new top-level issue comment, with the frozen commit, contribution link, reasons, relevant interests, and any superseded ballot link. Reactions do not count.
5. Tally: count each person's last valid new ballot posted within the window. Preserve comment links, timestamps, choices, contribution links, interests, and exclusions. A replacement ballot must be a new comment; flag edits made after closing.
6. Determine both participation and approval under the rules below. Record evidence, dissent, arithmetic, and outcome. A maintainer reports the result rather than choosing whether to honor it.
7. Integrate accepted text through a linked pull request. Check its diff against the voted version, update affected documentation and references, regenerate editions, and record the merge commit. Maintainers perform a fidelity check, not a second discretionary policy approval. Material changes require another review and vote; faithful editorial integration does not.
8. Reconsider whenever a contributor proposes a revision. Earlier decisions remain traceable in history; none is immune to replacement.

## Participation and approval

Use the eligible roster frozen at opening. Let C be its contributor count, S be valid SUPPORT ballots, O be valid OPPOSE ballots, and A be valid ABSTAIN ballots. Count each person once. Participation P = S + O + A; expressed preferences D = S + O. Non-voters and invalid, late, duplicate, or superseded ballots count toward neither P nor D.

For C >= 3, required participation Q = max(3, ceiling(C / 2)): at least half of eligible contributors, rounded up, and never fewer than three. With one or two eligible contributors, Q = 1. With no eligible contributors, no vote can decide a change. A vote meets quorum when P >= Q. For example, C = 3 or 5 requires three participants; C = 7 requires four; C = 10 requires five. Abstentions count toward quorum but not toward the approval percentage.

After quorum is met and D > 0, use the applicable exact approval check:

| Tier | Exact check | Minimum supporting ballots |
| --- | --- | --- |
| Ordinary substantive, C >= 3 | 5 × S >= 3 × D | ceiling(3 × D / 5) |
| Ordinary substantive, C < 3 | 2 × S > D | floor(D / 2) + 1 |
| Governance or central purpose, any C | 3 × S >= 2 × D | ceiling(2 × D / 3) |

Approval is S / D, not S / C or S / P. Exactly 60 percent passes in the ordinary tier; exactly two-thirds passes in the governance tier. Use integer arithmetic, not a rounded display percentage such as 66.7 percent. A tie does not pass.

| Expressed preferences D | Support for 60 percent | Support for two-thirds |
| --- | --- | --- |
| 3 | 2 | 2 |
| 4 | 3 | 3 |
| 5 | 3 | 4 |
| 6 | 4 | 4 |
| 7 | 5 | 5 |
| 8 | 5 | 6 |
| 9 | 6 | 6 |
| 10 | 6 | 7 |

The approval table does not replace the separate quorum check. With C = 5, three SUPPORT and two OPPOSE adopt an ordinary change but not a governance change. Two SUPPORT, one OPPOSE, and two ABSTAIN meet quorum and adopt either tier: approval is 2/3. With C = 10, three SUPPORT alone do not meet the five-person quorum, despite unanimous expressed support.

Abstention means declining to express a preference. Consequently, if quorum is met, one SUPPORT and all other participants abstaining can pass; report the small number of expressed preferences prominently. All abstentions means D = 0 and no decision. This is the deliberate consequence of excluding abstentions from approval, not evidence of broad affirmative support.

Record one of three outcomes: adopted when quorum and approval pass; not adopted when quorum is met and D > 0 but approval fails; no decision when quorum is missing or D = 0. The existing position remains in place in the latter two cases. Insufficient participation is not rejection of the proposal's merits. A fresh vote may be announced with a new window; do not extend a closed vote or alter its rules to manufacture a result. There is no founder override.

## Adoption, review, and rationale

Steve Smith explicitly adopted this model on September 26, 2026 as the current policy, replacing the earlier single-threshold model. This is a founding policy adoption recorded in D007, not a claim that a community ballot occurred. Adoption gives the policy continuing effect until revised; it creates no permanent or immune clause and no ongoing founder exception to contributor voting.

The tiers encourage exploration, require wider agreement for project commitments, and apply additional scrutiny to changes in decision-making power and purpose. The quorum reduces decisions by a tiny unrepresentative turnout, while excluding abstentions lets contributors decline to judge without opposing a proposal. These are design choices, not guarantees against capture or deadlock.

Review this policy after three completed proposals or thirty days of active participation, whichever occurs first. Assess participation, inactive membership, classification disputes, abstentions, eligibility manipulation, and barriers to useful contributions. This is a review checkpoint, not a scheduled automation. The current rules continue until revised; contributors can propose changes sooner. Independent review is encouraged but does not create an extra policy veto.

R21, [Python PEP 13](https://peps.python.org/pep-0013/), provides a precedent for two-thirds approval and a two-week governance voting window. This project adopts its own eligibility, quorum, and tier rules; Python's council authority and membership system are not imported.

## Evidence, disputes, and reconsideration

Voting selects the project's current position; it does not establish empirical truth. Preserve uncertainty and contrary evidence even when contributors adopt a policy. New evidence may motivate opposition, withdrawal by the author before adoption, or a fresh revision vote. A facilitator cannot cancel an unwanted result by declaring the evidence inadequate.

Exclude ballots only for an identified rule violation such as lateness, wrong version, lack of a qualifying contribution, duplication, or evidenced automation or impersonation. Publish reasons and allow challenge; do not treat a new account or unpopular opinion as evidence of manipulation. Record disputed ballots and both possible tallies. If a dispute cannot affect the outcome, integrate the uncontested result while recording the concern. If it could change the result, pause integration and seek a contributor vote on the specific procedural question, with independent review and the disputed identities disclosed. Do not claim consensus when identity or eligibility remains unresolved.

Implementation may be paused for a concrete technical mismatch, missing rights to publish submitted material, or an outcome-changing procedural dispute. State the exact obstacle and route to resolution. Such a pause is not authority to reject or rewrite an adopted position. Document delays; contributors may replace the facilitator or integrator by vote. Technical account control can still obstruct publication in practice, so the project must not claim the social rule is technically enforced.

Any contributor may propose reconsideration for new evidence, changed circumstances, a process error, or a reasoned change of judgment. New evidence is not a prerequisite for changing values or governance. Governance changes are decided under the rules in force when their vote opens and take effect prospectively; they cannot retroactively change an existing tally. There are no permanently protected clauses.

## Integration and platform limits

Use docs/templates/DECISION_RECORD.md and add adopted decisions to docs/DECISIONS.md. Keep accepted awaiting integration distinct from integrated. The record connects the proposal, frozen version, rules, qualification evidence, ballots, dissent, pull request, verification, and merge commit.

Issue and pull-request templates support the process. Voting, qualification review, and tallying are manual. No automatic merge, identity verification, background monitoring, or branch-protection configuration is installed by these documents. Technical write permissions remain separate from voting rights. Consider branch protections and distributed maintainer access through contributor governance when staffing permits.

Platform references: [GitHub issue and pull request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates) and [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches). These describe capabilities, not completed configuration.
