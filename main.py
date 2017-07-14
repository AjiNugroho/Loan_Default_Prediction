# -*- coding: utf-8 -*-
"""
Created on 7/13/17
Author: Jihoon Kim
"""

# import modules
import pandas as pd

from trim_data import drop_null_columns, split_loan_in_progress, categorize_target

# load data
loan = pd.read_csv('./data/loan.csv')

# preprocess data
drop_null_columns(loan)
loan_in_progress = split_loan_in_progress(loan)
loan = categorize_target(loan)



