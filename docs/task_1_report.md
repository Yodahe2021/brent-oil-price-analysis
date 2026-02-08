# Interim Report: Brent Oil Price Analysis
**Date:** Feb 08, 2026  
**Author:** [Your Name]

## 1. Planned Analysis Steps
1. **Data Ingestion & Cleaning:** Load historical prices and handle missing dates via forward filling.
2. **Exploratory Data Analysis (EDA):** Identify long-term trends, volatility clusters, and test for stationarity using the ADF test.
3. **Change Point Modeling:** Apply Bayesian Inference (PyMC) to detect statistical shifts in price means.
4. **Causal Mapping:** Match detected change points with the researched external events (OPEC policies, Geopolitical conflicts).
5. **Dashboard Development:** Create a Flask API and React frontend to allow stakeholders to explore the data interactively.

## 2. Initial EDA Findings
* **Trend Analysis:** The data shows three distinct "Eras": The relatively stable $20/barrel era (1987-2000), the super-cycle peak reaching $140+ (2008), and the modern volatile era (2014-Present).
* **Stationarity:** The Augmented Dickey-Fuller (ADF) test confirmed that the price is **non-stationary** (p-value > 0.05), suggesting that the mean is not constant and structural breaks exist.
* **Volatility:** High volatility spikes align with major crises (e.g., 2008 Financial Crisis and 2020 COVID-19 pandemic).

## 3. Assumptions and Limitations
* **Assumptions:** We assume that price changes shortly after a major event are significantly influenced by that event.
* **Limitations:** **Correlation is not Causation.** Statistical change points tell us *when* a change happened, but not *why*. Our causal links are hypotheses based on historical context.