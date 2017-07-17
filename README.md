# Loan Default Prediction

Author: Jihoon Kim

<img src="http://jihoon-kim.synology.me/wp-content/uploads/2017/07/LOAN.jpg">

## Objective
Objective of this project is modeling loan default prediction system by using `Lending Club` data.

## Data Description
These files contain complete loan data for all loans issued through the 2007-2015, including the current loan status (Current, Late, Fully Paid, etc.) and latest payment information. The file containing loan data through the "present" contains complete loan data for all loans issued through the previous completed calendar quarter. Additional features include credit scores, number of finance inquiries, address including zip codes, and state, and collections among others. The file is a matrix of about 890 thousand observations and 75 variables. A data dictionary is provided in a separate file.

## Environments
* Python 3.5
* tensorflow 1.2.1
* Keras 2.0
* scikit-learn 0.18.2
* pandas 0.20.2
* seaborn 0.7.1
* (Optional) imbalanced-learn 0.2.1 (for upsampling by SMOTE)
