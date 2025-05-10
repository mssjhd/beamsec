import streamlit as st
import json
import os

STATE_FILE = "session_state.json"

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    else:
        return {
            "b": 600,
            "h": 300,
            "cover": 30,
            "bar_bottom": 16,
            "num_bar_bottom": 6,
            "bar_top": 12,
            "num_bar_top": 6,
            "stirrups": 8,
        }

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

state = load_state()

st.title("Reinforcement Bar Calculator")

col1, col2 = st.columns(2)
with col1:
    state["b"] = st.number_input("b (mm)", value=state["b"])
with col2:
    state["h"] = st.number_input("h (mm)", value=state["h"])

state["cover"] = st.number_input("cover (mm)", value=state["cover"])
state["bar_bottom"] = st.number_input("Bar Bottom Diameter (mm)", value=state["bar_bottom"])
state["num_bar_bottom"] = st.number_input("Number of Bottom Bars", value=state["num_bar_bottom"], step=1)
state["bar_top"] = st.number_input("Bar Top Diameter (mm)", value=state["bar_top"])
state["num_bar_top"] = st.number_input("Number of Top Bars", value=state["num_bar_top"], step=1)
state["stirrups"] = st.number_input("Stirrups (mm)", value=state["stirrups"])

if st.button("Calculate .."):
    total_bars = state["num_bar_bottom"] + state["num_bar_top"]
    command_text = "LINE 0,0  10,7  "
    save_state(state)

    st.success("✅ Click below to copy this line:")
    st.code(command_text,language=None)


