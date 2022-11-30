import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import requests

@st.cache
st.title('Analyse du réseau de transports en commun de la ville de Rennes')
st.image('Bus-100x100.png')
df_bus = pd.read_csv("df_bus_retards.csv")

# Quasiment tous les éléments streamlit peuvent être affichés dans la "sidebar"

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
#conversion des secondes en heure min secondes
def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hour, min, sec)



# Table de toutes les lignes de bus et du retard a chaque arret

df_bus_ligne = df_bus[df_bus['ligne'].isin(lignes)]
st.subheader("Retards de bus les plus importants par ligne et arrêt")
df_bus_ligne=df_bus_ligne[df_bus_ligne['retard_a']=='oui'][['ligne','destination','nom_arret','arrivee_theorique','retard_arrivee']].sort_values(by='retard_arrivee',ascending=False)
df_bus['retard_arrivee']=df_bus['retard_arrivee'].apply(convert)
df_bus_ligne

option_tard = df_bus['retard_a'].unique()
tard = st.sidebar.multiselect(
	'retards ?',
	option_tard
	)
# Table 
df_bus_tard = df_bus[df_bus['retard_a'].isin(tard)]
st.write('Retards supérieurs à 5 minutes')
st.map(df_bus_tard[['latitude','longitude']])