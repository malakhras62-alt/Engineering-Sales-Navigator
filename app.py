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



# --- MODULE 4: EVALUATION PROCESS ---

elif st.session_state.row_index == 3:

    st.header("Phase 04: Evaluation Process & Criteria")

    st.subheader("In the evaluation process, what are the things that you take into consideration?")



    # LAYER 1: MAIN ANSWERS

    if st.session_state.sub_step == "main":

        if st.button("Answer 1: Usage, Demand, and Price"):

            st.session_state.selected_ans = "ans1"

            st.session_state.sub_step = "follow_up"

            st.rerun()

        if st.button("Answer 2: Usage and Price"):

            st.session_state.selected_ans = "ans2"

            st.session_state.sub_step = "follow_up"

            st.rerun()



    # LAYER 2: OBJECTIONS

    elif st.session_state.sub_step == "follow_up":

        

        # Branch for Answer 1

        if st.session_state.selected_ans == "ans1":

            st.info("🎯 **Objection/Follow-up 1:** How many faculty members should request the tool to guarantee the purchase if the price was convenient?")

            

            # LAYER 3: SUB-ANSWERS

            col1, col2, col3 = st.columns(3)

            with col1:

                if st.button("Sub-Answer 1: Dean is Enough"):

                    st.success("💡 **Final Follow-up:** What is the formal process for the Engineering Faculty to request a new tool?")

                    st.button("Next Objection ➡️", on_click=None) # Or move to next main question

            with col2:

                if st.button("Sub-Answer 2: Dean and Vice Dean"):

                    st.success("💡 **Final Follow-up:** What is the formal process for the Engineering Faculty to request a new tool?")

            with col3:

                if st.button("Sub-Answer 3: Specific Number of faculty"):

                    st.success("💡 **Final Follow-up:** What is the formal process for the Engineering Faculty to request a new tool?")

            

            st.divider()

            st.info("🎯 **Objection/Follow-up 2:** What should be the content view usage for you to consider the tool?")

            st.button("Next Main Question ➡️", on_click=next_row)



        # Branch for Answer 2

        elif st.session_state.selected_ans == "ans2":

            st.info("🎯 **Objection/Follow-up:** What should be the content view usage for you to consider the tool?")

            st.button("Next Main Question ➡️", on_click=next_row)



# --- MODULE 5: DECISION MAKER & POWER ---

elif st.session_state.row_index == 4:

    st.header("Phase 05: Decision Maker & Power")

    st.subheader("Who is the ultimate decision maker—Library Director, Library Committee, or Rector?")



    # LAYER 1: MAIN ANSWERS

    if st.session_state.sub_step == "main":

        if st.button("Answer 1: Library Director"):

            st.session_state.selected_ans = "ans1"

            st.session_state.sub_step = "follow_up"

            st.rerun()

        if st.button("Answer 2: Library Committee"):

            st.session_state.selected_ans = "ans2"

            st.session_state.sub_step = "follow_up"

            st.rerun()

        if st.button("Answer 3: Rector"):

            st.session_state.selected_ans = "ans3"

            st.session_state.sub_step = "follow_up"

            st.rerun()



    # LAYER 2: OBJECTIONS & SUB-STEPS

    elif st.session_state.sub_step == "follow_up":

        

        # Branch for Answer 1 (Direct Power)

        if st.session_state.selected_ans == "ans1":

            st.info("🎯 **Objection/Follow-up:** Since you hold the ultimate decision, what specific 'internal proof' do you need to justify the Purchase?")

            st.button("Next Main Question ➡️", on_click=next_row)



        # Branch for Answer 2 (Committee Influence)

        elif st.session_state.selected_ans == "ans2":

            st.info("🎯 **Objection/Follow-up:** Who sits on that committee, and which of those stakeholders usually has the highest influence regarding 'specialized' tools?")

            

            col1, col2, col3 = st.columns(3)

            with col1:

                if st.button("Sub-Answer 1: I will be voting"):

                    st.success("💡 **Final Follow-up:** How do they decide if this is a tool we should proceed with or not?")

                    st.button("Next Main Question ➡️", on_click=next_row)

            with col2:

                if st.button("Sub-Answer 2: Vice Dean / Dean"):

                    st.success("💡 **Strategy:** Focus on Faculty 'Scream' and Accreditation value.")

                    st.button("Next Main Question ➡️", on_click=next_row)

            with col3:

                if st.button("Sub-Answer 3: Rector / Vice Rector"):

                    st.success("💡 **Final Follow-up:** How does he decide if this is a tool we should proceed with or not?")

                    st.button("Next Main Question ➡️", on_click=next_row)



        # Branch for Answer 3 (Top-Down Power)

        elif st.session_state.selected_ans == "ans3":

            st.info("🎯 **Objection/Follow-up:** How does the Rector decide if this is a tool we should proceed with or not?")

            st.button("Next Main Question ➡️", on_click=next_row)



# --- MODULE 6: BUDGET & PRIORITIZATION ---

