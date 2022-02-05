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
        district = st.text_input('Digite um bairro:', '')        
        if(district):
            liquidity= round(Partner.get_district_liquidity(district)*100, 3)            
            st.markdown('A liquidez do bairro {} é de **{}**%.'.format(district, liquidity))
            Util.get_map(district)  

    def page_all():
        st.title('Todos os bairros')
        liquidities= Partner.get_all_district_liquidity()
        matrix = np.array([[0, 0]])
        for liquidity in liquidities:
            liq = round(float(liquidity[1])*100,3)
            row_to_be_added = np.array([liquidity[0], '{}%'.format(liq)])
            matrix = np.vstack ((matrix, row_to_be_added))
        matrix_ok = np.delete(matrix, 0, 0)        
        df = pd.DataFrame(
            matrix_ok,            
            columns=('Bairro', 'Liquidez'))

        st.dataframe(df)

    """def page_all():
        st.title('Todos os bairros')
        liquidities= Partner.get_all_district_liquidity()
        cont=0
        matrix = np.array([[0, 0]])
        for liquidity in liquidities:
            #if(cont == 20):
            #    break            
            loc = Util.get_location(liquidity[0])
            if(loc):
                row_to_be_added = np.array([loc.latitude, loc.longitude])
                matrix = np.vstack ((matrix, row_to_be_added))
            cont+=1

        matrix_ok = np.delete(matrix, 0, 0)
        location = Util.get_location2('Belo Horizonte')

        print(matrix_ok)

        df = pd.DataFrame(
        matrix_ok + [location.latitude, location.longitude],
        columns=['lat', 'lon'])        

        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=location.latitude,
                longitude=location.longitude,
                zoom=11,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    'HexagonLayer',
                    data=df,
                    get_position='[lon, lat]',
                    radius=200,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df,
                    get_position='[lon, lat]',
                    get_color='[200, 30, 0, 160]',
                    get_radius=200,
                ),
            ],
        ))"""


