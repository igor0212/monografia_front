import streamlit as st
from util import Util
from Service.partner import Partner
import pandas as pd
import numpy as np

class District:    
    def page():
        st.title('Bairro')      
        district = ''
        district = st.text_input('Digite um bairro de Belo Horizonte:', '')        
        if(district):
            month = st.select_slider("Escolha a quantidade de meses:", options= [0, 1,2,3,4,5,6,7,8,9,10,11,12], value=0)
            if(month > 0):
                liquidity= round(Partner.get_district_liquidity(district, month)*100, 3)
                st.markdown('A liquidez do bairro {} é de **{}%** no período de **{} {}**.'.format(district, liquidity, month, Util.format_month(month)))
                Util.get_map(district)  

    def page_all():
        st.title('Bairros de Belo Horizonte')
        month = st.select_slider("Escolha a quantidade de meses:", options= [0, 1,2,3,4,5,6,7,8,9,10,11,12], value=0)
        if(month > 0):
            liquidities= Partner.get_all_district_liquidity(month)
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
                columns=('Bairro', 'Liquidez'))
            st.dataframe(table)

            #Graphic
            graphic = pd.DataFrame({
            'date': list_name,
            'second column': list_liq
            })
            graphic = graphic.rename(columns={'date':'index'}).set_index('index')
            st.line_chart(graphic)