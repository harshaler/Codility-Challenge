# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 22:29:33 2021

@author: harshal erande
"""

import pandas as pd
from math import sqrt


# you can use this table as an example
df  = pd.DataFrame({
    'X': [0, 0, 1, 1],
    'Y': [1, 2, 1, 2],
    'pr': [0.3, 0.25, 0.15, 0.3]
})


class CheckIndependence:

    def __init__(self):
        self.version = 1


    def check_independence(self, df: pd.DataFrame):
        
        dfX = df.groupby('X').sum()
        dfY = df.groupby('Y').sum()


        df['PX']=df.X.map(dfX.pr)

        df['PY']=df.Y.map(dfY.pr)


        values = (df.PX * df.PY)==df.pr
        c = values.sum() - values.count()

        df['values']=values.astype(int)
       
        if (c==0):
            independent = True
        else:
            independent = False
            
        
        df_meanx = df[['X','PX']].drop_duplicates()
        df_meanx['sdx'] = (df_meanx.X-  (df_meanx.X*df_meanx.PX).sum())**2*df_meanx.PX
        df['meanx'] = (df_meanx.X*df_meanx.PX).sum()
       
        df_meany = df[['Y','PY']].drop_duplicates()
        df_meany['sdy'] = (df_meany.Y-  (df_meany.Y*df_meany.PY).sum())**2*df_meany.PY
        df['meany'] = (df_meany.Y*df_meany.PY).sum()
 

        values =(df.X-df.meanx)*(df.Y-df.meany)*df.pr
        cov = values.sum()

        #print(df_meanx)
        
        corr = cov/(df_meanx.sdx.sum()*df_meany.sdy.sum())
            
        return {'independent':independent, 'covariance':cov, 'correlation':corr}
    
a = CheckIndependence()
res = a.check_independence(df)
print(res)