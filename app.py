import streamlit as st

# --- 1. Session State Initialization ---
if 'row_index' not in st.session_state:
    st.session_state.row_index = -1  # Starts at Setup Phase
if 'sub_step' not in st.session_state:
    st.session_state.sub_step = "main"
if 'selected_ans' not in st.session_state:
    st.session_state.selected_ans = None
if 'univ_name' not in st.session_state:
    st.session_state.univ_name = ""
if 'stakeholder' not in st.session_state:
    st.session_state.stakeholder = ""
if 'solution_pitch' not in st.session_state:
    st.session_state.solution_pitch = ""

def next_row():
    st.session_state.row_index += 1
    st.session_state.sub_step = "main"
    st.session_state.selected_ans = None

st.set_page_config(page_title="Engineering Sales Navigator", layout="wide")

# --- 2. SETUP PHASE: University & Stakeholder ---
if st.session_state.row_index == -1:
    st.header("🏢 Meeting Setup")
    
    univ = st.text_input("What is the university name?", placeholder="e.g., University of Sharjah")
    
    st.subheader("Meeting Details")
    col_a, col_b = st.columns(2)
    
    with col_a:
        role = st.selectbox("With whom is the meeting?", [
            "Library",
            "Dean / Vice Dean of Engineering",
            "Dean / Vice Dean of Research",
            "Rector / Vice Rector",
            "Head of Department",
            "Professor"
        ])

    with col_b:
        pitch = st.selectbox("Which solution are you pitching?", [
            "Knovel",
            "Compendex Only", 
            "Compendex + Patent Plus", 
            "Patent Plus"
        ])
    
    if st.button("Start Meeting"):
        if not univ:
            st.error("Please enter a University Name to proceed.")
        else:
            st.session_state.univ_name = univ
            st.session_state.stakeholder = role
            st.session_state.solution_pitch = pitch
            st.session_state.row_index = 0 
            st.rerun()

