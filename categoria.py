import streamlit as st  # Biblioteca para criar a interface web
import pandas as pd  # Biblioteca para leitura e manipulação de dados
import json  # Biblioteca para trabalhar com arquivos JSON

# Importa o vetorizador que transforma textos em valores numéricos
from sklearn.feature_extraction.text import TfidfVectorizer

# Importa o algoritmo de classificação supervisionada
from sklearn.linear_model import LogisticRegression

# Importa o Pipeline para organizar as etapas do modelo
from sklearn.pipeline import Pipeline


#1. CONFIGURAÇÃO DO STREAMLIT (página web)

st.set_page_config(
    page_title="Chatbot Operadora Cartão",  # Título da aba
    page_icon="💳",                         # Ícone da aba
    layout="centered"                       # Centraliza o conteúdo
)

# Exibe o título principal da aplicação
st.title("🤖 Chatbot Atendimento - Operadora de Cartão")


#para testar vá até o terminal e digite: python streamlit run app.py
