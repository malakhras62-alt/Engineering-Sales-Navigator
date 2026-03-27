import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Engineering Sales Wizard", layout="wide")

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

# --- Exact Data Mapping from your Spreadsheets ---
data = [
    {
        "main_q": "How are your students currently accessing content?",
        "answers": {
            "Answer 1": {
                "text": "Through the platforms directly",
                "follow_up": "Which Platform or tools are they using?",
                "sub_answers": {
                    "A": ("MATLAB / Solidworks / AutoCad", "How do they get verified equations into those tools without risking human error from static PDFs?"),
                    "B": ("We don't Know they are specialized platforms", "If the library doesn't know the workflow, how can you ensure the budget supports actual results?")
                }
            },
            "Answer 2": {
                "text": "mainly through our library homepage search bar.",
                "follow_up": "Static lists are great for theory, but how do you ensure the interactive data (equations/tables) is available where they work?",
                "sub_answers": {
                    "A": ("We don't Have anything", "Without interactive tools, how do you prevent the 30% time-waste on manual data entry?"),
                    "B": ("We provide access to software like MATLAB separately", "MATLAB is the engine, but where do they get the validated fuel (material properties) to plug into it?")
                }
            }
        }
    },
    {
        "main_q": "How does the library currently link its subscription spend to 'Student Outcomes,' like Capstone project success or higher GPA for frequent users?",
        "answers": {
            "Answer 1": {
                "text": "We track usage and downloads",
                "follow_up": "Usage tells us they 'looked' at a PDF, but how do we prove it helped them 'build' a better project?",
                "sub_answers": {}
            },
            "Answer 2": {
                "text": "We don't have a formal way to track outcomes",
                "follow_up": "If we can't link spend to success, how do we protect the budget from 5% annual cuts?",
                "sub_answers": {}
            }
        }
    },
    {
        "main_q": "With the rise of GenAI, how do you ensure students are using 'Domain-Specific' AI that provides validated data rather than general AI that might hallucinate engineering values?",
        "answers": {
            "Answer 1": {
                "text": "Students use ChatGPT or general search",
                "follow_up": "General AI has a 15-20% hallucination rate in engineering. How do you protect the university's research integrity?",
                "sub_answers": {}
            },
            "Answer 2": {
                "text": "We expect faculty to guide them",
                "follow_up": "Faculty are busy; without a 'Safe Haven' of validated data, how do we prevent manual errors in student designs?",
                "sub_answers": {}
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
                    "A": ("Demand / Usage / Budget", "Let's align on a success plan to prove this specific value to the Rector.")
                }
            }
        }
    }
]

# --- UI RENDERER ---
st.sidebar.title("Meeting Controls")
st.sidebar.button("🔄 Reset Meeting", on_click=reset)
inst_name = st.sidebar.text_input("University Name", "University of Dubai")

if st.session_state.row_index < len(data):
    current_row = data[st.session_state.row_index]
    st.header(f"Phase {st.session_state.row_index + 1}")
    st.subheader(current_row["main_q"])

    if st.session_state.sub_step == "main":
        for key, val in current_row["answers"].items():
            if st.button(val["text"]):
                st.session_state.selected_ans = key
                st.session_state.sub_step = "follow_up"
                st.rerun()

    elif st.session_state.sub_step == "follow_up":
        ans_data = current_row["answers"][st.session_state.selected_ans]
        st.info(f"🎯 **Follow-up:** {ans_data['follow_up']}")
        
        if ans_data["sub_answers"]:
            for sub_key, sub_val in ans_data["sub_answers"].items():
                if st.button(sub_val[0]):
                    st.session_state.final_follow_up = sub_val[1]
                    st.session_state.sub_step = "final"
                    st.rerun()
        else:
            st.button("Next Main Question ➡️", on_click=next_row)

    elif st.session_state.sub_step == "final":
        st.success(f"💡 **Closing Insight:** {st.session_state.final_follow_up}")
        st.button("Next Main Question ➡️", on_click=next_row)
else:
    st.balloons()
    st.success("Meeting Complete!")

st.sidebar.divider()
st.sidebar.write(f"**Target:** {inst_name}")
