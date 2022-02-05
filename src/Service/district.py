import streamlit as st
from util import Util
from Service.partner import Partner

class District:    
    def page():
        st.title('Bairro')      
        district = ''
        district = st.text_input('Digite um bairro:', '')        
        if(district):
            liquidity= round(Partner.get_district_liquidity(district)*100, 3)            
            st.markdown('A liquidez do bairro {} é de **{}**%.'.format(district, liquidity))
            Util.get_map(district)  