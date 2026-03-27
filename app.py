import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Sales Navigator Wizard", layout="wide")

# --- Initialize Session State (The Program's Memory) ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'sub_step' not in st.session_state:
    st.session_state.sub_step = 0

def next_step():
    st.session_state.step += 1
    st.session_state.sub_step = 0

def reset():
    st.session_state.step = 1
    st.session_state.sub_step = 0

st.title("🚀 Engineering Sales Navigator: Interactive Wizard")
st.sidebar.button("🔄 Reset Meeting", on_click=reset)
inst_name = st.sidebar.text_input("Institution Name", "University of Dubai")

# --- STEP 1: CONTENT ACCESS ---
if st.session_state.step == 1:
    st.header("Module 01: Content Access")
    q1 = "How are your students currently accessing content?"
    st.subheader(q1)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Answer 1: Through the platforms directly"):
            st.session_state.sub_step = 1.1
    with col2:
        if st.button("Answer 2: Library homepage search bar"):
            st.session_state.sub_step = 1.2

    if st.session_state.sub_step == 1.1:
        st.info("🎯 **Follow-up:** Which Platform or tools are they using?")
        opt1 = st.button("1-A: MATLAB / Solidworks / AutoCad")
        opt2 = st.button("1-B: We don't Know / Specialized")
        if opt1:
            st.success("💡 **Next:** How do they get verified equations into those tools without risking human error from static PDFs?")
            st.button("Move to Next Module ➡️", on_click=next_step)
        if opt2:
            st.success("💡 **Next:** If the library doesn't know the workflow, how can you ensure the budget supports actual results?")
            st.button("Move to Next Module ➡️", on_click=next_step)

    if st.session_state.sub_step == 1.2:
        st.info("🎯 **Follow-up:** Static lists are great for theory, but how do you ensure the interactive data is available where they work?")
        opt3 = st.button("2-A: We don't Have anything")
        opt4 = st.button("2-B: We provide access to software like MATLAB separately")
        if opt3:
            st.error("💡 **Next:** Without interactive tools, how do you prevent the 30% time-waste on manual data entry?")
            st.button("Move to Next Module ➡️", on_click=next_step)
        if opt4:
            st.success("💡 **Next:** MATLAB is the engine, but where do they get the validated fuel (material properties) to plug into it?")
            st.button("Move to Next Module ➡️", on_click=next_step)

# --- STEP 2: DISCOVERY LAYERS ---
elif st.session_state.step == 2:
    st.header("Module 02: Discovery Layers")
    q2 = "Discovery layers often rely on exact keyword matching. How do you ensure a student looking for 'corrosion' doesn't miss 'oxidation'?"
    st.subheader(q2)

    if st.button("Answer 1: Our discovery tool handles synonyms"):
        st.info("🎯 **Follow-up:** Does it include engineering-specific taxonomies to catch variations like 'creep' vs 'deformation'?")
        st.button("Move to Next Module ➡️", on_click=next_step)
    
    if st.button("Answer 2: Students are responsible for their own search strings"):
        st.error("💡 **Next:** If they miss content, you are subscribing to 'Invisible Content.' How do you justify ROI?")
        st.button("Move to Next Module ➡️", on_click=next_step)

# --- STEP 3: AI & DATA INTEGRITY ---
elif st.session_state.step == 3:
    st.header("Module 03: AI & Data Integrity")
    q3 = "How do you ensure students are using an accurate AI that provides validated data?"
    st.subheader(q3)

    if st.button("Answer 1: We encourage ChatGPT for efficiency"):
        st.error("💡 **Next:** General AI has a 15-20% hallucination rate. How do you protect research integrity?")
        st.button("Move to Next Module ➡️", on_click=next_step)
    
    if st.button("Answer 2: We have no official AI policy"):
        st.warning("💡 **Next:** Without a policy, students go to the easiest tool. How do you provide a 'Safe Haven'?")
        st.button("Finish Discovery 🏁", on_click=reset)

st.sidebar.markdown(f"--- \n**Current Lead:** {inst_name}")
