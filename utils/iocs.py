import streamlit as st
from utils import config as cf
from utils.ioc_analysis import load_json_data, ioc_matching_module, filter_iocs

def app():

    data=load_json_data(cf.json_path)

    st.header("🔍 Indicators of Compromise (IoCs)")

    data_df, ioc_summary = ioc_matching_module(data)

    st.subheader("Rule-Based Matching")
    st.dataframe(data_df)
 
    st.markdown("<p style='font-size:20px; font-weight:bold;'>IoC Summary:</p>", unsafe_allow_html=True)
    st.dataframe(ioc_summary)

    st.markdown("---")

    left_column, right_column = st.columns([2, 1])
    # Left column: Model selection
    with left_column:
        filter_type = st.selectbox("Filter by:", ["IP Address", "Domain", "Hash", "URL", "CVE"])
    # Right column: Contamination slider
    with right_column:
        pass

    filtered_data = filter_iocs(data_df, filter_type)

    if not filtered_data.empty:
        st.subheader(f"Filter Type: {filter_type}")
        st.write(filtered_data)
    else:
        st.write("No data found for selected filter.")
