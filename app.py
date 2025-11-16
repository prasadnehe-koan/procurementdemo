
import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="AI Business Assistant",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide default Streamlit menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {display:none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================
LOGO_URL = "https://media.licdn.com/dms/image/v2/C4E0BAQGtXskL4EvJmA/company-logo_200_200/company-logo_200_200/0/1632401962756/koantek_logo?e=2147483647&v=beta&t=D4GLT1Pu2vvxLR1iKZZbUJWN7K_uaPSF0T1mZl6Le-o"

st.markdown(f"""
<style>
    .main-header {{
        background:  linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.25rem 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.25rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    
    .header-content {{
        flex: 1;
    }}
    
    .header-logo {{
        height: 60px;
        width: auto;
        max-width: 200px;
        object-fit: contain;
    }}
    
    .main-header h1 {{
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0;
    }}
    
    .main-header p {{
        color: rgba(255,255,255,0.9);
        font-size: 0.875rem;
        margin: 0.25rem 0 0 0;
    }}
    
    .nav-card {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-bottom: 1rem;
    }}
    
    .nav-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(102,126,234,0.4);
    }}
    
    .nav-icon {{
        font-size: 3rem;
        margin-bottom: 1rem;
    }}
    
    .nav-title {{
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }}
    
    .nav-description {{
        font-size: 0.9rem;
        opacity: 0.9;
    }}
    
    /* Style the buttons to look like nav cards */
    /* Remove Streamlit's default orange background */
    button[kind="secondary"], button[kind="primary"], button[data-baseweb="button"] {{
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 2rem !important;
    height: 200px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    white-space: pre-line !important;
    font-size: 4rem !important;
    line-height: 1.8 !important;
}}

/* Hover */
button[kind="secondary"]:hover,
button[kind="primary"]:hover,
button[data-baseweb="button"]:hover {{
    transform: translateY(-5px) !important;
    box-shadow: 0 8px 12px rgba(102,126,234,0.4) !important;
}}

/* Pressed */
button[kind="secondary"]:active,
button[kind="primary"]:active,
button[data-baseweb="button"]:active {{
    transform: translateY(-2px) !important;
}}
/* Increase inside text + emoji icon size */
button[kind="secondary"],
button[kind="primary"],
button[data-baseweb="button"] {{
    font-size: 2rem !important;      /* ⬆️ Increase text size */
    line-height: 1rem !important;    /* Better spacing */
    padding-top: 2.5rem !important;
    padding-bottom: 2.5rem !important;
}}

/* If icon/emoji is used (📊, 💬 etc), increase size */
button[kind="secondary"] span,
button[kind="primary"] span,
button[data-baseweb="button"] div span {{
    font-size: 4 rem !important;
    line-height: 3.2rem !important;
}}     

/* To ensure multiline stays centered */
button[kind="secondary"] div,
button[kind="primary"] div,
button[data-baseweb="button"] div {{
    font-size: 1.1rem !important;
    white-space: pre-line !important;
    text-align: center !important;
}}


</style>

<div class="main-header">
    <div class="header-content">
        <h1>📊 AI Business Assistant</h1>
        <p>Choose your tool below</p>
    </div>
    <img src="{LOGO_URL}" class="header-logo" alt="Koantek Logo" onerror="this.style.display='none'">
</div>
""", unsafe_allow_html=True)

# ==========================================================
# NAVIGATION CARDS
# ==========================================================
st.markdown("## Select a Tool")

col1, col2 = st.columns(2)

with col1:
    if st.button("📊\n\nReport Generator\n\n AI-powered business reports", key="nav_report", use_container_width=True):
        st.switch_page("1_📊_Report_Generator.py")

with col2:
    if st.button("💬\n\nAI Chatbot\n\nChat with AI about your business data", key="nav_chat", use_container_width=True):
        st.switch_page("2_💬_Chatbot.py")

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 0.8rem; padding: 0.75rem;">
    <p style="color: #6b7280;">Powered by Koantek</p>
</div>
""", unsafe_allow_html=True)



# import streamlit as st
# import requests
# import json
# import time
# import pandas as pd
# from datetime import datetime

# # ==========================================================
# # CONFIGURATION — UPDATE THESE VALUES
# # ==========================================================

# DATABRICKS_INSTANCE = st.secrets.get('DATABRICKS_INSTANCE')
# DATABRICKS_TOKEN = st.secrets.get('DB_token')
# NOTEBOOK_PATH = st.secrets.get('NOTEBOOK_PATH')
# VOLUME_PATH = st.secrets.get('VOLUME_PATH')
# CLUSTER_ID = st.secrets.get('CLUSTER_ID')
# CHATBOT_ENDPOINT=st.secrets.get('CHATBOT_ENDPOINT')



# # ==========================================================
# # PAGE CONFIG
# # ==========================================================
# st.set_page_config(
#     page_title="AI Report Generator",
#     page_icon="📊",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ==========================================================
# # INITIALIZE SESSION STATE
# # ==========================================================
# if 'monitoring_jobs' not in st.session_state:
#     st.session_state.monitoring_jobs = []
# if 'completed_jobs' not in st.session_state:
#     st.session_state.completed_jobs = []
# if 'chat_messages' not in st.session_state:
#     st.session_state.chat_messages = []

# # ==========================================================
# # MODERN CSS STYLING WITH FIXED CHAT INPUT
# # ==========================================================
# st.markdown("""
# <style>
#     /* Global Styles */
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
#     .block-container {
#         padding-top: 1rem;
#         padding-left: 2rem;
#         padding-right: 2rem;
#         max-width: 1400px;
#     }
    
#     * {
#         font-family: 'Inter', sans-serif;
#     }
    
#     /* Header Styles */
#     .main-header {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         padding: 1.25rem 1.5rem;
#         border-radius: 10px;
#         margin-bottom: 1.25rem;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#     }
    
#     .header-content {
#         flex: 1;
#     }
    
#     .header-logo {
#         height: 60px;
#         width: auto;
#         max-width: 200px;
#         object-fit: contain;
#     }
    
#     .main-header h1 {
#         color: white;
#         font-size: 1.5rem;
#         font-weight: 700;
#         margin: 0;
#         display: flex;
#         align-items: center;
#         gap: 0.5rem;
#     }
    
#     .main-header p {
#         color: rgba(255,255,255,0.9);
#         font-size: 0.875rem;
#         margin: 0.25rem 0 0 0;
#     }
    
#     /* Theme Variables */
#     [data-testid="stAppViewContainer"][data-theme="dark"] {
#         --background-color: #0e1117;
#         --card-background: #262730;
#         --text-primary: #fafafa;
#         --text-secondary: #a3a8b4;
#         --border-color: #464a57;
#         --hover-background: #1e2029;
#     }
    
#     [data-testid="stAppViewContainer"][data-theme="light"] {
#         --background-color: #ffffff;
#         --card-background: #ffffff;
#         --text-primary: #1f2937;
#         --text-secondary: #6b7280;
#         --border-color: #e5e7eb;
#         --hover-background: #f9fafb;
#     }
    
#     /* Input & Button Styles */
#     .stTextInput > div > div > input {
#         border-radius: 8px !important;
#         border: 2px solid var(--border-color) !important;
#         padding: 0.6rem 0.875rem !important;
#         font-size: 0.9rem !important;
#         transition: all 0.2s ease !important;
#         background-color: var(--card-background) !important;
#         color: var(--text-primary) !important;
#     }
    
#     .stTextInput > div > div > input:focus {
#         border-color: #667eea !important;
#         box-shadow: 0 0 0 3px rgba(102,126,234,0.1) !important;
#     }
    
#     .stButton > button {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
#         color: white !important;
#         border: none !important;
#         border-radius: 8px !important;
#         padding: 0.6rem 1.5rem !important;
#         font-size: 0.9rem !important;
#         font-weight: 600 !important;
#         transition: all 0.3s ease !important;
#         box-shadow: 0 2px 4px rgba(102,126,234,0.3) !important;
#         width: 100% !important;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-2px) !important;
#         box-shadow: 0 6px 12px rgba(102,126,234,0.4) !important;
#     }
    
#     /* CHAT-SPECIFIC STYLES (Fixed Input) */
#     .st-emotion-cache-ztusae.e1tzin5v2, 
#     .st-emotion-cache-1cypcdb.e1tzin5v2 {
#         position: fixed;
#         bottom: 0px;
#         left: 0;
#         right: 0;
#         width: 100%;
#         max-width: 1400px;
#         margin: 0 auto;
#         padding: 1rem 2rem 1rem 2rem;
#         background: var(--background-color);
#         box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
#         z-index: 1000;
#         border-top: 1px solid var(--border-color);
#         box-sizing: border-box;
#     }
    
#     .main > div { 
#         padding-bottom: 120px; 
#     }

#     /* Message Bubbles */
#     .chat-message {
#         margin-bottom: 1rem;
#         padding: 0.875rem 1rem;
#         border-radius: 12px;
#         max-width: 80%;
#         word-wrap: break-word;
#         animation: fadeIn 0.3s ease-in;
#     }
    
#     @keyframes fadeIn {
#         from { opacity: 0; transform: translateY(10px); }
#         to { opacity: 1; transform: translateY(0); }
#     }
    
#     .chat-message.user {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         margin-left: auto;
#         margin-right: 0;
#         text-align: left;
#     }
    
#     .chat-message.assistant {
#         background: var(--hover-background);
#         color: var(--text-primary);
#         border: 1px solid var(--border-color);
#         margin-right: auto;
#         margin-left: 0;
#     }
    
#     .chat-message-role {
#         font-size: 0.75rem;
#         font-weight: 600;
#         margin-bottom: 0.35rem;
#         opacity: 0.85;
#         display: flex;
#         align-items: center;
#         gap: 0.3rem;
#     }
    
#     .chat-message-content {
#         font-size: 0.9rem;
#         line-height: 1.6;
#         white-space: pre-wrap;
#     }

#     /* Empty State */
#     .chat-empty-wrapper {
#         height: 500px; 
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         background: var(--card-background);
#         border: 2px solid var(--border-color);
#         border-radius: 10px;
#     }
    
#     .chat-empty-state {
#         text-align: center;
#         color: var(--text-secondary);
#     }
    
#     .chat-empty-icon {
#         font-size: 4rem;
#         margin-bottom: 1rem;
#         opacity: 0.4;
#     }
    
#     .chat-empty-title {
#         font-size: 1.5rem;
#         font-weight: 700;
#         color: var(--text-primary);
#         margin-bottom: 0.5rem;
#     }
    
#     /* Progress Box */
#     .progress-box {
#         background: linear-gradient(135deg, rgba(102,126,234,0.1) 0%, rgba(118,75,162,0.1) 100%);
#         border: 2px solid #667eea;
#         border-radius: 8px;
#         padding: 0.75rem 1rem;
#         margin: 0.5rem 0 1rem 0;
#         display: flex;
#         align-items: center;
#         gap: 0.75rem;
#     }
    
#     .progress-icon {
#         font-size: 1.5rem;
#         animation: pulse 2s ease-in-out infinite;
#     }
    
#     @keyframes pulse {
#         0%, 100% { opacity: 1; transform: scale(1); }
#         50% { opacity: 0.7; transform: scale(1.05); }
#     }
    
#     .progress-content {
#         flex: 1;
#     }
    
#     .progress-text {
#         font-size: 0.95rem;
#         font-weight: 600;
#         color: #667eea;
#         margin-bottom: 0.15rem;
#     }
    
#     .progress-subtext {
#         font-size: 0.8rem;
#         color: var(--text-secondary);
#     }
    
#     /* Report Card Styles */
#     .report-card {
#         background: var(--card-background);
#         border: 1px solid var(--border-color);
#         border-radius: 10px;
#         padding: 0.875rem 1rem;
#         margin-bottom: 0.75rem;
#         transition: all 0.3s ease;
#         box-shadow: 0 1px 3px rgba(0,0,0,0.05);
#     }
    
#     .report-card:hover {
#         box-shadow: 0 4px 8px rgba(102,126,234,0.2);
#         transform: translateY(-1px);
#         border-color: #667eea;
#         background: var(--hover-background);
#     }
    
#     .report-card.new-report {
#         border: 2px solid #10b981;
#         background: linear-gradient(135deg, rgba(16,185,129,0.1) 0%, rgba(16,185,129,0.05) 100%);
#         animation: highlight 2s ease-in-out;
#     }
    
#     @keyframes highlight {
#         0%, 100% { opacity: 1; }
#         50% { opacity: 0.8; }
#     }
    
#     .report-name {
#         font-size: 0.95rem;
#         font-weight: 600;
#         color: var(--text-primary);
#         margin-bottom: 0.35rem;
#         display: flex;
#         align-items: center;
#         gap: 0.4rem;
#     }
    
#     .report-meta {
#         display: flex;
#         gap: 1rem;
#         color: var(--text-secondary);
#         font-size: 0.8rem;
#         margin-top: 0.35rem;
#     }
    
#     .report-meta-item {
#         display: flex;
#         align-items: center;
#         gap: 0.3rem;
#     }
    
#     /* Download Button */
#     .stDownloadButton > button {
#         background: #10b981 !important;
#         color: white !important;
#         border: none !important;
#         border-radius: 8px !important;
#         padding: 0.45rem 1rem !important;
#         font-size: 0.85rem !important;
#         font-weight: 600 !important;
#         transition: all 0.2s ease !important;
#         width: 100% !important;
#     }
    
#     .stDownloadButton > button:hover {
#         background: #059669 !important;
#         transform: scale(1.02) !important;
#     }
    
#     /* Section Headers */
#     .section-header {
#         font-size: 1.25rem;
#         font-weight: 700;
#         color: var(--text-primary);
#         margin: 1.25rem 0 0.75rem 0;
#         display: flex;
#         align-items: center;
#         gap: 0.5rem;
#     }
    
#     /* Stats Cards */
#     .stat-card {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         padding: 1rem;
#         border-radius: 10px;
#         color: white;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#     }
    
#     .stat-value {
#         font-size: 1.5rem;
#         font-weight: 700;
#         margin-bottom: 0.15rem;
#     }
    
#     .stat-label {
#         font-size: 0.8rem;
#         opacity: 0.9;
#     }
    
#     /* Empty State */
#     .empty-state {
#         text-align: center;
#         padding: 3rem;
#         color: var(--text-secondary);
#     }
    
#     .empty-state-icon {
#         font-size: 4rem;
#         margin-bottom: 1rem;
#         opacity: 0.5;
#     }
    
#     .empty-state h3 {
#         color: var(--text-primary);
#     }
    
#     /* Filter Select */
#     .stSelectbox > div > div {
#         border-radius: 8px !important;
#         border: 2px solid var(--border-color) !important;
#         transition: all 0.2s ease !important;
#         background-color: var(--card-background) !important;
#     }
    
#     .stSelectbox > div > div:focus-within {
#         border-color: #667eea !important;
#         box-shadow: 0 0 0 3px rgba(102,126,234,0.1) !important;
#     }
    
#     /* Hide Streamlit elements in chat input area */
#     .stTextInput > label {
#         display: none;
#     }
    
#     /* Footer */
#     .footer-text {
#         color: var(--text-secondary);
#     }
# </style>
# """, unsafe_allow_html=True)

# # ==========================================================
# # HELPER FUNCTIONS
# # ==========================================================
# def check_job_status(run_id):
#     """Check the status of a Databricks job run"""
#     headers = {
#         "Authorization": f"Bearer {DATABRICKS_TOKEN}",
#         "Content-Type": "application/json"
#     }
    
#     status_url = f"{DATABRICKS_INSTANCE}/api/2.1/jobs/runs/get?run_id={run_id}"
    
#     try:
#         response = requests.get(status_url, headers=headers, timeout=30)
#         if response.status_code == 200:
#             data = response.json()
#             state = data.get('state', {})
#             life_cycle_state = state.get('life_cycle_state', 'UNKNOWN')
#             result_state = state.get('result_state', None)
            
#             return {
#                 'life_cycle_state': life_cycle_state,
#                 'result_state': result_state,
#                 'is_terminal': life_cycle_state in ['TERMINATED', 'SKIPPED', 'INTERNAL_ERROR']
#             }
#     except:
#         pass
    
#     return None

# def get_report_count():
#     """Get current count of PDF reports"""
#     headers = {
#         "Authorization": f"Bearer {DATABRICKS_TOKEN}",
#         "Accept": "application/json"
#     }
    
#     url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/directories{VOLUME_PATH}"
    
#     try:
#         response = requests.get(url, headers=headers, timeout=30)
#         if response.status_code == 200:
#             files = response.json().get("contents", [])
#             df = pd.DataFrame(files)
#             if not df.empty:
#                 pdf_count = len(df[~df["is_directory"] & df["name"].str.endswith(".pdf")])
#                 return pdf_count
#     except:
#         pass
    
#     return 0

# def chat_with_bot(message):
#     """Collect all output_text content from Databricks model responses"""
#     if not all([DATABRICKS_TOKEN, CHATBOT_ENDPOINT]):
#         return "Error: Chatbot endpoint or token is not configured."
    
#     headers = {
#         "Authorization": f"Bearer {DATABRICKS_TOKEN}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "input": [
#             {
#                 "status": None,
#                 "content": message,
#                 "role": "user",
#                 "type": "message"
#             }
#         ]
#     }

#     try:
#         response = requests.post(CHATBOT_ENDPOINT, headers=headers, json=payload, timeout=300)
#         if response.status_code != 200:
#             return f"Error: {response.status_code} - {response.text}"

#         texts = []
#         raw = response.text.strip()
        
#         # Handle NDJSON
#         if '\n' in raw:
#             for line in raw.splitlines():
#                 line = line.strip()
#                 if not line:
#                     continue
#                 try:
#                     data = json.loads(line)
#                     if data.get("type") == "response.output_item.done":
#                         item = data.get("item", {})
#                         for content in item.get("content", []):
#                             if content.get("type") == "output_text":
#                                 texts.append(content.get("text", ""))
#                 except json.JSONDecodeError:
#                     continue
#         else:
#             try:
#                 data = json.loads(raw)
#                 if isinstance(data, dict) and "output" in data:
#                     for msg in data["output"]:
#                         for content in msg.get("content", []):
#                             if content.get("type") == "output_text":
#                                 texts.append(content.get("text", ""))
#             except Exception:
#                 pass

#         return "\n\n---\n\n".join(texts) if texts else "No response received. Check model/endpoint status."

#     except Exception as e:
#         return f"Error: {str(e)}"

# # ==========================================================
# # HEADER
# # ==========================================================
# LOGO_URL = "https://media.licdn.com/dms/image/v2/C4E0BAQGtXskL4EvJmA/company-logo_200_200/company-logo_200_200/0/1632401962756/koantek_logo?e=2147483647&v=beta&t=D4GLT1Pu2vvxLR1iKZZbUJWN7K_uaPSF0T1mZl6Le-o"

# st.markdown(f"""
# <div class="main-header">
#     <div class="header-content">
#         <h1>📊 AI Business Assistant</h1>
#         <p>Generate reports and chat with AI</p>
#     </div>
#     <img src="{LOGO_URL}" class="header-logo" alt="Koantek Logo" onerror="this.style.display='none'">
# </div>
# """, unsafe_allow_html=True)

# # ==========================================================
# # TABS
# # ==========================================================
# tab1, tab2 = st.tabs(["📊 Report Generator", "💬 Chatbot"])

# # ==========================================================
# # TAB 1: REPORT GENERATOR
# # ==========================================================
# with tab1:
#     col1, col2 = st.columns([5, 1], vertical_alignment="bottom")

#     with col1:
#         report_query = st.text_input(
#             "What would you like to analyze?",
#             placeholder="e.g., violation report / BU Analysis report etc.",
#             label_visibility="visible",
#             key="report_query_tab1"
#         )

#     with col2:
#         st.write("")
#         run_btn = st.button(
#             "Generate", 
#             use_container_width=True,
#             key="run_btn_tab1"
#         )

#     # JOB SUBMISSION & MONITORING LOGIC
#     if run_btn:
#         if not report_query.strip():
#             st.warning("⚠️ Please enter a query to generate a report.")
#         elif not all([DATABRICKS_TOKEN, DATABRICKS_INSTANCE, CLUSTER_ID, NOTEBOOK_PATH]):
#             st.error("🔧 Configuration Error: Please check your Databricks settings.")
#         else:
#             headers = {
#                 "Authorization": f"Bearer {DATABRICKS_TOKEN}",
#                 "Content-Type": "application/json"
#             }
            
#             payload = {
#                 "run_name": f"ai_report_{int(time.time())}",
#                 "existing_cluster_id": CLUSTER_ID,
#                 "notebook_task": {
#                     "notebook_path": NOTEBOOK_PATH,
#                     "base_parameters": {"user_question": report_query}
#                 }
#             }
            
#             submit_url = f"{DATABRICKS_INSTANCE}/api/2.1/jobs/runs/submit"
            
#             with st.spinner("🔄 Submitting job to Databricks..."):
#                 try:
#                     res = requests.post(submit_url, headers=headers, data=json.dumps(payload), timeout=30)
                    
#                     if res.status_code == 200:
#                         run_id = res.json().get("run_id")
#                         st.session_state.monitoring_jobs.append({
#                             'run_id': run_id,
#                             'query': report_query,
#                             'start_time': time.time(),
#                             'initial_count': get_report_count()
#                         })
#                         st.success(f"✅ Job submitted successfully! Run ID: `{run_id}`")
#                         st.info("💡 You can submit more queries while this one processes.")
#                         time.sleep(1)
#                         st.rerun()
#                     else:
#                         st.error(f"❌ Failed to start job: {res.status_code} - {res.text}")
#                 except requests.exceptions.RequestException as e:
#                     st.error(f"❌ Connection Error: {str(e)}")

#     # Job monitoring display
#     if st.session_state.monitoring_jobs:
#         jobs_to_remove = []
#         for idx, job in enumerate(st.session_state.monitoring_jobs):
#             run_id = job['run_id']
#             job_status = check_job_status(run_id)
#             current_report_count = get_report_count()
#             elapsed_time = int(time.time() - job['start_time'])
            
#             if current_report_count > job['initial_count'] or (job_status and job_status['is_terminal'] and job_status['result_state'] == 'SUCCESS'):
#                 if current_report_count > job['initial_count'] or elapsed_time > 300:
#                     jobs_to_remove.append(idx)
#                     if run_id not in st.session_state.completed_jobs:
#                         st.session_state.completed_jobs.append(run_id)
#                         st.success(f" Report generated for: {job['query']}")

#             elif job_status and job_status['is_terminal'] and job_status['result_state'] != 'SUCCESS':
#                 jobs_to_remove.append(idx)
#                 st.error(f"❌ Job failed: {job['query']} - {job_status['result_state']}")
        
#         for idx in sorted(jobs_to_remove, reverse=True):
#             st.session_state.monitoring_jobs.pop(idx)
        
#         if st.session_state.monitoring_jobs:
#             st.markdown("---")
#             st.markdown("### 🔄 Active Jobs")
#             for job in st.session_state.monitoring_jobs:
#                 elapsed_time = int(time.time() - job['start_time'])
#                 minutes, seconds = divmod(elapsed_time, 60)
#                 col1, col2 = st.columns([6, 1])
#                 with col1:
#                     st.markdown(f"""
#                     <div class="progress-box">
#                         <div class="progress-icon">⚙️</div>
#                         <div class="progress-content">
#                             <div class="progress-text">{job['query']}</div>
#                             <div class="progress-subtext">Run ID: {job['run_id']} • {minutes}m {seconds}s elapsed</div>
#                         </div>
#                     </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.write("")
#                     if st.button("Cancel", key=f"cancel_{job['run_id']}", use_container_width=True):
#                         st.session_state.monitoring_jobs = [j for j in st.session_state.monitoring_jobs if j['run_id'] != job['run_id']]
#                         st.rerun()
#             time.sleep(5)
#             st.rerun()

#     # REPORTS SECTION
#     col_header, col_filter = st.columns([3, 1])
#     with col_header:
#         st.markdown('<div class="section-header">📂 Generated Reports</div>', unsafe_allow_html=True)
#     with col_filter:
#         st.write("")
#         date_filter = st.selectbox(
#             "🔍 Filter",
#             ["Last 5 Reports", "Today", "Last 7 Days", "Last 30 Days", "All Reports"],
#             label_visibility="collapsed",
#             key="report_filter_tab1"
#         )

#     if not all([DATABRICKS_TOKEN, DATABRICKS_INSTANCE, VOLUME_PATH]):
#         st.warning("🔧 Please configure Databricks credentials to view reports.")
#     else:
#         headers = {"Authorization": f"Bearer {DATABRICKS_TOKEN}", "Accept": "application/json"}
#         url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/directories{VOLUME_PATH}"
        
#         try:
#             with st.spinner("📥 Loading reports..."):
#                 response = requests.get(url, headers=headers, timeout=60)
            
#             if response.status_code == 200:
#                 files = response.json().get("contents", [])
                
#                 if not files:
#                     st.markdown("""<div class="empty-state"><div class="empty-state-icon">📭</div><h3>No Reports Yet</h3><p>Generate your first report using the form above</p></div>""", unsafe_allow_html=True)
#                 else:
#                     df = pd.DataFrame(files)
#                     df["last_modified"] = pd.to_datetime(df["last_modified"], unit="ms")
#                     pdf_df = df[(~df["is_directory"]) & (df["name"].str.endswith(".pdf"))].sort_values("last_modified", ascending=False)
                    
#                     now = datetime.now()
#                     if date_filter == "Today": 
#                         pdf_df = pdf_df[pdf_df["last_modified"].dt.date == now.date()]
#                     elif date_filter == "Last 7 Days": 
#                         pdf_df = pdf_df[pdf_df["last_modified"] >= now - pd.Timedelta(days=7)]
#                     elif date_filter == "Last 30 Days": 
#                         pdf_df = pdf_df[pdf_df["last_modified"] >= now - pd.Timedelta(days=30)]
#                     elif date_filter == "Last 5 Reports": 
#                         pdf_df = pdf_df.head(5)
                    
#                     total_reports = len(pdf_df)
#                     total_size_mb = round(pdf_df["file_size"].sum() / (1024 * 1024), 2) if not pdf_df.empty else 0
                    
#                     col1, col2, col3 = st.columns(3)
#                     with col1: 
#                         st.markdown(f"""<div class="stat-card"><div class="stat-value">{total_reports}</div><div class="stat-label">Total Reports</div></div>""", unsafe_allow_html=True)
#                     with col2: 
#                         st.markdown(f"""<div class="stat-card"><div class="stat-value">{total_size_mb}</div><div class="stat-label">Total Size (MB)</div></div>""", unsafe_allow_html=True)
#                     with col3:
#                         latest = pdf_df.iloc[0]["last_modified"].strftime("%b %d") if not pdf_df.empty else "N/A"
#                         st.markdown(f"""<div class="stat-card"><div class="stat-value">{latest}</div><div class="stat-label">Latest Report</div></div>""", unsafe_allow_html=True)
                    
#                     st.write("")
                    
#                     if pdf_df.empty:
#                         st.info("📄 No reports match the selected filter.")
#                     else:
#                         for idx, row in pdf_df.iterrows():
#                             file_name, file_path = row["name"], row["path"]
#                             size_kb = round(row["file_size"] / 1024, 1)
#                             mod_time = row["last_modified"].strftime("%b %d, %Y %I:%M %p")
#                             is_new = (datetime.now() - row["last_modified"]).total_seconds() < 30
                            
#                             col1, col2 = st.columns([5, 1])
#                             with col1:
#                                 card_class = "report-card new-report" if is_new else "report-card"
#                                 new_badge = "🆕 " if is_new else ""
#                                 st.markdown(f"""
#                                 <div class="{card_class}">
#                                     <div class="report-name">{new_badge}📄 {file_name}</div>
#                                     <div class="report-meta"><div class="report-meta-item">🕒 {mod_time}</div><div class="report-meta-item">💾 {size_kb} KB</div></div>
#                                 </div>
#                                 """, unsafe_allow_html=True)
                            
#                             with col2:
#                                 file_api_url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/files{file_path}"
#                                 try:
#                                     file_res = requests.get(file_api_url, headers=headers, timeout=60) 
#                                     if file_res.status_code == 200:
#                                         pdf_bytes = file_res.content
#                                         st.write("")
#                                         st.download_button(label="⬇️ Download", data=pdf_bytes, file_name=file_name, mime="application/pdf", key=f"download_{file_name}_{idx}")
#                                     else: 
#                                         st.error(f"Error: {file_res.status_code}")
#                                 except requests.exceptions.RequestException as e: 
#                                     st.error(f"Failed to fetch file")
            
#             elif response.status_code == 404: 
#                 st.warning("📁 Volume path not found. Please verify your VOLUME_PATH configuration.")
#             else: 
#                 st.error(f"❌ Error listing files: {response.status_code} - {response.text}")
        
#         except requests.exceptions.RequestException as e: 
#             st.error(f"❌ Connection Error: Unable to connect to Databricks. {str(e)}")


# # ==========================================================
# # TAB 2: CHATBOT (Fixed Input)
# # ==========================================================
# with tab2:
#     # Scrollable Messages Area
#     messages_container = st.container(height=500) 
    
#     if not st.session_state.chat_messages:
#         messages_container.markdown(f"""
#         <div class="chat-empty-wrapper">
#             <div class="chat-empty-state">
#                 <div class="chat-empty-icon">💬</div>
#                 <div class="chat-empty-title">Start a conversation</div>
#                 <div class="chat-empty-subtitle">Ask me anything about your business data</div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
#     else:
#         for msg in st.session_state.chat_messages:
#             role_class = "user" if msg["role"] == "user" else "assistant"
#             role_emoji = "👤" if msg["role"] == "user" else "🤖"
#             content = str(msg["content"]) if not isinstance(msg["content"], str) else msg["content"]
            
#             messages_container.markdown(f"""
#             <div class="chat-message {role_class}">
#                 <div class="chat-message-role">{role_emoji} {msg["role"].capitalize()}</div>
#                 <div class="chat-message-content">{content}</div>
#             </div>
#             """, unsafe_allow_html=True)
    
#     # Fixed Input Area
#     st.markdown('<div class="chat-input-fixed">', unsafe_allow_html=True)
    
#     col1, col2, col3 = st.columns([7, 1, 1])
    
#     with col1:
#         chat_input = st.text_input(
#             "Message",
#             placeholder="Type your message here...",
#             label_visibility="collapsed",
#             key="chat_input_tab2"
#         )
    
#     with col2:
#         send_btn = st.button("📤 Send", use_container_width=True, key="send_chat_tab2")
    
#     with col3:
#         clear_btn = st.button("🗑️ Clear", use_container_width=True, key="clear_chat_tab2", 
#                               disabled=len(st.session_state.chat_messages) == 0)
    
#     st.markdown('</div>', unsafe_allow_html=True) 

#     # Handle button actions
#     if send_btn and chat_input.strip():
#         if not all([CHATBOT_ENDPOINT]):
#             st.session_state.chat_messages.append({"role": "user", "content": chat_input})
#             st.session_state.chat_messages.append({"role": "assistant", "content": "Chatbot endpoint is not configured."})
#             st.rerun()
#         else:
#             st.session_state.chat_messages.append({
#                 "role": "user",
#                 "content": chat_input
#             })
            
#             with st.spinner("🤖 Thinking..."):
#                 bot_response = chat_with_bot(chat_input)
            
#             st.session_state.chat_messages.append({
#                 "role": "assistant",
#                 "content": bot_response
#             })
            
#             st.rerun()
    
#     if clear_btn:
#         st.session_state.chat_messages = []
#         st.rerun()
        
# # ==========================================================
# # FOOTER
# # ==========================================================
# st.markdown("---")
# st.markdown("""
# <div style="text-align: center; font-size: 0.8rem; padding: 0.75rem;">
#     <p class="footer-text">Powered by Koantek</p>
# </div>
# """, unsafe_allow_html=True)

# # import streamlit as st
# # import requests
# # import json
# # import os
# # import time
# # import urllib.parse
# # import pandas as pd
# # from datetime import datetime

# # # ==========================================================
# # # CONFIGURATION — UPDATE THESE VALUES
# # # ==========================================================
# # DATABRICKS_INSTANCE = st.secrets['DATABRICKS_INSTANCE']
# # DATABRICKS_TOKEN =st.secrets['DB_token']  # replace with your PAT
# # NOTEBOOK_PATH = st.secrets['NOTEBOOK_PATH']
# # VOLUME_PATH = st.secrets['VOLUME_PATH']
# # CLUSTER_ID = st.secrets['CLUSTER_ID']
# # CHATBOT_ENDPOINT = st.secrets['CHATBOT_ENDPOINT']

# # # ==========================================================
# # # PAGE CONFIG
# # # ==========================================================
# # st.set_page_config(
# #     page_title="AI Report Generator",
# #     page_icon="📊",
# #     layout="wide",
# #     initial_sidebar_state="collapsed"
# # )

# # # ==========================================================
# # # INITIALIZE SESSION STATE
# # # ==========================================================
# # if 'monitoring_jobs' not in st.session_state:
# #     st.session_state.monitoring_jobs = []  # List of active jobs
# # if 'completed_jobs' not in st.session_state:
# #     st.session_state.completed_jobs = []  # Track completed jobs
# # if 'chat_messages' not in st.session_state:
# #     st.session_state.chat_messages = []  # Chat history

# # # ==========================================================
# # # MODERN CSS STYLING WITH FIXED CHAT INPUT
# # # ==========================================================
# # st.markdown("""
# # <style>
# #     /* Global Styles */
# #     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
# #     .block-container {
# #         padding-top: 1rem;
# #         padding-left: 2rem;
# #         padding-right: 2rem;
# #         max-width: 1400px;
# #     }
    
# #     * {
# #         font-family: 'Inter', sans-serif;
# #     }
    
# #     /* Header Styles */
# #     .main-header {
# #         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# #         padding: 1.25rem 1.5rem;
# #         border-radius: 10px;
# #         margin-bottom: 1.25rem;
# #         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
# #         display: flex;
# #         justify-content: space-between;
# #         align-items: center;
# #     }
    
# #     .header-content {
# #         flex: 1;
# #     }
    
# #     .header-logo {
# #         height: 60px;
# #         width: auto;
# #         max-width: 200px;
# #         object-fit: contain;
# #     }
    
# #     .main-header h1 {
# #         color: white;
# #         font-size: 1.5rem;
# #         font-weight: 700;
# #         margin: 0;
# #         display: flex;
# #         align-items: center;
# #         gap: 0.5rem;
# #     }
    
# #     .main-header p {
# #         color: rgba(255,255,255,0.9);
# #         font-size: 0.875rem;
# #         margin: 0.25rem 0 0 0;
# #     }
    
# #     /* Dark mode detection */
# #     @media (prefers-color-scheme: dark) {
# #         :root {
# #             --background-color: #1e1e1e;
# #             --card-background: #262626;
# #             --text-primary: #ffffff;
# #             --text-secondary: #a0a0a0;
# #             --border-color: #404040;
# #             --hover-background: #2d2d2d;
# #         }
# #     }
    
# #     @media (prefers-color-scheme: light) {
# #         :root {
# #             --background-color: #ffffff;
# #             --card-background: #ffffff;
# #             --text-primary: #1f2937;
# #             --text-secondary: #6b7280;
# #             --border-color: #e5e7eb;
# #             --hover-background: #f9fafb;
# #         }
# #     }
    
# #     /* Force theme variables for Streamlit dark mode */
# #     [data-testid="stAppViewContainer"][data-theme="dark"] {
# #         --background-color: #0e1117;
# #         --card-background: #262730;
# #         --text-primary: #fafafa;
# #         --text-secondary: #a3a8b4;
# #         --border-color: #464a57;
# #         --hover-background: #1e2029;
# #     }
    
# #     [data-testid="stAppViewContainer"][data-theme="light"] {
# #         --background-color: #ffffff;
# #         --card-background: #ffffff;
# #         --text-primary: #1f2937;
# #         --text-secondary: #6b7280;
# #         --border-color: #e5e7eb;
# #         --hover-background: #f9fafb;
# #     }
    
# #     .stTextInput > div > div > input {
# #         border-radius: 8px !important;
# #         border: 2px solid var(--border-color) !important;
# #         padding: 0.6rem 0.875rem !important;
# #         font-size: 0.9rem !important;
# #         transition: all 0.2s ease !important;
# #         background-color: var(--card-background) !important;
# #         color: var(--text-primary) !important;
# #     }
    
# #     .stTextInput > div > div > input:focus {
# #         border-color: #667eea !important;
# #         box-shadow: 0 0 0 3px rgba(102,126,234,0.1) !important;
# #     }
    
# #     /* Button Styles */
# #     .stButton > button {
# #         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
# #         color: white !important;
# #         border: none !important;
# #         border-radius: 8px !important;
# #         padding: 0.6rem 1.5rem !important;
# #         font-size: 0.9rem !important;
# #         font-weight: 600 !important;
# #         transition: all 0.3s ease !important;
# #         box-shadow: 0 2px 4px rgba(102,126,234,0.3) !important;
# #         width: 100% !important;
# #     }
    
# #     .stButton > button:hover {
# #         transform: translateY(-2px) !important;
# #         box-shadow: 0 6px 12px rgba(102,126,234,0.4) !important;
# #     }
    
# #     /* Progress Box */
# #     .progress-box {
# #         background: linear-gradient(135deg, rgba(102,126,234,0.1) 0%, rgba(118,75,162,0.1) 100%);
# #         border: 2px solid #667eea;
# #         border-radius: 8px;
# #         padding: 0.75rem 1rem;
# #         margin: 0.5rem 0 1rem 0;
# #         display: flex;
# #         align-items: center;
# #         gap: 0.75rem;
# #     }
    
# #     .progress-icon {
# #         font-size: 1.5rem;
# #         animation: pulse 2s ease-in-out infinite;
# #     }
    
# #     @keyframes pulse {
# #         0%, 100% { opacity: 1; transform: scale(1); }
# #         50% { opacity: 0.7; transform: scale(1.05); }
# #     }
    
# #     .progress-content {
# #         flex: 1;
# #     }
    
# #     .progress-text {
# #         font-size: 0.95rem;
# #         font-weight: 600;
# #         color: #667eea;
# #         margin-bottom: 0.15rem;
# #     }
    
# #     .progress-subtext {
# #         font-size: 0.8rem;
# #         color: var(--text-secondary);
# #     }
    
# #     /* Report Card Styles */
# #     .report-card {
# #         background: var(--card-background);
# #         border: 1px solid var(--border-color);
# #         border-radius: 10px;
# #         padding: 0.875rem 1rem;
# #         margin-bottom: 0.75rem;
# #         transition: all 0.3s ease;
# #         box-shadow: 0 1px 3px rgba(0,0,0,0.05);
# #     }
    
# #     .report-card:hover {
# #         box-shadow: 0 4px 8px rgba(102,126,234,0.2);
# #         transform: translateY(-1px);
# #         border-color: #667eea;
# #         background: var(--hover-background);
# #     }
    
# #     .report-card.new-report {
# #         border: 2px solid #10b981;
# #         background: linear-gradient(135deg, rgba(16,185,129,0.1) 0%, rgba(16,185,129,0.05) 100%);
# #         animation: highlight 2s ease-in-out;
# #     }
    
# #     @keyframes highlight {
# #         0%, 100% { opacity: 1; }
# #         50% { opacity: 0.8; }
# #     }
    
# #     .report-name {
# #         font-size: 0.95rem;
# #         font-weight: 600;
# #         color: var(--text-primary);
# #         margin-bottom: 0.35rem;
# #         display: flex;
# #         align-items: center;
# #         gap: 0.4rem;
# #     }
    
# #     .report-meta {
# #         display: flex;
# #         gap: 1rem;
# #         color: var(--text-secondary);
# #         font-size: 0.8rem;
# #         margin-top: 0.35rem;
# #     }
    
# #     .report-meta-item {
# #         display: flex;
# #         align-items: center;
# #         gap: 0.3rem;
# #     }
    
# #     /* Download Button */
# #     .stDownloadButton > button {
# #         background: #10b981 !important;
# #         color: white !important;
# #         border: none !important;
# #         border-radius: 8px !important;
# #         padding: 0.45rem 1rem !important;
# #         font-size: 0.85rem !important;
# #         font-weight: 600 !important;
# #         transition: all 0.2s ease !important;
# #         width: 100% !important;
# #     }
    
# #     .stDownloadButton > button:hover {
# #         background: #059669 !important;
# #         transform: scale(1.02) !important;
# #     }
    
# #     /* Section Headers */
# #     .section-header {
# #         font-size: 1.25rem;
# #         font-weight: 700;
# #         color: var(--text-primary);
# #         margin: 1.25rem 0 0.75rem 0;
# #         display: flex;
# #         align-items: center;
# #         gap: 0.5rem;
# #     }
    
# #     /* Stats Cards */
# #     .stat-card {
# #         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# #         padding: 1rem;
# #         border-radius: 10px;
# #         color: white;
# #         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
# #     }
    
# #     .stat-value {
# #         font-size: 1.5rem;
# #         font-weight: 700;
# #         margin-bottom: 0.15rem;
# #     }
    
# #     .stat-label {
# #         font-size: 0.8rem;
# #         opacity: 0.9;
# #     }
    
# #     /* Empty State */
# #     .empty-state {
# #         text-align: center;
# #         padding: 3rem;
# #         color: var(--text-secondary);
# #     }
    
# #     .empty-state-icon {
# #         font-size: 4rem;
# #         margin-bottom: 1rem;
# #         opacity: 0.5;
# #     }
    
# #     .empty-state h3 {
# #         color: var(--text-primary);
# #     }
    
# #     /* Filter Select */
# #     .stSelectbox > div > div {
# #         border-radius: 8px !important;
# #         border: 2px solid var(--border-color) !important;
# #         transition: all 0.2s ease !important;
# #         background-color: var(--card-background) !important;
# #     }
    
# #     .stSelectbox > div > div:focus-within {
# #         border-color: #667eea !important;
# #         box-shadow: 0 0 0 3px rgba(102,126,234,0.1) !important;
# #     }
    
# #     /* Alert overrides for dark mode */
# #     .stAlert {
# #         background-color: var(--card-background) !important;
# #         border-color: var(--border-color) !important;
# #         color: var(--text-primary) !important;
# #     }
    
# #     /* ChatGPT-Style Chat Interface */
# #     .chat-container {
# #         display: flex;
# #         flex-direction: column;
# #         height: calc(100vh - 250px);
# #         position: relative;
# #     }
    
# #     .chat-messages-wrapper {
# #         flex: 1;
# #         overflow-y: auto;
# #         padding: 1rem;
# #         margin-bottom: 0;
# #         background: var(--card-background);
# #         border: 2px solid var(--border-color);
# #         border-radius: 10px 10px 0 0;
# #         scroll-behavior: smooth;
# #     }
    
# #     /* Custom scrollbar */
# #     .chat-messages-wrapper::-webkit-scrollbar {
# #         width: 8px;
# #     }
    
# #     .chat-messages-wrapper::-webkit-scrollbar-track {
# #         background: var(--card-background);
# #         border-radius: 4px;
# #     }
    
# #     .chat-messages-wrapper::-webkit-scrollbar-thumb {
# #         background: var(--border-color);
# #         border-radius: 4px;
# #     }
    
# #     .chat-messages-wrapper::-webkit-scrollbar-thumb:hover {
# #         background: #667eea;
# #     }
    
# #     .chat-input-fixed {
# #         position: sticky;
# #         bottom: 0;
# #         background: var(--card-background);
# #         border: 2px solid var(--border-color);
# #         border-top: none;
# #         border-radius: 0 0 10px 10px;
# #         padding: 1rem;
# #         box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
# #         z-index: 100;
# #     }
    
# #     .chat-message {
# #         margin-bottom: 1rem;
# #         padding: 0.875rem 1rem;
# #         border-radius: 12px;
# #         max-width: 80%;
# #         word-wrap: break-word;
# #         animation: fadeIn 0.3s ease-in;
# #     }
    
# #     @keyframes fadeIn {
# #         from { opacity: 0; transform: translateY(10px); }
# #         to { opacity: 1; transform: translateY(0); }
# #     }
    
# #     .chat-message.user {
# #         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# #         color: white;
# #         margin-left: auto;
# #         margin-right: 0;
# #         text-align: left;
# #     }
    
# #     .chat-message.assistant {
# #         background: var(--hover-background);
# #         color: var(--text-primary);
# #         border: 1px solid var(--border-color);
# #         margin-right: auto;
# #         margin-left: 0;
# #     }
    
# #     .chat-message-role {
# #         font-size: 0.75rem;
# #         font-weight: 600;
# #         margin-bottom: 0.35rem;
# #         opacity: 0.85;
# #         display: flex;
# #         align-items: center;
# #         gap: 0.3rem;
# #     }
    
# #     .chat-message-content {
# #         font-size: 0.9rem;
# #         line-height: 1.6;
# #         white-space: pre-wrap;
# #     }
    
# #     .chat-empty-state {
# #         display: flex;
# #         flex-direction: column;
# #         align-items: center;
# #         justify-content: center;
# #         height: 100%;
# #         color: var(--text-secondary);
# #         text-align: center;
# #         padding: 2rem;
# #     }
    
# #     .chat-empty-icon {
# #         font-size: 4rem;
# #         margin-bottom: 1rem;
# #         opacity: 0.4;
# #     }
    
# #     .chat-empty-title {
# #         font-size: 1.5rem;
# #         font-weight: 700;
# #         color: var(--text-primary);
# #         margin-bottom: 0.5rem;
# #     }
    
# #     .chat-empty-subtitle {
# #         font-size: 0.95rem;
# #         color: var(--text-secondary);
# #     }
    
# #     /* Footer */
# #     .footer-text {
# #         color: var(--text-secondary);
# #     }
    
# #     /* Tabs styling */
# #     .stTabs [data-baseweb="tab-list"] {
# #         gap: 0.5rem;
# #     }
    
# #     .stTabs [data-baseweb="tab"] {
# #         padding: 0.75rem 1.5rem;
# #         font-weight: 600;
# #     }
    
# #     /* Hide Streamlit elements in chat input area */
# #     .chat-input-fixed .stTextInput > label {
# #         display: none;
# #     }
# # </style>
# # """, unsafe_allow_html=True)

# # # ==========================================================
# # # HELPER FUNCTIONS
# # # ==========================================================
# # def check_job_status(run_id):
# #     """Check the status of a Databricks job run"""
# #     headers = {
# #         "Authorization": f"Bearer {DATABRICKS_TOKEN}",
# #         "Content-Type": "application/json"
# #     }
    
# #     status_url = f"{DATABRICKS_INSTANCE}/api/2.1/jobs/runs/get?run_id={run_id}"
    
# #     try:
# #         response = requests.get(status_url, headers=headers, timeout=30)
# #         if response.status_code == 200:
# #             data = response.json()
# #             state = data.get('state', {})
# #             life_cycle_state = state.get('life_cycle_state', 'UNKNOWN')
# #             result_state = state.get('result_state', None)
            
# #             return {
# #                 'life_cycle_state': life_cycle_state,
# #                 'result_state': result_state,
# #                 'is_terminal': life_cycle_state in ['TERMINATED', 'SKIPPED', 'INTERNAL_ERROR']
# #             }
# #     except:
# #         pass
    
# #     return None

# # def get_report_count():
# #     """Get current count of PDF reports"""
# #     headers = {
# #         "Authorization": f"Bearer {DATABRICKS_TOKEN}",
# #         "Accept": "application/json"
# #     }
    
# #     url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/directories{VOLUME_PATH}"
    
# #     try:
# #         response = requests.get(url, headers=headers, timeout=30)
# #         if response.status_code == 200:
# #             files = response.json().get("contents", [])
# #             df = pd.DataFrame(files)
# #             if not df.empty:
# #                 pdf_count = len(df[~df["is_directory"] & df["name"].str.endswith(".pdf")])
# #                 return pdf_count
# #     except:
# #         pass
    
# #     return 0



# # def chat_with_bot(message):
# #     """Collect all output_text content from Databricks model responses"""
# #     headers = {
# #         "Authorization": f"Bearer {DATABRICKS_TOKEN}",
# #         "Content-Type": "application/json"
# #     }

# #     payload = {
# #         "input": [
# #             {
# #                 "status": None,
# #                 "content": message,
# #                 "role": "user",
# #                 "type": "message"
# #             }
# #         ]
# #     }

# #     try:
# #         # Some Databricks models return multiple JSON objects (NDJSON style)
# #         response = requests.post(CHATBOT_ENDPOINT, headers=headers, json=payload, timeout=300)
# #         if response.status_code != 200:
# #             return f"Error: {response.status_code} - {response.text}"

# #         texts = []

# #         # Try to handle newline-delimited JSON (NDJSON)
# #         raw = response.text.strip()
# #         for line in raw.splitlines():
# #             line = line.strip()
# #             if not line:
# #                 continue
# #             try:
# #                 data = json.loads(line)
# #             except json.JSONDecodeError:
# #                 continue

# #             # Each response.output_item.done carries one message item
# #             if data.get("type") == "response.output_item.done":
# #                 item = data.get("item", {})
# #                 for content in item.get("content", []):
# #                     if content.get("type") == "output_text":
# #                         texts.append(content.get("text", ""))

# #         # Fallback: if it was a single JSON blob
# #         if not texts:
# #             try:
# #                 data = json.loads(raw)
# #                 if isinstance(data, dict) and "output" in data:
# #                     for msg in data["output"]:
# #                         for content in msg.get("content", []):
# #                             if content.get("type") == "output_text":
# #                                 texts.append(content.get("text", ""))
# #             except Exception:
# #                 pass

# #         return "\n\n---\n\n".join(texts) if texts else "No output_text found."

# #     except Exception as e:
# #         return f"Error: {str(e)}"




# # # ==========================================================
# # # HEADER
# # # ==========================================================
# # LOGO_URL = "https://media.licdn.com/dms/image/v2/C4E0BAQGtXskL4EvJmA/company-logo_200_200/company-logo_200_200/0/1632401962756/koantek_logo?e=2147483647&v=beta&t=D4GLT1Pu2vvxLR1iKZZbUJWN7K_uaPSF0T1mZl6Le-o"

# # st.markdown(f"""
# # <div class="main-header">
# #     <div class="header-content">
# #         <h1>📊 AI Business Assistant</h1>
# #         <p>Generate reports and chat with AI</p>
# #     </div>
# #     <img src="{LOGO_URL}" class="header-logo" alt="Koantek Logo" onerror="this.style.display='none'">
# # </div>
# # """, unsafe_allow_html=True)

# # # ==========================================================
# # # TABS
# # # ==========================================================
# # tab1, tab2 = st.tabs(["📊 Report Generator", "💬 Chatbot"])

# # # ==========================================================
# # # TAB 1: REPORT GENERATOR
# # # ==========================================================
# # with tab1:
# #     col1, col2 = st.columns([5, 1], vertical_alignment="bottom")

# #     with col1:
# #         report_query = st.text_input(
# #             "What would you like to analyze?",
# #             placeholder="e.g., violation report / BU Analysis report etc.",
# #             label_visibility="visible",
# #             key="report_query"
# #         )

# #     with col2:
# #         st.write("")  # Spacer
# #         run_btn = st.button(
# #             "Generate", 
# #             use_container_width=True
# #         )

# #     # JOB SUBMISSION LOGIC
# #     if run_btn:
# #         if not report_query.strip():
# #             st.warning("⚠️ Please enter a query to generate a report.")
# #         elif not all([DATABRICKS_TOKEN, DATABRICKS_INSTANCE, CLUSTER_ID, NOTEBOOK_PATH]):
# #             st.error("🔧 Configuration Error: Please check your Databricks settings.")
# #         else:
# #             headers = {
# #                 "Authorization": f"Bearer {DATABRICKS_TOKEN}",
# #                 "Content-Type": "application/json"
# #             }
            
# #             payload = {
# #                 "run_name": f"ai_report_{int(time.time())}",
# #                 "existing_cluster_id": CLUSTER_ID,
# #                 "notebook_task": {
# #                     "notebook_path": NOTEBOOK_PATH,
# #                     "base_parameters": {"user_question": report_query}
# #                 }
# #             }
            
# #             submit_url = f"{DATABRICKS_INSTANCE}/api/2.1/jobs/runs/submit"
            
# #             with st.spinner("🔄 Submitting job to Databricks..."):
# #                 try:
# #                     res = requests.post(submit_url, headers=headers, data=json.dumps(payload), timeout=30)
                    
# #                     if res.status_code == 200:
# #                         run_id = res.json().get("run_id")
# #                         # Add new job to monitoring list
# #                         st.session_state.monitoring_jobs.append({
# #                             'run_id': run_id,
# #                             'query': report_query,
# #                             'start_time': time.time(),
# #                             'initial_count': get_report_count()
# #                         })
# #                         st.success(f"✅ Job submitted successfully! Run ID: `{run_id}`")
# #                         st.info("💡 You can submit more queries while this one processes.")
# #                         time.sleep(1)
# #                         st.rerun()
# #                     else:
# #                         st.error(f"❌ Failed to start job: {res.status_code} - {res.text}")
# #                 except requests.exceptions.RequestException as e:
# #                     st.error(f"❌ Connection Error: {str(e)}")

# #     # JOB MONITORING SECTION
# #     if st.session_state.monitoring_jobs:
# #         # Process each active job
# #         jobs_to_remove = []
        
# #         for idx, job in enumerate(st.session_state.monitoring_jobs):
# #             run_id = job['run_id']
# #             job_status = check_job_status(run_id)
# #             current_report_count = get_report_count()
            
# #             # Calculate elapsed time
# #             elapsed_time = int(time.time() - job['start_time'])
# #             minutes, seconds = divmod(elapsed_time, 60)
            
# #             # Check if new report appeared
# #             if current_report_count > job['initial_count']:
# #                 jobs_to_remove.append(idx)
# #                 if run_id not in st.session_state.completed_jobs:
# #                     st.session_state.completed_jobs.append(run_id)
# #                     st.success(f" Report generated for: {job['query']}")
            
# #             # Check if job completed or failed
# #             elif job_status and job_status['is_terminal']:
# #                 if job_status['result_state'] == 'SUCCESS':
# #                     # Keep monitoring for a bit longer to catch the file
# #                     if elapsed_time > 300:  # 5 minutes max wait after completion
# #                         jobs_to_remove.append(idx)
# #                 else:
# #                     jobs_to_remove.append(idx)
# #                     st.error(f"❌ Job failed: {job['query']} - {job_status['result_state']}")
        
# #         # Remove completed jobs
# #         for idx in sorted(jobs_to_remove, reverse=True):
# #             st.session_state.monitoring_jobs.pop(idx)
        
# #         # Display active jobs
# #         if st.session_state.monitoring_jobs:
# #             st.markdown("---")
# #             st.markdown("### 🔄 Active Jobs")
            
# #             for job in st.session_state.monitoring_jobs:
# #                 elapsed_time = int(time.time() - job['start_time'])
# #                 minutes, seconds = divmod(elapsed_time, 60)
                
# #                 col1, col2 = st.columns([6, 1])
                
# #                 with col1:
# #                     st.markdown(f"""
# #                     <div class="progress-box">
# #                         <div class="progress-icon">⚙️</div>
# #                         <div class="progress-content">
# #                             <div class="progress-text">{job['query']}</div>
# #                             <div class="progress-subtext">Run ID: {job['run_id']} • {minutes}m {seconds}s elapsed</div>
# #                         </div>
# #                     </div>
# #                     """, unsafe_allow_html=True)
                
# #                 with col2:
# #                     st.write("")  # Spacer
# #                     if st.button("Cancel", key=f"cancel_{job['run_id']}", use_container_width=True):
# #                         st.session_state.monitoring_jobs = [j for j in st.session_state.monitoring_jobs if j['run_id'] != job['run_id']]
# #                         st.rerun()
            
# #             # Auto-refresh every 5 seconds
# #             time.sleep(5)
# #             st.rerun()

# #     # REPORTS SECTION
# #     col_header, col_filter = st.columns([3, 1])
# #     with col_header:
# #         st.markdown('<div class="section-header">📂 Generated Reports</div>', unsafe_allow_html=True)
# #     with col_filter:
# #         st.write("")  # Spacer
# #         date_filter = st.selectbox(
# #             "🔍 Filter",
# #             ["Last 5 Reports", "Today", "Last 7 Days", "Last 30 Days", "All Reports"],
# #             label_visibility="collapsed"
# #         )

# #     if not all([DATABRICKS_TOKEN, DATABRICKS_INSTANCE, VOLUME_PATH]):
# #         st.warning("🔧 Please configure Databricks credentials to view reports.")
# #     else:
# #         headers = {
# #             "Authorization": f"Bearer {DATABRICKS_TOKEN}",
# #             "Accept": "application/json"
# #         }
        
# #         url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/directories{VOLUME_PATH}"
        
# #         try:
# #             with st.spinner("📥 Loading reports..."):
# #                 response = requests.get(url, headers=headers, timeout=60)
            
# #             if response.status_code == 200:
# #                 files = response.json().get("contents", [])
                
# #                 if not files:
# #                     st.markdown("""
# #                     <div class="empty-state">
# #                         <div class="empty-state-icon">📭</div>
# #                         <h3>No Reports Yet</h3>
# #                         <p>Generate your first report using the form above</p>
# #                     </div>
# #                     """, unsafe_allow_html=True)
# #                 else:
# #                     # Process files
# #                     df = pd.DataFrame(files)
# #                     df["last_modified"] = pd.to_datetime(df["last_modified"], unit="ms")
# #                     pdf_df = df[
# #                         (~df["is_directory"]) & 
# #                         (df["name"].str.endswith(".pdf"))
# #                     ].sort_values("last_modified", ascending=False)
                    
# #                     # Apply date filter
# #                     now = datetime.now()
# #                     if date_filter == "Last 5 Reports":
# #                         pdf_df = pdf_df.head(5)
# #                     elif date_filter == "Today":
# #                         pdf_df = pdf_df[pdf_df["last_modified"].dt.date == now.date()]
# #                     elif date_filter == "Last 7 Days":
# #                         cutoff = now - pd.Timedelta(days=7)
# #                         pdf_df = pdf_df[pdf_df["last_modified"] >= cutoff]
# #                     elif date_filter == "Last 30 Days":
# #                         cutoff = now - pd.Timedelta(days=30)
# #                         pdf_df = pdf_df[pdf_df["last_modified"] >= cutoff]
                    
# #                     # Stats
# #                     total_reports = len(pdf_df)
# #                     total_size_mb = round(pdf_df["file_size"].sum() / (1024 * 1024), 2) if not pdf_df.empty else 0
                    
# #                     # Display stats
# #                     col1, col2, col3 = st.columns(3)
                    
# #                     with col1:
# #                         st.markdown(f"""
# #                         <div class="stat-card">
# #                             <div class="stat-value">{total_reports}</div>
# #                             <div class="stat-label">Total Reports</div>
# #                         </div>
# #                         """, unsafe_allow_html=True)
                    
# #                     with col2:
# #                         st.markdown(f"""
# #                         <div class="stat-card">
# #                             <div class="stat-value">{total_size_mb}</div>
# #                             <div class="stat-label">Total Size (MB)</div>
# #                         </div>
# #                         """, unsafe_allow_html=True)
                    
# #                     with col3:
# #                         if not pdf_df.empty:
# #                             latest = pdf_df.iloc[0]["last_modified"].strftime("%b %d")
# #                         else:
# #                             latest = "N/A"
# #                         st.markdown(f"""
# #                         <div class="stat-card">
# #                             <div class="stat-value">{latest}</div>
# #                             <div class="stat-label">Latest Report</div>
# #                         </div>
# #                         """, unsafe_allow_html=True)
                    
# #                     st.write("")  # Spacer
                    
# #                     # Display reports
# #                     if pdf_df.empty:
# #                         st.info("📄 No reports match the selected filter.")
# #                     else:
# #                         for idx, row in pdf_df.iterrows():
# #                             file_name = row["name"]
# #                             file_path = row["path"]
# #                             size_kb = round(row["file_size"] / 1024, 1)
# #                             mod_time = row["last_modified"].strftime("%b %d, %Y %I:%M %p")
                            
# #                             # Check if this is a new report (within last 30 seconds)
# #                             is_new = (datetime.now() - row["last_modified"]).total_seconds() < 30
                            
# #                             col1, col2 = st.columns([5, 1])
                            
# #                             with col1:
# #                                 card_class = "report-card new-report" if is_new else "report-card"
# #                                 new_badge = "🆕 " if is_new else ""
# #                                 st.markdown(f"""
# #                                 <div class="{card_class}">
# #                                     <div class="report-name">
# #                                         {new_badge}📄 {file_name}
# #                                     </div>
# #                                     <div class="report-meta">
# #                                         <div class="report-meta-item">
# #                                             🕒 {mod_time}
# #                                         </div>
# #                                         <div class="report-meta-item">
# #                                             💾 {size_kb} KB
# #                                         </div>
# #                                     </div>
# #                                 </div>
# #                                 """, unsafe_allow_html=True)
                            
# #                             with col2:
# #                                 # Fetch file content
# #                                 file_api_url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/files{file_path}"
                                
# #                                 try:
# #                                     file_res = requests.get(file_api_url, headers=headers, timeout=60)
                                    
# #                                     if file_res.status_code == 200:
# #                                         pdf_bytes = file_res.content
# #                                         st.write("")  # Spacer for alignment
# #                                         st.download_button(
# #                                             label="⬇️ Download",
# #                                             data=pdf_bytes,
# #                                             file_name=file_name,
# #                                             mime="application/pdf",
# #                                             key=f"download_{file_name}_{idx}"
# #                                         )
# #                                     else:
# #                                         st.error(f"Error: {file_res.status_code}")
# #                                 except requests.exceptions.RequestException as e:
# #                                     st.error(f"Failed to fetch file")
            
# #             elif response.status_code == 404:
# #                 st.warning("📁 Volume path not found. Please verify your VOLUME_PATH configuration.")
# #             else:
# #                 st.error(f"❌ Error listing files: {response.status_code} - {response.text}")
        
# #         except requests.exceptions.RequestException as e:
# #             st.error(f"❌ Connection Error: Unable to connect to Databricks. {str(e)}")

# # # ==========================================================
# # # TAB 2: CHATBOT (ChatGPT-Style Interface)
# # # ==========================================================
# # with tab2:
# #     # Create chat container with fixed layout
# #     # st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
# #     # # Messages area (scrollable)
# #     # st.markdown('<div class="chat-messages-wrapper" id="chat-messages">', unsafe_allow_html=True)
    
# #     if not st.session_state.chat_messages:
# #         # Empty state
# #         st.markdown("""
# #         <div class="chat-empty-state">
# #             <div class="chat-empty-icon">💬</div>
# #             <div class="chat-empty-title">Start a conversation</div>
# #             <div class="chat-empty-subtitle">Ask me anything about your business data</div>
# #         </div>
# #         """, unsafe_allow_html=True)
# #     else:
# #         # Display messages
# #         for msg in st.session_state.chat_messages:
# #             role_class = "user" if msg["role"] == "user" else "assistant"
# #             role_emoji = "👤" if msg["role"] == "user" else "🤖"
# #             content = str(msg["content"]) if not isinstance(msg["content"], str) else msg["content"]
            
# #             st.markdown(f"""
# #             <div class="chat-message {role_class}">
# #                 <div class="chat-message-role">{role_emoji} {msg["role"].capitalize()}</div>
# #                 <div class="chat-message-content">{content}</div>
# #             </div>
# #             """, unsafe_allow_html=True)
        
# #         # Auto-scroll to bottom using JavaScript
# #         # st.markdown("""
# #         # <script>
# #         #     const chatMessages = document.getElementById('chat-messages');
# #         #     if (chatMessages) {
# #         #         chatMessages.scrollTop = chatMessages.scrollHeight;
# #         #     }
# #         # </script>
# #         # """, unsafe_allow_html=True)
    
# #     # st.markdown('</div>', unsafe_allow_html=True)  # End messages wrapper
    
# #     # Input area (fixed at bottom)
# #     # st.markdown('<div class="chat-input-fixed">', unsafe_allow_html=True)
    
# #     col1, col2, col3 = st.columns([7, 1, 1])
    
# #     with col1:
# #         chat_input = st.text_input(
# #             "Message",
# #             placeholder="Type your message here...",
# #             label_visibility="collapsed",
# #             key="chat_input"
# #         )
    
# #     with col2:
# #         send_btn = st.button("📤 Send", use_container_width=True, key="send_chat")
    
# #     with col3:
# #         clear_btn = st.button("🗑️ Clear", use_container_width=True, key="clear_chat", 
# #                               disabled=len(st.session_state.chat_messages) == 0)
    
# #     st.markdown('</div>', unsafe_allow_html=True)  # End input fixed
# #     st.markdown('</div>', unsafe_allow_html=True)  # End chat container
    
# #     # Handle button actions
# #     if send_btn and chat_input.strip():
# #         st.session_state.chat_messages.append({
# #             "role": "user",
# #             "content": chat_input
# #         })
        
# #         with st.spinner("🤖 Thinking..."):
# #             bot_response = chat_with_bot(chat_input)
        
# #         st.session_state.chat_messages.append({
# #             "role": "assistant",
# #             "content": bot_response
# #         })
        
# #         st.rerun()
    
# #     if clear_btn:
# #         st.session_state.chat_messages = []
# #         st.rerun()

# # # ==========================================================
# # # FOOTER
# # # ==========================================================
# # st.markdown("---")
# # st.markdown("""
# # <div style="text-align: center; font-size: 0.8rem; padding: 0.75rem;">
# #     <p class="footer-text">Powered by Koantek</p>
# # </div>
# # """, unsafe_allow_html=True)


