import streamlit as st
from util import Util
from Service.partner import Partner

class Region:    
    def page():
        st.title('Região')    
        region = ''
        region = st.text_input('Digite uma região:', '')
        if(region):
            liquidity= round(Partner.get_region_liquidity(region)*100, 3)            
            st.markdown('A liquidez da região {} é de **{}**%.'.format(region, liquidity))
            Util.get_map("Região {}".format(region), 12)
