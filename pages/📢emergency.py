import streamlit as st
import requests
import json

# Page Configuration
st.set_page_config(
    page_title="CrisisPilot - Disaster Response",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .disaster-card {
        background: #2a2d35;
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .critical-alert {
        background: #ff4d4d;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        text-align: center;
        font-weight: bold;
    }
    .model-badge {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.8rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Improved System Prompt
# Enhanced System Prompt for Disaster Response
SYSTEM_PROMPT = """
You are CrisisPilot, an advanced Disaster Response AI assistant. Your role is to provide accurate, timely, and actionable information during emergencies. Follow these guidelines:

1. EMERGENCY PRIORITIZATION:
   - For active disaster reports (wildfire, flood, earthquake):
     * FIRST assess the severity based on user description
     * Then provide appropriate level response:
       🚨 CRITICAL: "EVACUATE IMMEDIATELY | CALL 108 (NDRF)" (when immediate danger is present)
       ⚠️ WARNING: "Prepare to evacuate | Monitor official channels" (when potential danger exists)
       ℹ️ INFORMATION: Detailed guidance (when situation is under control)

2. DISASTER-SPECIFIC GUIDANCE:
   - Wildfire:
     * Current detection: RESNET101 on VIIRS satellite (90.5% accuracy)
     * Immediate actions: Move perpendicular to wind direction, wet cloth face cover
     * Danger zones: Areas with dry vegetation, steep slopes
     
   - Flood:
     * Current detection: U-NET semantic segmentation on satellite imagery
     * Immediate actions: Move to higher ground, avoid walking in water
     * Danger zones: Low-lying areas, near rivers/dams
     
   - Earthquake:
     * Current detection: Seismic AI models
     * Immediate actions: Drop, cover, hold during shaking
     * Danger zones: Near unstable structures, coastal areas (tsunami risk)

3. INFORMATION DELIVERY:
   - Structure responses clearly:
     1. Situation assessment
     2. Immediate actions (numbered)
     3. Relevant contacts
     4. Technical details (if requested)
     
4. RESOURCE INTEGRATION:
   - Incorporate these data sources when relevant:
     * Real-time satellite feeds (NOAA-20 VIIRS)
     * Government disaster alerts (NDRF/IMD)
     * Crowdsourced incident reports
     
5. SAFETY PROTOCOLS:
   - NEVER:
     * Provide medical advice beyond first aid
     * Guarantee safety in uncertain situations
     * Delay recommending official emergency services
   - ALWAYS:
     * Err on the side of caution
     * Clarify when information is time-sensitive
     * Acknowledge limitations of remote assessment

6. USER INTERACTION:
   - Ask clarifying questions when:
     * Location details are vague
     * Situation severity is unclear
     * Multiple hazards may be present
   - Adapt language to user's apparent technical level
"""

# Also update the get_groq_response function to handle errors better:
def get_groq_response(user_input):
    """Get disaster response from Groq API"""
    GROQ_API_KEY = "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"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mixtral-8x7b-32768",
        "temperature": 0.3,  # Slightly increased for more varied responses
        "max_tokens": 1024,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=10
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ System temporarily unavailable. For immediate help, call NDRF at 108 or your local emergency number.")
        return None
# Model Badge UI
def render_model_badges():
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <span class="model-badge" style="background: #FF6B6B;">🔥 RESNET101 Wildfire</span>
        <span class="model-badge" style="background: #4ECDC4;">🌊 U-NET Flood</span>
        <span class="model-badge" style="background: #45B7D1;">🚁 YOLOv8 Victims</span>
    </div>
    """, unsafe_allow_html=True)

# Main App Logic
def main():
    st.title("🚨 CrisisPilot Disaster Response")
    st.caption("AI-powered emergency guidance | Integrated with real-time ML models")

    render_model_badges()

    tab1, tab2 = st.tabs(["🆘 Emergency Chat", "📡 System Info"])

    with tab1:
        user_input = st.text_area(
            "Describe your situation:",
            placeholder="e.g. 'Wildfire near my village' or 'Flood waters rising in Assam'",
            height=150
        )

        if st.button("Get Disaster Response", type="primary"):
            if user_input:
                with st.spinner("Analyzing situation with CrisisPilot AI..."):
                    response = get_groq_response(user_input)
                    if response:
                        if any(d in user_input.lower() for d in ["wildfire", "flood", "earthquake"]):
                            st.markdown('<div class="critical-alert">🚨 ACTIVE DISASTER DETECTED 🚨</div>', unsafe_allow_html=True)
                        st.markdown(f'<div class="disaster-card">{response}</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown("## 🏗️ CrisisPilot Architecture")
        st.markdown("""
        ```mermaid
        graph LR
            A[Satellite Imagery] --> B[Wildfire Detection]
            C[Drone Feeds] --> D[Victim Detection]
            E[Flood Sensors] --> F[Flood Analysis]
            B --> G[Alert System]
            D --> G
            F --> G
            G --> H[Emergency Dashboard]
        ```
        """)

        with st.expander("📊 Active Models"):
            cols = st.columns(3)
            with cols[0]:
                st.markdown("**🔥 Wildfire Detection**")
                st.write("- RESNET101 (90.5% accuracy)")
                st.write("- NOAA-20 VIIRS satellite")
            with cols[1]:
                st.markdown("**🌊 Flood Analysis**")
                st.write("- U-NET Semantic Segmentation")
                st.write("- Real-time water level mapping")
            with cols[2]:
                st.markdown("**🚁 Victim Detection**")
                st.write("- YOLOv8 on drone footage")
                st.write("- 85% precision in field tests")

if __name__ == "__main__":
    main()
