import streamlit as st
import pandas as pd

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
if 'answers' not in st.session_state:
    st.session_state.answers = {}  # Added to track answers for CSV

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
                st.session_state.answers["Phase 01: Content Access"] = "Mainly through library homepage search bar"
                st.session_state.selected_ans = "ans1"; st.session_state.sub_step = "follow_up"; st.rerun()
            if st.button("Answer 2: We have some 'Reading Lists' integrated into the LMS."):
                st.session_state.answers["Phase 01: Content Access"] = "Reading Lists integrated into LMS"
                st.session_state.selected_ans = "ans2"; st.session_state.sub_step = "follow_up"; st.rerun()
            if st.button("Answer 3: Through the Publisher platform"):
                st.session_state.answers["Phase 01: Content Access"] = "Through the Publisher platform"
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
                st.session_state.answers["Phase 02: Active Tools"] = "MATLAB separately"
                st.session_state.selected_ans = "ans1"; st.session_state.sub_step = "follow_up"; st.rerun()
            if st.button("Answer 2: Technical tables"):
                st.session_state.answers["Phase 02: Active Tools"] = "Technical tables"
                st.session_state.selected_ans = "ans2"; st.session_state.sub_step = "follow_up"; st.rerun()
            if st.button("Answer 3: Faculty handles tools"):
                st.session_state.answers["Phase 02: Active Tools"] = "Faculty handles tools"
                st.session_state.selected_ans = "ans3"; st.session_state.sub_step = "follow_up"; st.rerun()

        elif st.session_state.sub_step == "follow_up":
            if st.session_state.selected_ans == "ans1":
                st.info("🎯 **Objection")
