import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_security_heatmap(data):
    pivot_data = data.pivot_table(
        values='denuncias',
        index='barrio',
        columns=pd.to_datetime(data['fecha']).dt.strftime('%Y-%m'),
        aggfunc='sum'
    )
    return px.imshow(
        pivot_data,
        title='Mapa de Calor - Denuncias por Barrio',
        labels={'x': 'Mes', 'y': 'Barrio', 'color': 'Denuncias'}
    )

def create_budget_bar(data):
    fig = go.Figure(data=[
        go.Bar(name='Asignado', x=data['secretaria'], y=data['presupuesto_asignado']),
        go.Bar(name='Ejecutado', x=data['secretaria'], y=data['presupuesto_ejecutado'])
    ])
    fig.update_layout(
        title='Presupuesto por Secretaría',
        barmode='group'
    )
    return fig