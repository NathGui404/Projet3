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
df_bus['retard_a']=df_bus['retard_arrivee'].apply(retard)
df_bus['retard_d']=df_bus['retard_depart'].apply(retard)

st.sidebar.image('logo_star.png', width=200)
with st.sidebar :
	with st.expander("Réseau Star :"):
		st.write("lignes de métro : 2")
		st.write("Lignes de bus : 152")
		st.write("Stations de vélo en libre service : 57")
		st.write("Parcs relais : 8")		
		st.image("reseau rennes.JPG")

option_ligne = df_bus['ligne'].unique()
lignes = st.sidebar.multiselect(
	'Quelle ligne ?',
	option_ligne, 
	option_ligne[0]
	)
# Table 
df_bus_ligne = df_bus[df_bus['ligne'].isin(lignes)]
st.write('Retards les plus importants')
df_bus_ligne=df_bus_ligne[df_bus_ligne['retard_a']=='oui'][['ligne','destination','nom_arret','arrivee_theorique','retard_arrivee']].sort_values(by='retard_arrivee',ascending=False)
df_bus_ligne

option_tard = df_bus['retard_a'].unique()
tard = st.sidebar.multiselect(
	'retards ?',
	option_tard, 
	option_tard[0]
	)
# Table 
df_bus_tard = df_bus[df_bus['retard_a'].isin(tard)]
st.write('Retards supérieurs à 3 minutes')
st.map(df_bus_tard[['latitude','longitude']])


