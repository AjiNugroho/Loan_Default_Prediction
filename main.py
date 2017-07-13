# -*- coding: utf-8 -*-
"""
Created on 7/13/17
Author: Jihoon Kim
"""

import pandas as pd

loan = pd.read_csv('./data/loan.csv')
lending = pd.read_csv('./data/lending_club_data.csv')

lending[lending.bad_loans==1].loan_status.value_counts()


bad_index = ['Charged Off',
             'Does not meet the credit policy. Status:Charged Off',
             'Default']

lending_bad = ['Charged Off',
               'Does not meet the credit policy.  Status:Charged Off',
               'Default']

lending.loan_status.value_counts()
lending[lending.loan_status.isin(lending_bad)].loan_status.value_counts()
loan.loan_status.value_counts()
loan[loan.loan_status.isin(bad_index)].loan_status.value_counts()
