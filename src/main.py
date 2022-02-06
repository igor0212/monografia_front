import streamlit as st
from Service.district import District
from Service.street import Street
from Service.region import Region

st.sidebar.title('Visualizar liquidez')
paginaSelecionada = st.sidebar.selectbox('Selecione o modo a ser visualizado a liquidez', ['Rua', 'Lista das Ruas', 'Bairro', 'Lista dos Bairros', 'Região', 'Lista das Regiões'])

if(paginaSelecionada == 'Rua'):
    Street.page()
elif(paginaSelecionada == 'Lista das Ruas'):
    Street.page_all()
elif(paginaSelecionada == 'Bairro'):
    District.page()
elif(paginaSelecionada == 'Lista dos Bairros'):
    District.page_all()
elif(paginaSelecionada == 'Região'):
    Region.page()
elif(paginaSelecionada == 'Lista das Regiões'):
    Region.page_all()
    






