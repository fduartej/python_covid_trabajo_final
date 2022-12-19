import numpy as np
import pandas as pd
import plotly.graph_objects as go
import geopandas as gpd
import streamlit as st
import matplotlib.pyplot as plt


def mostrarMapa():
    st.write(f"You selected option {departamento}")
    centro_vacunacion_filter = centro_vacunacion_all[(centro_vacunacion_all.departamento == departamento)]
    seleccion_geometria = gpd.GeoDataFrame(centro_vacunacion_filter, geometry=gpd.points_from_xy(centro_vacunacion_filter.longitud, centro_vacunacion_filter.latitud))
    selecion_geometria01=seleccion_geometria[(seleccion_geometria['latitud']!=0)|(seleccion_geometria['longitud']!=0)]
    eleccion=departamentos[departamentos['NOMBDEP']==departamento]
    fig, ax = plt.subplots(figsize = (8,10))
    eleccion.plot(ax = ax, color = 'White', edgecolor = 'grey')
    selecion_geometria01.plot(ax = ax, color = 'Red')
    st.pyplot(fig)


#main
departamentos = gpd.read_file('peru_departamental_simple.geojson')
centro_vacunacion = pd.read_csv('TB_CENTRO_VACUNACION.csv',delimiter=",")
ubigeo = pd.read_csv('TB_UBIGEOS.csv',delimiter=",")
ubigeo_subset = ubigeo[["id_ubigeo", "departamento"]]
centro_vacunacion_all=pd.merge(centro_vacunacion,ubigeo_subset,on='id_ubigeo')

values = departamentos['NOMBDEP'].tolist()
departamento=st.selectbox('Selecciona el departamento:',values,
                                on_change=mostrarMapa)



    
    
