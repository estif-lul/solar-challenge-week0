
# Solar Challenge Week 0 - Solar Data EDA

This project showcases exploratory data analysis (EDA) on solar and meteorological datasets from Benin, Sierra Leone, and Togo. The objective is to uncover relationships between solar irradiance, weather variables, and module performance, preparing the data for subsequent modeling or reporting. This analysis demonstrates the use of Python, particularly the pandas library, for robust data exploration.

## 📁 Project Structure

```
.
├── app/                  # Streamlit dashboard application
│   └── main.py
├── reports/              # Generated reports and summaries
├── screenshots/          # Visualizations and dashboard snapshots
├── src/                  # Source code for data processing and analysis
│   ├── notebooks/        # Jupyter notebooks for EDA
│   │   ├── benin_eda.ipynb
│   │   ├── sierraleone_eda.ipynb
│   │   └── togo_eda.ipynb
│   ├── benin_eda.py      # Script for Benin data analysis
│   ├── sierraleone_eda.py# Script for Sierra Leone data analysis
│   └── togo_eda.py       # Script for Togo data analysis
├── data/                 # Raw and cleaned datasets
│   ├── benin-malanville.csv
│   ├── benin-cleaned.csv
│   ├── sierraleone-bumbuna.csv
│   ├── sierraleone-cleaned.csv
│   ├── togo-dapaong_qc.csv
│   └── togo-cleaned.csv
├── .github/workflows/    # CI/CD workflows
│   └── ci.yml
├── .gitignore            # Git ignore file
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## ✨ Features

- **Data Cleaning & Outlier Removal:** Ensures data quality by handling missing values and filtering anomalies.
- **Correlation Analysis:** Utilizes heatmaps to identify relationships between variables like GHI, DNI, DHI, TModA, and TModB.
- **Scatter Plots:** Explores relationships such as WS, WSgust, WD vs. GHI, and RH vs. Tamb/GHI.
- **Wind Distribution Analysis:** Visualizes wind speed and direction using wind rose plots and histograms.
- **Time Series & Distribution Visualizations:** Analyzes temporal trends and variable distributions.
- **Bubble Charts:** Depicts multi-variable relationships, e.g., GHI vs. Tamb with bubble size representing RH.
- **Interactive Dashboard (Streamlit):** Streamlit app for dynamic data exploration and visualization.
- **CI/CD Integration (GitHub Actions):** Automated workflows using GitHub Actions for testing and deployment. 

## 🛠️ Installation & Setup
### Prerequisites
	- Python 3.8+
	- Git

### Local Setup

1.	Clone the Repository:
```bash
git clone https://github.com/estif-lul/solar-challenge-week0.git
cd solar-challenge-week0
```


2.	Create a Virtual Environment:
```bash
python -m venv venv
# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
3.	Install Dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Running the Streamlit Dashboard

Navigate to the app/ directory and run:
```bash
cd app
streamlit run main.py
```
This will launch the interactive dashboard in your default web browser. 

### Running Jupyter Notebooks

Navigate to the src/notebooks/ directory and open the desired notebook (e.g., benin_eda.ipynb) using Jupyter Notebook or JupyterLab:
```bash
cd src/notebooks
jupyter notebook
```

### Running Python Scripts

Execute the analysis scripts directly from the command line:
```bash
python src/benin_eda.py
python src/sierraleone_eda.py
python src/togo_eda.py
```

## 📊 Outputs

- **Cleaned Data**: Saved as [country]-cleaned.csv in the data/ directory.
- **Visualizations**: Generated plots and charts are saved in the screenshots/ directory.
- **Reports**: Summarized findings and analyses are available in the reports/ directory.


## 🤝 Contributing

Feel free to fork the repo and submit PRs. For major changes, please open an issue first.

