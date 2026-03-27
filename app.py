import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Engineering Sales Navigator", layout="wide")

st.title("🚀 Engineering Solution Sales Navigator")
st.sidebar.header("Meeting Setup")
inst_name = st.sidebar.text_input("Institution Name", "e.g., University of Dubai")

# --- Progress Bar ---
step = st.select_slider("Meeting Phase", options=["Intro", "Discovery", "AI Risk", "Demo", "Process", "The Close"])

st.divider()

# --- Logic Engine ---
if step == "Intro":
    st.subheader(f"Welcome to {inst_name}")
    st.info("💡 ACTION: Open SciVal Chart now.")
    st.write("**Commercial Insight:** Rankings are driven by citations; citations require seamless access.")

elif step == "Discovery":
    st.subheader("Q1: Access & Integration")
    choice = st.radio("How do they access content?", ["Discovery Layer (ExLibris)", "LMS (Blackboard/Canvas)"])
    
    if choice == "Discovery Layer (ExLibris)":
        st.warning("👉 FOLLOW-UP: 'When a student is stuck at midnight in the LMS, do they really leave to search your portal, or go to Google?'")
    else:
        st.warning("👉 FOLLOW-UP: 'Are these just static reading lists, or can students solve equations and digitize curves directly?'")

elif step == "AI Risk":
    st.subheader("Q2: AI Integrity")
    ai_choice = st.radio("What is their stance on AI?", ["They ban/discourage AI", "They use General AI (ChatGPT)"])
    
    if ai_choice == "They ban/discourage AI":
        st.error("💡 CHALLENGE: 'Since they use it anyway for speed, wouldn't it be safer to provide a Grounded AI that only cites peer-reviewed content?'")
    else:
        st.error("💡 CHALLENGE: 'General AI has a 15-20% hallucination rate. How do you protect research integrity?'")

elif step == "The Close":
    st.subheader("Q3: The Faculty Meeting (The 'Ask')")
    close_choice = st.radio("Librarian's Response:", ["Dean is too busy", "Start trial on website first"])
    
    if close_choice == "Dean is too busy":
        st.success("🎯 REBUTTAL: 'Let's frame it as an Engineering Data Integrity Briefing focused on Accreditation risk, not a demo.'")
    else:
        st.success("🎯 REBUTTAL: 'A passive trial is dead money. We need a Faculty Scream to justify the Rector's budget.'")

# --- Footer Guidance ---
st.sidebar.write("---")
st.sidebar.write(f"**MEDDPICC Focus:** {inst_name}")
