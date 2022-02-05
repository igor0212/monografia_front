import streamlit as st
from util import Util

class Region:    
    def page():
        st.title('Região')        
        Util.get_map('Pampulha')
