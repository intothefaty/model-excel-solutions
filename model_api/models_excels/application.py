# -*- coding: utf-8 -*-
import models_excels.app1_predict
import models_excels.app2_errors
import models_excels.app3_selection
import models_excels.app4_fendformat


def run_all(df):
    models_excels.app1_predict.app1(df)
    errors = models_excels.app2_errors.app2(df)
    df = models_excels.app3_selection.pred_error_df(errors)
    df = models_excels.app4_fendformat.app4(df)
    return df
