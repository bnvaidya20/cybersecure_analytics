import streamlit as st
from utils import cvss, home, ids, anomaly_detection, iocs

# Constants for styling and page configuration
PAGE_ICON = "🛡️"
LAYOUT = "wide"

def navigation():
    # Sidebar dropdown navigation
    st.sidebar.title("Navigation")
    menu_options = [
        "🏠 Home",
        "🛡️ Intrusion Detection System",
        "📊 Anomaly Detection",
        "🔍 Indicators of Compromise",
        "📋 CVSS Analysis"
    ]
    menu_selection = st.sidebar.selectbox("Go to:", menu_options)
    # Load the selected page
    if menu_selection == "🏠 Home":
        st.sidebar.divider()
        st.sidebar.subheader(f"{menu_selection}")
        st.sidebar.write(
            """
            - Introduction to the dashboard's capabilities and its use cases in modern cybersecurity.
            """
        ) 
        home.app()

    elif menu_selection == "🛡️ Intrusion Detection System":
        st.sidebar.divider()
        st.sidebar.subheader(f"{menu_selection}")
        st.sidebar.write(
            """
            - Analyze network traffic for potential intrusions.
            - Choose from pre-trained models like Random Forest, and SVM.
            - Visualize confusion matrices and feature importance.
            """
        )    
        ids.app()

    elif menu_selection == "📊 Anomaly Detection":
        st.sidebar.divider()
        st.sidebar.subheader(f"{menu_selection}")
        st.sidebar.write(
            """
            - Detect anomalies in network logs using Isolation Forest or Improved Isolation Forest models.
            - Customize detection sensitivity with adjustable contamination levels.
            - Visualize detected anomalies over time.
            """
        )
        anomaly_detection.app() 

    elif menu_selection == "🔍 Indicators of Compromise":
        st.sidebar.divider()
        st.sidebar.subheader(f"{menu_selection}")
        st.sidebar.write(
            """
            - Match IoCs such as IP addresses, domains, hashes, URLs, and CVEs using rule-based methods.
            - View and filter matched IoCs for detailed analysis.
            """
        )
        iocs.app()

    elif menu_selection == "📋 CVSS Analysis":
        st.sidebar.divider()
        st.sidebar.subheader(f"{menu_selection}")
        st.sidebar.write(
            """
            - Prioritize vulnerabilities using the Common Vulnerability Scoring System (CVSS).
            - Visualize vulnerability distributions and analyze priority counts.
            """
        )
        cvss.app()


def main():
    # Set the page configuration
    st.set_page_config(
        page_title="Cybersecure Dashboard",
        page_icon=PAGE_ICON,
        layout=LAYOUT,
        menu_items=None
    )

    # Title
    st.markdown(
        """
        <style>
        .background {
            background-color:#4CAF50;
            padding:10px;
            border-radius:10px;
        }
        .title {
            color:white;
            text-align: center;
            font-size: 2em;
            font-weight: bold;
        }
        .text {
            color:white;
            text-align:center;
            font-size:24px;
        }
        </style>
        <div class="background">
            <h1 class="title"> Welcome to CyberSecure Analytics Dashboard </h1>
            <p class="text"> One-stop Solution for Cybersecurity Insights ! </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    navigation()

if __name__ == "__main__":
    main()
