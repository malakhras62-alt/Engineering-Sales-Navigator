import streamlit as st
from fpdf import FPDF
import base64

# --- 1. Session State Initialization ---
if 'row_index' not in st.session_state:
    st.session_state.row_index = -1  
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

# --- 2. PDF Export Function ---
def create_pdf(univ, stakeholder, solution):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Meeting Summary Report", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt=f"University: {univ}", ln=True)
    pdf.cell(200, 10, txt=f"Stakeholder: {stakeholder}", ln=True)
    pdf.cell(200, 10, txt=f"Solution Pitched: {solution}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 10, txt="Outcome: The strategic alignment and discovery phases were completed. Follow-up regarding trials and Dean involvement is required.")
    
    return pdf.output(dest='S').encode('latin-1')

st.set_page_config(page_title="Engineering Sales Navigator", layout="wide")

# --- 3. SETUP PHASE ---
if st.session_state.row_index == -1:
    st.header("🏢 Meeting Setup")
    univ = st.text_input("What is the university name?", placeholder="e.g., University of Sharjah")
    
    st.subheader("Meeting Details")
    col_a, col_b = st.columns(2)
    with col_a:
        role = st.selectbox("With whom is the meeting?", ["Library", "Dean / Vice Dean of Engineering", "Dean / Vice Dean of Research", "Rector / Vice Rector", "Head of Department", "Professor"])
    with col_b:
        pitch = st.selectbox("Which solution are you pitching?", ["Knovel", "Compendex Only", "Compendex + Patent Plus", "Patent Plus"])
    
    if st.button("Start Meeting"):
        if not univ:
            st.error("Please enter a University Name to proceed.")
        else:
            st.session_state.univ_name = univ
            st.session_state.stakeholder = role
            st.session_state.solution_pitch = pitch
            st.session_state.row_index = 0 
            st.rerun()

# --- 4. GATEKEEPER LOGIC ---
elif st.session_state.row_index >= 0:
    is_library = st.session_state.stakeholder == "Library"
    is_knovel = st.session_state.solution_pitch == "Knovel"

    if not (is_library and is_knovel):
        st.warning("⚠️ **Under Construction**")
        st.info(f"The flow for **{st.session_state.stakeholder}** + **{st.session_state.solution_pitch}** is coming soon.")
        if st.button("⬅️ Back to Setup"):
            st.session_state.row_index = -1
            st.rerun()
        st.stop() 

    # --- 5. LIBRARY + KNOVEL FLOW (PHASES 01-08) ---
    if st.session_state.row_index == 0:
        st.header("Phase 01: Content Access")
        st.subheader("How are your students currently accessing content?")
        if st.session_state.sub_step == "main":
            if st.button("Answer 1: Mainly library search bar"):
                st.session_state.selected_ans = "ans1"; st.session_state.sub_step = "follow_up"; st.rerun()
            if st.button("Answer 2: Reading Lists in LMS"):
                st.session_state.selected_ans = "ans2"; st.session_state.sub_step = "follow_up"; st.rerun()
            if st.button("Answer 3: Publisher platform"):
                st.session_state.selected_ans = "ans3"; st.session_state.sub_step = "follow_up"; st.rerun()
        elif st.session_state.sub_step == "follow_up":
            st.info("🎯 **Objection Context:** Keyword matching vs. Concept search.")
            st.button("Next Main Question ➡️", on_click=next_row)

    elif st.session_state.row_index == 1:
        st.header("Phase 02: Active Tools")
        st.subheader("How is the library providing 'Active Tools' (calculators) vs. 'Passive Reading'?")
        if st.button("Faculty handles tools"):
            st.info("🎯 **Objection:** Wouldn't it be great to combine literature and tools?")
        st.button("Next Main Question ➡️", on_click=next_row)

    elif st.session_state.row_index == 2:
        st.header("Phase 03: Data Extraction")
        st.subheader("How would the library address a request to interact with a graph?")
        st.button("Manual Extraction", on_click=next_row)

    elif st.session_state.row_index == 3:
        st.header("Phase 04: Evaluation")
        st.button("Usage, Demand, Price", on_click=next_row)

    elif st.session_state.row_index == 4:
        st.header("Phase 05: Decision Maker")
        st.radio("Selection:", ["Director", "Committee", "Rector"])
        st.button("Next ➡️", on_click=next_row)

    elif st.session_state.row_index == 5:
        st.header("Phase 06: Budget")
        st.button("Confirm Budget Logic", on_click=next_row)

    elif st.session_state.row_index == 6:
        st.header("Phase 07: Timeline")
        st.button("Next Quarter", on_click=next_row)

    # --- FINAL WRAP UP PAGE ---
    elif st.session_state.row_index == 7:
        st.balloons()
        st.header("✅ Meeting Complete")
        st.write(f"Meeting with **{st.session_state.stakeholder}** at **{st.session_state.univ_name}**.")
        st.write(f"Solution: **{st.session_state.solution_pitch}**")
        
        st.divider()
        st.subheader("Export Results")
        
        # PDF Generation Button
        pdf_data = create_pdf(st.session_state.univ_name, st.session_state.stakeholder, st.session_state.solution_pitch)
        st.download_button(
            label="📄 End Meeting & Download PDF",
            data=pdf_data,
            file_name=f"Meeting_{st.session_state.univ_name}.pdf",
            mime="application/pdf"
        )
        
        if st.button("Restart Navigator"):
            st.session_state.row_index = -1
            st.rerun()
