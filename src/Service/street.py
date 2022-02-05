import streamlit as st
from util import Util
from Service.partner import Partner

class Street:    
    def page():
        st.title('Rua')    
        street = ''
        street = st.text_input('Digite uma rua:', '')
        if(street):
            liquidity= round(Partner.get_street_liquidity(street)*100, 3)            
            st.markdown('A liquidez da rua {} é de **{}**%.'.format(street, liquidity))
            Util.get_map(street)
