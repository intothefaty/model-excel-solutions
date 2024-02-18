# -*- coding: utf-8 -*-

import models.croston as cr
import models.des as des
import models.sma as sma
import models.ses as ses
import models.winterholt as wh
import models.tsb as tsb
#import models.regression as reg


cr_pred_df = cr.take_croston_pred()
des_pred_df = des.take_des_pred()
ses_pred_df = ses.take_ses_pred()
sma_pred_df = sma.take_sma_pred()
wh_pred_df = wh.take_wh_pred()
tsb_pred_df = tsb.take_tsb_pred()
#reg_pred_df = reg.take_reg_pred()


cr_pred_df.to_excel('pred_excels/cr_pred.xlsx', index=False)
des_pred_df.to_excel('pred_excels/des_pred.xlsx', index=False)
ses_pred_df.to_excel('pred_excels/ses_pred.xlsx', index=False)
sma_pred_df.to_excel('pred_excels/sma_pred.xlsx', index=False)
wh_pred_df.to_excel('pred_excels/wh_pred.xlsx', index=False)
tsb_pred_df.to_excel('pred_excels/tsb_pred.xlsx', index=False)
#reg_pred_df.to_excel('pred_excels/reg_pred.xlsx', index=False)



