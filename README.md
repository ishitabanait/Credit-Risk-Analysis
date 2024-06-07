# Credit Risk Analysis

## Introduction

Credit risk represents the potential for financial loss when borrowers fail to meet their debt obligations. It is a critical consideration for lenders, encompassing both borrower-specific factors and broader economic conditions. Credit risk is typically assessed and quantified using credit ratings provided by agencies such as FICO, S&P Global, Moody’s, and Fitch Ratings. These ratings help determine the likelihood of default and the associated financial risks.

## Key Components of Credit Risk

1. **Expected Losses**: These are the losses that can be reasonably forecasted based on historical data and statistical models. They include:

   - **Expected Credit Loss (ECL)**: This is the anticipated amount that a lender might lose when lending to a borrower. It is calculated using the formula:

     $ \text{ECL} = \text{PD} \times \text{LGD} \times \text{EAD} $

     where:
     - **PD (Probability of Default)**: The likelihood that a borrower will default on their debt.
     - **LGD (Loss Given Default)**: The proportion of the total exposure that cannot be recovered once a default occurs.
     - **EAD (Exposure at Default)**: The total value that a lender is exposed to at the time of default.

2. **Unexpected Losses**: These losses arise from adverse economic conditions that are not predictable based on historical data.

3. **Exceptional (Stress) Losses**: These losses occur due to severe economic downturns and are generally considered extreme but plausible scenarios.

## Regulatory Framework and Capital Requirements

Banks are required to maintain sufficient capital to cover potential loan defaults, ensuring financial stability and solvency. The balance sheet of a bank must include risk-weighted assets and liabilities plus capital to meet regulatory capital requirements.

### Basel II Accord

The Basel II Accord provides a comprehensive framework for determining the capital requirements of banks. It consists of three pillars:

1. **Minimum Capital Requirements**: Specifies how much capital a bank needs to hold based on its risk-weighted assets.
2. **Supervisory Review**: Ensures that banks have sound internal processes in place to assess and manage their risks.
3. **Market Discipline**: Promotes transparency and requires banks to disclose their risk exposures and capital adequacy.

### Risk Weights and Credit Ratings

Credit ratings significantly influence the amount of capital that needs to be held against different types of exposures. Sovereign debts, for instance, are weighted according to the credit rating of the country, as provided by agencies like S&P Global. The risk-weight percentages vary depending on the type of borrower and the nature of the facility:

- **Retail Exposure**: 75% of each exposure.
- **Mortgage Exposure**: 35% of each exposure.

### Approaches to Risk Weighting

Banks can adopt different approaches to calculate the risk weights for their exposures:

- **Standardized Approach (SA)**: Utilizes external credit ratings to determine risk weights.
- **Foundation Internal Ratings-Based (F-IRB) Approach**: Banks estimate PD, while other components like LGD and EAD are provided by regulators.
- **Advanced Internal Ratings-Based (A-IRB) Approach**: Banks estimate PD, LGD, and EAD, providing greater flexibility and precision.

### Advantages of IRB Approaches

The IRB approaches, especially the Advanced IRB, offer several advantages, including better risk sensitivity and the ability to use internal models to more accurately assess risk components. This allows banks to hold capital that more closely aligns with their actual risk profiles, leading to more efficient capital allocation and enhanced risk management.

In summary, credit risk analysis is a multifaceted process involving the assessment of potential losses from borrowers' defaults, adherence to regulatory requirements, and the strategic management of capital. By leveraging both external credit ratings and internal risk models, banks can more effectively mitigate credit risk and ensure financial stability.

---

## PD Model

In this PD model, we follow a structured approach to estimate the Probability of Default (PD) using logistic regression and other statistical techniques. Below is a detailed explanation of each step involved in this process:

### 1. Data Preparation

- **Pre-processed Test and Target Data**: We start with pre-processed datasets for training (train dataset) and testing (test dataset). The target data (dependent variable) indicates whether a borrower has defaulted or not.

### 2. Model Training

- **Logistic Regression**: Applied to the train dataset to model the relationship between the independent variables (features) and the probability of default.
- **Statistical Significance**: We study the p-values of the variables to determine which ones are statistically significant. Variables with p-values below a certain threshold (e.g., 0.05) are considered significant and included in the final model.

### 3. Feature Selection and Model Testing

- **Feature Selection**: Based on the p-values, we select the significant features and use them to build the final logistic regression model.
- **Model Evaluation**: To evaluate the model's performance, we use metrics such as confusion matrix, AUROC (Area Under Receiver Operating Characteristic curve), Gini index, and KS (Kolmogorov-Smirnov) score.

  - **Confusion Matrix**: Shows the true positives, true negatives, false positives, and false negatives, helping us understand the model's accuracy.
  - **AUROC Score**: Measures the model's ability to distinguish between default and non-default cases. A higher AUROC indicates better model performance.
  - **Gini Index**: Derived from the AUROC and provides a measure of model discriminatory power.
  - **KS Score**: Measures the maximum difference between the cumulative distributions of the default and non-default cases, indicating the model's effectiveness in distinguishing between the two groups.

### 4. PD Calculation and Scorecard Creation

