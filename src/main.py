import streamlit as st
from District.district import District

st.sidebar.title('Visualizar liquidez')
paginaSelecionada = st.sidebar.selectbox('Selecione o modo a ser visualizado a liquidez', ['Rua', 'Bairro', 'Região'])

if(paginaSelecionada == 'Rua'):
    st.title('Rua')   

elif(paginaSelecionada == 'Bairro'):
    District.page()
    






