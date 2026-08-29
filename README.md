# 🌐 NetSage AI
An AI-assisted network troubleshooting assistant with mandatory human review for Cisco lab environments.

Python • CSV • HTML5 • Chart.js • Cisco Packet Tracer • LLM API

**LIVE DASHBOARD** ✨: [Open `dashboard.html`](Project_Files/dashboard.html)  
**DEMO VIDEO** 🎥: [Watch Demo](Demo/Demo_Video.mp4)

## 🧭 Table of Contents
- [About](#-about)
- [Features](#-features)
- [Architecture](#-architecture)
- [Request Lifecycle](#-request-lifecycle)
- [Tech Stack](#-tech-stack)
- [Responsible AI & Safety](#-responsible-ai--safety)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Author](#-author)

---

## 🎯 About
NetSage AI replaces the guesswork and trial-and-error that junior network engineers face when diagnosing complex lab environments. When a PC cannot reach a server, is the problem a VLAN mismatch, routing error, DHCP failure, DNS issue, or ACL block? 

This project centralizes symptoms, topology notes, and Cisco `show` command outputs into a single, intelligent platform. It uses structured AI prompts to suggest root causes and fixes, but critically, it enforces a **mandatory human-in-the-loop review** before any configuration is applied, ensuring network safety and preventing AI hallucinations.

---

## 🧩 Features
| Feature | Description |
| :--- | :--- |
| 📚 **Case Dataset** | 30 real-world Cisco Packet Tracer scenarios covering Layers 1 through 7. |
| 🐍 **Rule Checker** | Deterministic Python script that instantly catches obvious config errors (e.g., interface down, APIPA addresses). |
| 🤖 **AI Diagnosis** | Structured prompting that forces the AI to output strict JSON with root cause, confidence, evidence, and fix steps. |
| 👨‍💻 **Human Review** | Mandatory oversight system logging every case as Accepted, Edited, or Rejected by a human expert. |
| 📊 **Visual Dashboard** | Interactive HTML dashboard displaying issue distribution, AI agreement rates (83%), and correction logs. |

---

## 🏗 Architecture
```text
┌──────────────────────┐          ┌──────────────────────────┐          ┌──────────────────────┐
│    DATA LAYER        │          │    PROCESSING LAYER      │          │    ACTION LAYER      │
│                      │          │                          │          │                      │
│  Cisco Packet Tracer │─────────▶│  Python Rule Checker     │─────────▶│  Human Reviewer      │
│  (30 Lab Scenarios)  │          │  (Deterministic Checks)  │          │  (Accept/Edit/Reject)│
│  Show-Command Output │          │  (Instant Validation)    │          │  (Apply & Verify)    │
└──────────────────────┘          └────────────┬─────────────┘          └──────────────────────┘
                                               │ 
                                               │ (If no obvious error found)
                                               ▼ 
                                     ┌──────────────────────────┐
                                     │  AI Diagnosis Engine     │
                                     │  (Structured JSON Output)│
                                     │  (Root Cause & Evidence) │
                                     └────────────┬─────────────┘
                                                  │
                                                  ▼
                                     ┌──────────────────────────┐      ┌──────────────────────┐
                                     │  Interactive Dashboard   │◀─────│  Responsible AI Log  │
                                     │  (Charts & Metrics)      │      │  (Failure Analysis)  │
                                     └──────────────────────────┘      └──────────────────────┘




## 🔄 Request Lifecycle

```text
  STEP 1: OBSERVE                  STEP 2: VALIDATE                   STEP 3: DIAGNOSE
┌──────────────────────┐          ┌──────────────────────┐          ┌──────────────────────┐
│  Network Symptom     │          │  Python Rule Checker │          │  AI Diagnosis Engine │
│  (e.g., Ping fails)  │─────────▶│  Scans show-commands │─────────▶│  Analyzes evidence   │
│  + Show Commands     │          │  for obvious errors  │          │  Generates JSON      │
└──────────────────────┘          └──────────┬───────────┘          └──────────┬───────────┘
                                             │                                  │
                        ┌────────────────────┘                                  │
                        │ (Error Found: e.g., "Interface Down")                 │
                        ▼                                                       ▼
               ┌──────────────────────┐                              ┌──────────────────────┐
               │  Instant Alert       │                              │  Structured Output:  │
               │  "Fix Physical Layer"│                              │  • Root Cause        │
               └──────────────────────┘                              │  • Confidence Score  │
                                                                     │  • Evidence Quote    │
                                                                     │  • Next Command      │
                                                                     │  • Fix Steps         │
                                                                     └──────────┬───────────┘
                                                                                │
  STEP 4: REVIEW                 STEP 5: RESOLVE                                │
┌──────────────────────┐        ┌──────────────────────┐                        │
│  Human Expert        │◀───────│  Mandatory Human     │◀───────────────────────┘
│  Applies Fix &       │        │  Review Decision:    │
│  Verifies Network    │        │  ✅ Accepted (83%)   │
│  (Ping succeeds)     │        │  ✏️ Edited (3%)     │
└──────────────────────┘        │  ❌ Rejected (17%)  │
                                └──────────────────────┘
```

---

## 🛠 Tech Stack

**Core & Scripts**
* **Python 3.x** — Deterministic rule checking and CSV data processing
* **JSON / CSV** — Structured data exchange and dataset management

**AI & Simulation**
* **LLM API** (Microsoft Copilot / ChatGPT) — Natural language diagnosis and JSON generation
* **Cisco Packet Tracer** — Network simulation and `show` command extraction

**Dashboard & UI**
* **HTML5 / CSS3** — Lightweight, dependency-free dashboard structure
* **Chart.js** — Interactive data visualization (Pie, Bar, Doughnut charts)

**Dev Tools**
* **Git + GitHub** — Version control and project hosting
* **OBS Studio** — Professional demo video recording

---

## 🔒 Responsible AI & Safety

* **Mandatory Human-in-the-Loop:** No AI-generated fix is ever applied to the network without explicit human approval (Accept/Edit/Reject).
* **Deterministic Safety Net:** The Python Rule Checker runs *before* the AI, catching obvious Layer 1/3 errors to prevent unnecessary AI hallucinations.
* **Strict Output Formatting:** AI is forced to output pure JSON with mandatory `evidence` fields, preventing vague or unstructured guesses.
* **Transparent Failure Logging:** All 5 instances of AI failure are explicitly documented in the `Responsible_AI_Log.docx` to highlight the limits of autonomous troubleshooting.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher
* A modern web browser (Chrome, Edge, Firefox)
* (Optional) Cisco Packet Tracer to view the original `.pkt` lab files

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/netsage-ai.git
cd netsage-ai

# 2. Run the Python Rule Checker
python Project_Files/rule_checker.py
# This will read Datasets/cases.csv and print deterministic alerts to the console.

# 3. View the Interactive Dashboard
# Simply double-click the file below to open it in your default web browser:
Project_Files/dashboard.html
```

---

## 📁 Project Structure

```text
netsage-ai/
├── Project_Files/              # Core executable files
│   ├── rule_checker.py         # Deterministic Python validation script
│   └── dashboard.html          # Interactive visual analytics dashboard
│
├── Datasets/                   # Raw data and tracking logs
│   ├── cases.csv               # 30 network troubleshooting scenarios
│   └── review_log.csv          # AI vs Human agreement tracking
│
├── Prompts/                    # AI interaction templates
│   ├── system_prompt.md        # Core rules and JSON formatting instructions
│   └── user_prompt_template.md # Standardized case submission format
│
├── Responsible_AI_Log/         # Safety and oversight documentation
│   └── Responsible_AI_Log.docx # Detailed analysis of 5 AI corrections
│
├── Demo/                       # Media and presentation assets
│   ├── Demo_Video.mp4          # 5-minute project walkthrough
│   └── Dashboard_Screenshot.pdf# High-resolution dashboard export
│
├── Summary_Document.pdf        # Comprehensive project report
└── README.md                   # You are here!
```

---


## 👨‍💻 Author

**Harshita Pandey** 

## 📩 Contact Info

* 💼 **LinkedIn:** [Connect on LinkedIn](www.linkedin.com/in/harshita-pandey-6a16903a6)
* 🐙 **GitHub:** [Follow on GitHub](https://github.com/harshitapkp2005-cpu)


