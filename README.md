# Project 07: # 🚀 Social Media Content Pipeline (n8n + AI + Telegram)

> "Send a simple content idea to a Telegram bot and get platform-ready content generated, reviewed, and scheduled directly into Google Sheets."

---

## 📌 Project Overview
This project is an automated **Social Media Content Generation & Scheduling Pipeline** built using **n8n**, **Telegram Bot API**, **Google Gemini AI Agent**, and **Google Sheets**.

It eliminates manual content creation by converting raw ideas into formatted social media drafts (LinkedIn, X/Twitter, Instagram), managing approvals, and auto-scheduling them.

---

## 🛠 Tech Stack
- **Automation Engine:** n8n Workflow Automation
- **Messaging Interface:** Telegram Bot API
- **AI Model:** Google Gemini Chat Model (AI Agent)
- **Database / Content Calendar:** Google Sheets
- **Language / Environment:** Python 3.11+, Virtual Environment (`venv`)

---

## 🔄 Workflow Detailed Flow

### 1. New Content Request (Fallback Path)
- **Telegram Trigger** receives a new topic/idea.
- **Switch Node** routes it to the **AI Agent** (powered by **Google Gemini Chat Model**).
- The AI Agent generates formatted content for LinkedIn, X (Twitter), and Instagram.
- **Code Node** formats the output JSON.
- **Google Sheets Node** appends/updates the row with `Pending` status.
- **Telegram Node** sends the generated content back to the user with a unique `Content_ID` for approval.

### 2. Approval Management (Rule 0 - Approve)
- User replies with approval commands (e.g., `Approve 363-7`).
- **Analyzer Node** extracts the `Content_ID` and sets status to `Approved`.
- **Google Sheets Node** finds and updates the row status in the content calendar.
- **If Node** verifies success and sends an approval confirmation via Telegram.

### 3. Rejection Management (Rule 0 - Reject)
- User replies with rejection commands (e.g., `Reject 363-7` or `Reject 363-7: change intro`).
- **Analyzer Node** extracts the `Content_ID` and marks status as `Rejected`.
- **Google Sheets Node** updates the row status in Google Sheets to `Rejected`.
- **Telegram Node** notifies the user that the post status has been marked as rejected.

### 4. Schedule Management (Rule 1)
- User sends scheduling updates (e.g., `Schedule 363-7 on 2026-11-01`).
- **Schedule_Analyzer Node** extracts the target `Scheduled_Date` and `Content_ID`.
- **Google Sheets Node** updates the `Scheduled_Date` column in the sheet.
- **Telegram Node** sends a scheduling confirmation message back to Telegram.