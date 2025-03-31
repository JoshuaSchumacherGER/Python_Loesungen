import dash
from dash import dcc, html
import plotly.express
import pandas, requests

def getISSPosition():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    return data["iss_position"]

def createMap():
    df = pandas.DataFrame([getISSPosition()])
    fig = plotly.express.scatter_geo(df, lat="latitude", lon="longitude", title="ISS Position")
    return fig

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("ISS Position", style={"font-family": "Arial", "text-align": "center"}),
    dcc.Graph(figure=createMap(), style={"height": "90vh"})
])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
