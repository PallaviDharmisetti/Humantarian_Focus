# 🛡️ Humanitarian Intelligence & War Impact System

## 📌 Project Overview

The **Humanitarian Intelligence & War Impact System** is an interactive dashboard built using Python and Streamlit. It demonstrates how data visualization and simplified mathematical models can be used to explore hypothetical conflict scenarios and estimate humanitarian aid requirements.

The project focuses on presenting scenario inputs, impact estimates, and logistical support requirements through a user-friendly dashboard.

## ✨ Features

- **Interactive Mission Control:** Select a weapon category and model, enter the number of strikes, specify impacted locations, and adjust scenario parameters.
- **Impact Estimation:** Display illustrative blast-radius, fatality, injury, and affected-population estimates.
- **Impact Visualization:** Compare single-strike and multiple-strike area estimates using interactive bar charts.
- **Humanitarian Logistics:** Estimate drinking water, food rations, medical packs, and transport requirements.
- **Technical Specifications:** Display the selected category, configured yield, and illustrative deployment assumptions.
- **Interactive Dashboard:** Explore results through Streamlit controls and analysis tabs.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Math (Python standard library)

## 📂 Project Structure

```text
humanitarian-intelligence-system/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible newer version
- Git
- Visual Studio Code (recommended)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/humanitarian-intelligence-system.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the project folder

```bash
cd humanitarian-intelligence-system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 📊 Dashboard Sections

### 1. Impact Visualization
Displays illustrative impact-area estimates and compares a single strike with the configured number of strikes.

### 2. Logistical Support
Presents estimated quantities of water, food, medical supplies, and transport capacity for humanitarian response planning.

### 3. Arsenal Specifications
Shows the selected model, configured yield, and simplified scenario assumptions.

## 🎯 Project Objectives

- Demonstrate Python-based interactive dashboard development.
- Apply basic mathematical calculations to hypothetical scenarios.
- Present data through interactive charts and tables.
- Explore how decision-support interfaces can communicate humanitarian logistics estimates.

## ⚠️ Limitations and Responsible Use

This project is an **educational prototype**, not a validated humanitarian assessment or operational planning system.

The blast-radius formulas, casualty estimates, weapon yields, and supply calculations are simplified assumptions. They have not been validated against authoritative scientific or humanitarian datasets. The model does not account for overlapping impact zones, shelter, terrain, population distribution, medical capacity, or other critical real-world factors.

Its outputs must not be treated as reliable predictions of casualties, actual weapon performance, or real-world aid requirements.

## 🚀 Future Enhancements

- Add interactive maps for affected areas.
- Incorporate verified humanitarian population and infrastructure datasets.
- Improve uncertainty handling and explainability.
- Add scenario comparison and downloadable reports.
- Develop more robust, validated humanitarian needs assessment methods.

## 👩‍💻 Author

Developed as a Python and data visualization dashboard prototype.

---

*Built with Python, Streamlit, Pandas, and Plotly.*
