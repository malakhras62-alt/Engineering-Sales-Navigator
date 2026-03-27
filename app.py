import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Engineering Sales Navigator", layout="wide")

st.title("🚀 Engineering Solution Sales Navigator")
st.sidebar.header("Meeting Setup")
inst_name = st.sidebar.text_input("Institution Name", "e.g., University of Dubai")

# --- Progress Bar based on Spreadsheet Rows ---
step = st.select_slider("Meeting Phase", options=[
    "01. Intro & Access", 
    "02. Discovery Layers", 
    "03. AI & Data Integrity", 
    "04. Active Tools", 
    "05. Material Property", 
    "06. Equations & Graphs",
    "07. Process & Decision"
])

st.divider()

# --- ROW 1: CONTENT ACCESS ---
if step == "01. Intro & Access":
    st.subheader("Module: Content Access")
    q1 = "How are your students currently accessing content?"
    st.markdown(f"**Question:** {q1}")
    
    ans1 = st.radio("Response:", ["Select...", "Through the platforms directly", "Mainly through our library homepage search bar"])

    if ans1 == "Through the platforms directly":
        st.info("🎯 **Follow-up:** Which Platform or tools are they using?")
        sub_ans = st.selectbox("Sub-Response:", ["Select...", "MATLAB / Solidworks / AutoCad", "We don't Know they are specialized platforms"])
        if sub_ans == "MATLAB / Solidworks / AutoCad":
            st.success("💡 **Next:** How do they get verified equations into those tools without risking human error from static PDFs?")
        elif sub_ans == "We don't Know they are specialized platforms":
            st.success("💡 **Next:** If the library doesn't know the workflow, how can you ensure the budget supports actual results?")

    elif ans1 == "Mainly through our library homepage search bar":
        st.info("🎯 **Follow-up:** Static lists are great for theory, but how do you ensure the interactive data is available right where they are doing the work?")
        sub_ans = st.selectbox("Sub-Response:", ["Select...", "We don't Have anything", "We provide access to software like MATLAB separately"])
        if sub_ans == "We don't Have anything":
            st.error("💡 **Next:** Without interactive tools, how do you prevent the 30% time-waste on manual data entry?")
        elif sub_ans == "We provide access to software like MATLAB separately":
            st.success("💡 **Next:** MATLAB is the engine, but where do they get the validated fuel (material properties) to plug into it?")

# --- ROW 2: DISCOVERY LAYERS ---
elif step == "02. Discovery Layers":
    st.subheader("Module: Discovery & Search")
    q2 = "Discovery layers often rely on exact keyword matching. How do you ensure a student looking for 'corrosion' doesn't miss content using the term 'oxidation'?"
    st.markdown(f"**Question:** {q2}")
    
    ans2 = st.radio("Response:", ["Select...", "Our discovery tool handles synonyms", "Students are responsible for their own search strings"])
    
    if ans2 == "Our discovery tool handles synonyms":
        st.info("🎯 **Follow-up:** Most tools use general dictionaries. Does yours include engineering-specific taxonomies to catch variations like 'creep' vs 'deformation'?")
    elif ans2 == "Students are responsible for their own search strings":
        st.error("💡 **Next:** If they miss content, the library is subscribing to 'Invisible Content.' How do you justify the ROI of hidden data?")

# --- ROW 3: AI & DATA INTEGRITY ---
elif step == "03. AI & Data Integrity":
    st.subheader("Module: AI Integrity")
    q3 = "How do you ensure students are using an accurate AI that provides validated data rather than general AI that might hallucinate engineering values?"
    st.markdown(f"**Question:** {q3}")
    
    ans3 = st.radio("Response:", ["Select...", "We encourage ChatGPT for efficiency", "We have no official AI policy", "We use specialized academic AI"])
    
    if ans3 == "We encourage ChatGPT for efficiency":
        st.error("💡 **Next:** General AI has a 15-20% hallucination rate in engineering. How do you protect the university's research integrity?")
    elif ans3 == "We have no official AI policy":
        st.warning("💡 **Next:** Without a policy, students go to the easiest tool. How do you provide a 'Safe Haven' of validated engineering data?")

# --- ROW 7: PROCESS & DECISION (MEDDPICC) ---
elif step == "07. Process & Decision":
    st.subheader("Module: Decision Making")
    q7 = "Who is the ultimate decision maker Library director or Library Committee or rector?"
    st.markdown(f"**Question:** {q7}")
    
    ans7 = st.radio("Response:", ["Select...", "Library Director", "Library Committee", "Rector"])
    
    if ans7 == "Library Director":
        st.info("🎯 **Follow-up:** Since you hold the ultimate decision, what specific 'internal proof' do you need to justify the Purchase?")
        sub_ans7 = st.selectbox("Requirements:", ["Select...", "Demand", "Usage", "Budget", "Demand, Usage and Budget"])
        if sub_ans7:
            st.success(f"💡 **Next:** Let's focus on {sub_ans7} to ensure we meet your specific criteria for approval.")

# --- SIDEBAR TRACKER ---
st.sidebar.divider()
st.sidebar.write(f"**Lead:** {inst_name}")
st.sidebar.write("**Status:** Interactive Discovery")
