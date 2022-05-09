import pandas
import requests
import plotly.graph_objects as go
import json

class ISSCoordinates:
    def __init__(self, 
                 longitude: float,
                 latitude: float):
        self.longitude = longitude 
        self.latitude = latitude

class ISSNowSession(requests.sessions.Session):
    def __init__(self, 
                 url: str, 
                 header=None, 
                 payload=None, 
                 verify=False):
        requests.sessions.Session.__init__(self)
        self.url = url
        self.header = header
        self.payload = payload
        self.verify = verify
       
    def get_iss_coordinates(self) -> ISSCoordinates:
        response = self.get(self.url)
        if not 200 <= response.status_code <= 300:
            return 
        data = dict(json.loads(response.text)).get('iss_position')
        result = ISSCoordinates(float(data.get('longitude')), 
                                float(data.get('latitude')))
        return result
       
        
def main():
    iss_position_session = ISSNowSession("http://api.open-notify.org/iss-now.json")
    iss_coordinates = iss_position_session.get_iss_coordinates()
    
    df = pandas.DataFrame({'long': [iss_coordinates.longitude],
                           'lat': [iss_coordinates.latitude],
                           'text': ["ISS"]})
                           
    fig = go.Figure(data=go.Scattergeo(lon = df['long'],
                                       lat = df['lat'],
                                       text = df['text']))
    
    fig.update_layout(title = 'ISS Position')
    fig.show()
            
if __name__ == "__main__":
    main()
