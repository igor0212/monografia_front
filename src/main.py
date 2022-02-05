import streamlit as st
from Service.district import District
from Service.street import Street
from Service.region import Region

st.sidebar.title('Visualizar liquidez')
paginaSelecionada = st.sidebar.selectbox('Selecione o modo a ser visualizado a liquidez', ['Rua', 'Todas as Ruas', 'Bairro', 'Todos os Bairros', 'Região', 'Todas as Regiões'])

if(paginaSelecionada == 'Rua'):
    Street.page()
elif(paginaSelecionada == 'Todas as Ruas'):
    Street.page_all()
elif(paginaSelecionada == 'Bairro'):
    District.page()
elif(paginaSelecionada == 'Todos os Bairros'):
    District.page_all()
elif(paginaSelecionada == 'Região'):
    Region.page()
elif(paginaSelecionada == 'Todas as Regiões'):
    Region.page_all()
    






