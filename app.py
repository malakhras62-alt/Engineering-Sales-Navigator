import streamlit as st

# --- Session State Initialization ---
if 'row_index' not in st.session_state:
    st.session_state.row_index = 0
if 'sub_step' not in st.session_state:
    st.session_state.sub_step = "main"
if 'selected_ans' not in st.session_state:
    st.session_state.selected_ans = None

def next_row():
    st.session_state.row_index += 1
    st.session_state.sub_step = "main"
    st.session_state.selected_ans = None

st.title("🚀 Engineering Sales Navigator")

# --- MODULE 1: CONTENT ACCESS ---
if st.session_state.row_index == 0:
    st.header("Phase 01: Content Access")
    st.subheader("How are your students currently accessing content?")
    
    if st.session_state.sub_step == "main":
        if st.button("Answer 1: Mainly through our library homepage search bar."):
            st.session_state.selected_ans = "ans1"
            st.session_state.sub_step = "follow_up"
            st.rerun()
        if st.button("Answer 2: We have some 'Reading Lists' integrated into the LMS."):
            st.session_state.selected_ans = "ans2"
            st.session_state.sub_step = "follow_up"
            st.rerun()
        if st.button("Answer 3: Through the Publisher platform"):
            st.session_state.selected_ans = "ans3"
            st.session_state.sub_step = "follow_up"
            st.rerun()

    elif st.session_state.sub_step == "follow_up":
        if st.session_state.selected_ans == "ans1":
            st.info("🎯 **Objection:** Discovery layers often rely on exact keyword matching. How do you ensure a student looking for 'corrosion' doesn't miss content using the term 'oxidation'?")
            if st.button("1-A: Our search engine uses basic Boolean logic and tagging."):
                st.success("💡 **Follow-up:** If a student isn't a 'Search Expert,' they miss out on content you paid for.")
                st.button("Next Main Question ➡️", on_click=next_row)
            if st.button("1-B: We teach students how to search better in workshops."):
                st.success("💡 **Follow-up:** Engineering students still need synonyms they might not know.")
                st.button("Next Main Question ➡️", on_click=next_row)
            if st.button("1-C: We trust metadata."):
                st.success("💡 **Follow-up:** Aren't you essentially paying for a library where books are invisible?")
                st.button("Next Main Question ➡️", on_click=next_row)

        elif st.session_state.selected_ans == "ans2":
            st.info("🎯 **Objection:** How do they search beyond that list or pull values out with Graphs and Equations?")
            st.button("Next Main Question ➡️", on_click=next_row)

        elif st.session_state.selected_ans == "ans3":
            st.info("🎯 **Objection:** Searching multiple databases individually leads to missing info and wasted time.")
            st.button("Next Main Question ➡️", on_click=next_row)

# --- MODULE 2: ACTIVE TOOLS ---
elif st.session_state.row_index == 1:
    st.header("Phase 02: Active Tools & Workflow")
    st.subheader("How is the library providing 'Active Tools' (calculators) rather than just 'Passive Reading'?")

    if st.session_state.sub_step == "main":
        if st.button("Answer 1: MATLAB separately"):
            st.session_state.selected_ans = "ans1"
            st.session_state.sub_step = "follow_up"
            st.rerun()
        if st.button("Answer 2: Technical tables"):
            st.session_state.selected_ans = "ans2"
            st.session_state.sub_step = "follow_up"
            st.rerun()
        if st.button("Answer 3: Faculty handles tools"):
            st.session_state.selected_ans = "ans3"
            st.session_state.sub_step = "follow_up"
            st.rerun()

    elif st.session_state.sub_step == "follow_up":
        if st.session_state.selected_ans == "ans1":
            st.info("🎯 **Objection:** Where do they find the validated material properties for those models?")
            st.button("Next Main Question ➡️", on_click=next_row)
        elif st.session_state.selected_ans == "ans2":
            st.info("🎯 **Objection:** Are those tables just pictures in a PDF or can students export data?")
            st.button("Next Main Question ➡️", on_click=next_row)
        elif st.session_state.selected_ans == "ans3":
            st.info("🎯 **Objection:** Would it be great to combine literature and tools in a single solution?")
            st.button("Next Main Question ➡️", on_click=next_row)

# --- MODULE 3: DATA EXTRACTION ---
elif st.session_state.row_index == 2:
    st.header("Phase 03: Data Extraction")
    st.subheader("How would the library address a request to extract a graph or property?")
    if st.button("Manual Extraction"):
        st.error("🎯 **Objection:** Manual extraction is the #1 mistake causing inaccurate information.")
        st.button("Next Main Question ➡️", on_click=next_row)

# --- MODULE 4: EVALUATION ---
elif st.session_state.row_index == 3:
    st.header("Phase 04: Evaluation Process")
    if st.button("Usage, Demand, Price"):
        st.info("🎯 **Objection:** How many faculty members should request the tool to guarantee purchase?")
        st.button("Next Main Question ➡️", on_click=next_row)

# --- MODULE 5: DECISION MAKER ---
elif st.session_state.row_index == 4:
    st.header("Phase 05: Decision Maker & Power")
    st.subheader("Who is the ultimate decision maker?")

    if st.session_state.sub_step == "main":
        if st.button("Library Director"):
            st.session_state.selected_ans = "ans1"
            st.session_state.sub_step = "follow_up"
            st.rerun()
        if st.button("Library Committee"):
            st.session_state.selected_ans = "ans2"
            st.session_state.sub_step = "follow_up"
            st.rerun()
        if st.button("Rector"):
            st.session_state.selected_ans = "ans3"
            st.session_state.sub_step = "follow_up"
            st.rerun()

    elif st.session_state.sub_step == "follow_up":
        if st.session_state.selected_ans == "ans1":
            st.info("🎯 **Objection:** What specific 'internal proof' do you need to justify the purchase?")
            st.button("Next Main Question ➡️", on_click=next_row)
        elif st.session_state.selected_ans == "ans2":
            st.info("🎯 **Objection:** Who sits on the committee and has the highest influence?")
            st.button("Next Main Question ➡️", on_click=next_row)
        elif st.session_state.selected_ans == "ans3":
            st.info("🎯 **Objection:** How does the Rector decide if this is a tool we should proceed with?")
            st.button("Next Main Question ➡️", on_click=next_row)

# --- MODULE 6: BUDGET ---
elif st.session_state.row_index == 5:
    st.header("Phase 06: Budget & Financial Reality")
    st.subheader("Is there a specific budget set aside for new tools?")

    if st.session_state.sub_step == "main":
        if st.button("Depends on budget later this year"):
            st.session_state.selected_ans = "ans1"
            st.session_state.sub_step = "follow_up"
            st.rerun()
        if st.button("No budget / Need to cancel tool"):
            st.session_state.selected_ans = "ans2"
            st.session_state.sub_step = "follow_up"
            st.rerun()

    elif st.session_state.sub_step == "follow_up":
        st.info("🎯 **Objection:** What criteria make a tool a 'top priority' on your list?")
        st.button("Complete Wizard 🏁", on_click=next_row)