- **PD Calculation**: Using the final logistic regression model, we calculate the PD for individual accounts.
- **Scorecard Creation**: A scorecard is created to assign a credit score to each account based on the calculated PD. This scorecard helps in translating the model outputs into a more interpretable format for credit risk assessment.
  - **Credit Score Range**: We set the credit score range from 300 to 850. This range is chosen to align with common credit scoring systems, making it easier to understand and compare.

### 5. Cutoffs and PD Records

- **Setting Cutoffs**: We define cutoffs for different PD levels, such as 10% and 5%. These cutoffs help in categorizing accounts based on their risk levels.
- **Reviewing Records**: Records are reviewed to identify accounts with PD at or above these cutoffs, helping in risk segmentation and targeted interventions.

### 6. Saving Model and Data

- **Saving Scorecard Data**: The scorecard data is saved as a CSV file for further analysis and reporting.
- **Model Preservation**: The trained logistic regression model is saved using the pickle module. This allows the model to be reused for future calculations, such as estimating the Expected Loss (EL).

### 7. Future Use

- **Expected Loss Calculation**: The saved model will be used to calculate the EL, which combines the PD with Loss Given Default (LGD) and Exposure at Default (EAD) to estimate potential losses.

---

### LGD Model

LGD, or Loss Given Default, represents the proportion of a loan that is not recovered in the event of default. This model aims to estimate the recovery rate, calculated as the ratio of actual recoveries to the funded amount.

To develop the LGD model, a two-stage approach is employed:

1. **Stage 1 - Logistic Regression on Recovery Rate**: A logistic regression model is applied to the recovery rate to classify loans into two groups: those with a recovery rate greater than zero and those with zero recovery rate.
2. **Stage 2 - Linear Regression on Positive Recovery Rates**: For loans with a recovery rate greater than zero, a linear regression model is utilized to estimate the recovery rate.

The results from both stages are combined using the pickle module for efficient storage and retrieval.

### EAD Model

EAD, or Exposure at Default, measures the potential exposure a bank faces when a borrower defaults. It is calculated as the proportion of the funded amount that remains outstanding at default.

The EAD model adopts a straightforward approach:

- **Linear Regression on Credit Conversion Factor (CCF)**: The CCF, calculated as the ratio of outstanding principal to the funded amount, is estimated using a linear regression model.

### Model Integration

After validating each stage of the LGD model, including the logistic regression and subsequent linear regression, and developing the EAD model, they are integrated into the credit risk assessment process. The PD (Probability of Default) model is imported using the pickle module, and all three models—PD, LGD, and EAD—are utilized to calculate the Expected Loss (EL) for each loan category.

The EL is determined by multiplying the probabilities of default, the estimated recovery rates, and the exposure at default. Finally, the overall Expected Loss of the bank is computed, providing valuable insights into potential credit risks and informing strategic decision-making processes.

---

## Conclusion

Our comprehensive analysis of the Probability of Default (PD) model, Loss Given Default (LGD) model, and Exposure at Default (EAD) model yields valuable insights into credit risk assessment and mitigation strategies:

- **PD Model Evaluation**: The PD model effectively predicts the probability of default for each loan record, achieving an accuracy of 86.17%. Although the AUROC score and Gini index suggest moderate discriminatory power, the KS statistic indicates minimal separation between default and non-default

 cases. The creation of scorecards with scores ranging from 300 to 850 for individual loan records provides a practical tool for credit risk assessment.

- **LGD Model Analysis**: The LGD model shows promising results. The Stage-1 logistic model achieves an accuracy of 74.16%, while the Stage-2 linear model indicates a normal distribution of recovery rates, suggesting a robust and reliable model.

- **EAD Model Assessment**: The EAD model, utilizing a linear regression approach, demonstrates a predominantly normal distribution in credit conversion factors (CCFs), reinforcing its reliability and accuracy.

Considering these findings, we observe an Expected Loss (EL) of 9.0%, which is within the acceptable range of less than 10%. This aligns with industry standards, as banks typically hold 10% of their assets as capital. The observed EL falls within the range of 2% to 10%, indicating a prudent risk management approach.

### Future Work

Future work could involve:
- Refining the models by incorporating additional features or enhancing existing algorithms to improve predictive accuracy.
- Exploring alternative modeling techniques to address observed limitations and boost model performance.
- Continuously monitoring and updating the models to adapt to changing market conditions and evolving regulatory requirements.

By continually refining and enhancing our credit risk models, banks can manage their portfolios more effectively and minimize potential losses, ensuring financial stability and resilience amidst dynamic economic environments.

---

## Repository Contents

- **Data Preparation**: Scripts and notebooks for data cleaning and preprocessing.
- **Model Training**: Code for training the PD, LGD, and EAD models.
- **Model Evaluation**: Tools and metrics used for assessing model performance.
- **Scorecard Creation**: Scripts for generating credit scorecards based on the PD model.
- **Model Saving and Loading**: Code for saving models using the pickle module and loading them for future use.
- **Expected Loss Calculation**: Scripts for integrating PD, LGD, and EAD models to calculate Expected Loss.

---

For detailed documentation and code, please refer to the individual files and folders in the repository.

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and improvements are always welcome!

---

© [2024] [Ishita Banait]. All rights reserved.

---

This README file provides a comprehensive overview of the project, ensuring clarity and understanding for anyone interested in the details of credit risk analysis and the methodologies employed.
