# ATS Portals Automation Reference

This guide details reliable automation strategies for enterprise Applicant Tracking Systems (ATS).

## 1. Greenhouse (boards.greenhouse.io & job-boards.greenhouse.io)

### Key Characteristics
- Direct job application endpoints with structured form fields (`#first_name`, `#last_name`, `#email`, `#phone`).
- Resume uploads via `input[type="file"]#resume` or `button[aria-label="Attach"]`.
- Cover Letter: Always look for "Enter manually" button or `textarea#cover_letter_text` to inject the tailored human pitch.
- Location Fields: Often powered by React-Select. Type the city/state (e.g., "Coconut Creek"), wait 300ms for options, and dispatch Enter or click `.select__menu-notice` / `.select__option`.
- Security Verification: Certain high-security tech employers (e.g. Coinbase) trigger a one-time numeric passcode sent to the applicant's email during form submission. Read the code from Gmail and input it into the confirmation field.

---

## 2. Workday (myworkdayjobs.com)

### Key Characteristics
- Requires an active candidate profile (`userHome` / Candidate Home).
- Synthetic Event Model: Workday buttons frequently have `tabindex="-2"` and ignore native `.click()`. Always trigger clicks on parent wrappers `div[data-automation-id="click_filter"]` or use `form.requestSubmit()`.
- Steps Flow: Typically 6 to 8 steps (Account -> Resume Autofill -> Contact Info -> Experience -> Questionnaire -> Disclosures -> Review -> Submit).
- Resume Parsing: Uploading the PDF resume autofills 90% of fields automatically. Always verify parsed fields before submitting.

---

## 3. Lever (jobs.lever.co)

### Key Characteristics
- Clean, lightweight forms with standard HTML inputs.
- Single-page application format.
- Resume upload via standard file input.
- Additional information / cover letter text box directly accessible on page.
