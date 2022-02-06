import streamlit as st
from util import Util
from Service.partner import Partner
import numpy as np
import pandas as pd

class Street:    
    def page():
        st.title('Rua')    
        street = ''
        street = st.text_input('Digite uma rua de Belo Horizonte:', '')
        if(street):
            month = st.select_slider("Escolha a quantidade de meses:", options= [0, 1,2,3,4,5,6,7,8,9,10,11,12], value=0)
            if(month > 0):
                liquidity= round(Partner.get_street_liquidity(street, month)*100, 3)            
                st.markdown('A liquidez da {} é de **{}%** no período de **{} {}**.'.format(street, liquidity, month, Util.format_month(month)))
                Util.get_map(street)

    def page_all():
        st.title('Ruas de Belo Horizonte')
        month = st.select_slider("Escolha a quantidade de meses:", options= [0,1,2,3,4,5,6,7,8,9,10,11,12], value=0)
        if(month > 0):
            liquidities= Partner.get_all_street_liquidity(month)
            matrix = np.array([[0, 0]])
            list_name = []
            list_liq = []            
            for liquidity in liquidities:
                liq = round(float(liquidity[1])*100,3)
                row_to_be_added = np.array([liquidity[0].replace("-", " "), '{}%'.format(liq)])                
                list_name.insert(0,liquidity[0])
                list_liq.insert(0, liq)
                matrix = np.vstack ((matrix, row_to_be_added))                
            matrix_ok = np.delete(matrix, 0, 0)        

            #Table
            table = pd.DataFrame(
                matrix_ok,            
                columns=('Ruas', 'Liquidez'))
            st.dataframe(table)

            #Graphic
            graphic = pd.DataFrame({
            'date': list_name,
            'second column': list_liq
            })
            graphic = graphic.rename(columns={'date':'index'}).set_index('index')
            st.line_chart(graphic)