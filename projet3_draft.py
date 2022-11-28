import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import requests


st.title('Analyse du réseau de transports en commun de la ville de Rennes')
st.write("Lignes de bus")
st.image('https://github.com/NathGui404/Projet3/blob/main/Bus-100x100.png')
df_bus = pd.read_csv("df_bus.csv")

# Quasiment tous les éléments streamlit peuvent être affichés dans la "sidebar"
st.sidebar.title("Réseau Star Key Facts")
st.sidebar.write("2 lignes de métro")
st.sidebar.write("Ligne a - lancement Mars 2022")
st.sidebar.write("Ligne b – lancement Juillet 2022")
st.sidebar.write("Lignes de bus : 152")
st.sidebar.write("Stations de vélo en libre service : 57")
st.sidebar.write("Parcs relais : 8")


st.sidebar.write('Quelle ligne ?')
option_ligne = df_bus['ligne'].unique()
lignes = st.sidebar.multiselect(
	"Choix des lignes", 
	option_ligne, 
	option_ligne[0]
	)

# Table 
df_bus_ligne = df_bus[df_bus['ligne'].isin(lignes)]
st.write('Caractéristiques ligne')
df_bus_ligne





