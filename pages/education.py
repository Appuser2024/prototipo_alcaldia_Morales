import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def show(data):
    st.title('Secretaría de Educación')
    
    # Mapa de instituciones educativas
    st.subheader('Ubicación de Instituciones Educativas')
    fig_map = px.scatter_mapbox(
        data,
        lat='latitud',
        lon='longitud',
        hover_name='institucion',
        hover_data=['estudiantes', 'docentes'],
        zoom=13,
        height=500,
        size='estudiantes',
        size_max=25,
        title='Mapa de Instituciones Educativas'
    )
    
    fig_map.update_layout(
        mapbox_style="open-street-map",
        mapbox=dict(
            center=dict(lat=data['latitud'].mean(), 
                       lon=data['longitud'].mean())
        )
    )
    st.plotly_chart(fig_map, use_container_width=True)
    
    # Gráfico de barras - Estudiantes por institución
    fig_students = go.Figure(data=[
        go.Bar(name='Estudiantes', x=data['institucion'], y=data['estudiantes']),
        go.Bar(name='Docentes', x=data['institucion'], y=data['docentes'])
    ])
    fig_students.update_layout(
        title='Distribución de Estudiantes y Docentes por Institución',
        barmode='group'
    )
    st.plotly_chart(fig_students)
    
    # Métricas educativas
    col1, col2, col3 = st.columns(3)
    with col1:
        total_estudiantes = data['estudiantes'].sum()
        st.metric("Total Estudiantes", f"{total_estudiantes:,}")
    with col2:
        total_docentes = data['docentes'].sum()
        st.metric("Total Docentes", f"{total_docentes:,}")
    with col3:
        ratio = total_estudiantes / total_docentes
        st.metric("Ratio Estudiantes/Docente", f"{ratio:.1f}")
    
    # Tabla de datos
    st.subheader("Detalle por Institución")
    st.dataframe(
        data[['institucion', 'estudiantes', 'docentes']].style.format({
            'estudiantes': '{:,}',
            'docentes': '{:,}'
        })
    )