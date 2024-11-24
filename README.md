# Friendly Reminder App Documentation

## Overview

The **Friendly Reminder App** is a simple and efficient tool built with **Streamlit** that allows users to set reminders for specific tasks. This app continuously checks the current time and triggers notifications when the scheduled reminder time matches. It provides an easy-to-use interface for setting and managing reminders, helping users stay on track with their tasks.

## Features

- **Set Custom Reminders**: Users can input a message and specify a time for the reminder.
- **Real-Time Notifications**: The app will notify the user with a reminder when the specified time matches the current time.
- **Manage Reminders**: View all reminders set and clear them when needed.
  
## How to Use

1. **Enter a Reminder Message**: Type the task or message you would like to be reminded about.
2. **Set the Reminder Time**: Enter the time in **HH:MM** format (24-hour format) when you would like the reminder to be triggered.
3. **Click "Set Reminder"**: Once you’ve filled out both fields, click the button to set the reminder.
4. **Notifications**: The app will check the current time continuously and notify you when the reminder time is reached.
5. **View and Manage Reminders**: You can see the list of reminders and their scheduled times. You can also clear all reminders if needed.

## Try the Tool Online

You can use the **Friendly Reminder App** directly by visiting the following link:

[Try the Reminder App](https://remainderproject-ep8emybqsudqsnnviedsr3.streamlit.app/)

## Code Overview

This application uses Python's **Streamlit** library for the user interface and the **threading** module to run the reminder check in the background. The **datetime** module is used to handle and compare time values. 

### Main Components:

1. **Reminder Input**: Users input a message and time for the reminder.
2. **Reminder Check**: The app checks the current time in a background thread and triggers reminders when the time matches.
3. **Clear All Reminders**: Users can clear all reminders with a click of a button.

### Background Thread:
A separate thread runs continuously in the background, checking the system's current time every 30 seconds. If the reminder time matches the current time, it triggers a notification and removes the reminder from the list.

## Example Use Case

1. **Set Reminder**: You enter "Meeting with John" as the message and "14:30" as the time.
2. **Notification**: When the clock strikes 14:30, a reminder will pop up saying "Meeting with John."

## How to Run Locally

If you would like to run the Friendly Reminder App on your local machine, follow these steps:

### Prerequisites

- Python 3.8 or later
- Required Python packages: `Streamlit`, `time`, `threading`, `datetime`
