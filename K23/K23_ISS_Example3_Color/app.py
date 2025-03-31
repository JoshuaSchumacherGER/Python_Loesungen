import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
import requests

def getISSPosition():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    pos = data["iss_position"]
    return {"latitude": float(pos["latitude"]), "longitude": float(pos["longitude"])}

def createMap():
    iss_pos = getISSPosition()

    fig = go.Figure()

    # Länder laden
    countries = pd.read_csv("world_countries.csv") 

    
    countries["color_value"] = range(len(countries))

    fig.add_trace(go.Choropleth(
        locations = countries['CODE'],
        z = countries['color_value'],
        text = countries['COUNTRY'],
        colorscale = 'Viridis',  # Alternativ: 'Rainbow', 'Turbo', 'Cividis'
        showscale = False,
        marker_line_color='white',
        marker_line_width=0.5,
    ))

    # ISS Position hinzufügen
    fig.add_trace(go.Scattergeo(
        lat=[iss_pos["latitude"]],
        lon=[iss_pos["longitude"]],
        mode='markers',
        marker=dict(size=10, color='red'),
        name='ISS'
    ))

    fig.update_geos(
        showcountries=True,
        countrycolor="black",
        showcoastlines=True,
        coastlinecolor="gray",
        projection_type="natural earth"
    )

    fig.update_layout(
        title="Aktuelle Position der ISS mit Ländergrenzen",
        geo=dict(
            showland=True,
            landcolor="lightgray",
        ),
        margin=dict(l=0, r=0, t=40, b=0)
    )

    return fig

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("ISS Position", style={"font-family": "Arial", "text-align": "center"}),
    dcc.Graph(figure=createMap(), style={"height": "90vh"})
])

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=8050)