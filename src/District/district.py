import streamlit as st
from util import Util

class District:    
    def page():
        st.title('Bairro')      
        district = ''
        district = st.text_input('Digite um bairro:', '')
        if(district):
            Util.get_map(district)  