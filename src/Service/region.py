import streamlit as st
from util import Util
from Service.partner import Partner
import numpy as np
import pandas as pd

class Region:    
    def page():
        st.title('Região')    
        region = ''
        region = st.text_input('Digite uma região:', '')
        if(region):
            liquidity= round(Partner.get_region_liquidity(region)*100, 3)            
            st.markdown('A liquidez da região {} é de **{}**%.'.format(region, liquidity))
            Util.get_map("Região {}".format(region), 12)

    def page_all():
        st.title('Todas as regiões')
        liquidities= Partner.get_all_region_liquidity()
        matrix = np.array([[0, 0]])
        for liquidity in liquidities:
            liq = round(float(liquidity[1])*100,3)
            row_to_be_added = np.array([liquidity[0], '{}%'.format(liq)])
            matrix = np.vstack ((matrix, row_to_be_added))
        matrix_ok = np.delete(matrix, 0, 0)        
        df = pd.DataFrame(
            matrix_ok,            
            columns=('Região', 'Liquidez'))

        st.dataframe(df)
