import streamlit as st
from util import Util

class Street:    
    def page():
        st.title('Rua')    
        street = ''
        street = st.text_input('Digite uma rua:', '')
        if(street):
            Util.get_map(street)
