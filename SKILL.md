---
name: auto-job-apply
description: Find suitable jobs, prepare tailored applications, submit ATS forms, and discover recruiters for requested outreach. Use for automated job application workflows, Greenhouse/Workday/Lever forms, and job-related recruiter emails.
---

# Job Applications and Recruiter Outreach

## Scope and candidate facts

Follow the user's requested scope: discovery, drafts, applications, outreach, or a combination. A request to find jobs does not authorize submissions; a request to apply authorizes matching applications within the stated criteria. Send recruiter outreach only when requested. Honor existing authorization without asking again for each job. Installing or editing this skill does not authorize applications or emails. A daily target does not itself create a scheduled automation.

Use the current resume and user-provided profile as the source of truth. Confirm missing essentials such as target roles, locations, work authorization, sponsorship requirements, and which resume to use before dependent submissions. Never infer demographic answers, invent accomplishments, certifications, employment, or metrics. Use confirmed preferences for optional disclosures, or leave them unanswered when allowed.

## Tool and path compatibility

This skill is shared across Claude Code, Codex, Antigravity (AGY), and other agents. Use tools actually available in the current session; do not assume a specific tool name or an existing logged-in browser session.

- **Claude Code**: use Claude in Chrome (`mcp__claude-in-chrome__*` tools) for navigating, reading, and filling ATS forms, or another browser MCP (such as Playwright) if that is what is connected. If no browser tool is available, tell the user to run `/chrome` to connect it and continue with discovery and drafting meanwhile. For email, use the Gmail connector (`mcp__claude_ai_Gmail__*`) when connected; authenticate it first if only the `authenticate` tool is listed. If the connector can only create drafts, create the draft and report that it still needs to be sent. Use `WebFetch`/`WebSearch` for public job pages and recruiter research. File uploads into a page may not be possible through the browser tool; if so, stop at that step for that job and ask the user to attach the resume.
- **Codex**: read and follow the available browser skill before navigating or filling forms. Use observed page controls and the supported upload mechanism.
- **Antigravity**: use the built-in browser subagent and the user's Chrome profile when available.
- In all agents, prefer a connected email tool for Gmail operations and fall back to the browser. If login, upload, or email access is unavailable, report the blocker and continue independent preparation. Do not claim a connection exists merely because this skill is installed.
- Resolve scripts and references relative to this SKILL.md's directory (Claude Code shows it as the skill's base directory), not the shell working directory.
- Store generated documents, screenshots, and `job_pipeline_report.md` in the user's chosen writable output directory, otherwise a `job-applications` directory in the current workspace. Use company, requisition ID, and date in artifact names.

## 1. Discover and verify jobs

Prefer employer careers pages and direct ATS postings over aggregators. Read the existing pipeline report before starting and deduplicate by company and requisition ID or canonical job URL.

Optional discovery helper (use this skill's actual directory):

```sh
python3 <skill-dir>/scripts/scan_fresh_jobs.py 10
python3 <skill-dir>/scripts/scan_fresh_jobs.py 10 --keywords "platform engineer,backend" --boards "stripe,datadog"
```

The bundled helper searches Greenhouse boards (a default list, or `--boards`) by title keywords (IAM/security by default, or `--keywords`). It does not search Lever or Workday, filter by location, verify posting age, or establish eligibility. Boards that fail to load are listed on stderr, so empty output does not prove there are no jobs. Use direct career-site searches for other roles and to resolve missing results.

Open each selected posting, verify it remains open, and check the complete requirements and location against the user's criteria. Do not expand criteria simply to meet a quota.

## 2. Prepare applications

Read [ATS portal guidance](references/ats_portals.md) for the relevant portal and [writing guidance](references/outreach_guidelines.md) for cover letters.

Fill confirmed candidate details and upload the intended resume. Review parsed employment, dates, education, and screening answers. Tailor a concise cover letter when the portal supports it or the user requests one; record when no field or attachment option exists. Do not put a cover letter in an unrelated field.

Review the complete application before submission. Capture a review screenshot when supported, avoiding unnecessary sensitive disclosures. If an unknown required answer blocks one application, record it and continue other independent work.

## 3. Submit and verify

Submit only within the authorized scope, using the portal's visible workflow. Let the user handle login challenges or CAPTCHA that require their interaction. For an application-specific email code, use authorized mailbox access and match the message to the current company and application; do not store codes in reports.

Verify a receipt page, application ID, candidate dashboard status, or confirmation email. A click or absence of an error is not confirmation. If submission times out or the result is uncertain, check the dashboard or confirmation email before retrying; do not blindly submit again. Mark unresolved results `unknown` and report them.

## 4. Recruiter discovery and requested outreach

Read [recruiter discovery](references/recruiter_discovery.md). Research relevant recruiters and record source URLs. Only send to verified addresses, never to guessed corporate email patterns.

For requested outreach, follow [writing guidance](references/outreach_guidelines.md), verify recipient and resume attachment, and send within the authorized scope. Check prior outreach to avoid duplicates. If sending is ambiguous, inspect Sent mail or the provider result before retrying. Draft-only requests remain drafts. State that an application was submitted only when submission is confirmed.

## 5. Report progress

Update `job_pipeline_report.md` after each meaningful action. Include company, title, requisition ID, canonical URL, date/time with timezone, resume version, status, confirmation evidence, contact source, outreach status, and artifact links when available. Preserve existing history.

Distinguish discovered, prepared, submitted, draft, sent, blocked, and unknown statuses. Finish with confirmed application and email counts, skipped jobs and reasons, and any remaining blockers. Do not report quota completion based on prepared forms or attempted submissions.
