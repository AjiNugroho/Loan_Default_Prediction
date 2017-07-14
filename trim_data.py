# -*- coding: utf-8 -*-
"""
Created on 7/14/17
Author: Jihoon Kim
"""

import feature_index


def drop_null_columns(data):
    """Drop columns (most of values are null)"""
    data.drop(feature_index.null_cols, axis=1, inplace=True)
    return None


def split_loan_in_progress(data):
    """Return table of loan in progress. It drops the loan in progress from loan data internally."""
    progress_bool = data.loan_status.isin(feature_index.in_progress_index)
    loan_in_progress = data[progress_bool].drop('loan_status', axis=1)
    data.drop(list(loan_in_progress.index), axis=0, inplace=True)
    return loan_in_progress


def categorize_target(data):
    """Returns encoded loan status: Safe, Warning and Bad"""

    def func(x):
        if x['loan_status'] in feature_index.bad_index:
            return 0
        elif x['loan_status'] in feature_index.warning_index:
            return 1
        else:
            return 2

    data['loan_status_coded'] = data.apply(func, axis=1)
    data.drop('loan_status', axis=1, inplace=True)
    return data


def ext_num_from_sub_grade(data):
    data['sub_grade'] = data['sub_grade'].map(lambda x: int(x.lstrip('ABCDEFG')))
    return data
