# BYFIT opt-in evolution workflow

This workflow runs only after the user explicitly asks to record learning, analyze accumulated outcomes, or update the Skill.

## 1. Define the lesson

Capture the minimum useful information:

- Product category and buyer type.
- Deal stage and buyer concern.
- Message strategy used.
- Observable outcome.
- What evidence supports the proposed lesson.
- Whether the lesson is reusable or only case-specific.

Do not store raw conversations or personal contact information in this public repository.

## 2. Sanitize

Remove or generalize:

- person and company names;
- emails, phones, addresses, domains, and account handles;
- exact order values and confidential prices;
- supplier or partner-factory identities;
- attachments and private document details;
- dates or product combinations that would make the customer identifiable.

Retain exact metrics only when the user approves their reuse and their source is documented.

## 3. Select the update

Read [evolution rules](evolution_rules.md). Choose the smallest change that improves a future decision:

- refine a trigger or routing rule;
- correct a scoring signal;
- add a sourced FAQ pattern;
- add an approved anonymized case;
- update a time-sensitive market fact with an authoritative source and date;
- remove or consolidate duplicated instructions.

Do not update multiple unrelated files from one lesson.

## 4. Record provenance

When a journal entry is useful, append a sanitized record to `evolution_journal.md`:

```markdown
### Evolution YYYY-MM-DD — [short title]
- Trigger: [user-authorized learning request]
- File changed: [path]
- Evidence: [sanitized outcome or authoritative source]
- Change: [what changed]
- Confidence: [High/Medium/Low]
- Privacy check: Passed
```

`inquiry_log.md` is an optional aggregate log, not a required per-customer CRM. If used, record non-identifying categories and outcomes only.

## 5. Validate and sync

1. Review `git diff` for unsupported claims, duplicated rules, and leaked private data.
2. Run the bundled Skill validator against the repository root.
3. Verify every new relative link exists.
4. Test the changed route or response behavior when material.
5. Commit with a concise message and sync to the authorized Git remote.

If validation or privacy review fails, correct the change before syncing.

## Pattern report

When the user asks what the Skill has learned, analyze only available sanitized records. Report sample size and missing outcomes. Useful dimensions include product, market, buyer concern, stage, response, conversion, and confidence. Do not calculate reply or conversion rates from records whose outcome is unknown.
