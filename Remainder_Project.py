import time
import threading
import streamlit as st
from datetime import datetime

# Global variable to store reminders
reminders = []


def check_reminder():
    """
    Continuously checks the current time and triggers reminders when the time matches.
    """
    while True:
        current_time = datetime.now()
        for reminder in reminders:
            message, reminder_time = reminder
            if reminder_time.hour == current_time.hour and reminder_time.minute == current_time.minute:
                st.warning(f"Reminder: {message}")
                reminders.remove(reminder)  # Remove the triggered reminder
        time.sleep(30)  # Check every 30 seconds


# Start a thread to check reminders in the background
threading.Thread(target=check_reminder, daemon=True).start()

# Streamlit UI
st.title("Friendly Reminder App")
st.markdown("Set reminders to help you stay on top of your tasks!")

# Input for reminder message
reminder_message = st.text_input("What would you like to be reminded about?")

# Input for reminder time in HH:MM format
reminder_time = st.text_input("When would you like to be reminded? (HH:MM in 24-hour format)")

# Button to set the reminder
if st.button("Set Reminder"):
    if not reminder_message or not reminder_time:
        st.error("Please provide both a message and a valid time in HH:MM format.")
    else:
        try:
            # Parse reminder time
            reminder_hour, reminder_minute = map(int, reminder_time.split(":"))
            if not (0 <= reminder_hour < 24) or not (0 <= reminder_minute < 60):
                raise ValueError("Invalid time format.")

            # Add the reminder to the list
            reminder_datetime = datetime.now().replace(hour=reminder_hour, minute=reminder_minute, second=0, microsecond=0)
            reminders.append((reminder_message, reminder_datetime))
            st.success(f"Reminder set for {reminder_time}. You will be notified!")

        except ValueError:
            st.error("Invalid time format. Please enter the time in HH:MM format.")

# Display the list of reminders
if reminders:
    st.markdown("### Your Reminders")
    for i, (message, reminder_time) in enumerate(reminders):
        st.markdown(f"{i + 1}. **{message}** at **{reminder_time.strftime('%H:%M')}**")

# Button to clear all reminders
if st.button("Clear All Reminders"):
    reminders.clear()
    st.success("All reminders cleared.")
