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

# ... (Phases 01 through 05 remain the same) ...

# --- MODULE 6: BUDGET & PRIORITIZATION ---
elif st.session_state.row_index == 5:
    st.header("Phase 06: Budget & Financial Reality")
    st.subheader("Since tools and databases prices rise 5% annually, is there a budget set aside for new tools?")

    if st.session_state.sub_step == "main":
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Answer 1: Depends on budget later this year"):
                st.session_state.selected_ans = "ans1"
                st.session_state.sub_step = "follow_up"
                st.rerun()
        with col2:
            if st.button("Answer 2: No budget / Need to cancel a tool"):
                st.session_state.selected_ans = "ans2"
                st.session_state.sub_step = "follow_up"
                st.rerun()

    elif st.session_state.sub_step == "follow_up":
        st.info("🎯 **Objection:** What makes a new tool a top priority for you?")
        st.button("Next Main Question ➡️", on_click=next_row)

# --- MODULE 7: STRATEGIC AI INTEGRITY (FIXED INDEX) ---
elif st.session_state.row_index == 6:
    st.header("Phase 07: Strategic AI Integrity")
    st.subheader("With the rise of GenAI, how do you ensure students are using 'Domain-Specific' AI rather than general AI?")

    if st.session_state.sub_step == "main":
        if st.button("Answer 1: We encourage ChatGPT for efficiency"):
            st.session_state.selected_ans = "ans1"
            st.session_state.sub_step = "follow_up"
            st.rerun()
        if st.button("Answer 2: No official AI policy"):
            st.session_state.selected_ans = "ans2"
            st.session_state.sub_step = "follow_up"
            st.rerun()

    elif st.session_state.sub_step == "follow_up":
        if st.session_state.selected_ans == "ans1":
            st.error("🎯 **Objection:** General AI has a 15-20% hallucination rate. How do you protect research integrity?")
        else:
            st.warning("🎯 **Objection:** Without a 'Safe Haven' of validated data, students use unverified tools.")
        st.button("Next Main Question ➡️", on_click=next_row)

# --- MODULE 8: TIMELINE & PROCUREMENT (FIXED INDEX) ---
elif st.session_state.row_index == 7:
    st.header("Phase 08: Timeline & Procurement")
    st.subheader("After the trial, when would you like the start date to be?")

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

    elif st.session_state.sub_step == "follow_up":
        st.info("🎯 **Objection:** How long does signing take? Any Procurement/Finance approvals needed?")
        if st.button("Yes (Procurement involved)"):
            st.session_state.sub_step = "final_check"
            st.rerun()
        if st.button("No (Direct Approval)"):
            st.button("Finish ➡️", on_click=next_row)

    elif st.session_state.sub_step == "final_check":
        st.warning("🎯 **Final Follow-up:** Do they typically have a backlog?")
        st.button("Complete Meeting 🏁", on_click=next_row)
