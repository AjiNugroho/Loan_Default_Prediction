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
    loan_in_progress = data[progress_bool]
    data.drop(list(loan_in_progress.index), axis=0, inplace=True)
    return loan_in_progress
