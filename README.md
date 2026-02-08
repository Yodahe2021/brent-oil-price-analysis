Brent Oil Price Analysis: Change Point & Statistical Modeling
![alt text](https://img.shields.io/badge/Data_Science-10_Academy-blue)

![alt text](https://img.shields.io/badge/Python-3.9+-green)

![alt text](https://img.shields.io/badge/Bayesian_Inference-PyMC-orange)
📌 Project Overview
As a Data Scientist at Birhan Energies, this project focuses on analyzing how major political and economic events affect Brent oil prices. The objective is to provide actionable intelligence for investors, policymakers, and energy companies by identifying structural breaks in price data and associating them with historical events.
🎯 Objectives
Identify key events (OPEC decisions, conflicts, economic sanctions) that impacted oil prices.
Quantify the impact of these events using Bayesian Change Point Analysis.
Develop a full-stack dashboard (Flask + React) to visualize these insights.
📂 Project Structure
code
Text
├── data/
│   ├── brent_oil_prices.csv   # Raw historical data (1987-2022)
│   └── external_events.csv    # Compiled list of 10-15 geopolitical events
├── docs/
│   └── interim_report.md      # Task 1: Planning and EDA findings
├── notebooks/
│   ├── 01_eda_analysis.ipynb  # Task 1: Exploratory Data Analysis
│   └── 02_change_point.ipynb  # Task 2: PyMC Bayesian Modeling
├── backend/                   # Flask API (Task 3)
├── frontend/                  # React Application (Task 3)
├── requirements.txt           # Project dependencies
└── README.md
🛠️ Installation & Setup
1. Clone the repository
code
Bash
git clone https://github.com/YOUR_USERNAME/brent-oil-analysis.git
cd brent-oil-analysis
2. Set up Virtual Environment
code
Bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate  # Windows
3. Install Dependencies
code
Bash
pip install -r requirements.txt
📈 Methodology
Task 1: Foundation & EDA
Research: Compiled a structured dataset of 15 key global events.
EDA: Analyzed time-series properties like Trend, Seasonality, and Stationarity (ADF Test).
Finding: Brent oil prices are non-stationary, requiring change-point models to identify shifts in regimes.
Task 2: Bayesian Change Point Detection
Using PyMC, we implemented a model to detect structural breaks:
Priors: Defined a discrete uniform prior for the switchpoint (
τ
τ
).
Likelihood: Modeled the price as a Normal distribution with shifting means (
μ
1
,
μ
2
μ 
1
​
 ,μ 
2
​
 
).
Inference: Used MCMC sampling to identify the most likely date of change.
Insight: Successfully identified the 2014 Price Collapse, showing a drop from ~
105
t
o
 
105to 
52.
🚀 Upcoming Features (Task 3)
Flask Backend: API endpoints to serve processed data and model results.
React Dashboard: Interactive charts using Recharts/D3.js to visualize event-price correlations.
🤝 Acknowledgments
Tutors: Kerod, Filimon, Mahbubah.
Organization: 10 Academy - Artificial Intelligence Mastery.
