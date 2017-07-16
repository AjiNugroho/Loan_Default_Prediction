# -*- coding: utf-8 -*-
"""
Created on 7/16/17
Author: Jihoon Kim
"""
import feature_index
import pandas as pd


def one_hot_encoder(loan):
    print("====================[Data Types]====================")
    print(loan.dtypes)
    categorical_variables = feature_index.categorical
    loan_one_hot_encoded = pd.get_dummies(loan, columns=categorical_variables)
    return loan_one_hot_encoded
