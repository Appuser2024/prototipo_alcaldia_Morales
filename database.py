import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Coordenadas del municipio
MORALES_LAT = 2.7556
MORALES_LON = -76.6272

def generate_sample_data():
    # Datos de seguridad
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    security_data = pd.DataFrame({
        'fecha': dates,
        'denuncias': np.random.randint(0, 10, size=len(dates)),
        'tipo': np.random.choice(['Hurto', 'Riña', 'Vandalismo'], size=len(dates)),
        'barrio': np.random.choice(['Centro', 'Sur', 'Norte', 'Occidente'], size=len(dates))
    })
    
    # Datos de salud
    health_data = pd.DataFrame({
        'fecha': dates[:30],
        'atenciones': np.random.randint(50, 200, size=30),
        'tipo_servicio': np.random.choice(['Urgencias', 'Consulta General', 'Vacunación'], size=30),
        'centro_salud': np.random.choice(['Hospital Central', 'Puesto de Salud 1', 'Puesto de Salud 2'], size=30)
    })
    
    # Datos de educación
    education_data = pd.DataFrame({
        'institucion': ['Colegio 1', 'Colegio 2', 'Colegio 3', 'Colegio 4'],
        'estudiantes': np.random.randint(200, 1000, size=4),
        'docentes': np.random.randint(10, 50, size=4),
        'latitud': [MORALES_LAT + np.random.random()/100 for _ in range(4)],
        'longitud': [MORALES_LON + np.random.random()/100 for _ in range(4)]
    })
    
    # Datos de presupuesto (usando valores más pequeños o np.random.randint con dtype=np.int64)
    budget_data = pd.DataFrame({
        'secretaria': ['Gobierno', 'Salud', 'Educación', 'Obras Públicas', 'Hacienda'],
        'presupuesto_asignado': np.random.randint(1000, 5000, size=5, dtype=np.int64) * 1_000_000,
        'presupuesto_ejecutado': np.random.randint(500, 4000, size=5, dtype=np.int64) * 1_000_000
    })
    
    return {
        'security': security_data,
        'health': health_data,
        'education': education_data,
        'budget': budget_data
    }

if __name__ == "__main__":
    # Test the function
    data = generate_sample_data()
    print("Sample data generated successfully!")
    print(f"Number of security records: {len(data['security'])}")