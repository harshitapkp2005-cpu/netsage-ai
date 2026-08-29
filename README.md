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

**🔄 Request Lifecycle**
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