elif st.session_state.row_index == 5:

    st.header("Phase 06: Budget & Financial Reality")

    st.subheader("Since tools and databases prices rise 5% annually and the budget is getting tighter, is there a specific budget set aside for new tools?")



    # LAYER 1: MAIN ANSWERS

    if st.session_state.sub_step == "main":

        col1, col2 = st.columns(2)

        with col1:

            if st.button("Answer 1: Depends on the budget received later this year"):

                st.session_state.selected_ans = "ans1"

                st.session_state.sub_step = "follow_up"

                st.rerun()

        with col2:

            if st.button("Answer 2: No budget / Need to cancel a tool to subscribe"):

                st.session_state.selected_ans = "ans2"

                st.session_state.sub_step = "follow_up"

                st.rerun()



    # LAYER 2: OBJECTIONS & QUARTERLY TIMELINES

    elif st.session_state.sub_step == "follow_up":

        

        # Logic for Answer 1

        if st.session_state.selected_ans == "ans1":

            st.info("🎯 **Objection/Follow-up 1:** When is the next budget confirmed?")

            q_cols = st.columns(4)

            with q_cols[0]: st.button("Q1", on_click=None)

            with q_cols[1]: st.button("Q2", on_click=None)

            with q_cols[2]: st.button("Q3", on_click=None)

            with q_cols[3]: st.button("Q4", on_click=None)

            

            st.divider()

            st.info("🎯 **Objection/Follow-up 2:** Do you have prioritized new solutions on your list that you would like to first subscribe to if you get additional budget?")

            

            c1, c2 = st.columns(2)

            with c1:

                if st.button("Yes"):

                    st.success("💡 **Follow-up:** If you are evaluating a new tool within this period, what makes it a top priority for you?")

            with c2:

                if st.button("No"):

                    st.warning("💡 **Pivot:** How can we ensure the Engineering Dean's requirements put this at the top of the priority list?")

            

            st.button("Next Main Question ➡️", on_click=next_row)



        # Logic for Answer 2 (The "Replacement" Strategy)

        elif st.session_state.selected_ans == "ans2":

            st.info("🎯 **Objection/Follow-up 1:** Do you have prioritized new solutions on your list that you would like to first subscribe to if you get additional budget?")

            

            c1, c2 = st.columns(2)

            with c1:

                if st.button("Yes (Prioritized)"):

                    st.success("💡 **Follow-up:** What are the criteria that put a tool on that top priority list?")

            with c2:

                if st.button("No (Not yet)"):

                    st.error("💡 **Objection/Follow-up 2:** If you are evaluating a new database or tool, what things make you consider it a top priority?")

            

            st.button("Next Main Question ➡️", on_click=next_row)



# --- MODULE 7: TIMELINE & PROCUREMENT ---

elif st.session_state.row_index == 6:

    st.header("Phase 08: Timeline & Procurement")

    st.subheader("After the trial, if usage is good, demand is high, and the price is reasonable, when would you like the start date to be?")



    # LAYER 1: MAIN ANSWERS (START DATES)

    if st.session_state.sub_step == "main":

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button("Answer 1: 01 Jan"):

                st.session_state.selected_ans = "jan"

                st.session_state.sub_step = "follow_up"

                st.rerun()

        with col2:

            if st.button("Answer 2: Next Quarter"):

                st.session_state.selected_ans = "next_q"

                st.session_state.sub_step = "follow_up"

                st.rerun()

        with col3:

            if st.button("Answer 3: Sept"):

                st.session_state.selected_ans = "sept"

                st.session_state.sub_step = "follow_up"

                st.rerun()



    # LAYER 2: SIGNING PROCESS & APPROVALS

    elif st.session_state.sub_step == "follow_up":

        st.info("🎯 **Objection/Follow-up:** How long does the signing process take? Any additional approvals we need to secure from other departments like Procurement or Finance?")

        

        c1, c2 = st.columns(2)

        with c1:

            if st.button("1-A: Yes (Procurement/Finance involved)"):

                st.session_state.sub_step = "final_check"

                st.rerun()

        with c2:

            if st.button("1-B: No (Direct Library Approval)"):

                st.success("💡 **Strategy:** Focus on the direct paperwork flow to meet your requested start date.")

                st.button("Next Main Question ➡️", on_click=next_row)



    # LAYER 3: THE BACKLOG DRILL-DOWN

    elif st.session_state.sub_step == "final_check":

        st.warning("🎯 **Final Follow-up:** Do they typically have a backlog we should account for now?")

        

        b1, b2 = st.columns(2)

        with b1:

            if st.button("Yes (There is a backlog)"):

                st.error("💡 **Action Item:** We should start the paperwork 4-6 weeks earlier to ensure we hit your start date.")

                st.button("Next Main Question ➡️", on_click=next_row)

        with b2:

            if st.button("No (Clear process)"):

                st.success("💡 **Action Item:** We will align our proposal timeline with their standard processing time.")
