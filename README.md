# Auto Job Apply: Autonomous ATS Application & Recruiter Outreach Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-orange.svg)](https://github.com/mrh-jishan/auto-job-apply)
[![Antigravity Skill](https://img.shields.io/badge/Antigravity-Custom%20Skill-brightgreen.svg)](https://github.com/mrh-jishan/auto-job-apply)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)](https://github.com/mrh-jishan/auto-job-apply)

An autonomous end-to-end job application, ATS portal submission, recruiter discovery, and cold outreach engine built for **Claude Code**, **Google Antigravity (AGY)**, **Codex**, and other autonomous coding agents. One `SKILL.md` works in all of them.

Unlike spammy "Easy Apply" bots that submit resumes to aggregators where thousands of applicants compete, **Auto Job Apply** targets direct corporate portals (Greenhouse, Workday, Lever), embeds tailored cover letters directly into the application, discovers the hiring manager or technical recruiter on LinkedIn, and delivers concise, personalized cold outreach via Gmail.

---

## Architecture Overview

```mermaid
flowchart TD
    A["1. Discovery: Scan Corporate ATS APIs"] --> B["2. Form Staging & Custom Cover Letter"]
    B --> C["3. Submit Application & Capture Screenshot"]
    C --> D["4. LinkedIn Recruiter Discovery"]
    D --> E["5. Direct Recruiter Outreach (Gmail)"]
    E --> F["6. Audit Trail & Pipeline Tracker"]
```

---

## Key Features

1. **Direct Corporate ATS Automation**:
   - Native support for **Greenhouse**, **Workday**, and **Lever** enterprise portals.
   - Handles React-Select dropdowns, dynamic location pickers, and Workday synthetic event models.
   - Automatically solves one-time passcode verification emails sent during submission.

2. **Embedded Tailored Cover Letters**:
   - Injects concise, role-matched impact bullets directly into the ATS portal's "Cover Letter" field.
   - Eliminates generic fluff by focusing on quantifiable engineering outcomes.

3. **Recruiter Intelligence**:
   - Discovers domain-specialized technical recruiters and talent acquisition leaders on LinkedIn and public sources.
   - Only emails verified addresses (published, user-provided, or from prior correspondence). Guessed corporate patterns are never used as recipients.

4. **Human-Style Cold Outreach**:
   - Composes punchy, unique emails (under 120 words) matching candidate credentials directly to job requisitions.
   - Strictly enforces zero em dashes for authentic human readability.
   - Automatically attaches PDF resumes and saves visual delivery receipts.

5. **Visual Audit Trail**:
   - Captures high-resolution screenshot receipts for every stage:
     - Form Review (`{company}_application_form.png`)
     - Portal Submission (`{company}_submitted.png`)
     - Outreach Sent Confirmation (`{company}_sent.png`)

---

## Directory Structure

```text
auto-job-apply/
├── SKILL.md                          # Shared skill runbook (Claude Code, AGY, Codex)
├── README.md                         # Project documentation and setup guide
├── LICENSE                           # MIT License
├── agents/
│   └── openai.yaml                   # Codex skill display metadata
├── references/
│   ├── ats_portals.md                # Workday, Greenhouse & Lever automation quirks & selectors
│   ├── recruiter_discovery.md        # Recruiter search & verified-contact rules
│   └── outreach_guidelines.md        # Concise cold email & cover letter formulas (0 em dashes)
└── scripts/
    └── scan_fresh_jobs.py            # Greenhouse board scanner (--keywords, --boards)
```

---

## Quickstart & Installation

### Option 1: Install as a Claude Code Skill
Personal (all projects):
```bash
git clone https://github.com/mrh-jishan/auto-job-apply.git ~/.claude/skills/auto-job-apply
```
Or per project: clone into `.claude/skills/auto-job-apply` inside the repo. Then ask Claude to apply to jobs, or invoke it directly with `/auto-job-apply`.

Claude Code uses **Claude in Chrome** for ATS forms (run `/chrome` to connect it) and the **Gmail connector** for outreach when it is connected.

### Option 2: Install as a Global Antigravity Skill
To make this skill available across all workspaces on your machine:
```bash
git clone https://github.com/mrh-jishan/auto-job-apply.git ~/.gemini/config/skills/auto-job-apply
```

### Option 3: Install into a Project Workspace (AGY / Codex)
To use this skill within a specific repository or project:
```bash
mkdir -p .agents/skills
git clone https://github.com/mrh-jishan/auto-job-apply.git .agents/skills/auto-job-apply
```

### Option 4: Run the Job Scanner Standalone
Query verified tech company boards for fresh active roles:
```bash
python3 scripts/scan_fresh_jobs.py 10
python3 scripts/scan_fresh_jobs.py 10 --keywords "platform engineer,backend" --boards "stripe,datadog"
```

---

## How It Works

Once installed, activate the skill in Claude Code, Antigravity, or Codex by asking:
> *"Apply to 10 senior IAM or cloud security jobs today, include tailored cover letters in the portal, find the recruiters on LinkedIn, and send cold emails."*

The agent will automatically:
1. Scan active corporate job boards.
2. Fill and validate application fields using your resume and profile data.
3. Inject tailored cover letters into portal forms.
4. Submit the applications and capture review screenshots.
5. Identify the dedicated technical recruiter on LinkedIn.
6. Draft and dispatch personalized outreach notes with your resume attached via Gmail.
7. Update your master `job_pipeline_report.md` tracking table.

---

## License

MIT License. See [LICENSE](LICENSE) for details. Built by [Robiul Hassan](https://github.com/mrh-jishan).
