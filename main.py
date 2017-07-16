# -*- coding: utf-8 -*-
"""
Created on 7/13/17
Author: Jihoon Kim
"""

# import modules
import pandas as pd
from feature_eng import trim_features
from trim_data import drop_null_columns, categorize_target, split_loan_in_progress
from one_hot_encoding import one_hot_encoder
import feature_index


# load data
loan = pd.read_csv('./data/loan.csv')

# pre-process data
drop_null_columns(loan)
loan_in_progress = split_loan_in_progress(loan)
loan = categorize_target(loan)

# Feature Engineering by EDA
trim_features(loan)

# one-hot encoding
loan = loan[feature_index.features]
loan_one_hot_encoded = one_hot_encoder(loan)