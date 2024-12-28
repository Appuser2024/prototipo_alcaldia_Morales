# pages/health.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def show(data):
    st.title('Secretaría de Salud')
    
    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        selected_centro = st.selectbox('Centro de Salud', data['centro_salud'].unique())
    with col2:
        selected_servicio = st.selectbox('Tipo de Servicio', data['tipo_servicio'].unique())
    
    # Datos filtrados
    filtered_data = data[
        (data['centro_salud'] == selected_centro) &
        (data['tipo_servicio'] == selected_servicio)
    ]
    
    # Gráfico de atenciones por día
    fig_timeline = px.line(
        filtered_data,
        x='fecha',
        y='atenciones',
        title=f'Atenciones Diarias - {selected_centro}',
        labels={'fecha': 'Fecha', 'atenciones': 'Número de Atenciones'}
    )
    st.plotly_chart(fig_timeline)
    
    # Distribución de servicios
    fig_pie = px.pie(
        data,
        values='atenciones',
        names='tipo_servicio',
        title='Distribución de Servicios de Salud'
    )
    st.plotly_chart(fig_pie)
    
    # Métricas
    col1, col2, col3 = st.columns(3)
    with col1:
        total_atenciones = data['atenciones'].sum()
        st.metric("Total Atenciones", f"{total_atenciones:,}")
    with col2:
        promedio_diario = data['atenciones'].mean()
        st.metric("Promedio Diario", f"{promedio_diario:.0f}")
    with col3:
        max_atenciones = data['atenciones'].max()
        st.metric("Máximo Diario", f"{max_atenciones:,}")