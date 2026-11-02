# Commercial document revision playbook

Read this file when creating or revising a PI, quotation, price list, catalog, contract, QC/certification pack, shipping instruction, or another customer-facing commercial file.

## Contents

- Source priority and change matrix
- Scope preservation
- PI and sample PI
- Quotation and price list
- Catalog and product sheet
- Contract and supplier qualification
- QC, safety, and certification material
- Shipping instructions
- Calculation and visual verification
- Handoff

## Source priority

Use this order when instructions conflict:

1. The user's latest explicit approval.
2. The buyer's requested corrections, limited to changes the user has authorized.
3. The latest source file or quotation.
4. Older files and repository templates.

Flag unresolved conflicts instead of choosing silently.

## Build a change matrix

Before editing, extract every requested change:

| Requested change | Current value | New value | Source | Affected fields/pages | Status |
|---|---|---|---|---|---|

Use `Confirmed`, `Needs approval`, `Conflict`, or `Not found`. Apply only confirmed changes. Keep the matrix internal unless the user asks to see it.

## Preserve scope

- Change only what the user or buyer requested and what is necessary to keep the document internally consistent.
- Preserve unrelated wording, layout, formulas, images, models, prices, terms, and bank information.
- Do not convert a buyer request into a concession without the user's approval.
- Do not silently replace a legal company name, beneficiary, bank account, Incoterm, port, currency, unit, or price formula.
- When a buyer corrects an address or company name, reproduce it exactly, including punctuation, floor, district, postal code, and country.

## PI and sample PI

Verify together:

- seller and buyer legal details;
- PI number and date;
- product name, model, photograph, construction, color, dimensions, and included accessories;
- quantity, unit, unit price, subtotal, freight/courier line, discounts, and grand total;
- whether a sample is free, chargeable, refundable, or credited against a future order;
- payment terms, delivery term, loading port, lead time, and validity;
- bank details and beneficiary, without changing them unless explicitly authorized.

The photograph and description must represent the same product. If the source image is wrong, replace it rather than covering it with text. If a sample is cut from a larger mold or production piece, describe the delivered sample accurately without implying that its cut size is the bulk-product manufacturing size.

## Quotation and price list

- For a new buyer/project's first substantive reply, do not send a quotation, price list, price range or priced catalog. Follow [discovery before quotation](discovery_before_quotation.md) before later customer-facing pricing. Editing an existing authorized document is not itself permission to send it or bypass this gate.
- Normalize currency, unit, model, specification, Incoterm, and port on every line.
- Apply a price formula only when the user supplies it for this document.
- Recalculate subtotals and totals independently after editing.
- State inclusions and exclusions consistently, especially freight, customs, installation, sample cost, courier cost, packaging, and optional accessories.
- Keep quotation validity, warranty, lead time, MOQ, and container-loading claims only when confirmed.
- When a value changes, search the entire workbook or document for stale copies of the old value.

## Catalog and product sheet

- Keep brand, company name, model prefix, product category, photographs, specifications, and captions consistent.
- Remove legacy logos cleanly from the underlying image or layout; do not hide them with a visibly placed rectangle.
- Do not reuse one product image for a different model unless the user confirms it is representative.
- Preserve image proportions and readable tables.
- Separate product facts from marketing claims; confirm certificates and performance values before publication.

## Contract and supplier-qualification files

- Preserve clause numbering and bilingual alignment.
- Check that defined terms, parties, product scope, payment, delivery, inspection, warranty, liability, confidentiality, IP, termination, and dispute clauses agree across the document.
- Do not state that a certificate, test, patent clearance, factory ownership, or customer reference exists unless evidence is supplied.
- When reducing risk for both parties, make obligations measurable: document, deadline, acceptance test, cure period, or liability cap.

## QC, safety, and certification material

- Distinguish an internal QC procedure, inspection record, laboratory test report, management-system certificate, product certificate, declaration, and regulatory registration.
- Confirm certificate holder, product/model scope, standard, issuing body, report/certificate number, and validity date.
- If a certificate is unavailable, use accurate conditional language such as `can be arranged if required`; do not imply current certification.

## Shipping instructions

- Preserve fixed shipper data exactly.
- Confirm consignee, notify party, ports, marks, cargo description, package count/type, gross/net weight, measurement, and container information.
- Use standard package terms consistently: `PKGS`, `PALLETS`, `CARTONS`, or `WOODEN CASES` as applicable.
- Uppercase English input only when the user requests that behavior; do not uppercase email addresses or case-sensitive codes if it would make them invalid.
- Keep the final form on one page only when readability remains acceptable.

## Calculation check

For every edited financial document:

1. Recalculate each line from quantity × unit price.
2. Recalculate discounts, freight/courier, credits, and total separately.
3. Check rounding at the displayed precision.
4. Compare the visible total with any formula-backed total.
5. Confirm that a free item is not accidentally included in the product subtotal.

Do not infer a missing total from memory. Ask or calculate only from confirmed values.

## Visual verification

Render the finished file in its intended output format and inspect every page:

- correct product image and color;
- no clipped text, overlapping cells, hidden formulas, or broken page breaks;
- readable fonts and tables;
- aligned headers, footers, signatures, and totals;
- correct A4 or requested page size;
- no legacy logo, placeholder, comment, or revision mark left behind;
- selectable/searchable text where practical.

Fix visual defects before delivery. For a spreadsheet, also verify the printed page preview, not only the cell grid.

## Handoff

Deliver the finished file first. Then summarize:

- changed items;
- preserved commercial terms;
- any field that still needs confirmation;
- whether totals and visual rendering were verified.
