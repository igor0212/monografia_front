import streamlit as st
from util import Util
from Service.partner import Partner
import pandas as pd
import numpy as np
#import pydeck as pdk

class District:    
    def page():
        st.title('Bairro')      
        district = ''
        district = st.text_input('Digite um bairro de Belo Horizonte:', '')        
        if(district):
            liquidity= round(Partner.get_district_liquidity(district)*100, 3)            
            st.markdown('A liquidez do bairro {} é de **{}**%.'.format(district, liquidity))
            Util.get_map(district)  

    def page_all():
        st.title('Todos os bairros de Belo Horizonte')
        liquidities= Partner.get_all_district_liquidity()
        matrix = np.array([[0, 0]])
        list_name = []
        list_liq = []
        cont = 0
        for liquidity in liquidities:
            liq = round(float(liquidity[1])*100,3)
            row_to_be_added = np.array([liquidity[0], '{}%'.format(liq)])
            if(cont < 20):
                list_name.insert(0,liquidity[0])
                list_liq.insert(0, liq)            
            matrix = np.vstack ((matrix, row_to_be_added))
            cont += 1
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