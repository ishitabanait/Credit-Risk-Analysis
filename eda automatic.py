# C:/Users/91942/Desktop/loan/loan_clean.csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def automated_EDA(file_path):
    # Load the data
    data = pd.read_csv(file_path)

    # Display data shape
    print("Data Shape :\n", data.shape)

    # Display data head
    print("\n------------------------\nData head :\n", data.head())

    # Display data info
    print("\n------------------------\ndata info :\n", data.info())

    # Display data description
    print("\n------------------------\ndata describtion :\n", data.describe())

    # Handling missing data
    numerical_data = data.select_dtypes(include=['float64', 'int64']).columns
    categorical_data = data.select_dtypes(include=['object']).columns

    # Handling missing numerical data by filling with mean
    for feature in numerical_data:
        data[feature].fillna(data[feature].mean(), inplace=True)

    # Handling missing categorical data by filling with mode
    for feature in categorical_data:
        mode_value = data[feature].mode()[0]
        data[feature].fillna(mode_value, inplace=True)

    print("\n------------------------")
    print("MISSING DATA AFTER IMPUTATION\n")
    print("MISSING NUMERICAL DATA COUNT", data[numerical_data].isnull().sum().sum())
    print("MISSING CATEGORICAL DATA COUNT", data[categorical_data].isnull().sum().sum())

    # Correlation matrix for numeric columns
    '''corr = data[numerical_data].corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()'''

    # Distribution plots for numeric columns
    '''for feature in numerical_data:
        plt.figure(figsize=(8, 6))
        sns.histplot(data=data, x=feature, kde=True)
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.show()'''

    # Value counts and bar plots for categorical columns
    '''for feature in categorical_data:
        plt.figure(figsize=(8, 6))
        sns.countplot(data=data, x=feature, order=data[feature].value_counts().index)
        plt.title(f'Count of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.show()'''

    # Boxplots for numerical columns against categorical columns
    '''for feature in numerical_data:
        if len(data[feature].unique()) > 5:  # Only plot boxplot if more than 5 unique values
            plt.figure(figsize=(8, 6))
            sns.boxplot(data=data, x='loan_status', y=feature)
            plt.title(f'{feature} by Loan Status')
            plt.xlabel('Loan Status')
            plt.ylabel(feature)
            plt.xticks(rotation=45)
            plt.show()'''

    # Pairplot for pairwise relationships between numerical columns
    plt.figure(figsize=(12, 10))
    sns.pairplot(data[numerical_data], diag_kind='kde')
    plt.title('Pairwise Relationships between Numerical Columns')
    plt.show()

# Example usage
automated_EDA("C:/Users/91942/Desktop/loan/loan_clean.csv")