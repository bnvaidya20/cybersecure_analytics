
import streamlit as st
from utils import config as cf
from utils.ad_analysis import load_ad_data, run_anomaly_detection, run_anomaly_detection_feature_eng, plot_anomalies_over_time

def app():

    st.header("📊 Anomaly Detection")

    data = load_ad_data(cf.ad_data_path)
    print("Data shape:", data.shape)

    left_column, right_column = st.columns([1, 2])
    # Left column: Model selection
    with left_column:
        model_name = st.selectbox(
            "Select a model:", 
            ["IF Anomaly Detector", "Improved IF Anomaly Detector"]
        )
    # Right column: Contamination slider
    with right_column:
        contamination = st.slider(
            "Select contamination level", 
            min_value=0.01, 
            max_value=0.04, 
            value=0.01, 
            step=0.01
        )

    st.markdown("---")

    if contamination:
        if model_name == "IF Anomaly Detector":
            data, timestamp, anomalies_count, anomalies = run_anomaly_detection(data, contamination)
        else:
            data, timestamp, anomalies_count, anomalies = run_anomaly_detection_feature_eng(data, contamination)

        st.subheader("Anomalies Count")
        st.dataframe(anomalies_count)

        st.subheader("Detected Anomalies")
        st.dataframe(anomalies)

        st.subheader("Anomaly Detection Plot")
        fig = plot_anomalies_over_time(data, timestamp, figsize=cf.MEDIUM_SIZE)
        st.pyplot(fig)
    else:
        st.error("Invalid contamination value.")
