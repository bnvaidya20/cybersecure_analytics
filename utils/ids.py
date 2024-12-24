import streamlit as st
from utils import config as cf
from utils.ids_analysis import load_ids_data, load_model, evaluate_model, plot_confusion_matrix, plot_feature_importance

def app():

    st.header("🛡️ Intrusion Detection System (IDS)")

    X, y = load_ids_data(cf.cicids_data_parts)

    left_column, right_column = st.columns([2, 1])
    # Left column: Model selection
    with left_column:
        model_name = st.selectbox("Select a model:", list(cf.MODEL_PATHS.keys()))
    # Right column: Contamination slider
    with right_column:
        pass

    model_path = cf.MODEL_PATHS.get(model_name)
    model = load_model(model_path)

    st.markdown("---")

    if model:
        accuracy, cm, report = evaluate_model(model, X, y)
        st.subheader(f"Model Evaluation: {model_name}")
        st.markdown("<p style='font-size:20px; font-weight:bold;'>Accuracy:</p>", unsafe_allow_html=True)
        st.write(f"{accuracy * 100:.2f}%")
        st.markdown("<p style='font-size:20px; font-weight:bold;'>Classification Report:</p>", unsafe_allow_html=True)
        st.text(report)

        st.subheader("Confusion Matrix")
        fig_cm = plot_confusion_matrix(cm, figsize=cf.MEDIUM_SIZE)
        st.pyplot(fig_cm)

        if model_name in ["Random Forest"]:
            st.subheader("Feature Importance")
            fig_fi = plot_feature_importance(model, X.columns, figsize=cf.MEDIUM_SIZE)
            if fig_fi:
                st.pyplot(fig_fi)
    else:
        st.error("Model could not be loaded. Please try another.")
