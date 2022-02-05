import streamlit as st
from util import Util
from Service.partner import Partner
import numpy as np
import pandas as pd

class Street:    
    def page():
        st.title('Rua')    
        street = ''
        street = st.text_input('Digite uma rua:', '')
        if(street):
            liquidity= round(Partner.get_street_liquidity(street)*100, 3)            
            st.markdown('A liquidez da rua {} é de **{}**%.'.format(street, liquidity))
            Util.get_map(street)

    def page_all():
        st.title('Todas as ruas')
        liquidities= Partner.get_all_street_liquidity()
        matrix = np.array([[0, 0]])
        for liquidity in liquidities:
            liq = round(float(liquidity[1])*100,3)
            row_to_be_added = np.array([liquidity[0].replace("-", " "), '{}%'.format(liq)])
            matrix = np.vstack ((matrix, row_to_be_added))
        matrix_ok = np.delete(matrix, 0, 0)        
        df = pd.DataFrame(
            matrix_ok,            
            columns=('Ruas', 'Liquidez'))

        st.dataframe(df)
