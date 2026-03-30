import streamlit as st
import pandas as pd
from datetime import datetime
import os
from fpdf import FPDF

# --- 1. Session State Initialization ---
if 'row_index' not in st.session_state:
    st.session_state.row_index = -1  
if 'sub_step' not in st.session_state:
    st.session_state.sub_step = "main"
if 'selected_ans' not in st.session_state:
    st.session_state.selected_ans = None
if 'meeting_log' not in st.session_state:
    st.session_state.meeting_log = [] # This stores all your answers

def record_and_next(question_label, answer_text):
    """Saves the answer to the log and moves to the next question."""
    st.session_state.meeting_log.append(f"{question_label}: {answer_text}")
    st.session_state.row_index += 1
    st.session_state.sub_step = "main"
    st.session_state.selected_ans = None

# --- 2. Permanent Storage (CSV) ---
def save_to_csv(univ, stakeholder, solution, log_list):
    file_name = "meeting_records.csv"
    detailed_answers = " | ".join(log_list) # Combines all answers into one string
    
    new_data = {
        "Date": [datetime.now().strftime("%Y-%m-%d %H:%M")],
        "University": [univ],
        "Stakeholder": [stakeholder],
        "Solution": [solution],
        "Answers_Log": [detailed_answers]
    }
    df_new = pd.DataFrame(new_data)
    
    if not os.path.isfile(file_name):
        df_new.to_csv(file_name, index=False)
    else:
        df_new.to_csv(file_name, mode='a', header=False, index=False)

# --- 3. SETUP PHASE ---
if st.session_state.row_index == -1:
    st.header("🏢 Meeting Setup")
    univ = st.text_input("University Name", placeholder="e.g., University of Sharjah")
    role = st.selectbox("Stakeholder", ["Library", "Dean of Engineering"])
    pitch = st.selectbox("Solution", ["Knovel", "Compendex"])
    
    if st.button("Start Meeting"):
        st.session_state.univ_name = univ
        st.session_state.stakeholder = role
        st.session_state.solution_pitch = pitch
        st.session_state.row_index = 0
        st.rerun()

# --- 4. LIBRARY + KNOVEL FLOW ---
elif st.session_state.row_index == 0:
    st.header("Phase 01: Content Access")
    if st.session_state.sub_step == "main":
        if st.button("Mainly Library Search Bar"):
            st.session_state.selected_ans = "Search Bar"; st.session_state.sub_step = "follow_up"; st.rerun()
        if st.button("Reading Lists in LMS"):
            st.session_state.selected_ans = "LMS Lists"; st.session_state.sub_step = "follow_up"; st.rerun()
            
    elif st.session_state.sub_step == "follow_up":
        st.info(f"You selected: {st.session_state.selected_ans}")
        if st.button("Confirm & Next Question"):
            # This is where we SAVE the answer to the CSV log
            record_and_next("Phase 01 Access", st.session_state.selected_ans)
            st.rerun()

# --- 5. WRAP UP & SAVE ---
elif st.session_state.row_index >= 1: # Adjust this index based on your total phases
    st.header("✅ Meeting Complete")
    
    if st.button("💾 Save to Database (CSV) & End Meeting"):
        save_to_csv(
            st.session_state.univ_name, 
            st.session_state.stakeholder, 
            st.session_state.solution_pitch,
            st.session_state.meeting_log
        )
        st.success(f"Meeting for {st.session_state.univ_name} recorded successfully!")
        
    if st.checkbox("View Saved History"):
        if os.path.exists("meeting_records.csv"):
            st.dataframe(pd.read_csv("meeting_records.csv"))

    if st.button("Restart"):
        st.session_state.row_index = -1
        st.session_state.meeting_log = []
        st.rerun()
