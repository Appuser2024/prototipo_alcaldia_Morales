import streamlit as st
import plotly.express as px
import numpy as np
from utils import create_security_heatmap

# Coordenadas del municipio
MORALES_LAT = 2.7556
MORALES_LON = -76.6272

def show(data):
    st.title('Secretaría de Gobierno y Seguridad')
    
    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        selected_barrio = st.selectbox('Seleccionar Barrio', data['barrio'].unique())
    with col2:
        selected_tipo = st.selectbox('Tipo de Incidente', data['tipo'].unique())
    
    # Mapa de incidentes usando Plotly
    filtered_data = data[
        (data['barrio'] == selected_barrio) &
        (data['tipo'] == selected_tipo)
    ]
    
    st.subheader('Mapa de Incidentes')
    
    # Crear datos de ejemplo para el mapa
    map_data = filtered_data.copy()
    map_data['lat'] = [MORALES_LAT + np.random.random()/100 for _ in range(len(filtered_data))]
    map_data['lon'] = [MORALES_LON + np.random.random()/100 for _ in range(len(filtered_data))]
    
    fig = px.scatter_mapbox(
        map_data,
        lat='lat',
        lon='lon',
        hover_data=['tipo', 'fecha'],
        zoom=13,
        height=600,
        title='Mapa de Incidentes'
    )
    
    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox=dict(
            center=dict(lat=MORALES_LAT, lon=MORALES_LON)
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Gráficos adicionales
    st.plotly_chart(create_security_heatmap(data))