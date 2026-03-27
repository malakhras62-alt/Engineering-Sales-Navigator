import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Sales Wizard", layout="wide")

# --- Session State Initialization ---
if 'row_index' not in st.session_state:
    st.session_state.row_index = 0
if 'sub_step' not in st.session_state:
    st.session_state.sub_step = "main"

def next_row():
    st.session_state.row_index += 1
    st.session_state.sub_step = "main"

def reset():
    st.session_state.row_index = 0
    st.session_state.sub_step = "main"

# --- Data Mapping from your Spreadsheet ---
# Each dictionary represents a row in your Renewals file
data = [
    {
        "main_q": "How are your students currently accessing content?",
        "answers": {
            "Answer 1": {
                "text": "Through the platforms directly",
                "follow_up": "Which Platform or tools are they using?",
                "sub_answers": {
                    "Answer 1-A": ("MATLAB / Solidworks / AutoCad", "How do they get verified equations into those tools without risking human error from static PDFs?"),
                    "Answer 1-B": ("We don't Know they are specialized platforms", "If the library doesn't know the workflow, how can you ensure the budget supports actual results?")
                }
            },
            "Answer 2": {
                "text": "mainly through our library homepage search bar.",
                "follow_up": "Static lists are great for theory, but how do you ensure the interactive data (equations/tables) is available where they work?",
                "sub_answers": {
                    "Answer 2-A": ("We don't Have anything", "Without interactive tools, how do you prevent the 30% time-waste on manual data entry?"),
                    "Answer 2-B": ("We provide access to software like MATLAB separately", "MATLAB is the engine, but where do they get the validated fuel (material properties) to plug into it?")
                }
            }
        }
    },
    {
        "main_q": "Discovery layers often rely on exact keyword matching. How do you ensure a student looking for 'corrosion' doesn't miss 'oxidation'?",
        "answers": {
            "Answer 1": {
                "text": "Our discovery tool handles synonyms",
                "follow_up": "Does it include engineering-specific taxonomies to catch variations like 'creep' vs 'deformation'?",
                "sub_answers": {} # Empty - will trigger next module
            },
            "Answer 2": {
                "text": "Students are responsible for their own search strings",
                "follow_up": "If they miss content, the library is subscribing to 'Invisible Content.' How do you justify the ROI?",
                "sub_answers": {} # Empty
            }
        }
    },
    {
        "main_q": "Who is the ultimate decision maker Library director or Library Committee or rector?",
        "answers": {
            "Answer 1": {
                "text": "Library Director",
                "follow_up": "Since you hold the ultimate decision, what specific 'internal proof' do you need to justify the Purchase?",
                "sub_answers": {
                    "Answer 1-A": ("Demand / Usage / Budget", "Let's align on a success plan to prove this specific value.")
                }
            }
        }
    }
]

# --- UI RENDERER ---
st.sidebar.title("Controls")
st.sidebar.button("🔄 Reset Meeting", on_click=reset)
inst_name = st.sidebar.text_input("University Name", "University of Dubai")

if st.session_state.row_index < len(data):
    current_row = data[st.session_state.row_index]
    st.header(f"Question {st.session_state.row_index + 1}")
    st.subheader(current_row["main_q"])

    # Show Main Answers
    if st.session_state.sub_step == "main":
        for key, val in current_row["answers"].items():
            if st.button(val["text"]):
                st.session_state.selected_ans = key
                st.session_state.sub_step = "follow_up"
                st.rerun()

    # Show Follow-up and Sub-Answers
    elif st.session_state.sub_step == "follow_up":
        ans_data = current_row["answers"][st.session_state.selected_ans]
        st.info(f"🎯 **Follow-up:** {ans_data['follow_up']}")
        
        # Check if sub-answers exist
        if ans_data["sub_answers"]:
            for sub_key, sub_val in ans_data["sub_answers"].items():
                if st.button(sub_val[0]):
                    st.session_state.final_follow_up = sub_val[1]
                    st.session_state.sub_step = "final"
                    st.rerun()
        else:
            # If empty, move to next main question
            st.button("Move to Next Main Question ➡️", on_click=next_row)

    # Show Final Follow-up
    elif st.session_state.sub_step == "final":
        st.success(f"💡 **Closing Insight:** {st.session_state.final_follow_up}")
        st.button("Move to Next Main Question ➡️", on_click=next_row)

else:
    st.balloons()
    st.success("Meeting Flow Complete!")
    st.button("Start New Meeting", on_click=reset)

st.sidebar.divider()
st.sidebar.write(f"**Current Lead:** {inst_name}")
