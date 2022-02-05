import streamlit as st
from util import Util

class Region:    
    def page():
        st.title('Região')    
        region = ''
        region = st.text_input('Digite uma região:', '')
        if(region):
            Util.get_map(region)
