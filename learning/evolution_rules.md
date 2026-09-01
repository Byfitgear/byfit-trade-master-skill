# BYFIT evolution rules

Use these rules only when the user explicitly asks to record learning, analyze patterns, or update this Skill. Ordinary buyer analysis and reply drafting must not change repository files.

## Privacy and evidence gate

This repository is public. Before any learning update:

1. Remove names, email addresses, phone numbers, exact quotations, addresses, supplier identities, and other customer-identifying or commercially sensitive details.
2. Confirm that the remaining pattern is useful without the private data.
3. Separate the user's reported outcome from the model's interpretation.
4. Add product, company, regulatory, price, performance, or case claims only when a source is recorded and the claim is suitable for future customer-facing use.
5. Do not turn a template, hypothetical example, or one-off inference into a BYFIT fact.

If safe anonymization would remove the evidence needed to understand the lesson, do not store it in this public repository.

## Candidate changes

| Candidate | Minimum evidence | Preferred change |
|---|---|---|
| Repeated buyer question | Three independently observed, sanitized examples | Add or refine one FAQ answer |
| Scoring mismatch | Three outcomes showing the same directional error | Calibrate the relevant scoring signal |
| Effective subject or CTA | At least five comparable uses with recorded outcomes | Add a qualified recommendation, not a guarantee |
| New buyer subtype | Several cases that existing types cannot explain | Add a subtype only if it changes the recommended action |
| Successful case | User confirms the outcome and approves anonymized reuse | Add a sourced, anonymized case with no invented metrics |
| New market insight | Current authoritative source or repeated verified evidence | Add the source and `as of` date |
| Certification or regulation | Current regulator or standards-body source | Record product scope, market, status, and date |

One example may justify a temporary note or an investigation question; it usually does not justify a universal rule.

## Change quality

- Prefer correcting or replacing a weak rule over indefinite append-only growth.
- Keep one authoritative location for each instruction or fact.
- Remove duplication when the new version supersedes it.
- Preserve useful history in Git rather than retaining contradictory prose in the live Skill.
- Make the narrowest change supported by the evidence.
- Include provenance in the changed content when future users need it: source, date, confidence, and scope.

## Stop conditions

Do not update when:

- the user has not authorized a Skill change;
- the evidence contains unsanitized customer or supplier data;
- the outcome is unknown;
- the rule already exists;
- a current authoritative source cannot confirm a time-sensitive claim;
- the proposed change would encode a personal preference as a universal requirement.

## Validation requirement

After an authorized update:

1. Review the complete diff.
2. Check relative Markdown links.
3. Run the Skill validator.
4. Test the changed behavior with a realistic, privacy-safe prompt when the change is material.
5. Commit and sync the repository only after validation succeeds.
