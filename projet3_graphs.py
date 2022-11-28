import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import requests


st.title('Analyse du réseau de transports en commun de la ville de Rennes')
st.image('Bus-100x100.png')
df_bus = pd.read_csv("df_bus_retards.csv")

# Quasiment tous les éléments streamlit peuvent être affichés dans la "sidebar"
st.sidebar.image('logo_star.png')
st.sidebar.title("Réseau Star :")
st.sidebar.write("  2 lignes de métro")
st.sidebar.write("  Ligne a - lancement Mars 2022")
st.sidebar.write("  Ligne b – lancement Juillet 2022")
st.sidebar.write("  Lignes de bus : 152")
st.sidebar.write("  Stations de vélo en libre service : 57")
st.sidebar.write("  Parcs relais : 8")

option_ligne = df_bus['ligne'].unique()
lignes = st.sidebar.multiselect(
	'Quelle ligne ?',
	option_ligne, 
	option_ligne[0]
	)
# Table 
df_bus_ligne = df_bus[df_bus['ligne'].isin(lignes)]
st.write('trajet ligne')
df_bus_ligne

option_ligne_2 = df_bus['retard_a'].unique()
lignes_2 = st.sidebar.selectbox(
	'retards ?',
	option_ligne_2, 
	option_ligne_2[0]
	)
# Table 
df_bus_ligne_2 = df_bus[df_bus['retard_a'].isin(lignes_2)]
st.write('Retards supérieurs à 5 minutes')
st.map(df_bus_ligne_2[['latitude','longitude']])


