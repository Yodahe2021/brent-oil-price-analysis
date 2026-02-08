# Brent Oil Analysis: Strategic Interim Report
**Project:** Change Point Analysis of Global Oil Markets  
**Stakeholder:** Birhan Energies

## 1. Analysis Workflow & Methodology
Our approach follows a modular data science pipeline:
1. **Ingestion:** Loading historical prices with robust error handling.
2. **EDA:** Investigating stationarity (ADF test) and volatility regimes.
3. **Change Point Detection:** Using Bayesian MCMC (PyMC) to find structural breaks.
4. **Causal Attribution:** Mapping statistical breaks to historical geopolitical events.

## 2. Assumptions & Data Limitations
### Correlation vs. Causal Impact
*   **The Difference:** A statistical change point identifies a shift in the price *mean*, but it does not inherently prove a specific event caused it. 
*   **The Approach:** We assume that structural breaks occurring within a ±5-day window of a major event are highly likely to be caused by that event. However, we acknowledge that multiple factors (market sentiment, USD strength, and supply chain lag) contribute simultaneously.
### Limitations
*   Data frequency is daily; intra-day shocks are smoothed out.
*   The analysis currently focuses on Brent Crude only, ignoring regional benchmarks like WTI or Urals.

## 3. Communication Strategy
To maximize the impact of these insights, we utilize the following channels:
*   **Investors:** Quarterly **interactive dashboards** highlighting volatility regimes to support portfolio hedging.
*   **Policymakers:** Bi-annual **Policy Briefs** focusing on energy security and price stability during conflict.
*   **Energy Companies:** A **REST API (Flask)** providing real-time change point data for operational supply chain planning.