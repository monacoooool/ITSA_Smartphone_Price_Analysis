# 📊 ITSA Smartphone Price Analysis

This repository contains the code and data used for an **Interrupted Time Series Analysis (ITSA)** to assess the impact of a policy decision on smartphone pricing trends.

---

## 📂 Repository Structure

Below is the structured organization of the repository:


```text
ITSA_Smartphone_Price_Analysis/
├── python/
│   ├── itsa_model.py           # ITSA model estimation
│   ├── statistical_tests.py    # Implementation of statistical tests
│   ├── visualization.py        # Data visualization functions
│   ├── robustness_check.py     # Robustness index calculation
│
├── data/
│   ├── smartphone_prices.csv   # Cleaned and processed dataset
│
├── scripts/
│   ├── main_analysis.py        # Main script for executing ITSA
│
├── output/
│   ├── figures/                # Graphical outputs (plots, trends)
│   ├── results/                # Statistical results, model summaries
│   ├── regression_output.txt   # ITSA regression summary
│
├── docs/
│   ├── methodology.md          # Methodology documentation
│
├── LICENSE                     # Repository license
├── README.md                   # Repository description and instructions
└── requirements.txt            # List of required Python packages
```
---

## ⚙️ Getting Started  

Follow these steps to set up the repository:

# Clone the repository
git clone https://github.com/monacoooool/ITSA_Smartphone_Price_Analysis.git

# Navigate into the project directory
cd ITSA_Smartphone_Price_Analysis

# Install dependencies
pip install -r requirements.txt

---

## 📌 Prerequisites  

The following **Python libraries** are required:

- pandas            # Data manipulation
- numpy             # Numerical operations
- statsmodels       # Statistical modeling
- matplotlib        # Data visualization
- seaborn           # Enhanced data visualization

---

## 🛠 Analysis Pipeline  

The analysis follows these key steps:

1️⃣ **Data Preprocessing (`scripts/main_analysis.py`)**  
   - Data cleaning and transformation  
   - Handling missing values  

2️⃣ **Statistical Analysis (`python/statistical_tests.py`)**  
   - Descriptive statistics  
   - Hypothesis testing  

3️⃣ **ITSA Model (`python/itsa_model.py`)**  
   - Pre- and post-intervention trend estimation  
   - Model significance testing  

4️⃣ **Robustness Check (`python/robustness_check.py`)**  
   - Sensitivity analysis  

5️⃣ **Visualization (`python/visualization.py`)**  
   - Graphical representation of results  

---

## 📊 Dataset Structure  

The dataset is stored in `data/smartphone_prices.csv` and includes the following variables:

- Date: Date of smartphone release
- Model: Smartphone model name
- Price: Initial market price
- Inflation_Adjusted_Price: Price adjusted for inflation

---

## 📄 License  

This project is **open-source** and distributed under the **MIT License**.  
See the **LICENSE** file for details.

---

## 📬 Contact  

For any inquiries, feel free to reach out:

📧 **Luigi Monaco** - monacoluigi03@gmail.com  
🔗 **GitHub Repository** - [Project Link](https://github.com/monacoooool/ITSA_Smartphone_Price_Analysis)

---
