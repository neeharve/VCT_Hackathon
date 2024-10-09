import streamlit as st
import time
from datetime import datetime
from bedrock_client import generate_text, get_mock_response

# Page configuration
st.set_page_config(page_title="Valorant AI Chat", page_icon="🎮", layout="wide")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'test_mode' not in st.session_state:
    st.session_state.test_mode = False

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to submit message
def submit_message():
    user_input = st.session_state.user_input
    if user_input.strip() == "":
        st.warning("Please enter a message.")
        return

    # Append user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "avatar": "assets/user_avatar.png",
        "timestamp": get_current_timestamp()
    })

    # Generate AI response
    if st.session_state.test_mode:
        ai_response = get_mock_response(user_input)
    else:
        ai_response = generate_text(user_input)

    # Append AI response
    st.session_state.messages.append({
        "role": "ai",
        "content": ai_response,
        "avatar": "assets/valorant_ai.jpeg",
        "timestamp": get_current_timestamp()
    })

    # Clear user input
    st.session_state.user_input = ""

# Main app layout
st.title("Valorant AI Chat")

# Test mode toggle
st.session_state.test_mode = st.sidebar.checkbox("Enable Test Mode", value=st.session_state.test_mode)

# Chat display
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=message["avatar"]):
        st.write(f"**{message['role'].capitalize()}:** {message['content']}")
        st.caption(message["timestamp"])

# User input
st.text_input("Type your message here...", key="user_input", on_change=submit_message)

# Display current mode
if st.session_state.test_mode:
    st.sidebar.success("Test Mode: Enabled")
else:
    st.sidebar.info("Test Mode: Disabled")

# Custom CSS to remove the grey box
st.markdown("""
<style>
    .stApp {
        background-color: transparent;
    }
</style>
""", unsafe_allow_html=True)