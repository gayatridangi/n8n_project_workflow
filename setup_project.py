
import os

# Zaroori folders ki list
folders = [
    "workflows",
    "config",
    "docs"
]

# Zaroori files aur unka initial safe content
files = {
    ".env.example": """# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# AI / Claude API Configuration
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Google Sheets Configuration
GOOGLE_SHEET_ID=your_google_sheet_id_here
""",

    ".gitignore": """# Environment and secret files
.env
venv/
__pycache__/
*.pyc
.DS_Store
""",

    "requirements.txt": """# Python dependencies
python-dotenv==1.0.1
requests==2.31.0
""",

    "README.md": """# Project 07: Social Media Content Pipeline

> "Message an idea to a bot, get a week of platform-ready content back — with your own approval built in."

## Overview
An automated n8n workflow triggered via Telegram. Users send a content idea, target audience, and brand tone. The AI generates platform-specific drafts, and approval commands update the Google Sheets calendar.

## Setup & Installation
1. Clone repository and open in VS Code.
2. Create virtual environment and install dependencies:
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. Copy .env.example to .env and fill real credentials.
4. Import n8n workflow JSON into your n8n instance.
""",

    "config/sheet_columns.csv": """Content_ID,Content_Idea,Target_Audience,Brand_Tone,LinkedIn_Post,X_Thread,Instagram_Caption,Approval_Status,Scheduled_Date,Approved_At
363-7,AI Productivity Tools,Startup Founders,Professional,LinkedIn post draft...,X thread draft...,Instagram caption draft...,Pending,,
""",

    "workflows/n8n_telegram_content_pipeline.json": """{
  "name": "Social Media Content Pipeline",
  "nodes": [],
  "connections": {}
}
"""
}

def create_project_structure():
    print("🚀 Creating Social Media Content Pipeline structure...")
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"📁 Folder created: {folder}")
        
    for filepath, content in files.items():
        parent_dir = os.path.dirname(filepath)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"📄 File created: {filepath}")
        else:
            print(f"⚠️ File already exists: {filepath}")
            
    print("\n✅ Project structure setup completed successfully!")

if __name__ == "__main__":
    create_project_structure()
