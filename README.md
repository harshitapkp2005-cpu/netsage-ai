# 📡 NetSage AI

AI-assisted network troubleshooting assistant with mandatory human review for Cisco lab environments

**Python** **Cisco Packet Tracer** **AI/ML** **Network Engineering** **Chart.js**


---

##  Table of Contents

- [🎯 About](#-about)
- [🧩 Components](#-components)
- [🏗 Architecture](#-architecture)
- [🛠 Tech Stack](#-tech-stack)
- [🔒 Responsible AI & Safety](#-responsible-ai--safety)
- [🚀 Getting Started](#-getting-started)
- [📁 Project Structure](#-project-structure)
- [📊 Results](#-results)
- [👨‍💻 Author](#-author)

---

## 🎯 About

NetSage AI replaces the guesswork and trial-and-error approach that junior network engineers use when troubleshooting complex network issues. It centralizes symptom analysis, show-command interpretation, root cause identification, and fix verification into a single, intelligent platform — built with production-grade AI prompting and mandatory human oversight.

When a PC cannot reach a server, is the problem VLAN misconfiguration, routing failure, DHCP issue, DNS error, ACL block, or NAT problem? NetSage AI analyzes evidence and suggests diagnoses, but **always requires human approval** before implementation — ensuring network safety and preventing AI hallucinations from causing real damage.

---

## 🧩 Components

| Component | Description |
|-----------|-------------|
| **📊 Case Dataset** | 30 real-world troubleshooting scenarios covering all OSI layers (Physical to Application) |
| **🤖 AI Diagnosis Engine** | Structured prompts forcing JSON output with root cause, confidence, evidence, and fix steps |
| **🐍 Python Rule Checker** | Deterministic validation catching obvious errors (interface down, APIPA, ACL blocks) instantly |
| **✅ Human Review System** | Mandatory expert review marking each case as Accepted, Edited, or Rejected |
| ** Interactive Dashboard** | Visual analytics showing AI performance, issue distribution, and correction logs |
| ** Responsible AI Log** | Detailed documentation of 5 cases where AI failed and required human correction |

---

## 🏗 Architecture

🏗 Architecture
┌────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    NETSAGE AI ARCHITECTURE                                 │
└────────────────────────────────────────────────────────────────────────────────────────────┘

  [ 1. DATA LAYER ]                 [ 2. PROCESSING LAYER ]                [ 3. ACTION LAYER ]

┌──────────────────────┐          ┌──────────────────────────┐          ┌──────────────────────┐
│  Cisco Packet Tracer │          │   Python Rule Checker    │          │  Human Reviewer      │
│  (30 Lab Scenarios)  │─────────▶│  (Deterministic Checks)  │─────────▶│  (Accept/Edit/Reject)│
│  Show-Command Output │          │  (Instant Validation)    │          │  (Apply & Verify)    │
└──────────────────────┘          └────────────┬─────────────┘          └──────────────────────┘
                                               │ 
                                               │ (If no obvious error found)
                                               ▼ 
                                     ┌──────────────────────────┐
                                     │    AI Diagnosis Engine   │
                                     │  (Structured JSON Output)│
                                     │  (Root Cause & Evidence) │
                                     └────────────┬─────────────┘
                                                  │
                                                  ▼
                                     ┌──────────────────────────┐      ┌──────────────────────┐
                                     │  Interactive Dashboard   │◀─────│  Responsible AI Log  │
                                     │  (Charts & Metrics)      │      │  (Failure Analysis)  │
                                     └──────────────────────────┘      └──────────────────────┘

### Request Lifecycle
┌────────────────────────────────────────────────────────────────────────────────────────────┐
│                               TROUBLESHOOTING REQUEST LIFECYCLE                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘

  STEP 1: OBSERVE                  STEP 2: VALIDATE                   STEP 3: DIAGNOSE
┌──────────────────────┐          ┌──────────────────────┐          ┌──────────────────────┐
│  Network Symptom     │          │  Python Rule Checker │          │  AI Diagnosis Engine │
│  (e.g., Ping fails)  │─────────▶│  Scans show-commands│─────────▶│  Analyzes evidence   │
│  + Show Commands     │          │  for obvious errors  │          │  Generates JSON      │
└──────────────────────┘          └──────────┬───────────┘          └──────────┬───────────┘
                                             │                                 │
                        ┌────────────────────┘                                 │
                        │ (Error Found: e.g., "Interface Down")                │
                        ▼                                                      ▼
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
┌──────────────────────┐        ┌─────────────────────┐                        │
│  Human Expert        │◀───────│  Mandatory Human    │◀──────────────────────┘
│  Applies Fix &       │        │  Review Decision:    │
│  Verifies Network    │        │  ✅ Accepted (83%)  │
│  (Ping succeeds)     │        │  ✏️ Edited (3%)     │
└──────────────────────┘        │  ❌ Rejected (17%)  │
                                └──────────────────────┘

---

## 🛠 Tech Stack

### Network Simulation
- **Cisco Packet Tracer** - Building 30 realistic lab scenarios
- **Cisco IOS Commands** - show ip interface brief, show vlan brief, show ip route, etc.

### AI & Automation
- **Microsoft Copilot / ChatGPT** - AI diagnosis engine
- **Structured Prompting** - JSON-enforced output format
- **Python 3.x** - Rule checker and automation scripts

### Data & Visualization
- **CSV / Excel** - Dataset management and review logs
- **HTML5 + Chart.js** - Interactive dashboard with pie/bar charts
- **JavaScript** - Client-side analytics and rendering

### Documentation
- **Markdown** - README and technical documentation
- **Microsoft Word** - Summary document and Responsible AI log
- **OBS Studio** - Demo video recording

---

## 🔒 Responsible AI & Safety

### Human-in-the-Loop Requirement
✅ **All AI diagnoses require human approval** before implementation  
✅ **Zero autonomous changes** - no AI can modify network configurations  
✅ **Evidence-based reasoning** - AI must cite specific command outputs  
✅ **Confidence scoring** - Low confidence triggers mandatory human review

### AI Failure Documentation
We documented **5 critical cases** where the AI failed and required human correction:

| Case | AI Diagnosis | Human Correction | Why AI Failed |
|------|--------------|------------------|---------------|
| **08** | VLAN mismatch (70%) | Trunk vs Access port | Ignored empty `show interfaces trunk` output |
| **12** | VLAN deleted (80%) | Wrong encapsulation ID | Confused Layer 2 switch with Layer 2/3 router |
| **17** | Route missing (60%) | Blackhole route (Null0) | Didn't understand Null0 drops traffic |
| **22** | DHCP off (50%) | Exhausted address pool | Defaulted to common answer without reading config |
| **26** | Interface down (40%) | ACL blocking ICMP | Guessed Layer 1 while Layer 4 evidence present |

### Safety Metrics
- **83% AI Agreement Rate** - 25 out of 30 cases diagnosed correctly
- **17% Human Correction Rate** - 5 cases required expert intervention
- **100% Human Review** - Every single case reviewed before implementation

---

## 🚀 Getting Started

### Prerequisites
- **Cisco Packet Tracer** (free via Cisco Networking Academy)
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Web Browser** (Chrome, Edge, or Firefox)
- **AI Access** (Microsoft Copilot, ChatGPT, or Google AI Studio)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/netsage-ai.git
cd netsage-ai

# 2. Run the Python Rule Checker
cd Project_Files
python rule_checker.py

# 3. Open the Dashboard
# Double-click: Dashboard/dashboard.html
# Or open in browser: file:///path/to/dashboard.html

# 4. Test AI Diagnosis
# Open Prompts/system_prompt.md
# Copy to AI chat tool (Copilot/ChatGPT)
# Paste case data from Datasets/cases.csv

## Quick Test
# Verify Python installation
python --version

# Run rule checker
python Project_Files/rule_checker.py

# Expected output:
# ==================================================
#       NetSage AI - Rule Checker Started
# ==================================================
# [Case_01] Symptom: PC1 cannot ping gateway...
#   -> No obvious deterministic errors found...
# ==================================================

### 📁 Project Structure

netsage-ai/
│
├──  README.md                            # Professional documentation
├──  Summary_Document.docx                # Complete project report
│
├──  Project_Files/                       # Core system components
│   ├──  rule_checker.py                  # Deterministic validation script
│   └──  dashboard.html                   # Interactive analytics dashboard
│
├──  Datasets/                            # Data management
│   ├──  cases.csv                        # 30 troubleshooting scenarios
│   └──  review_log.csv                   # AI acceptance/rejection tracking
│
├──  Prompts/                             # AI interaction templates
│   ├──  system_prompt.md                 # AI system instructions + examples
│   └──  user_prompt_template.md          # Case submission template
│
├──  Responsible_AI_Log/                  # Safety documentation
│   └──  Responsible_AI_Log.docx          # 5 AI failure case studies
│
└──  Demo/                                # Visual demonstration
    ├──  Demo_Video.mp4                   # 5-minute project walkthrough
    └──  Dashboard_Screenshot.pdf         # Dashboard visualization

### 📺 Demo Video

  Watch our 5-minute demonstration showcasing the complete troubleshooting workflow:

  ┌──────────────────────────────────────────────────────────────────────────────────────┐
  │                                                                                      │
  │   ▶ BROKEN CASE          ▶ AI DIAGNOSIS          ▶ HUMAN REVIEW          ▶ FIX     │
  │   ─────────────          ─────────────           ────────────           ──────       │
  │   Packet Tracer          JSON Output             Accept/Reject          Verify       │
  │   Scenario Loaded        Root Cause              Expert Decision        Success      │
  │   Symptom Shown          Confidence Score        Correction Applied     Tested       │
  │                                                                                      │
  └──────────────────────────────────────────────────────────────────────────────────────┘

  🎥 Video Location: Demo/Demo_Video.mp4
  
  📋 Video Contents:
     • Network fault demonstration in Cisco Packet Tracer
     • AI diagnosis with structured JSON output
     • Human review and correction process
     • Fix implementation and verification
     • Dashboard analytics overview

### Author

   Name:            Harshita Pandey
   LinkedIn:        www.linkedin.com/in/harshita-pandey-6a16903a6
   GitHub:          https://github.com/harshitapkp2005-cpu
