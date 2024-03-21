# -*- coding: utf-8 -*-

import models_excels.models.croston as cr
import models_excels.models.des as des
import models_excels.models.sma as sma
import models_excels.models.ses as ses
import models_excels.models.winterholt as wh
import models_excels.models.tsb as tsb


# import models.regression as reg

def app1(df):
    cr_pred_df = cr.take_croston_pred(df)
    des_pred_df = des.take_des_pred(df)
    ses_pred_df = ses.take_ses_pred(df)
    sma_pred_df = sma.take_sma_pred(df)
    wh_pred_df = wh.take_wh_pred(df)
    tsb_pred_df = tsb.take_tsb_pred(df)
    # reg_pred_df = reg.take_reg_pred()

    cr_pred_df.to_excel('models_excels/pred_excels/cr_pred.xlsx', index=False)
    des_pred_df.to_excel('models_excels/pred_excels/des_pred.xlsx', index=False)
    ses_pred_df.to_excel('models_excels/pred_excels/ses_pred.xlsx', index=False)
    sma_pred_df.to_excel('models_excels/pred_excels/sma_pred.xlsx', index=False)
    wh_pred_df.to_excel('models_excels/pred_excels/wh_pred.xlsx', index=False)
    tsb_pred_df.to_excel('models_excels/pred_excels/tsb_pred.xlsx', index=False)
    # reg_pred_df.to_excel('pred_excels/reg_pred.xlsx', index=False)
