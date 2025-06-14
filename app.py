import streamlit as st
import openai
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="AgroGPT - Your AI Farming Assistant",
    page_icon="🌾",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom CSS for better UI
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .chat-message.user {
        background-color: #2b313e;
        color: white;
    }
    .chat-message.assistant {
        background-color: #f0f2f6;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🌾 AgroGPT")
st.markdown("""
    Your AI-powered agricultural consultant. Ask questions about farming, crops, weather, 
    soil health, pest control, and market trends. Get practical, actionable advice for your farming needs.
""")

# Sidebar
with st.sidebar:
    st.header("About AgroGPT")
    st.markdown("""
    AgroGPT is designed to help farmers and agricultural professionals with:
    - Crop selection and management
    - Weather-based farming advice
    - Soil health information
    - Pest control solutions
    - Market trends and insights
    
    Simply type your question in plain language to get started!
    """)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask your farming question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response (placeholder for now - you'll need to integrate with your AI model)
    response = "This is a placeholder response. Please integrate your AI model here."
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>AgroGPT - Making farming smarter, one question at a time 🌱</p>
    </div>
""", unsafe_allow_html=True)

