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
        list_name = []
        list_liq = []
        for liquidity in liquidities:
            liq = round(float(liquidity[1])*100,3)
            row_to_be_added = np.array([liquidity[0], '{}%'.format(liq)])    
            list_name.insert(0,liquidity[0])
            list_liq.insert(0, liq)            
            matrix = np.vstack ((matrix, row_to_be_added))
        matrix_ok = np.delete(matrix, 0, 0)        

        #Table
        table = pd.DataFrame(
            matrix_ok,            
            columns=('Região', 'Liquidez'))
        st.dataframe(table) 

        #Graphic
        graphic = pd.DataFrame({
        'date': list_name,
        'second column': list_liq
        })
        graphic = graphic.rename(columns={'date':'index'}).set_index('index')
        st.line_chart(graphic)