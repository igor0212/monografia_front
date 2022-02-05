import streamlit as st
from util import Util

class Street:    
    def page():
        st.title('Rua')        
        Util.get_map('Avenida dos engenheiros')
