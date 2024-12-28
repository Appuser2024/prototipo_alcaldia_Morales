import streamlit as st # type: ignore

def show():
    st.title('Sistema Centralizado de Información')
    st.subheader(f'Alcaldía de Morales, Cauca')
    
    st.markdown("""
    ### Bienvenido al Sistema de Gestión Municipal
    
    Este sistema permite:
    - Visualización de indicadores clave
    - Gestión de datos por secretaría
    - Monitoreo de presupuesto
    - Mapas interactivos
    """)
    
    # Métricas principales
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Población", "35,420", "+2.3%")
    with col2:
        st.metric("Presupuesto Ejecutado", "$12.5B", "85%")
    with col3:
        st.metric("Proyectos Activos", "24", "+3")