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

# --- MODULE 1: CONTENT ACCESS ---
if st.session_state.row_index == 0:
    st.header("Phase 01: Content Access")
    st.subheader("How are your students currently accessing content?")
    
    # LAYER 1: MAIN ANSWERS
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

    # LAYER 2: OBJECTIONS & SUB-ANSWERS
    elif st.session_state.sub_step == "follow_up":
        
        # Branch for Answer 1
        if st.session_state.selected_ans == "ans1":
            st.info("🎯 **Objection:** Discovery layers often rely on exact keyword matching. How do you ensure a student looking for 'corrosion' doesn't miss content using the term 'oxidation'?")
            if st.button("1-A: Our search engine uses basic Boolean logic and tagging."):
                st.success("💡 **Follow-up:** If a student isn't a 'Search Expert,' they miss out on content you paid for. How do you justify the ROI of content that stays hidden?")
                st.button("Next Main Question ➡️", on_click=next_row)
            if st.button("1-B: We teach students how to search better in workshops."):
                st.success("💡 **Follow-up:** But even if you teach them how to do a search, Engineering students still needs information about topics not directly related to their department and might not be knowledgable about the synonyms that they need to include.")
                st.button("Next Main Question ➡️", on_click=next_row)
            if st.button("1-C: We trust the metadata provided by the publishers."):
                st.success("💡 **Follow-up:** If the search isn't 'Concept-Based,' aren't you essentially paying for a library where the books are invisible to the users?")
                st.button("Next Main Question ➡️", on_click=next_row)

        # Branch for Answer 2
        elif st.session_state.selected_ans == "ans2":
            st.info("🎯 **Objection:** Static lists are great for theory, but if they want to search beyond that list or pull values out with Graphs and Equations what would they do?")
            st.button("Next Main Question ➡️", on_click=next_row)

        # Branch for Answer 3
        elif st.session_state.selected_ans == "ans3":
            st.info("🎯 **Objection:** So the user needs to access multiple databases and search individually between them to find the information.")
            if st.button("3-A: Accessing multiple databases individually"):
                st.error("💡 **Follow-up:** Would not that result to missing information and data not to mention that amount of time they need to spend to find what they are looking for?")
                st.button("Next Main Question ➡️", on_click=next_row)

# --- MODULE 2: ACTIVE TOOLS ---
elif st.session_state.row_index == 1:
    st.header("Phase 02: Active Tools & Workflow")
    st.subheader("Engineering requires 'doing.' How is the library providing 'Active Tools' (calculators/converters) rather than just 'Passive Reading' (PDFs)?")

    # LAYER 1: MAIN ANSWERS
    if st.session_state.sub_step == "main":
        if st.button("Answer 1: We provide access to software like MATLAB separately."):
            st.session_state.selected_ans = "ans1"
            st.session_state.sub_step = "follow_up"
            st.rerun()
        if st.button("Answer 2: Our specialized databases have some technical tables."):
            st.session_state.selected_ans = "ans2"
            st.session_state.sub_step = "follow_up"
            st.rerun()
        if st.button("Answer 3: Faculty handles practical tools; we provide the literature."):
            st.session_state.selected_ans = "ans3"
            st.session_state.sub_step = "follow_up"
            st.rerun()

    # LAYER 2: OBJECTIONS
    elif st.session_state.sub_step == "follow_up":
        
        # Branch for Answer 1
        if st.session_state.selected_ans == "ans1":
            st.info("🎯 **Objection:** MATLAB is the engine, but where do students find the validated material properties to plug into those models without spending hours searching journals?")
            st.button("Next Main Question ➡️", on_click=next_row)

        # Branch for Answer 2
        elif st.session_state.selected_ans == "ans2":
            st.info("🎯 **Objection:** Are those tables just pictures in a PDF, or can students export the data points directly into Excel or CAD?")
            st.button("Next Main Question ➡️", on_click=next_row)

        # Branch for Answer 3
        elif st.session_state.selected_ans == "ans3":
            st.info("🎯 **Objection:** Would it not be great to combine the literature provided by the library with the tools in a single solution?")
            st.button("Next Main Question ➡️", on_click=next_row)

# --- MODULE 3: DATA EXTRACTION & ACCURACY ---
elif st.session_state.row_index == 2:
    st.header("Phase 03: Data Extraction & Accuracy")
    st.subheader("If a researcher or a student asks the library to extract a graph to interact with it or get a material property under specific conditions, how would the library address that?")

    # LAYER 1: MAIN ANSWERS
    if st.session_state.sub_step == "main":
        if st.button("Answer 1: We don't have a specific tool; students handle extraction manually."):
            st.session_state.selected_ans = "ans1"
            st.session_state.sub_step = "follow_up"
            st.rerun()
        if st.button("Answer 2: We refer them to specialized digitization software."):
            st.session_state.selected_ans = "ans2"
            st.session_state.sub_step = "follow_up"
            st.rerun()

    # LAYER 2: OBJECTIONS
    elif st.session_state.sub_step == "follow_up":
        
        # Branch for Answer 1 (Focus on Human Error)
        if st.session_state.selected_ans == "ans1":
            st.error("🎯 **Objection:** Extracting data manually out of graphs is the #1 mistake in getting inaccurate information—not to mention the typo errors or miscalculation mistakes they can have.")
            st.info("💡 **Insight:** How is the library mitigating the risk of students using faulty data in their Capstone or Research projects?")
            st.button("Next Main Question ➡️", on_click=next_row)

        # Branch for Answer 2 (Focus on Friction)
        elif st.session_state.selected_ans == "ans2":
            st.info("🎯 **Objection:** Moving between multiple tools creates 'Data Friction.' Would it not be more secure to have a single source where the data is interactive right on the page?")
            st.button("Next Main Question ➡️", on_click=next_row)
