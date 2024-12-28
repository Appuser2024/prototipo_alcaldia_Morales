import streamlit as st
from pages import home, security, health, education
from database import generate_sample_data
import utils

st.set_page_config(
    page_title="Alcaldía de Morales - Sistema Centralizado",
    page_icon="🏛️",
    layout="wide"
)

# Generación de datos de ejemplo
data = generate_sample_data()

# Menú lateral
st.sidebar.title('Navegación')
page = st.sidebar.radio('Ir a:', [
    'Inicio',
    'Seguridad',
    'Salud',
    'Educación',
    'Presupuesto'
])

# Enrutamiento de páginas
if page == 'Inicio':
    home.show()
elif page == 'Seguridad':
    security.show(data['security'])
elif page == 'Salud':
    health.show(data['health'])
elif page == 'Educación':
    education.show(data['education'])
elif page == 'Presupuesto':
    st.title('Secretaría de Hacienda')
    st.plotly_chart(utils.create_budget_bar(data['budget']))