import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Engineering Sales Wizard", layout="wide")

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

def reset():
    st.session_state.row_index = 0
    st.session_state.sub_step = "main"
    st.session_state.selected_ans = None

# --- Complete Data Mapping from Renewals Spreadsheet ---
data = [
    {
        "main_q": "How are your students currently accessing content?",
        "answers": {
            "Answer 1": {"text": "Through the platforms directly", "follow_up": "Which Platform or tools are they using?", "sub_answers": {"A": ("MATLAB / Solidworks / AutoCad", "How do they get verified equations into those tools without risking human error from static PDFs?"), "B": ("We don't Know they are specialized platforms", "If the library doesn't know the workflow, how can you ensure the budget supports actual results?")}},
            "Answer 2": {"text": "mainly through our library homepage search bar.", "follow_up": "Static lists are great for theory, but how do you ensure the interactive data is available where they work?", "sub_answers": {"A": ("We don't Have anything", "Without interactive tools, how do you prevent the 30% time-waste on manual data entry?"), "B": ("We provide access to software like MATLAB separately", "MATLAB is the engine, but where do they get the validated fuel (material properties) to plug into it?")}}
        }
    },
    {
        "main_q": "Discovery layers often rely on exact keyword matching. How do you ensure a student looking for 'corrosion' doesn't miss 'oxidation'?",
        "answers": {
            "Answer 1": {"text": "Our discovery tool handles synonyms", "follow_up": "Does it include engineering-specific taxonomies to catch variations like 'creep' vs 'deformation'?", "sub_answers": {}},
            "Answer 2": {"text": "Students are responsible for their own search strings", "follow_up": "If they miss content, the library is subscribing to 'Invisible Content.' How do you justify the ROI?", "sub_answers": {}}
        }
    },
    {
        "main_q": "How do you ensure students are using an accurate AI that provides validated data rather than general AI that might hallucinate?",
        "answers": {
            "Answer 1": {"text": "We encourage ChatGPT for efficiency", "follow_up": "General AI has a 15-20% hallucination rate in engineering. How do you protect the university's research integrity?", "sub_answers": {}},
            "Answer 2": {"text": "We have no official AI policy", "follow_up": "Without a policy, students go to the easiest tool. How do you provide a 'Safe Haven' of validated engineering data?", "sub_answers": {}}
        }
    },
    {
        "main_q": "Engineering requires 'doing.' How is the library providing 'Active Tools' rather than just 'Passive Reading'?",
        "answers": {
            "Answer 1": {"text": "We provide e-books and journals", "follow_up": "Those are great for theory, but how do students extract data into their design tools without manual errors?", "sub_answers": {}},
            "Answer 2": {"text": "We have specialized databases", "follow_up": "Do these databases allow students to solve equations or digitize graphs directly on the page?", "sub_answers": {}}
        }
    },
    {
        "main_q": "How are you addressing a student's need to extract a graph or a property into their design tool?",
        "answers": {
            "Answer 1": {"text": "They manually transcribe or screenshot", "follow_up": "Manual transcription is the #1 source of human error in design. How are you mitigating this risk?", "sub_answers": {}},
            "Answer 2": {"text": "We use OCR tools", "follow_up": "OCR often fails with complex engineering symbols and units. Have you seen the impact on project accuracy?", "sub_answers": {}}
        }
    },
    {
        "main_q": "In the evaluation process, what are the things that you take into consideration?",
        "answers": {
            "Answer 1": {"text": "Usage and Price", "follow_up": "If usage is high but purely from 'passive reading,' does that prove the students are actually becoming better engineers?", "sub_answers": {}},
            "Answer 2": {"text": "Faculty Feedback", "follow_up": "How do you ensure you get feedback from the Dean, not just a few vocal students?", "sub_answers": {}}
        }
    },
    {
        "main_q": "Who is the ultimate decision maker—Library director, Library Committee, or Rector?",
        "answers": {
            "Answer 1": {"text": "Library Director", "follow_up": "Since you hold the ultimate decision, what specific 'internal proof' do you need to justify the Purchase?", "sub_answers": {"A": ("Demand / Usage / Budget", "Let's align on a success plan to prove this specific value to the Rector.")}}
        }
    },
    {
        "main_q": "Is there a specific budget set aside for new tools despite the 5% annual rise?",
        "answers": {
            "Answer 1": {"text": "No, the budget is frozen", "follow_up": "In that case, are we looking to reallocate funds from lower-performing tools to support the Engineering College?", "sub_answers": {}},
            "Answer 2": {"text": "Yes, for strategic innovations", "follow_up": "How do we ensure this solution is categorized as a 'Strategic Innovation' for the next board meeting?", "sub_answers": {}}
        }
    }
]

# --- UI RENDERER ---
st.sidebar.title("Meeting Controls")
st.sidebar.button("🔄 Reset Meeting", on_click=reset)
inst_name = st.sidebar.text_input("University Name", "University of Dubai")

if st.session_state.row_index < len(data):
    current_row = data[st.session_state.row_index]
    st.header(f"Question {st.session_state.row_index + 1} of {len(data)}")
    st.progress((st.session_state.row_index + 1) / len(data))
    st.subheader(current_row["main_q"])

    if st.session_state.sub_step == "main":
        for key, val in current_row["answers"].items():
            if st.button(val["text"]):
                st.session_state.selected_ans = key
                st.session_state.sub_step = "follow_up"
                st.rerun()

    elif st.session_state.sub_step == "follow_up":
        ans_data = current_row["answers"][st.session_state.selected_ans]
        st.info(f"🎯 **Follow-up Question:** {ans_data['follow_up']}")
        
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
    st.success("🏁 Meeting Flow Complete! All strategic points addressed.")
    st.button("Start New Meeting", on_click=reset)

st.sidebar.divider()
st.sidebar.write(f"**Target:** {inst_name}")
