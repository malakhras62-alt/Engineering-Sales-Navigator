# --- MODULE 5: DECISION MAKER & POWER ---
elif st.session_state.row_index == 4:
    st.header("Phase 05: Decision Maker & Power")
    st.subheader("Who is the ultimate decision maker—Library Director, Library Committee, or Rector?")

    if st.session_state.sub_step == "main":
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Answer 1: Library Director"):
                st.session_state.selected_ans = "ans1"
                st.session_state.sub_step = "follow_up"
                st.rerun()
        with col2:
            if st.button("Answer 2: Library Committee"):
                st.session_state.selected_ans = "ans2"
                st.session_state.sub_step = "follow_up"
                st.rerun()
        with col3:
            if st.button("Answer 3: Rector"):
                st.session_state.selected_ans = "ans3"
                st.session_state.sub_step = "follow_up"
                st.rerun()

    elif st.session_state.sub_step == "follow_up":
        if st.session_state.selected_ans == "ans1":
            st.info("🎯 **Objection:** Since you hold the ultimate decision, what specific 'internal proof' do you need to justify the Purchase?")
            st.button("Next Main Question ➡️", on_click=next_row)
            
        elif st.session_state.selected_ans == "ans2":
            st.info("🎯 **Objection:** Who sits on that committee, and which stakeholders have the highest influence?")
            if st.button("Sub-Answer: Dean / Vice Dean"):
                st.success("💡 **Strategy:** Focus on Faculty 'Scream' and Accreditation value.")
                st.button("Next Main Question ➡️", on_click=next_row)
            
        elif st.session_state.selected_ans == "ans3":
            st.info("🎯 **Objection:** How does the Rector decide if this is a tool we should proceed with or not?")
            st.button("Next Main Question ➡️", on_click=next_row)

# --- MODULE 6: BUDGET & PRIORITIZATION ---
elif st.session_state.row_index == 5:
    st.header("Phase 06: Budget & Financial Reality")
    st.subheader("Since tools and databases prices rise 5% annually, is there a specific budget set aside for new tools?")

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
        # Add a placeholder button so this block isn't empty
        st.info("🎯 **Objection:** What makes a new tool a top priority for you?")
        st.button("Next Main Question ➡️", on_click=next_row)
