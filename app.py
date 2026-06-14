import streamlit as st
from streamlit_option_menu import option_menu

from pages.dashboard import show_dashboard
from pages.login import show_login
from pages.register import show_register
from pages.chatbot import show_chatbot
from pages.job_search import show_job_search
from pages.resume_analyzer import show_resume_analyzer
from pages.resume_builder import show_resume_builder
from pages.profile import show_profile
from pages.tracker import show_tracker


# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="JobSpark AI",
    page_icon="🚀",
    layout="wide"
)

# ----------------------------------
# SESSION STATE
# ----------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------------------------
# LOGIN / REGISTER
# ----------------------------------

if not st.session_state.logged_in:

    auth_choice = st.sidebar.radio(
        "Authentication",
        ["Login", "Register"]
    )

    if auth_choice == "Login":
        show_login()
    else:
        show_register()

    st.stop()

# ----------------------------------
# LIGHT THEME
# ----------------------------------

st.markdown("""
<style>

/* Main App */

.stApp{
    background-color:#FFFFFF;
    color:#111827;
}

/* Sidebar */

[data-testid="stSidebar"]{
    background-color:#F8FAFC;
    border-right:1px solid #E5E7EB;
}

/* Metric Cards */

div[data-testid="metric-container"]{
    background-color:#FFFFFF;
    border:1px solid #E5E7EB;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.05);
}

/* Buttons */

.stButton > button{
    background-color:#2563EB;
    color:white;
    border:none;
    border-radius:10px;
}

.stButton > button:hover{
    background-color:#1D4ED8;
    color:white;
}

/* Inputs */

.stTextInput input,
.stTextArea textarea{
    background-color:#FFFFFF;
    color:#111827;
    border:1px solid #D1D5DB;
}

/* Upload */

[data-testid="stFileUploader"]{
    border:2px dashed #CBD5E1;
    border-radius:12px;
    padding:10px;
}

/* Headings */

h1,h2,h3{
    color:#111827;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:

    if "user" in st.session_state:

        st.image(
            "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
            width=90
        )

        st.markdown(
            f"### {st.session_state.user.get('name','User')}"
        )

        st.caption(
            st.session_state.user.get('email','')
        )

        st.divider()

    selected = option_menu(
        menu_title="🚀 JobSpark AI",
        options=[
            "Dashboard",
            "Profile",
            "AI Chatbot",
            "Job Search",
            "Resume Builder",
            "Resume Analyzer",
            "Application Tracker"
        ],
        icons=[
            "house",
            "person-circle",
            "robot",
            "search",
            "file-earmark-person",
            "graph-up",
            "clipboard-check"
        ],
        default_index=0
    )

    st.divider()

    if st.button("🚪 Logout"):

        st.session_state.logged_in = False

        if "user" in st.session_state:
            del st.session_state.user

        st.rerun()

# ----------------------------------
# PAGE ROUTING
# ----------------------------------

if selected == "Dashboard":

    show_dashboard()

elif selected == "Profile":

    show_profile()

elif selected == "AI Chatbot":

    show_chatbot()

elif selected == "Job Search":

    show_job_search()

elif selected == "Resume Builder":

    show_resume_builder()

elif selected == "Resume Analyzer":

    show_resume_analyzer()

elif selected == "Application Tracker":

    show_tracker()