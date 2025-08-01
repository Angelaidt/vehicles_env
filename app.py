import pandas as pd
import plotly.express as px
import streamlit as st

# Criando um cabeçalho para o aplicativo
st.header("Análise de Frota")
st.write("Monitore o estoque de veículos. Analise a distribuição de modelos e condições  \
para otimizar as vendas e o mix de produtos.")

car_data = pd.read_csv('vehicles_us.csv')  # lendo os dados
hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar dispersão')  # criar um botão

if scatter_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de '
        'vendas de carros')

    # criar um grafico de dispersão
    # criar um gráfico de dispersão
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
