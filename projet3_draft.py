import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import requests


st.title('Analyse du réseau de transports en commun de la ville de Rennes')
st.write("")

df = pd.read_csv("velib.csv")

# Quasiment tous les éléments streamlit peuvent être affichés dans la "sidebar"
st.sidebar.title("Réseau Star Key Facts")
st.sidebar.write("2 lignes de métro")
st.sidebar.write("Ligne a - lancement Mars 2022")
st.sidebar.write("Ligne b – lancement Juillet 2022")
st.sidebar.write("Lignes de bus : 152")
st.sidebar.write("Stations de vélo en libre service : 57")
st.sidebar.write("Parcs relais : 8")


option_velo = st.sidebar.selectbox(
	    'Quel type de vélo ?',
	    ('mechanical', 'ebike'))

# On peut créer plusieurs "colonnes" pour afficher des éléments côte à côte
# La liste qui suit contient 2 éléments, il y aura donc 2 colonnes
# La première colonne a un poids de "2", elle sera donc 2 fois plus large
col1, col2 = st.columns([2, 1])

# Les éléments à afficher dans chaque colonne :
with col1:
	fig, ax = plt.subplots()
	ax = sns.boxplot(df[option_velo])
	st.pyplot(fig)
with col2:
	fig, ax = plt.subplots()
	ax = sns.boxplot(df[option_velo])
	st.pyplot(fig)
