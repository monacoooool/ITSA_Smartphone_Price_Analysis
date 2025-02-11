
# Interrupted Time Series Analysis (ITSA) of Smartphone Prices

## Methodology

### **Introduction**
This document outlines the methodological framework applied in the **Interrupted Time Series Analysis (ITSA) of Smartphone Prices**. The objective is to assess whether the introduction of a policy intervention on **May 16, 2019**, affected smartphone price trends.

---

### **Data Preprocessing**
The dataset was preprocessed as follows:

- **Handling Missing Values:** Any missing entries were removed to ensure consistency.
- **Feature Selection:** The analysis focused on the **second column (time)** and **fourth column (price)**.
- **Data Formatting:** The **time variable** was converted to a proper datetime format, and **price values** were converted to numeric.

---

### **Statistical Analysis**
A comprehensive statistical analysis was performed, including:

- **Descriptive Statistics:** Summary measures such as **mean, median, and variance** were calculated.
- **Trend Identification:** Examination of **price variations over time**.
- **Pre- and Post-Intervention Comparison:** Analysis of **price trends before and after May 16, 2019**.

---

### **Interrupted Time Series Analysis (ITSA)**
The ITSA model was implemented as follows:

- **Regression Framework:** A **linear regression model** was used to estimate price trends.
- **Key Variables:**
  - **Time (β1):** Represents the trend in prices **before** the intervention.
  - **Intervention (β2):** Binary variable indicating **pre- and post-intervention** periods.
  - **Interaction Term (β3):** Captures **changes in trend** following the intervention.
- **Significance Testing:** The **p-values** associated with **β1 and β3** were evaluated to determine statistical significance.

---

### **Robustness Check**
To assess the stability of the results:

- **Alternative Specifications:** The model was tested with **different time windows**.
- **Outlier Analysis:** Potential **extreme values** were identified and their impact was examined.
- **Robustness Index:** A metric was calculated to measure the **consistency of the intervention effect**.

---

### **Reproducibility**
The dataset and scripts used for this analysis are included in the **repository**. Users can replicate the analysis by following the setup instructions.
