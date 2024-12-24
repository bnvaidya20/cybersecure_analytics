import streamlit as st

def app():
    st.header("🏠 Home")

    # Overview Section
    st.subheader("Overview")
    st.write(
        "In today's interconnected world, cybersecurity threats are increasingly complex. "
        "Managing them effectively requires robust tools capable of real-time analysis, detection, and mitigation."
    )
    st.write(
        "The CyberSecure Analytics is a Python-based tool that integrates with open-source datasets to analyze "
        "and report cybersecurity threats. It leverages datasets like CICIDS 2017, Suricata SCI01 logs, "
        "OTX AlienVault Pulses, and CVE to provide insights and streamline cybersecurity management."
    )
    st.markdown("---")

    # Project Objective Section
    st.subheader("🎯 Project Objective")
    st.write(
        """
        The primary goal of this project is to design and implement a cybersecurity management tool with the following capabilities:
        - **Intrusion Detection Analysis**: Utilize the CICIDS 2017 dataset for network traffic analysis.
        - **Threat Intelligence Integration**: Leverage OTX AlienVault Pulses for real-time threat intelligence.
        - **Log Analysis**: Analyze logs using Suricata SCI01 data for anomaly detection.
        - **Vulnerability Tracking**: Integrate CVE data to identify and respond to known vulnerabilities.
        """
    )
    st.markdown("---")

    # Datasets Section
    st.subheader("📂 Datasets Used")
    st.write(
        """
        The CyberSecure Analytics utilizes the following datasets to achieve its objectives:
        
        1. **CICIDS 2017 Dataset**:
            - Provides labeled network intrusion detection system (NIDS) data.
            - Includes features like protocol, timestamps, source/destination IPs, and attack labels.
        
        2. **Suricata SCI01 Logs**:
            - Contains detailed log data from the Suricata intrusion detection system.
            - Can be used for detecting malicious patterns.
        
        3. **OTX AlienVault Pulses**:
            - Real-time threat intelligence fetched using the OTX API.
            - Supplies threat intelligence, including Indicators of Compromise (IoCs).
        
        4. **CVE Dataset**:
            - Comprehensive database of common vulnerabilities and exposures.
            - Provides a regularly updated list of known vulnerabilities.
        """
    )
    st.markdown("---")
