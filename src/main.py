import streamlit as st
from Service.district import District
from Service.street import Street
from Service.region import Region

st.sidebar.title('Visualizar liquidez')
paginaSelecionada = st.sidebar.selectbox('Selecione o modo a ser visualizado a liquidez', ['Rua', 'Bairro', 'Região'])

if(paginaSelecionada == 'Rua'):
    Street.page()
elif(paginaSelecionada == 'Bairro'):
    District.page()
elif(paginaSelecionada == 'Região'):
    Region.page()
    






