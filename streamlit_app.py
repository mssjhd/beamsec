import flet as ft
import json
import os
import pyperclip  # Ensure you have pyperclip installed


# File path to store the input values
STATE_FILE = "session_state.json"

# Load session state from file
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    else:
        # Default values if no state file exists
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

# Save session state to file
def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def main(page: ft.Page):
    page.title = "Reinforcement Bar Calculator"
    
    # Set page alignment to center both vertically and horizontally
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Load the previous session state or use default values
    state = load_state()

    # Define input fields with values from session state
    b_input = ft.TextField(label="b (mm)", value=str(state["b"]))
    h_input = ft.TextField(label="h (mm)", value=str(state["h"]))
    cover_input = ft.TextField(label="cover (mm)", value=str(state["cover"]))
    bar_bottom_input = ft.TextField(label="Bar Bottom Diameter (mm)", value=str(state["bar_bottom"]))
    num_bar_bottom_input = ft.TextField(label="Number of Bottom Bars", value=str(state["num_bar_bottom"]))
    bar_top_input = ft.TextField(label="Bar Top Diameter (mm)", value=str(state["bar_top"]))
    num_bar_top_input = ft.TextField(label="Number of Top Bars", value=str(state["num_bar_top"]))
    stirrups_input = ft.TextField(label="Stirrups (mm)", value=str(state["stirrups"]))

    # Button behavior to calculate and save state
    def calculate_click(e):
        # Ensure values are numeric
        try:
            total_bars = int(num_bar_bottom_input.value) + int(num_bar_top_input.value)

            # Copy the result to the clipboard
            pyperclip.copy(str(total_bars))
            pyperclip.copy("LINE 0,0  10,7  ")

            # Update the session state and save it to the file
            state["b"] = int(b_input.value)
            state["h"] = int(h_input.value)
            state["cover"] = int(cover_input.value)
            state["bar_bottom"] = int(bar_bottom_input.value)
            state["num_bar_bottom"] = int(num_bar_bottom_input.value)
            state["bar_top"] = int(bar_top_input.value)
            state["num_bar_top"] = int(num_bar_top_input.value)
            state["stirrups"] = int(stirrups_input.value)

            save_state(state)  # Save updated state to file

            # Show a success message (optional)
            page.add(ft.Text("✅ Total Bars copied to clipboard!", color="green"))

        except ValueError:
            page.add(ft.Text("Please enter valid numbers for all fields.", color="red"))

    # Calculate button
    calculate_button = ft.ElevatedButton("Calculate ..", on_click=calculate_click)

    # Add components to the page, placing them inside centered rows and columns
    page.add(
        ft.Column(
            controls=[
                ft.Row(
        controls=[
        ft.Container(content=b_input, expand=True),
        ft.Container(content=h_input, expand=True),
    ],
    spacing=10
                ),
                cover_input,
                bar_bottom_input,
                num_bar_bottom_input,
                bar_top_input,
                num_bar_top_input,
                stirrups_input,
                calculate_button
            ],
            alignment=ft.MainAxisAlignment.CENTER  # Center vertically
        )
    )

# Run the app
ft.app(target=main)
