import pandas as pd
import os
import numpy as np
from statsmodels.api import OLS, add_constant

# File path
file_path = '/Users/luigimonaco/Documents/cod/phonedata.csv'  # Insert the correct path here
if not os.path.exists(file_path):
    print(f"The file {file_path} was not found. Please wait for the upload and try again.")
else:
    # Load data
    df = pd.read_csv(file_path)
    print(f"Initial number of rows in dataset: {df.shape[0]}")
    print("Raw data preview:")
    print(df.head())

    # Verify that the CSV has at least 4 columns
    if df.shape[1] < 4:
        raise ValueError("The CSV file does not contain at least four columns. Please check the file content.")

    # Select necessary columns (second column: time, and fourth column: price)
    df = df.iloc[:, [1, 3]]
    df.columns = ['Release Year', 'Price']

    # Convert the 'Release Year' column to datetime
    df['Release Year'] = pd.to_datetime(df['Release Year'], errors='coerce')

    # Print the number of rows after datetime conversion
    print(f"Number of rows after datetime conversion: {df.shape[0]}")
    
    # Remove any NaN values in 'Release Year' and 'Price'
    df = df.dropna(subset=['Release Year', 'Price'])
    df['Price'] = df['Price'].replace('[^0-9.]', '', regex=True).astype(float)
    
    # Print the number of rows after cleaning
    print(f"Number of rows after cleaning NaNs: {df.shape[0]}")

    # Check if the dataframe is empty after cleaning
    if df.empty:
        raise ValueError("Error: The dataset is empty after cleaning. Please check the CSV file content.")

    # Define the critical date
    critical_date = pd.to_datetime("2019-05-16")
    df['After'] = (df['Release Year'] >= critical_date).astype(int)

    # Create time variable and interaction term
    df['Time'] = (df['Release Year'] - df['Release Year'].min()).dt.days
    df['Interaction'] = df['Time'] * df['After']
    
    # Print the final number of elements in the dataset
    print(f"Final number of elements in dataset: {df.shape[0]}")
    print("Cleaned data preview:")
    print(df.head())

    # Function to compute the robustness index using bootstrap resampling
    def compute_robustness_index(df, iterations=100):
        beta3_values = []
        for _ in range(iterations):
            sample_df = df.sample(frac=0.8, replace=True)  # Bootstrap resampling
            X = add_constant(sample_df[['Time', 'After', 'Interaction']].astype(float))
            y = sample_df['Price']
            model = OLS(y, X).fit()
            beta3_values.append(model.params['Interaction'])
        beta3_values = np.array(beta3_values)
        robustness_index = 1 - (np.std(beta3_values) / np.mean(np.abs(beta3_values)))
        return robustness_index
    
    # Fit the ITSA model without additional transformations
    X = add_constant(df[['Time', 'After', 'Interaction']].astype(float))
    y = df['Price']
    itsa_model = OLS(y, X).fit()

    # Compute robustness index
    robustness_score = compute_robustness_index(df)

    # Print the detailed model summary
    print(itsa_model.summary())
    
    # Extract required coefficients and statistics
    beta1 = itsa_model.params['Time']
    beta3 = itsa_model.params['Interaction']
    p_value_beta1 = itsa_model.pvalues['Time']
    p_value_beta3 = itsa_model.pvalues['Interaction']
    r_squared = itsa_model.rsquared
    
    print("\nModel coefficients:")
    print(f"Beta1 (pre-intervention slope): {beta1}, p-value: {p_value_beta1}")
    print(f"Beta3 (post-intervention slope change): {beta3}, p-value: {p_value_beta3}")
    print(f"Model R-squared: {r_squared}")
    print(f"Robustness Index: {robustness_score}")
    
    # Interpret the significance test
    alpha = 0.05  # Significance level
    if p_value_beta1 < alpha:
        print("Beta1 coefficient is significant.")
    else:
        print("Beta1 coefficient is NOT significant.")
    
    if p_value_beta3 < alpha:
        print("Beta3 coefficient is significant.")
    else:
        print("Beta3 coefficient is NOT significant.")
