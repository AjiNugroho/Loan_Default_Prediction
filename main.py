# -*- coding: utf-8 -*-
"""
Created on 7/13/17
Author: Jihoon Kim
"""

# import modules
import pandas as pd

from trim_data import drop_null_columns, split_loan_in_progress, categorize_target, ext_num_from_sub_grade

# load data
loan = pd.read_csv('./data/loan.csv')

# pre-process data
drop_null_columns(loan)
loan_in_progress = split_loan_in_progress(loan)
loan = categorize_target(loan)
loan = ext_num_from_sub_grade(loan)




