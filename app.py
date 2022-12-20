import numpy as np
import pandas as pd
import plotly.graph_objects as go
import geopandas as gpd
import streamlit as st
import matplotlib.pyplot as plt


departamentos = gpd.read_file('per_admbnda_adm2_ign_20200714.shp')
departamentos['ADM1_ES_MAYUS']= departamentos['ADM1_ES'].str.upper()
centro_vacunacion = pd.read_csv('TB_CENTRO_VACUNACION.csv',delimiter=",")
ubigeo = pd.read_csv('TB_UBIGEOS.csv',delimiter=",")
ubigeo_subset = ubigeo[["id_ubigeo", "departamento"]]
centro_vacunacion_all=pd.merge(centro_vacunacion,ubigeo_subset,on='id_ubigeo')
values = departamentos['ADM1_ES_MAYUS'].tolist()
set_departamentos=set(values)
lista_departamentos=list(set_departamentos)
lista_departamentos.sort()
st.markdown('**Centros de Vacunacion Covid por Departamento**')
departamento=st.selectbox('Selecciona el departamento:',lista_departamentos)

centro_vacunacion_filter = centro_vacunacion_all[(centro_vacunacion_all.departamento == departamento)]
seleccion_geometria = gpd.GeoDataFrame(centro_vacunacion_filter, geometry=gpd.points_from_xy(centro_vacunacion_filter.longitud, centro_vacunacion_filter.latitud))
seleccion_geometria011=seleccion_geometria[(seleccion_geometria.latitud<0)&(seleccion_geometria.latitud>-19)]
seleccion_geometria012=seleccion_geometria011[(seleccion_geometria011.longitud<-65)&(seleccion_geometria011.longitud>-85)]
latitud_mean=seleccion_geometria012.latitud.mean()
latitus_std=seleccion_geometria012.latitud.std()
longitud_mean=seleccion_geometria012.longitud.mean()
longitud_std=seleccion_geometria012.longitud.std()
factor=4
seleccion_geometria013=seleccion_geometria012[(seleccion_geometria012.latitud>=latitud_mean-factor*latitus_std)&(seleccion_geometria012.latitud<=latitud_mean+factor*latitus_std)]
seleccion_geometria014=seleccion_geometria013[(seleccion_geometria013.longitud>=longitud_mean-factor*longitud_std)&(seleccion_geometria013.longitud<=longitud_mean+factor*longitud_std)]
eleccion=departamentos[departamentos['ADM1_ES_MAYUS']==departamento]
fig, ax = plt.subplots(figsize = (8,10))
eleccion.plot(ax = ax, color = 'White', edgecolor = 'grey')
seleccion_geometria014.plot(ax = ax, color = 'Red')
st.pyplot(fig)



    
    
