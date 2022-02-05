import streamlit as st
from util import Util

class District:    
    def page():
        st.title('Bairro')        
        Util.get_map('Castelo')
