import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import requests

#fonction de chargement des données
def load_data():
	bus_data_path = 'df_bus_retards.csv'
	data = pd.read_csv(bus_data_path)
	return data
#fonction de conversion des secondes en heure min secondes
def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hour, min, sec)

df_bus=load_data()

# La sidebar marche. Résumé du réseau et image du réseau

st.sidebar.image('logo_star.png', width=200)

with st.sidebar :
	with st.expander("Réseau Star :"):
		st.write("lignes de métro : 2")
		st.write("Lignes de bus : 152")
		st.write("Stations de vélo en libre service : 57")
		st.write("Parcs relais : 8")		
		st.image("reseau rennes.JPG")
		
option_ligne = 'df_bus['ligne'].unique()
option_ligne.append('All')
lignes = st.sidebar.selectbox(
    'Selectionnez une ligne',
	str(option_ligne),
	)

st.title('Analyse du réseau de transports en commun de la ville de Rennes')
st.image('Bus-100x100.png')
st.subheader("Retards de bus les plus importants par ligne et arrêt")

if option_ligne!='All':
	df_bus_ligne = df_bus[df_bus['ligne']==ligne]
	df_bus_ligne=df_bus_ligne[df_bus_ligne['retard_a']=='oui'][['ligne','destination','nom_arret','arrivee_theorique','retard_arrivee']].sort_values(by='retard_arrivee',ascending=False)
	st.write(df_bus_ligne)
else:
	df_bus=[df_bus['retard_a']=='oui'][['ligne','destination','nom_arret','arrivee_theorique','retard_arrivee']].sort_values(by='retard_arrivee',ascending=False)
	st.write(df_bus)


# Table de toutes les lignes de bus et du retard a chaque arret

option_tard = df_bus['retard_a'].unique()
tard = st.sidebar.multiselect(
	'retards ?',
	option_tard
	)
# Table 
df_bus_tard = df_bus[df_bus['retard_a'].isin(tard)]
st.write('Retards supérieurs à 5 minutes')
st.map(df_bus_tard[['latitude','longitude']])