# --- 3. GATEKEEPER LOGIC ---
elif st.session_state.row_index >= 0:
    # Only allow Library + Knovel to see the detailed flow
    is_library = st.session_state.stakeholder == "Library"
    is_knovel = st.session_state.solution_pitch == "Knovel"

    if not (is_library and is_knovel):
        st.warning("⚠️ **Under Construction**")
        st.info(f"The specialized flow for **{st.session_state.stakeholder}** + **{st.session_state.solution_pitch}** is currently being built.")
        if st.button("⬅️ Back to Setup"):
            st.session_state.row_index = -1
            st.rerun()
        st.stop() 

    # --- 4. LIBRARY + KNOVEL FLOW ---
    
    # --- PHASE 01: CONTENT ACCESS ---
    if st.session_state.row_index == 0:
        st.header("Phase 01: Content Access")
        st.subheader("How are your students currently accessing content?")
        
        if st.session_state.sub_step == "main":
            if st.button("Answer 1: Mainly through our library homepage search bar."):
                st.session_state.selected_ans = "ans1"; st.session_state.sub_step = "follow_up"; st.rerun()
            if st.button("Answer 2: We have some 'Reading Lists' integrated into the LMS."):
                st.session_state.selected_ans = "ans2"; st.session_state.sub_step = "follow_up"; st.rerun()
            if st.button("Answer 3: Through the Publisher platform"):
                st.session_state.selected_ans = "ans3"; st.session_state.sub_step = "follow_up"; st.rerun()

        elif st.session_state.sub_step == "follow_up":
            if st.session_state.selected_ans == "ans1":
                st.info("🎯 **Objection:** Discovery layers rely on keyword matching. How do you ensure students don't miss 'oxidation' when searching 'corrosion'?")
                if st.button("1-A: Basic Boolean logic/tagging"):
                    st.success("💡 **Follow-up:** If they aren't 'Search Experts,' they miss content you paid for. How do you justify the ROI?")
                    st.button("Next Main Question ➡️", on_click=next_row)
                if st.button("1-B: We teach them in workshops"):
                    st.success("💡 **Follow-up:** Engineering students need info on topics outside their department; they won't know the synonyms needed.")
                    st.button("Next Main Question ➡️", on_click=next_row)
                if st.button("1-C: Trust publisher metadata"):
                    st.success("💡 **Follow-up:** If search isn't 'Concept-Based,' aren't you paying for an invisible library?")
                    st.button("Next Main Question ➡️", on_click=next_row)

            elif st.session_state.selected_ans == "ans2":
                st.info("🎯 **Objection:** Static lists are great for theory, but how do they pull values from interactive Graphs and Equations?")
                st.button("Next Main Question ➡️", on_click=next_row)

            elif st.session_state.selected_ans == "ans3":
                st.info("🎯 **Objection:** Accessing multiple databases individually leads to missing info and wasted time.")
                st.button("Next Main Question ➡️", on_click=next_row)

    # --- PHASE 02: ACTIVE TOOLS ---
    elif st.session_state.row_index == 1:
        st.header("Phase 02: Active Tools & Workflow")
        st.subheader("How is the library providing 'Active Tools' (calculators) rather than just 'Passive Reading' (PDFs)?")

        if st.session_state.sub_step == "main":
            if st.button("Answer 1: MATLAB separately"):
                st.session_state.selected_ans = "ans1"; st.session_state.sub_step = "follow_up"; st.rerun()
            if st.button("Answer 2: Technical tables"):
                st.session_state.selected_ans = "ans2"; st.session_state.sub_step = "follow_up"; st.rerun()
            if st.button("Answer 3: Faculty handles tools"):
                st.session_state.selected_ans = "ans3"; st.session_state.sub_step = "follow_up"; st.rerun()

        elif st.session_state.sub_step == "follow_up":
            if st.session_state.selected_ans == "ans1":
                st.info("🎯 **Objection:** Where do students find validated material properties to plug into MATLAB without hours of searching?")
            elif st.session_state.selected_ans == "ans2":
                st.info("🎯 **Objection:** Are those tables just pictures, or can students export data directly to Excel/CAD?")
            elif st.session_state.selected_ans == "ans3":
                st.info("🎯 **Objection:** Wouldn't it be great to combine literature and tools in a single solution?")
            st.button("Next Main Question ➡️", on_click=next_row)

    # --- PHASE 03: DATA EXTRACTION ---
    elif st.session_state.row_index == 2:
        st.header("Phase 03: Data Extraction & Accuracy")
        st.subheader("How would the library address a request to interact with a graph or get a material property?")
        if st.button("Answer 1: Manual Extraction"):
            st.error("🎯 **Objection:** Manual extraction is the #1 mistake causing inaccurate information and typo errors.")
            st.button("Next Main Question ➡️", on_click=next_row)
        if st.button("Answer 2: Specialized Digitization Software"):
            st.info("🎯 **Objection:** Moving between tools creates 'Data Friction.' Why not have interactive data on the page?")
            st.button("Next Main Question ➡️", on_click=next_row)

    # --- PHASE 04: EVALUATION PROCESS ---
    elif st.session_state.row_index == 3:
        st.header("Phase 04: Evaluation Process")
        st.subheader("What do you take into consideration during evaluation?")
        if st.button("Usage, Demand, Price"):
            st.info("🎯 **Objection:** How many faculty members must request a tool to guarantee purchase?")
            st.button("Next Main Question ➡️", on_click=next_row)
        if st.button("Usage and Price"):
            st.info("🎯 **Objection:** What specific content view usage do you consider 'good'?")
            st.button("Next Main Question ➡️", on_click=next_row)

    # --- PHASE 05: DECISION MAKER ---
    elif st.session_state.row_index == 4:
        st.header("Phase 05: Decision Maker & Power")
        st.subheader("Who is the ultimate decision maker?")
        ans = st.radio("Select Response:", ["Library Director", "Library Committee", "Rector"])
        if st.button("Confirm Response"):
            if ans == "Library Director": st.info("🎯 **Objection:** What 'internal proof' do you need to justify the purchase?")
            elif ans == "Library Committee": st.info("🎯 **Objection:** Who has the highest influence on specialized tools?")
            else: st.info("🎯 **Objection:** How does the Rector decide if we should proceed?")
            st.button("Next Main Question ➡️", on_click=next_row)

    # --- PHASE 06: BUDGET ---
    elif st.session_state.row_index == 5:
        st.header("Phase 06: Budget & Financial Reality")
        st.subheader("Is there a specific budget set aside for new tools?")
        if st.button("Depends on budget received later"):
            st.info("🎯 **Objection:** When is that confirmed (Q1-Q4)? Do you have a prioritized list?")
            st.button("Next Main Question ➡️", on_click=next_row)
        if st.button("No budget / Need to cancel a tool"):
            st.error("🎯 **Objection:** What criteria make a new tool a 'top priority' to replace an old one?")
            st.button("Next Main Question ➡️", on_click=next_row)

    # --- PHASE 07: TIMELINE ---
    elif st.session_state.row_index == 6:
        st.header("Phase 07: Timeline & Procurement")
        st.subheader("When would you like the start date to be?")
        st.button("01 Jan", on_click=next_row)
        st.button("Next Quarter", on_click=next_row)
        st.button("September", on_click=next_row)

    # --- PHASE 08: THE DEAN MEETING ---
    elif st.session_state.row_index == 7:
        st.header("Phase 08: Strategic Alignment (The Dean)")
        st.subheader("Feasibility of a 15-min meeting with the Dean next week?")
        if st.button("Let's start trial first"):
            st.error("🎯 **Objection:** A trial without faculty endorsement is a 'dead trial.' We need alignment first.")
        if st.button("I'll talk to the Dean myself"):
            st.info("🎯 **Objection:** I'll reach out to highlight key points and keep you in CC to save you time.")
        if st.button("Next Main Question ➡️"):
            next_row()

    # --- PHASE 09: WRAP UP ---
    elif st.session_state.row_index == 8:
        st.balloons()
        st.header("✅ Meeting Complete")
        st.write(f"Meeting with **{st.session_state.stakeholder}** at **{st.session_state.univ_name}**.")
        st.write(f"Solution Pitched: **{st.session_state.solution_pitch}**")
        if st.button("Restart Navigator"):
            st.session_state.row_index = -1
            st.rerun()

import pandas as pd
from datetime import datetime
import os

def save_to_csv(univ, stakeholder, solution):
    file_name = "meeting_history.csv"
    
    # Create the data row
    new_data = {
        "Date": [datetime.now().strftime("%Y-%m-%d %H:%M")],
        "University": [univ],
        "Stakeholder": [stakeholder],
        "Solution": [solution],
        "Status": ["Completed"]
    }
    df_new = pd.DataFrame(new_data)
    
    # If file doesn't exist, create it with headers. If it does, append without headers.
    if not os.path.isfile(file_name):
        df_new.to_csv(file_name, index=False)
    else:
        df_new.to_csv(file_name, mode='a', header=False, index=False)

# --- Inside your Final Wrap-Up Page (Phase 09) ---
if st.button("🏁 End Meeting & Save to Database"):
    save_to_csv(st.session_state.univ_name, st.session_state.stakeholder, st.session_state.solution_pitch)
    st.success("Data saved to meeting_history.csv!")

if st.checkbox("Show Meeting History"):
    if os.path.exists("meeting_history.csv"):
        history_df = pd.read_csv("meeting_history.csv")
        st.dataframe(history_df)
    else:
        st.write("No history found yet.")

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
