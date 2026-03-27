import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Engineering Sales Navigator", layout="wide")

st.title("🚀 Engineering Solution Sales Navigator")
st.sidebar.header("Meeting Setup")
inst_name = st.sidebar.text_input("Institution Name", "e.g., University of Dubai")

# --- Progress Bar based on your spreadsheet rows ---
# (You can add more stages here as you add rows from your PDF)
step = st.select_slider("Meeting Phase", options=["Intro", "Access & Discovery", "AI & Data Integrity", "Process & Budget"])

st.divider()

# --- THE DYNAMIC LOGIC ENGINE (Mapping to Renewals.pdf) ---

if step == "Access & Discovery":
    # --- ROW 1 FROM SPREADSHEET ---
    st.subheader("Module: Content Access")
    main_q = "How are your students currently accessing content?"
    st.markdown(f"**Main Question:** {main_q}")
    
    # Layer 1: Potential Answers
    ans_choice = st.radio("Select Response:", ["Select...", "Through the platforms directly", "Mainly through library homepage search bar"])

    if ans_choice == "Through the platforms directly": # Answer 1
        st.info(f"🎯 **Follow-up:** Which platforms or tools are they using?") # Objection/Follow-up 1
        
        # Layer 2: Answers 1-A and 1-B
        ans_1_layer = st.selectbox("Specific Tools:", ["Select...", "MATLAB / Solidworks / AutoCAD", "We don't know / Specialized"])
        
        if ans_1_layer == "MATLAB / Solidworks / AutoCAD": # Answer 1-A
            st.success("💡 **Next Step:** How do they get verified equations into those tools without risking human error from static PDFs?") # Follow-up 1-A
        elif ans_1_layer == "We don't know / Specialized": # Answer 1-B
            st.success("💡 **Next Step:** If the library doesn't know the workflow, how do you ensure the budget supports actual results?") # Follow-up 1-B

    elif ans_choice == "Mainly through library homepage search bar": # Answer 2
        st.info(f"🎯 **Follow-up:** Static lists are great for theory, but how do you ensure interactive data is available where they work?") # Objection/Follow-up 2
        
        # Layer 2: Answers 2-A and 2-B
        ans_2_layer = st.selectbox("Library Support:", ["Select...", "We don't have anything", "We provide software like MATLAB separately"])
        
        if ans_2_layer == "We don't have anything": # Answer 2-A
            st.error("💡 **Next Step:** Without interactive tools, how do you prevent the 30% time-waste on manual data entry?") # Follow-up 2-A
        elif ans_2_layer == "We provide software like MATLAB separately": # Answer 2-B
            st.success("💡 **Next Step:** MATLAB is the engine, but where do they get the validated 'fuel' (material properties) for it?") # Follow-up 2-B

elif step == "AI & Data Integrity":
    # --- ROW 2 FROM SPREADSHEET ---
    st.subheader("Module: AI Risks")
    main_q_ai = "How do you ensure students are using accurate AI with validated data?"
    st.markdown(f"**Main Question:** {main_q_ai}")

    ans_ai = st.radio("Select Response:", ["Select...", "We don't have an AI policy", "Students use ChatGPT/Gemini", "We have a specialized research AI"])

    if ans_ai == "We don't have an AI policy": # Answer 1
        st.info("🎯 **Follow-up:** Without a policy, how do you manage the risk of students citing hallucinated data in their designs?")
        # Logic continues to Answer 1-A / 1-B as per your spreadsheet...

# --- SIDEBAR MEDDPICC TRACKER ---
st.sidebar.divider()
st.sidebar.write(f"**Current Lead:** {inst_name}")
st.sidebar.write("**MEDDPICC Status:** Deep Discovery")
