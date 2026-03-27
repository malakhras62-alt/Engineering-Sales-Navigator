import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Engineering Sales Navigator", layout="wide")

st.title("🚀 Engineering Solution Sales Navigator")
st.sidebar.header("Meeting Setup")
inst_name = st.sidebar.text_input("Institution Name", "e.g., University of Dubai")

# --- Progress Bar ---
step = st.select_slider("Meeting Phase", options=["Intro", "Access & Integration", "AI Risk", "The Close"])

st.divider()

# --- MODULE 1: ACCESS & INTEGRATION ---
if step == "Access & Integration":
    st.subheader(f"Step 2: Access & Discovery at {inst_name}")
    
    # LAYER 1: Main Question
    main_q = st.radio(
        "Main Question: How are your students currently accessing content?",
        ["Select...", "1. Through the platforms directly", "2. Mainly through our library homepage search bar"]
    )

    # LAYER 2: First Follow-up based on Answer 1
    if main_q == "1. Through the platforms directly":
        st.info("🎯 Follow-up: 'Which specific platforms or tools are they using?'")
        layer_1_ans = st.selectbox("Librarian's Response:", ["Select...", "1-1: MATLAB / Solidworks / AutoCAD", "1-2: We don't know (Specialized)"])
        
        if layer_1_ans == "1-1: MATLAB / Solidworks / AutoCAD":
            st.success("💡 CHALLENGER PIVOT: 'How do they get verified equations into those platforms without risking human error from static PDFs?'")
        elif layer_1_ans == "1-2: We don't know (Specialized)":
            st.error("💡 CHALLENGER PIVOT: 'If the library doesn't know the workflow, how can you ensure the budget supports actual engineering results?'")

    # LAYER 2: First Follow-up based on Answer 2
    elif main_q == "2. Mainly through our library homepage search bar":
        st.info("🎯 Follow-up: 'Static lists are great for theory, but how do you ensure the interactive data (equations/tables) is available right where they are doing the work?'")
        layer_2_ans = st.selectbox("Librarian's Response:", ["Select...", "2-1: We don't have anything", "2-2: We provide software like MATLAB separately"])
        
        if layer_2_ans == "2-1: We don't have anything":
            st.error("💡 CHALLENGER PIVOT: 'Without interactive tools, how do you prevent the 30% time-waste on manual data entry?'")
        elif layer_2_ans == "2-2: We provide software like MATLAB separately":
            st.success("💡 CHALLENGER PIVOT: 'MATLAB is the engine, but where do they get the validated fuel—the material properties—to plug into it?'")

# --- MODULE 2: AI RISK (Placeholder for next session) ---
elif step == "AI Risk":
    st.subheader("Next Module: AI Integrity")
    st.write("Ready to build the AI Risk logic tree...")

# --- Sidebar MEDDPICC Tracker ---
st.sidebar.divider()
st.sidebar.write(f"**Current Lead:** {inst_name}")
st.sidebar.write("**MEDDPICC Status:** Discovery Stage")
