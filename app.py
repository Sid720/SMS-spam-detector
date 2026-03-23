import streamlit as st
import pickle
import time

try:
    cv = pickle.load(open('cv.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model files not found.")

st.markdown("""
    <style>
    /* Status Container */
    .status-container {
        border: 1px solid #d1d5db;
        border-radius: 8px;
        padding: 10px 15px;
        background-color: #f9fafb;
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 20px;
    }
    
    /* The Green Loading Dot/Bar */
    .status-indicator {
        width: 12px;
        height: 12px;
        background-color: #10b981;
        border-radius: 50%;
        box-shadow: 0 0 8px #10b981;
    }

    /* Animation for "Thinking" */
    @keyframes pulse {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(1.2); }
        100% { opacity: 1; transform: scale(1); }
    }
    
    .thinking-active {
        animation: pulse 1.5s infinite ease-in-out;
    }

    .status-text {
        font-family: 'Courier New', Courier, monospace;
        font-size: 13px;
        font-weight: bold;
        color: #374151;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("SMS Spam Checker")

status_placeholder = st.empty()

status_placeholder.markdown("""
    <div class="status-container">
        <div class="status-indicator"></div>
        <div class="status-text">SYSTEM STATUS: READY</div>
    </div>
    """, unsafe_allow_html=True)

input_text = st.text_area("Enter Message Analysis Input:", height=150)

if st.button('Run Diagnostics'):
    if input_text.strip():
        
        status_placeholder.markdown("""
            <div class="status-container">
                <div class="status-indicator thinking-active"></div>
                <div class="status-text">SYSTEM STATUS: ANALYZING PATTERNS...</div>
            </div>
            """, unsafe_allow_html=True)
        
        time.sleep(1.5)
        
      
        data = cv.transform([input_text]).toarray()
        prediction = model.predict(data)
        
        if prediction[0] == 1:
            status_placeholder.markdown("""
                <div class="status-container" style="border-color: #ef4444;">
                    <div class="status-indicator" style="background-color: #ef4444; box-shadow: 0 0 8px #ef4444;"></div>
                    <div class="status-text" style="color: #ef4444;">SYSTEM STATUS: THREAT DETECTED</div>
                </div>
                """, unsafe_allow_html=True)
            st.error("**SPAM DETECTED**")
        else:
            status_placeholder.markdown("""
                <div class="status-container" style="border-color: #10b981;">
                    <div class="status-indicator"></div>
                    <div class="status-text" style="color: #10b981;">SYSTEM STATUS: CLEAN</div>
                </div>
                """, unsafe_allow_html=True)
            st.success("**MESSAGE VERIFIED**")
    else:
        st.warning("Please enter text to analyze.")

st.markdown("---")
st.caption(f"Logged in as: sid.gedam720s@gamil.com")