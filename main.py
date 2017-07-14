# -*- coding: utf-8 -*-
"""
Created on 7/13/17
Author: Jihoon Kim
"""

# import modules
import pandas as pd
from trim_data import drop_null_columns
from trim_data import split_loan_in_progress
from trim_data import categorize_target
from trim_data import ext_num_from_sub_grade
from trim_data import drop_emp_title
from trim_data import fill_na_annual_inc


# load data
loan = pd.read_csv('./data/loan.csv')

# pre-process data
drop_null_columns(loan)
loan_in_progress = split_loan_in_progress(loan)
loan = categorize_target(loan)

# Feature Engineering by EDA
loan = ext_num_from_sub_grade(loan)
drop_emp_title(loan)
fill_na_annual_inc(loan)



