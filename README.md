🛡 NetSage AI
AI-Assisted Network Troubleshooting Assistant with Mandatory Human Review
Python | Cisco Packet Tracer | LLM API | HTML5 | Data Visualization
Status: 🟢 Production Ready | Safety Level: 🔒 Human-in-the-Loop
🧭 Table of Contents
About
Core Modules
Architecture
Request Lifecycle
Tech Stack
Responsible AI & Safety
Getting Started
Project Structure
Author
🎯 About
Junior network engineers often struggle to connect complex network symptoms to their root causes. Is it a VLAN mismatch, a routing loop, or a security ACL blocking traffic?
NetSage AI solves this by acting as an intelligent "Network Doctor." It analyzes symptoms and Cisco show command outputs to diagnose issues instantly. However, unlike standard AI tools, NetSage enforces a Safety Rule: no fix is accepted without Mandatory Human Review. This ensures that AI hallucinations never damage live network infrastructure.
🧩 Core Modules
Module
Description
🧪 Case Dataset
30 real-world broken network scenarios (VLAN, Routing, DHCP, ACL, Wireless) built in Cisco Packet Tracer.
🐍 Rule Checker
A Python script that performs deterministic checks (e.g., catching physical link down or APIPA errors) instantly.
🧠 AI Diagnosis
Structured LLM prompts that force JSON output containing Root Cause, Confidence, and Evidence.
👨‍💼 Human Review
A mandatory validation step where a senior engineer must Accept, Edit, or Reject the AI's suggestion.
📊 Dashboard
An interactive HTML dashboard visualizing AI performance, issue distribution, and the "Responsible AI Log."
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
🔄 Request Lifecycle
┌────────────────────────────────────────────────────────────────────────────────────────────┐
│                               TROUBLESHOOTING REQUEST LIFECYCLE                            │
└────────────────────────────────────────────────────────────────────────────────────────────┘

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
🛠 Tech Stack
Network Simulation
Cisco Packet Tracer – Building 30 realistic lab scenarios (Routers, Switches, APs).
Backend & Logic
Python 3.x – Running the deterministic Rule Checker script.
LLM API (Copilot/ChatGPT) – Powering the diagnosis engine with structured prompts.
Frontend & Visualization
HTML5 / CSS3 – Lightweight, dependency-free dashboard.
Chart.js – Rendering interactive pie and bar charts for AI performance metrics.
🛡 Responsible AI & Safety
This project prioritizes safety over automation. We identified 5 Critical Failure Modes where AI hallucinated or missed context, requiring human correction:
Case 08 (Trunking vs. VLAN): AI missed the empty trunk table.
Case 12 (Encapsulation): AI confused router config with switch database.
Case 17 (Blackhole Routes): AI failed to understand the Null0 interface.
Case 22 (DHCP Exhaustion): AI guessed "Service Down" instead of reading the exclusion range.
Case 26 (ACL vs. Physical): AI ignored Layer 4 security logs and guessed a physical break.
Conclusion: AI is a powerful assistant, but the "Human-in-the-Loop" is non-negotiable for network safety.
🚀 Getting Started
Prerequisites
Python 3.8+
Cisco Packet Tracer
Web Browser (Chrome/Edge)
Installation & Execution
Run the Rule Checker:
bash
12
View the Dashboard:
Open Project_Files/dashboard.html in your web browser to view the analytics.
Simulate a Case:
Open Datasets/cases.csv, pick a case, and run it through your preferred LLM using the prompts in Prompts/system_prompt.md.
📁 Project Structure
text
12345678910111213141516
👨‍💻 Author
[Your Name]
College: [Your College Name]
Role: Network Architect & AI Engineer
