import streamlit as st
from utils.cve_analysis import load_cve_data, run_cve_analysis, plot_priority_distribution
from utils import config as cf

def app():

    st.header("📋 CVSS Analysis")

    cve_data = load_cve_data(cf.cve_file_path)
    print("Data shape:", cve_data.shape)

    priority_counts = run_cve_analysis(cve_data)

    st.subheader("Vulnerability Priority Distribution")

    st.markdown("<p style='font-size:20px; font-weight:bold;'>Priority Counts:</p>", unsafe_allow_html=True)
    st.write(priority_counts)

    st.markdown("---")

    fig=plot_priority_distribution(priority_counts, figsize=cf.MEDIUM_SIZE)
    st.pyplot(fig)
