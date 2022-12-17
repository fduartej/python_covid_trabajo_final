import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st


centro_vacunacion = pd.read_csv('TB_CENTRO_VACUNACION.csv',delimiter=",")
centro_vacunacion.head()

ubigeo = pd.read_csv('TB_UBIGEOS.csv',delimiter=",")
ubigeo.head()

option = st.selectbox('Selecciona el departamento:',('AMAZONAS','ANCASH','APURIMAC','AREQUIPA','AYACUCHO','CAJAMARCA','CALLAO','CUSCO','HUANCAVELICA','HUANUCO','ICA','JUNIN','LA LIBERTAD','LAMBAYEQUE','LIMA','LORETO','MADRE DE DIOS','MOQUEGUA','PASCO','PIURA','PUNO','SAN MARTIN','TACNA','TUMBES','UCAYALI'))
st.write('Seleccionó:', option)