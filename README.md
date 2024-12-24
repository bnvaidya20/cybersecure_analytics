# CyberSecure Analytics Dashboard

## Overview
The **CyberSecure Analytics Dashboard** is an interactive, Python-based application designed to streamline cybersecurity management tasks. It leverages advanced data analysis and visualization techniques to help security professionals detect, analyze, and mitigate threats effectively. Built using the Streamlit framework, the dashboard integrates open-source datasets and models to provide insights across multiple domains of cybersecurity.

## Features

1. **Home Page (Overview):**
   - Introduction to the dashboard's capabilities and its use cases in modern cybersecurity.

2. **Intrusion Detection System (IDS):**
   - Analyze network traffic for potential intrusions.
   - Choose from pre-trained models like Random Forest, and SVM.
   - Visualize confusion matrices and feature importance.

3. **Anomaly Detection:**
   - Detect anomalies in network logs using Isolation Forest or Improved Isolation Forest models.
   - Customize detection sensitivity with adjustable contamination levels.
   - Visualize detected anomalies over time.

4. **Indicators of Compromise (IoCs):**
   - Match IoCs such as IP addresses, domains, hashes, URLs, and CVEs using rule-based methods.
   - View and filter matched IoCs for detailed analysis.

5. **CVSS Analysis:**
   - Prioritize vulnerabilities using the Common Vulnerability Scoring System (CVSS).
   - Visualize vulnerability distributions and analyze priority counts.

## Technology Stack
- **Programming Language:** Python
- **Framework:** Streamlit
- **Data Sources:** CICIDS 2017, Suricata SCI01 logs, OTX AlienVault Pulses, and Common Vulnerabilities and Exposures (CVE)
- **Visualization:** Matplotlib, and Seaborn

## Installation

### Prerequisites
- Python 3.8 or higher
- Pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/bnvaidya20/cybersecure_analytics.git
   cd cybersecure_analytics
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open the application in your browser using the URL provided by Streamlit (typically `http://localhost:8501`).


## Usage
1. Navigate to the desired page using the sidebar.
2. Interact with the tools by selecting models, adjusting parameters, and viewing results.
3. Analyze outputs such as confusion matrices, feature importance, detected anomalies, IoCs, and CVSS distributions.

## Contributing
Contributions are welcome! If you'd like to add features or fix issues:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with detailed descriptions of changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, please contact:
- **Email:** bnvaidya@mail.com
- **GitHub:** [Binod Vaidya](https://github.com/bnvaidya20)

