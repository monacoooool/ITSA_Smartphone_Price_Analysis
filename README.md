# ITSA_Smartphone_Price_Analysis
By analyzing the sanctions imposed on Huawei during the previous Trump administration (05-16-2019), we will investigate how the smartphone market responded to this decision and assess its impact on pricing trends.


## Repository Structure

```plaintext
ITSA_Smartphone_Price_Analysis/
│── python/
│   ├── itsa_model.py           # ITSA model estimation
│   ├── statistical_tests.py    # Implementation of statistical tests
│   ├── visualization.py        # Functions for plotting results
│   ├── robustness_check.py     # Robustness index calculation
│
│── data/
│   ├── smartphone_prices.csv   # Cleaned and processed dataset
│
│── scripts/
│   ├── main_analysis.py        # Main script for executing ITSA
│
│── output/
│   ├── figures/                # Graphical outputs (plots, trends)
│   ├── results/                # Statistical results, model summaries
│   ├── regression_output.txt   # ITSA regression summary
│
│── docs/
│   ├── methodology.md          # Methodology documentation
│
│── LICENSE                     # Repository license
│── README.md                   # Repository description and instructions
│── requirements.txt             # List of required Python packages


## Prerequisites

The following Python libraries are required:

```r
- readr        # CSV file reading
- labstatR     # Basic statistical functions
- tseries      # Time series analysis
- moments      # Skewness and kurtosis calculation
- VIM          # Missing data handling
- gridExtra    # Layout for graphical outputs
- lmtest       # Jarque-Bera test
- nortest      # Normality tests
- MASS         # Ordinal logistic regression
- car          # Model diagnostics
- olsrr        # Model diagnostics
- pscl         # Pseudo R-squared
- pwr          # Statistical power analysis
- dplyr        # Data manipulation
- caret        # Machine Learning and data preprocessing
- pROC         # ROC curves
- brant        # Proportional odds test for ordinal models
- xgboost      # Advanced machine learning models


## Key Features

- **Robust Time Series Analysis** using Interrupted Time Series Analysis (ITSA)
- **Pre- and Post-Intervention Trend Estimation** to assess policy impact
- **Statistical Significance Testing** for trend changes with p-values and confidence intervals
- **Robustness Index Calculation** to evaluate model stability
- **Comprehensive Visualizations** including time series plots and regression trend lines
- **Automated Model Diagnostics** for assessing model fit and collinearity
- **Effect Size Estimation** to quantify the impact of intervention on pricing trends
- **Reproducible Data Pipeline** with structured preprocessing and analysis scripts

## Prerequisites

The following Python libraries are required to run the ITSA analysis:

```plaintext
- pandas        # Data manipulation and CSV file reading
- numpy         # Numerical computations
- statsmodels   # Statistical modeling and ITSA implementation
- matplotlib    # Data visualization
- seaborn       # Statistical data visualization
- scipy         # Advanced statistical functions
- scikit-learn  # Machine learning and regression diagnostics
- missingno     # Missing data visualization
- tqdm          # Progress bar for iterative processes



## Getting Started

To run the ITSA analysis, follow these steps:

```sh
# Clone the repository
git clone https://github.com/your-username/ITSA_Smartphone_Price_Analysis.git
cd ITSA_Smartphone_Price_Analysis

# Install dependencies
pip install -r requirements.txt

# Run the complete analysis
python scripts/main_analysis.py data/smartphone_prices.csv

## Analysis Pipeline

### 1. Data Preprocessing (`python/data_preprocessing.py`)
- Handling missing values
- Converting date formats for time series analysis
- Creating pre- and post-intervention variables
- Normalizing price values

### 2. Basic Statistical Analysis (`python/statistical_tests.py`)
- Descriptive statistics
- Confidence intervals
- Hypothesis testing
- Outlier analysis
- Correlation matrices

### 3. Normality Tests (`python/statistical_tests.py`)
- Shapiro-Wilk test
- Kolmogorov-Smirnov test
- Jarque-Bera test
- Anderson-Darling test
- Bonferroni correction for multiple tests
- Statistical power analysis

### 4. Visualizations (`python/visualization.py`)
- Time series plots with trendlines
- Boxplots for outlier detection
- Q-Q plots for normality assessment

### 5. ITSA Model Estimation (`python/itsa_model.py`)
- Ordinary Least Squares (OLS) regression for ITSA
- Pre- and post-intervention slope estimation
- Statistical significance assessment
- Confidence intervals for model parameters

### 6. Post-Model Diagnostics and Validation (`python/robustness_check.py`)
- Residual analysis for model validation
- Variance Inflation Factor (VIF) for multicollinearity assessment
- Robustness index calculation
- Statistical power analysis for model stability

### 7. Results and Interpretation (`output/results/`)
- Exported statistical summaries
- Graphical outputs for publication
- Regression results for further interpretation

## Dataset Structure

The dataset should be saved in `data/` and includes the following variables:

- **date**: Release date of the smartphone
- **model**: Specific model name
- **price**: Original launch price of the smartphone
- **adjusted_price**: Inflation-adjusted price for standardization

## Citation

If you use this software in your research, please cite:

```bibtex
@software{Monaco2025,
  author = {Monaco, Luigi},
  title = {The Impact of a Tariff on the Technology Sector: The Huawei Case},
  year = {2025},
  url = {https://github.com/your-username/ITSA_Smartphone_Price_Analysis}
}

LICENSE?

Contact

For any inquiries regarding this project, feel free to reach out:
	•	Luigi Monaco
📧 monacoluigi03@gmail.com
🔗 Project Link - GitHub Repository

