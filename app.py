import streamlit as st
import requests
import json
import os
import time
import urllib.parse
import pandas as pd
from datetime import datetime

# ==========================================================
# CONFIGURATION — UPDATE THESE VALUES
# ==========================================================
DATABRICKS_INSTANCE = "https://adb-2662932819691267.7.azuredatabricks.net"
DATABRICKS_TOKEN = st.secrets['DB_token']  # replace with your PAT
NOTEBOOK_PATH = "/Workspace/Users/prasad.nehe@koantekorg.onmicrosoft.com/pdf_creation/Procurement_report_generation_agent"
VOLUME_PATH = "/Volumes/ai_demos/testing_db/pdf_files"
CLUSTER_ID = "1022-104015-tldaj682"

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="AI Report Generator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# INITIALIZE SESSION STATE
# ==========================================================
if 'monitoring_jobs' not in st.session_state:
    st.session_state.monitoring_jobs = []  # List of active jobs
if 'completed_jobs' not in st.session_state:
    st.session_state.completed_jobs = []  # Track completed jobs

# ==========================================================
# MODERN CSS STYLING
# ==========================================================
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .block-container {
        padding-top: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 1400px;
    }
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Styles */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.25rem 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.25rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .header-content {
        flex: 1;
    }
    
    .header-logo {
        height: 70px;
        width: auto;
        max-width: 220px;
        object-fit: contain;
        padding: 0.6rem 1.5rem;
        margin-top: 20px;
       

    }
    
    .main-header h1 {
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        font-size: 0.875rem;
        margin: 0.25rem 0 0 0;
    }
    
    /* Input Section */
    .input-section {
        background: var(--background-color);
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.06);
        margin-bottom: 1.25rem;
        border: 1px solid var(--border-color);
    }
    
    /* Dark mode detection */
    @media (prefers-color-scheme: dark) {
        :root {
            --background-color: #1e1e1e;
            --card-background: #262626;
            --text-primary: #ffffff;
            --text-secondary: #a0a0a0;
            --border-color: #404040;
            --hover-background: #2d2d2d;
        }
    }
    
    @media (prefers-color-scheme: light) {
        :root {
            --background-color: #ffffff;
            --card-background: #ffffff;
            --text-primary: #1f2937;
            --text-secondary: #6b7280;
            --border-color: #e5e7eb;
            --hover-background: #f9fafb;
        }
    }
    
    /* Force theme variables for Streamlit dark mode */
    [data-testid="stAppViewContainer"][data-theme="dark"] {
        --background-color: #0e1117;
        --card-background: #262730;
        --text-primary: #fafafa;
        --text-secondary: #a3a8b4;
        --border-color: #464a57;
        --hover-background: #1e2029;
    }
    
    [data-testid="stAppViewContainer"][data-theme="light"] {
        --background-color: #ffffff;
        --card-background: #ffffff;
        --text-primary: #1f2937;
        --text-secondary: #6b7280;
        --border-color: #e5e7eb;
        --hover-background: #f9fafb;
    }
    
    .stTextInput > div > div > input {
        border-radius: 8px !important;
        border: 2px solid var(--border-color) !important;
        padding: 0.6rem 0.875rem !important;
        font-size: 0.9rem !important;
        transition: all 0.2s ease !important;
        background-color: var(--card-background) !important;
        color: var(--text-primary) !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102,126,234,0.1) !important;
    }
    
    /* Button Styles */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.5rem !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 4px rgba(102,126,234,0.3) !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(102,126,234,0.4) !important;
    }
    
    /* Progress Box */
    .progress-box {
        background: linear-gradient(135deg, rgba(102,126,234,0.1) 0%, rgba(118,75,162,0.1) 100%);
        border: 2px solid #667eea;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .progress-icon {
        font-size: 1.5rem;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.7; transform: scale(1.05); }
    }
    
    .progress-content {
        flex: 1;
    }
    
    .progress-text {
        font-size: 0.95rem;
        font-weight: 600;
        color: #667eea;
        margin-bottom: 0.15rem;
    }
    
    .progress-subtext {
        font-size: 0.8rem;
        color: var(--text-secondary);
    }
    
    .cancel-btn {
        background: #ef4444 !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 0.4rem 0.8rem !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        cursor: pointer;
        transition: all 0.2s ease !important;
    }
    
    .cancel-btn:hover {
        background: #dc2626 !important;
    }
    
    /* Report Card Styles */
    .report-card {
        background: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 10px;
        padding: 0.875rem 1rem;
        margin-bottom: 0.75rem;
        transition: all 0.3s ease;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    .report-card:hover {
        box-shadow: 0 4px 8px rgba(102,126,234,0.2);
        transform: translateY(-1px);
        border-color: #667eea;
        background: var(--hover-background);
    }
    
    .report-card.new-report {
        border: 2px solid #10b981;
        background: linear-gradient(135deg, rgba(16,185,129,0.1) 0%, rgba(16,185,129,0.05) 100%);
        animation: highlight 2s ease-in-out;
    }
    
    @keyframes highlight {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .report-name {
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.35rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }
    
    .report-meta {
        display: flex;
        gap: 1rem;
        color: var(--text-secondary);
        font-size: 0.8rem;
        margin-top: 0.35rem;
    }
    
    .report-meta-item {
        display: flex;
        align-items: center;
        gap: 0.3rem;
    }
    
    /* Download Button */
    .stDownloadButton > button {
        background: #10b981 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.45rem 1rem !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
    }
    
    .stDownloadButton > button:hover {
        background: #059669 !important;
        transform: scale(1.02) !important;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 1.25rem 0 0.75rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Stats Cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stat-value {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.15rem;
    }
    
    .stat-label {
        font-size: 0.8rem;
        opacity: 0.9;
    }
    
    /* Empty State */
    .empty-state {
        text-align: center;
        padding: 3rem;
        color: var(--text-secondary);
    }
    
    .empty-state-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        opacity: 0.5;
    }
    
    .empty-state h3 {
        color: var(--text-primary);
    }
    
    /* Filter Select */
    .stSelectbox > div > div {
        border-radius: 8px !important;
        border: 2px solid var(--border-color) !important;
        transition: all 0.2s ease !important;
        background-color: var(--card-background) !important;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102,126,234,0.1) !important;
    }
    
    /* Alert overrides for dark mode */
    .stAlert {
        background-color: var(--card-background) !important;
        border-color: var(--border-color) !important;
        color: var(--text-primary) !important;
    }
    
    /* Footer */
    .footer-text {
        color: var(--text-secondary);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================
def check_job_status(run_id):
    """Check the status of a Databricks job run"""
    headers = {
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    status_url = f"{DATABRICKS_INSTANCE}/api/2.1/jobs/runs/get?run_id={run_id}"
    
    try:
        response = requests.get(status_url, headers=headers, timeout=30)
        if response.status_code == 200:
            data = response.json()
            state = data.get('state', {})
            life_cycle_state = state.get('life_cycle_state', 'UNKNOWN')
            result_state = state.get('result_state', None)
            
            return {
                'life_cycle_state': life_cycle_state,
                'result_state': result_state,
                'is_terminal': life_cycle_state in ['TERMINATED', 'SKIPPED', 'INTERNAL_ERROR']
            }
    except:
        pass
    
    return None

def get_report_count():
    """Get current count of PDF reports"""
    headers = {
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        "Accept": "application/json"
    }
    
    url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/directories{VOLUME_PATH}"
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            files = response.json().get("contents", [])
            df = pd.DataFrame(files)
            if not df.empty:
                pdf_count = len(df[~df["is_directory"] & df["name"].str.endswith(".pdf")])
                return pdf_count
    except:
        pass
    
    return 0

# ==========================================================
# HEADER
# ==========================================================
LOGO_URL = "https://media.licdn.com/dms/image/v2/C4E0BAQGtXskL4EvJmA/company-logo_200_200/company-logo_200_200/0/1632401962756/koantek_logo?e=2147483647&v=beta&t=D4GLT1Pu2vvxLR1iKZZbUJWN7K_uaPSF0T1mZl6Le-o"

st.markdown(f"""
<div class="main-header">
    <div class="header-content">
        <h1>📊 AI Business Report Generator</h1>
        <p>Create intelligent reports</p>
    </div>
    <img src="{LOGO_URL}" class="header-logo" alt="Koantek Logo" onerror="this.style.display='none'">
</div>
""", unsafe_allow_html=True)

# ==========================================================
# QUERY INPUT SECTION
# ==========================================================
col1, col2 = st.columns([5, 1], vertical_alignment="bottom")

with col1:
    report_query = st.text_input(
        "What would you like to analyze?",
        placeholder="e.g., violation report / BU Analysis report etc.",
        label_visibility="visible"
    )

with col2:
    st.write("")  # Spacer
    run_btn = st.button(
        "Generate", 
        use_container_width=True
    )

# ==========================================================
# JOB SUBMISSION LOGIC
# ==========================================================
if run_btn:
    if not report_query.strip():
        st.warning("⚠️ Please enter a query to generate a report.")
    elif not all([DATABRICKS_TOKEN, DATABRICKS_INSTANCE, CLUSTER_ID, NOTEBOOK_PATH]):
        st.error("🔧 Configuration Error: Please check your Databricks settings.")
    else:
        headers = {
            "Authorization": f"Bearer {DATABRICKS_TOKEN}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "run_name": f"ai_report_{int(time.time())}",
            "existing_cluster_id": CLUSTER_ID,
            "notebook_task": {
                "notebook_path": NOTEBOOK_PATH,
                "base_parameters": {"user_question": report_query}
            }
        }
        
        submit_url = f"{DATABRICKS_INSTANCE}/api/2.1/jobs/runs/submit"
        
        with st.spinner("🔄 Submitting job to Databricks..."):
            try:
                res = requests.post(submit_url, headers=headers, data=json.dumps(payload), timeout=30)
                
                if res.status_code == 200:
                    run_id = res.json().get("run_id")
                    # Add new job to monitoring list
                    st.session_state.monitoring_jobs.append({
                        'run_id': run_id,
                        'query': report_query,
                        'start_time': time.time(),
                        'initial_count': get_report_count()
                    })
                    st.success(f"✅ Job submitted successfully! Run ID: `{run_id}`")
                    st.info("💡 You can submit more queries while this one processes.")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(f"❌ Failed to start job: {res.status_code} - {res.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Connection Error: {str(e)}")

# ==========================================================
# JOB MONITORING SECTION
# ==========================================================
if st.session_state.monitoring_jobs:
    # Process each active job
    jobs_to_remove = []
    
    for idx, job in enumerate(st.session_state.monitoring_jobs):
        run_id = job['run_id']
        job_status = check_job_status(run_id)
        current_report_count = get_report_count()
        
        # Calculate elapsed time
        elapsed_time = int(time.time() - job['start_time'])
        minutes, seconds = divmod(elapsed_time, 60)
        
        # Check if new report appeared
        if current_report_count > job['initial_count']:
            jobs_to_remove.append(idx)
            if run_id not in st.session_state.completed_jobs:
                st.session_state.completed_jobs.append(run_id)
                st.success(f"🎉 Report generated for: {job['query']}")
        
        # Check if job completed or failed
        elif job_status and job_status['is_terminal']:
            if job_status['result_state'] == 'SUCCESS':
                # Keep monitoring for a bit longer to catch the file
                if elapsed_time > 300:  # 5 minutes max wait after completion
                    jobs_to_remove.append(idx)
            else:
                jobs_to_remove.append(idx)
                st.error(f"❌ Job failed: {job['query']} - {job_status['result_state']}")
    
    # Remove completed jobs
    for idx in sorted(jobs_to_remove, reverse=True):
        st.session_state.monitoring_jobs.pop(idx)
    
    # Display active jobs
    if st.session_state.monitoring_jobs:
        st.markdown("---")
        st.markdown("### 🔄 Active Jobs")
        
        for job in st.session_state.monitoring_jobs:
            elapsed_time = int(time.time() - job['start_time'])
            minutes, seconds = divmod(elapsed_time, 60)
            
            col1, col2 = st.columns([6, 1])
            
            with col1:
                st.markdown(f"""
                <div class="progress-box">
                    <div class="progress-icon">⚙️</div>
                    <div class="progress-content">
                        <div class="progress-text">{job['query']}</div>
                        <div class="progress-subtext">Run ID: {job['run_id']} • {minutes}m {seconds}s elapsed</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.write("")  # Spacer
                if st.button("Cancel", key=f"cancel_{job['run_id']}", use_container_width=True):
                    st.session_state.monitoring_jobs = [j for j in st.session_state.monitoring_jobs if j['run_id'] != job['run_id']]
                    st.rerun()
        
        # Auto-refresh every 5 seconds
        time.sleep(5)
        st.rerun()

# ==========================================================
# REPORTS SECTION
# ==========================================================
col_header, col_filter = st.columns([3, 1])
with col_header:
    st.markdown('<div class="section-header">📂 Generated Reports</div>', unsafe_allow_html=True)
with col_filter:
    st.write("")  # Spacer
    date_filter = st.selectbox(
        "🔍 Filter",
        ["Last 5 Reports", "Today", "Last 7 Days", "Last 30 Days", "All Reports"],
        label_visibility="collapsed"
    )

if not all([DATABRICKS_TOKEN, DATABRICKS_INSTANCE, VOLUME_PATH]):
    st.warning("🔧 Please configure Databricks credentials to view reports.")
else:
    headers = {
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        "Accept": "application/json"
    }
    
    url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/directories{VOLUME_PATH}"
    
    try:
        with st.spinner("📥 Loading reports..."):
            response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            files = response.json().get("contents", [])
            
            if not files:
                st.markdown("""
                <div class="empty-state">
                    <div class="empty-state-icon">📭</div>
                    <h3>No Reports Yet</h3>
                    <p>Generate your first report using the form above</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                # Process files
                df = pd.DataFrame(files)
                df["last_modified"] = pd.to_datetime(df["last_modified"], unit="ms")
                pdf_df = df[
                    (~df["is_directory"]) & 
                    (df["name"].str.endswith(".pdf"))
                ].sort_values("last_modified", ascending=False)
                
                # Apply date filter
                now = datetime.now()
                if date_filter == "Last 5 Reports":
                    pdf_df = pdf_df.head(5)
                elif date_filter == "Today":
                    pdf_df = pdf_df[pdf_df["last_modified"].dt.date == now.date()]
                elif date_filter == "Last 7 Days":
                    cutoff = now - pd.Timedelta(days=7)
                    pdf_df = pdf_df[pdf_df["last_modified"] >= cutoff]
                elif date_filter == "Last 30 Days":
                    cutoff = now - pd.Timedelta(days=30)
                    pdf_df = pdf_df[pdf_df["last_modified"] >= cutoff]
                
                # Stats
                total_reports = len(pdf_df)
                total_size_mb = round(pdf_df["file_size"].sum() / (1024 * 1024), 2) if not pdf_df.empty else 0
                
                # Display stats
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown(f"""
                    <div class="stat-card">
                        <div class="stat-value">{total_reports}</div>
                        <div class="stat-label">Total Reports</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    <div class="stat-card">
                        <div class="stat-value">{total_size_mb}</div>
                        <div class="stat-label">Total Size (MB)</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    if not pdf_df.empty:
                        latest = pdf_df.iloc[0]["last_modified"].strftime("%b %d")
                    else:
                        latest = "N/A"
                    st.markdown(f"""
                    <div class="stat-card">
                        <div class="stat-value">{latest}</div>
                        <div class="stat-label">Latest Report</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.write("")  # Spacer
                
                # Display reports
                if pdf_df.empty:
                    st.info("📄 No reports match the selected filter.")
                else:
                    # Highlight newest report
                    newest_time = pdf_df.iloc[0]["last_modified"]
                    
                    for idx, row in pdf_df.iterrows():
                        file_name = row["name"]
                        file_path = row["path"]
                        size_kb = round(row["file_size"] / 1024, 1)
                        mod_time = row["last_modified"].strftime("%b %d, %Y %I:%M %p")
                        
                        # Check if this is a new report (within last 30 seconds)
                        is_new = (datetime.now() - row["last_modified"]).total_seconds() < 30
                        
                        col1, col2 = st.columns([5, 1])
                        
                        with col1:
                            card_class = "report-card new-report" if is_new else "report-card"
                            new_badge = "🆕 " if is_new else ""
                            st.markdown(f"""
                            <div class="{card_class}">
                                <div class="report-name">
                                    {new_badge}📄 {file_name}
                                </div>
                                <div class="report-meta">
                                    <div class="report-meta-item">
                                        🕒 {mod_time}
                                    </div>
                                    <div class="report-meta-item">
                                        💾 {size_kb} KB
                                    </div>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col2:
                            # Fetch file content
                            file_api_url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/files{file_path}"
                            
                            try:
                                file_res = requests.get(file_api_url, headers=headers, timeout=30)
                                
                                if file_res.status_code == 200:
                                    pdf_bytes = file_res.content
                                    st.write("")  # Spacer for alignment
                                    st.download_button(
                                        label="⬇️ Download",
                                        data=pdf_bytes,
                                        file_name=file_name,
                                        mime="application/pdf",
                                        key=f"download_{file_name}_{idx}"
                                    )
                                else:
                                    st.error(f"Error: {file_res.status_code}")
                            except requests.exceptions.RequestException as e:
                                st.error(f"Failed to fetch file")
        
        elif response.status_code == 404:
            st.warning("📁 Volume path not found. Please verify your VOLUME_PATH configuration.")
        else:
            st.error(f"❌ Error listing files: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Connection Error: Unable to connect to Databricks. {str(e)}")

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 0.8rem; padding: 0.75rem;">
    <p class="footer-text">Powered by Koantek</p>
</div>
""", unsafe_allow_html=True)
# import streamlit as st
# import requests
# import json
# import os
# import time
# import urllib.parse
# import pandas as pd
# from datetime import datetime

# # ==========================================================
# # CONFIGURATION — UPDATE THESE VALUES
# # ==========================================================
# DATABRICKS_INSTANCE = "https://adb-2662932819691267.7.azuredatabricks.net"
# DATABRICKS_TOKEN = "dapi7332ef1f2a4ad0adb5364cd04220cc26-2"  # replace with your PAT
# NOTEBOOK_PATH = "/Workspace/Users/prasad.nehe@koantekorg.onmicrosoft.com/pdf_creation/Procurement_report_generation_agent"
# VOLUME_PATH = "/Volumes/ai_demos/testing_db/pdf_files"
# CLUSTER_ID = "1022-104015-tldaj682"



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
# # MODERN CSS STYLING
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
    
#     /* Input Section */
#     .input-section {
#         background: white;
#         padding: 1rem;
#         border-radius: 10px;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.06);
#         margin-bottom: 1.25rem;
#         border: 1px solid #e5e7eb;
#     }
    
#     .stTextInput > div > div > input {
#         border-radius: 8px !important;
#         border: 2px solid #e5e7eb !important;
#         padding: 0.6rem 0.875rem !important;
#         font-size: 0.9rem !important;
#         transition: all 0.2s ease !important;
#     }
    
#     .stTextInput > div > div > input:focus {
#         border-color: #667eea !important;
#         box-shadow: 0 0 0 3px rgba(102,126,234,0.1) !important;
#     }
    
#     /* Button Styles */
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
    
#     /* Report Card Styles */
#     .report-card {
#         background: white;
#         border: 1px solid #e5e7eb;
#         border-radius: 10px;
#         padding: 0.875rem 1rem;
#         margin-bottom: 0.75rem;
#         transition: all 0.3s ease;
#         box-shadow: 0 1px 3px rgba(0,0,0,0.05);
#     }
    
#     .report-card:hover {
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         transform: translateY(-1px);
#         border-color: #667eea;
#     }
    
#     .report-name {
#         font-size: 0.95rem;
#         font-weight: 600;
#         color: #1f2937;
#         margin-bottom: 0.35rem;
#         display: flex;
#         align-items: center;
#         gap: 0.4rem;
#     }
    
#     .report-meta {
#         display: flex;
#         gap: 1rem;
#         color: #6b7280;
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
#         color: #1f2937;
#         margin: 1.25rem 0 0.75rem 0;
#         display: flex;
#         align-items: center;
#         gap: 0.5rem;
#     }
    
#     /* Stats Cards */
#     .stats-container {
#         display: grid;
#         grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
#         gap: 0.75rem;
#         margin-bottom: 1.25rem;
#     }
    
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
    
#     /* Alert Styles */
#     .stAlert {
#         border-radius: 8px !important;
#     }
    
#     /* Spinner */
#     .stSpinner > div {
#         border-top-color: #667eea !important;
#     }
    
#     /* Empty State */
#     .empty-state {
#         text-align: center;
#         padding: 3rem;
#         color: #6b7280;
#     }
    
#     .empty-state-icon {
#         font-size: 4rem;
#         margin-bottom: 1rem;
#     }
    
#     /* Filter Select */
#     .stSelectbox > div > div {
#         border-radius: 8px !important;
#         border: 2px solid #e5e7eb !important;
#         transition: all 0.2s ease !important;
#     }
    
#     .stSelectbox > div > div:focus-within {
#         border-color: #667eea !important;
#         box-shadow: 0 0 0 3px rgba(102,126,234,0.1) !important;
#     }
    
#     /* Divider */
#     hr {
#         margin: 2rem 0;
#         border: none;
#         border-top: 2px solid #e5e7eb;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ==========================================================
# # HEADER
# # ==========================================================
# st.markdown("""
# <div class="main-header">
#     <h1>📊 AI Business Report Generator</h1>
#     <p>Create intelligent reports </p>
# </div>
# """, unsafe_allow_html=True)

# # ==========================================================
# # QUERY INPUT SECTION
# # ==========================================================
# # st.markdown('<div class="input-section">', unsafe_allow_html=True)

# col1, col2 = st.columns([5, 1],vertical_alignment="bottom")

# with col1:
#     report_query = st.text_input(
#         "What would you like to analyze?",
#         placeholder="e.g., voiletion report /BU Anaysis report etc.",
#         label_visibility="visible"
#     )

# with col2:
#     st.write("")# Spacer
#     run_btn = st.button("Generate", use_container_width=True)

# st.markdown('</div>', unsafe_allow_html=True)

# # ==========================================================
# # JOB SUBMISSION LOGIC
# # ==========================================================
# if run_btn:
#     if not report_query.strip():
#         st.warning("⚠️ Please enter a query to generate a report.")
#     elif not all([DATABRICKS_TOKEN, DATABRICKS_INSTANCE, CLUSTER_ID, NOTEBOOK_PATH]):
#         st.error("🔧 Configuration Error: Please check your Databricks settings in secrets.")
#     else:
#         headers = {
#             "Authorization": f"Bearer {DATABRICKS_TOKEN}",
#             "Content-Type": "application/json"
#         }
        
#         payload = {
#             "run_name": f"ai_report_{int(time.time())}",
#             "existing_cluster_id": CLUSTER_ID,
#             "notebook_task": {
#                 "notebook_path": NOTEBOOK_PATH,
#                 "base_parameters": {"user_question": report_query}
#             }
#         }
        
#         submit_url = f"{DATABRICKS_INSTANCE}/api/2.1/jobs/runs/submit"
        
#         with st.spinner("🔄 Submitting job to Databricks..."):
#             try:
#                 res = requests.post(submit_url, headers=headers, data=json.dumps(payload), timeout=30)
                
#                 if res.status_code == 200:
#                     run_id = res.json().get("run_id")
#                     st.success(f"✅ Job submitted successfully! Run ID: `{run_id}`")
#                     st.info("💡 Your report will appear below once processing is complete. This may take a few minutes.")
#                 else:
#                     st.error(f"❌ Failed to start job: {res.status_code} - {res.text}")
#             except requests.exceptions.RequestException as e:
#                 st.error(f"❌ Connection Error: {str(e)}")

# # ==========================================================
# # REPORTS SECTION
# # ==========================================================
# col_header, col_filter = st.columns([3, 1])
# with col_header:
#     st.markdown('<div class="section-header">📂 Generated Reports</div>', unsafe_allow_html=True)
# with col_filter:
#     st.write("")  # Spacer
#     date_filter = st.selectbox(
#         "🔍 Filter",
#         ["Last 5 Reports", "Today", "Last 7 Days", "Last 30 Days", "All Reports"],
#         label_visibility="collapsed"
#     )

# if not all([DATABRICKS_TOKEN, DATABRICKS_INSTANCE, VOLUME_PATH]):
#     st.warning("🔧 Please configure Databricks credentials in your secrets to view reports.")
# else:
#     headers = {
#         "Authorization": f"Bearer {DATABRICKS_TOKEN}",
#         "Accept": "application/json"
#     }
    
#     url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/directories{VOLUME_PATH}"
    
#     try:
#         with st.spinner("📥 Loading reports..."):
#             response = requests.get(url, headers=headers, timeout=30)
        
#         if response.status_code == 200:
#             files = response.json().get("contents", [])
            
#             if not files:
#                 st.markdown("""
#                 <div class="empty-state">
#                     <div class="empty-state-icon">📭</div>
#                     <h3>No Reports Yet</h3>
#                     <p>Generate your first report using the form above</p>
#                 </div>
#                 """, unsafe_allow_html=True)
#             else:
#                 # Process files
#                 df = pd.DataFrame(files)
#                 df["last_modified"] = pd.to_datetime(df["last_modified"], unit="ms")
#                 pdf_df = df[
#                     (~df["is_directory"]) & 
#                     (df["name"].str.endswith(".pdf"))
#                 ].sort_values("last_modified", ascending=False)
                
#                 # Apply date filter
#                 now = datetime.now()
#                 if date_filter == "Last 5 Reports":
#                     pdf_df = pdf_df.head(5)
#                 elif date_filter == "Today":
#                     pdf_df = pdf_df[pdf_df["last_modified"].dt.date == now.date()]
#                 elif date_filter == "Last 7 Days":
#                     cutoff = now - pd.Timedelta(days=7)
#                     pdf_df = pdf_df[pdf_df["last_modified"] >= cutoff]
#                 elif date_filter == "Last 30 Days":
#                     cutoff = now - pd.Timedelta(days=30)
#                     pdf_df = pdf_df[pdf_df["last_modified"] >= cutoff]
#                 # "All Reports" shows everything (no filter)
                
#                 # Stats
#                 total_reports = len(pdf_df)
#                 total_size_mb = round(pdf_df["file_size"].sum() / (1024 * 1024), 2)
                
#                 # Display stats
#                 col1, col2, col3 = st.columns(3)
                
#                 with col1:
#                     st.markdown(f"""
#                     <div class="stat-card">
#                         <div class="stat-value">{total_reports}</div>
#                         <div class="stat-label">Total Reports</div>
#                     </div>
#                     """, unsafe_allow_html=True)
                
#                 with col2:
#                     st.markdown(f"""
#                     <div class="stat-card">
#                         <div class="stat-value">{total_size_mb}</div>
#                         <div class="stat-label">Total Size (MB)</div>
#                     </div>
#                     """, unsafe_allow_html=True)
                
#                 with col3:
#                     if not pdf_df.empty:
#                         latest = pdf_df.iloc[0]["last_modified"].strftime("%b %d")
#                     else:
#                         latest = "N/A"
#                     st.markdown(f"""
#                     <div class="stat-card">
#                         <div class="stat-value">{latest}</div>
#                         <div class="stat-label">Latest Report</div>
#                     </div>
#                     """, unsafe_allow_html=True)
                
#                 st.write("")  # Spacer
                
#                 # Display reports
#                 if pdf_df.empty:
#                     st.info("📄 No PDF reports found. Only PDF files are displayed.")
#                 else:
#                     for idx, row in pdf_df.iterrows():
#                         file_name = row["name"]
#                         file_path = row["path"]
#                         size_kb = round(row["file_size"] / 1024, 1)
#                         mod_time = row["last_modified"].strftime("%b %d, %Y %I:%M %p")
                        
#                         col1, col2 = st.columns([5, 1])
                        
#                         with col1:
#                             st.markdown(f"""
#                             <div class="report-card">
#                                 <div class="report-name">
#                                     📄 {file_name}
#                                 </div>
#                                 <div class="report-meta">
#                                     <div class="report-meta-item">
#                                         🕒 {mod_time}
#                                     </div>
#                                     <div class="report-meta-item">
#                                         💾 {size_kb} KB
#                                     </div>
#                                 </div>
#                             </div>
#                             """, unsafe_allow_html=True)
                        
#                         with col2:
#                             # Fetch file content
#                             file_api_url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/files{file_path}"
                            
#                             try:
#                                 file_res = requests.get(file_api_url, headers=headers, timeout=30)
                                
#                                 if file_res.status_code == 200:
#                                     pdf_bytes = file_res.content
#                                     st.write("")  # Spacer for alignment
#                                     st.download_button(
#                                         label="⬇️ Download",
#                                         data=pdf_bytes,
#                                         file_name=file_name,
#                                         mime="application/pdf",
#                                         key=f"download_{file_name}_{idx}"
#                                     )
#                                 else:
#                                     st.error(f"Error: {file_res.status_code}")
#                             except requests.exceptions.RequestException as e:
#                                 st.error(f"Failed to fetch file")
        
#         elif response.status_code == 404:
#             st.warning("📁 Volume path not found. Please verify your VOLUME_PATH configuration.")
#         else:
#             st.error(f"❌ Error listing files: {response.status_code} - {response.text}")
    
#     except requests.exceptions.RequestException as e:
#         st.error(f"❌ Connection Error: Unable to connect to Databricks. {str(e)}")

# # ==========================================================
# # FOOTER
# # ==========================================================
# st.markdown("---")
# st.markdown("""
# <div style="text-align: center; color: #9ca3af; font-size: 0.8rem; padding: 0.75rem;">
#     <p>Powered by Koantek..</p>
# </div>
# """, unsafe_allow_html=True)

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
# # # MODERN CSS STYLING
# # # ==========================================================
# # st.markdown("""
# # <style>
# #     /* Global Styles */
# #     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
# #     .block-container {
# #         padding-top: 2rem;
# #         padding-left: 3rem;
# #         padding-right: 3rem;
# #         max-width: 1400px;
# #     }
    
# #     * {
# #         font-family: 'Inter', sans-serif;
# #     }
    
# #     /* Header Styles */
# #     .main-header {
# #         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# #         padding: 2rem;
# #         border-radius: 12px;
# #         margin-bottom: 2rem;
# #         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
# #     }
    
# #     .main-header h1 {
# #         color: white;
# #         font-size: 2rem;
# #         font-weight: 700;
# #         margin: 0;
# #         display: flex;
# #         align-items: center;
# #         gap: 0.5rem;
# #     }
    
# #     .main-header p {
# #         color: rgba(255,255,255,0.9);
# #         font-size: 1rem;
# #         margin: 0.5rem 0 0 0;
# #     }
    
# #     /* Input Section */
# #     .input-section {
# #         background: white;
# #         padding: 1.5rem;
# #         border-radius: 12px;
# #         box-shadow: 0 2px 8px rgba(0,0,0,0.08);
# #         margin-bottom: 2rem;
# #         border: 1px solid #e5e7eb;
# #     }
    
# #     .stTextInput > div > div > input {
# #         border-radius: 8px !important;
# #         border: 2px solid #e5e7eb !important;
# #         padding: 0.75rem 1rem !important;
# #         font-size: 1rem !important;
# #         transition: all 0.2s ease !important;
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
# #         padding: 0.75rem 2rem !important;
# #         font-size: 1rem !important;
# #         font-weight: 600 !important;
# #         transition: all 0.3s ease !important;
# #         box-shadow: 0 4px 6px rgba(102,126,234,0.3) !important;
# #         width: 100% !important;
# #     }
    
# #     .stButton > button:hover {
# #         transform: translateY(-2px) !important;
# #         box-shadow: 0 6px 12px rgba(102,126,234,0.4) !important;
# #     }
    
# #     /* Report Card Styles */
# #     .report-card {
# #         background: white;
# #         border: 1px solid #e5e7eb;
# #         border-radius: 12px;
# #         padding: 1.25rem;
# #         margin-bottom: 1rem;
# #         transition: all 0.3s ease;
# #         box-shadow: 0 2px 4px rgba(0,0,0,0.05);
# #     }
    
# #     .report-card:hover {
# #         box-shadow: 0 8px 16px rgba(0,0,0,0.12);
# #         transform: translateY(-2px);
# #         border-color: #667eea;
# #     }
    
# #     .report-name {
# #         font-size: 1.1rem;
# #         font-weight: 600;
# #         color: #1f2937;
# #         margin-bottom: 0.5rem;
# #         display: flex;
# #         align-items: center;
# #         gap: 0.5rem;
# #     }
    
# #     .report-meta {
# #         display: flex;
# #         gap: 1.5rem;
# #         color: #6b7280;
# #         font-size: 0.875rem;
# #         margin-top: 0.5rem;
# #     }
    
# #     .report-meta-item {
# #         display: flex;
# #         align-items: center;
# #         gap: 0.35rem;
# #     }
    
# #     /* Download Button */
# #     .stDownloadButton > button {
# #         background: #10b981 !important;
# #         color: white !important;
# #         border: none !important;
# #         border-radius: 8px !important;
# #         padding: 0.5rem 1.5rem !important;
# #         font-size: 0.9rem !important;
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
# #         font-size: 1.5rem;
# #         font-weight: 700;
# #         color: #1f2937;
# #         margin: 2rem 0 1rem 0;
# #         display: flex;
# #         align-items: center;
# #         gap: 0.5rem;
# #     }
    
# #     /* Stats Cards */
# #     .stats-container {
# #         display: grid;
# #         grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
# #         gap: 1rem;
# #         margin-bottom: 2rem;
# #     }
    
# #     .stat-card {
# #         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# #         padding: 1.5rem;
# #         border-radius: 12px;
# #         color: white;
# #         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
# #     }
    
# #     .stat-value {
# #         font-size: 2rem;
# #         font-weight: 700;
# #         margin-bottom: 0.25rem;
# #     }
    
# #     .stat-label {
# #         font-size: 0.875rem;
# #         opacity: 0.9;
# #     }
    
# #     /* Alert Styles */
# #     .stAlert {
# #         border-radius: 8px !important;
# #     }
    
# #     /* Spinner */
# #     .stSpinner > div {
# #         border-top-color: #667eea !important;
# #     }
    
# #     /* Empty State */
# #     .empty-state {
# #         text-align: center;
# #         padding: 3rem;
# #         color: #6b7280;
# #     }
    
# #     .empty-state-icon {
# #         font-size: 4rem;
# #         margin-bottom: 1rem;
# #     }
    
# #     /* Divider */
# #     hr {
# #         margin: 2rem 0;
# #         border: none;
# #         border-top: 2px solid #e5e7eb;
# #     }
# # </style>
# # """, unsafe_allow_html=True)

# # # ==========================================================
# # # HEADER
# # # ==========================================================
# # st.markdown("""
# # <div class="main-header">
# #     <h1>📊 AI Business Report Generator</h1>
# #     <p>Create intelligent business reports powered by Databricks and AI</p>
# # </div>
# # """, unsafe_allow_html=True)

# # # ==========================================================
# # # QUERY INPUT SECTION
# # # ==========================================================
# # st.markdown('<div class="input-section">', unsafe_allow_html=True)

# # col1, col2 = st.columns([5, 1])

# # with col1:
# #     report_query = st.text_input(
# #         "What would you like to analyze?",
# #         placeholder="e.g., violation report , BU analysis etc. ",
# #         key="report_query",
# #         label_visibility="visible"
# #     )

# # with col2:
# #     st.write("")  # Spacer
# #     run_btn = st.button("🚀 Generate", use_container_width=True)

# # st.markdown('</div>', unsafe_allow_html=True)

# # # ==========================================================
# # # JOB SUBMISSION LOGIC
# # # ==========================================================
# # if run_btn:
# #     if not report_query.strip():
# #         st.warning("⚠️ Please enter a query to generate a report.")
# #     elif not all([DATABRICKS_TOKEN, DATABRICKS_INSTANCE, CLUSTER_ID, NOTEBOOK_PATH]):
# #         st.error("🔧 Configuration Error: Please check your Databricks settings in secrets.")
# #     else:
# #         headers = {
# #             "Authorization": f"Bearer {DATABRICKS_TOKEN}",
# #             "Content-Type": "application/json"
# #         }
        
# #         payload = {
# #             "run_name": f"ai_report_{int(time.time())}",
# #             "existing_cluster_id": CLUSTER_ID,
# #             "notebook_task": {
# #                 "notebook_path": NOTEBOOK_PATH,
# #                 "base_parameters": {"user_question": report_query}
# #             }
# #         }
        
# #         submit_url = f"{DATABRICKS_INSTANCE}/api/2.1/jobs/runs/submit"
        
# #         with st.spinner("🔄 Submitting job to Databricks..."):
# #             try:
# #                 res = requests.post(submit_url, headers=headers, data=json.dumps(payload), timeout=30)
                
# #                 if res.status_code == 200:
# #                     run_id = res.json().get("run_id")
# #                     st.success(f"✅ Job submitted successfully! Run ID: `{run_id}`")
# #                     st.info("💡 Your report will appear below once processing is complete. This may take a few minutes.")
# #                 else:
# #                     st.error(f"❌ Failed to start job: {res.status_code} - {res.text}")
# #             except requests.exceptions.RequestException as e:
# #                 st.error(f"❌ Connection Error: {str(e)}")

# # # ==========================================================
# # # REPORTS SECTION
# # # ==========================================================
# # st.markdown('<div class="section-header">📂 Generated Reports</div>', unsafe_allow_html=True)

# # if not all([DATABRICKS_TOKEN, DATABRICKS_INSTANCE, VOLUME_PATH]):
# #     st.warning("🔧 Please configure Databricks credentials in your secrets to view reports.")
# # else:
# #     headers = {
# #         "Authorization": f"Bearer {DATABRICKS_TOKEN}",
# #         "Accept": "application/json"
# #     }
    
# #     url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/directories{VOLUME_PATH}"
    
# #     try:
# #         with st.spinner("📥 Loading reports..."):
# #             response = requests.get(url, headers=headers, timeout=30)
        
# #         if response.status_code == 200:
# #             files = response.json().get("contents", [])
            
# #             if not files:
# #                 st.markdown("""
# #                 <div class="empty-state">
# #                     <div class="empty-state-icon">📭</div>
# #                     <h3>No Reports Yet</h3>
# #                     <p>Generate your first report using the form above</p>
# #                 </div>
# #                 """, unsafe_allow_html=True)
# #             else:
# #                 # Process files
# #                 df = pd.DataFrame(files)
# #                 df["last_modified"] = pd.to_datetime(df["last_modified"], unit="ms")
# #                 pdf_df = df[
# #                     (~df["is_directory"]) & 
# #                     (df["name"].str.endswith(".pdf"))
# #                 ].sort_values("last_modified", ascending=False)
                
# #                 # Stats
# #                 total_reports = len(pdf_df)
# #                 total_size_mb = round(pdf_df["file_size"].sum() / (1024 * 1024), 2)
                
# #                 # Display stats
# #                 col1, col2, col3 = st.columns(3)
                
# #                 with col1:
# #                     st.markdown(f"""
# #                     <div class="stat-card">
# #                         <div class="stat-value">{total_reports}</div>
# #                         <div class="stat-label">Total Reports</div>
# #                     </div>
# #                     """, unsafe_allow_html=True)
                
# #                 with col2:
# #                     st.markdown(f"""
# #                     <div class="stat-card">
# #                         <div class="stat-value">{total_size_mb}</div>
# #                         <div class="stat-label">Total Size (MB)</div>
# #                     </div>
# #                     """, unsafe_allow_html=True)
                
# #                 with col3:
# #                     if not pdf_df.empty:
# #                         latest = pdf_df.iloc[0]["last_modified"].strftime("%b %d")
# #                     else:
# #                         latest = "N/A"
# #                     st.markdown(f"""
# #                     <div class="stat-card">
# #                         <div class="stat-value">{latest}</div>
# #                         <div class="stat-label">Latest Report</div>
# #                     </div>
# #                     """, unsafe_allow_html=True)
                
# #                 st.write("")  # Spacer
                
# #                 # Display reports
# #                 if pdf_df.empty:
# #                     st.info("📄 No PDF reports found. Only PDF files are displayed.")
# #                 else:
# #                     for idx, row in pdf_df.iterrows():
# #                         file_name = row["name"]
# #                         file_path = row["path"]
# #                         size_kb = round(row["file_size"] / 1024, 1)
# #                         mod_time = row["last_modified"].strftime("%b %d, %Y %I:%M %p")
                        
# #                         col1, col2 = st.columns([5, 1])
                        
# #                         with col1:
# #                             st.markdown(f"""
# #                             <div class="report-card">
# #                                 <div class="report-name">
# #                                     📄 {file_name}
# #                                 </div>
# #                                 <div class="report-meta">
# #                                     <div class="report-meta-item">
# #                                         🕒 {mod_time}
# #                                     </div>
# #                                     <div class="report-meta-item">
# #                                         💾 {size_kb} KB
# #                                     </div>
# #                                 </div>
# #                             </div>
# #                             """, unsafe_allow_html=True)
                        
# #                         with col2:
# #                             # Fetch file content
# #                             file_api_url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/files{file_path}"
                            
# #                             try:
# #                                 file_res = requests.get(file_api_url, headers=headers, timeout=30)
                                
# #                                 if file_res.status_code == 200:
# #                                     pdf_bytes = file_res.content
# #                                     st.write("")  # Spacer for alignment
# #                                     st.download_button(
# #                                         label="⬇️ Download",
# #                                         data=pdf_bytes,
# #                                         file_name=file_name,
# #                                         mime="application/pdf",
# #                                         key=f"download_{file_name}_{idx}"
# #                                     )
# #                                 else:
# #                                     st.error(f"Error: {file_res.status_code}")
# #                             except requests.exceptions.RequestException as e:
# #                                 st.error(f"Failed to fetch file")
        
# #         elif response.status_code == 404:
# #             st.warning("📁 Volume path not found. Please verify your VOLUME_PATH configuration.")
# #         else:
# #             st.error(f"❌ Error listing files: {response.status_code} - {response.text}")
    
# #     except requests.exceptions.RequestException as e:
# #         st.error(f"❌ Connection Error: Unable to connect to Databricks. {str(e)}")

# # # ==========================================================
# # # FOOTER
# # # ==========================================================
# # st.markdown("---")
# # st.markdown("""
# # <div style="text-align: center; color: #6b7280; font-size: 0.875rem; padding: 1rem;">
# #     <p>Powered by Databricks & Streamlit | AI Report Generator v2.0</p>
# # </div>
# # """, unsafe_allow_html=True)


# # # ==========================================================
# # # PAGE CONFIG
# # # ==========================================================
# # st.set_page_config(page_title="AI Report Generator ", page_icon="📊", layout="wide")

# # # ==========================================================
# # # COMPACT DATARICKS-STYLE CSS
# # # ==========================================================
# # st.markdown("""
# # <style>
# # .block-container {padding-top:1.5rem; padding-left:2rem; padding-right:2rem;}
# # h1, h2, h3, h4 {font-family:'Inter', sans-serif;}
# # h1 {font-size:1.5rem !important; margin-bottom:0.3rem;}
# # p, label, .stTextInput label, .stCaption {font-size:0.9rem !important;}
# # .stTextInput>div>div>input {
# #     height:2.2rem !important;
# #     font-size:0.9rem !important;
# #     border-radius:5px !important;
# # }
# # .stButton>button {
# #     background-color:#FF3621 !important;
# #     color:white !important;
# #     border:none !important;
# #     border-radius:5px !important;
# #     padding:0.45rem 1rem !important;
# #     font-size:0.9rem !important;
# #     margin-top:0.2rem !important;
# # }
# # .stButton>button:hover {background-color:#E32F18 !important;}
# # .file-row {
# #     display:flex; justify-content:space-between; align-items:center;
# #     padding:8px 12px; border:1px solid #E5E7EB; border-radius:6px;
# #     margin-bottom:6px; background-color:#FAFAFA;
# # }
# # .file-row:hover {background-color:#F3F4F6;}
# # .file-info {display:flex; flex-direction:column;}
# # .file-title {font-weight:600; color:#111827;}
# # .file-meta {font-size:12px; color:#6B7280;}
# # </style>
# # """, unsafe_allow_html=True)

# # # ==========================================================
# # # HEADER
# # # ==========================================================
# # st.markdown("### 🧠 AI Business Report Generator")
# # st.caption("Trigger Databricks notebook jobs to create and download business PDF reports.")

# # # ==========================================================
# # # QUERY INPUT + BUTTON (INLINE + COMPACT)
# # # ==========================================================
# # col1, col2 = st.columns([4, 1])
# # with col1:
# #     report_query = st.text_input("Enter business query", placeholder="e.g., Voiletion Analysis report", label_visibility="collapsed")
# # with col2:
# #     st.write("")  # spacer for vertical alignment
# #     run_btn = st.button("🚀 Generate Report", use_container_width=True)

# # # ==========================================================
# # # JOB SUBMISSION
# # # ==========================================================
# # if run_btn:
# #     if not report_query.strip():
# #         st.warning("Please enter a query.")
# #     else:
# #         headers = {"Authorization": f"Bearer {DATABRICKS_TOKEN}", "Content-Type": "application/json"}
# #         payload = {
# #             "run_name": f"ai_report_{int(time.time())}",
# #             "existing_cluster_id": CLUSTER_ID,
# #             "notebook_task": {"notebook_path": NOTEBOOK_PATH, "base_parameters": {"user_question": report_query}},
# #         }

# #         submit_url = f"{DATABRICKS_INSTANCE}/api/2.1/jobs/runs/submit"
# #         with st.spinner("Submitting Databricks job..."):
# #             res = requests.post(submit_url, headers=headers, data=json.dumps(payload))
# #             if res.status_code == 200:
# #                 run_id = res.json()["run_id"]
# #                 st.success(f" Job submitted successfully (Run ID: `{run_id}`)")
# #             else:
# #                 st.error(f" Failed to start job: {res.text}")

# # st.divider()

# # # ==========================================================
# # # REPORT LIST (COMPACT + INLINE DOWNLOAD)
# # # ==========================================================
# # st.markdown("#### 📂 Generated Reports")

# # headers = {"Authorization": f"Bearer {DATABRICKS_TOKEN}", "Accept": "application/json"}
# # url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/directories{VOLUME_PATH}"

# # response = requests.get(url, headers=headers)
# # if response.status_code == 200:
# #     files = response.json().get("contents", [])
# #     if not files:
# #         st.info("No PDF reports found.")
# #     else:
# #         df = pd.DataFrame(files)
# #         df["last_modified"] = pd.to_datetime(df["last_modified"], unit="ms")
# #         pdf_df = df[~df["is_directory"] & df["name"].str.endswith(".pdf")].sort_values("last_modified", ascending=False)

# #         for _, row in pdf_df.iterrows():
# #             file_name = row["name"]
# #             file_path = row["path"]
# #             size_kb = round(row["file_size"] / 1024, 1)
# #             mod_time = row["last_modified"].strftime("%Y-%m-%d %H:%M")

# #             file_api_url = f"{DATABRICKS_INSTANCE}/api/2.0/fs/files{file_path}"
# #             file_res = requests.get(file_api_url, headers=headers)

# #             if file_res.status_code == 200:
# #                 pdf_bytes = file_res.content
# #                 with st.container():
# #                     c1, c2 = st.columns([6, 1])
# #                     with c1:
# #                         st.markdown(
# #                             f"""
# #                             <div class="file-row">
# #                                 <div class="file-info">
# #                                     <div class="file-title">{file_name}</div>
# #                                     <div class="file-meta">🕒 {mod_time} | 💾 {size_kb} KB</div>
# #                                 </div>
# #                             </div>
# #                             """,
# #                             unsafe_allow_html=True,
# #                         )
# #                     with c2:
# #                         st.download_button(
# #                             label="⬇️",
# #                             data=pdf_bytes,
# #                             file_name=file_name,
# #                             mime="application/pdf",
# #                             key=file_name
# #                         )
# #             else:
# #                 st.error(f"❌ Error fetching {file_name}")
# # else:
# #     st.error(f"❌ Error listing files: {response.status_code} - {response.text}")

