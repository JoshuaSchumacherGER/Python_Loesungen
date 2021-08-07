# Author: AwSnap

import plotly.graph_objects as pg_o  # imports
import pandas
import requests  # imports

# getting the data from the link
response = requests.get('http://api.open-notify.org/iss-now.json')

ISS_data = response.content  # setting response as a variable

decoded_ISS_data = ISS_data.decode()  # decoding the data from bytes to a string

ISS_dict = eval(decoded_ISS_data)  # turning the ISS_data into a dictionary

# turning the positions (long) into a int
ISS_pos_lon = ISS_dict['iss_position']['longitude']

ISS_pos_lat = ISS_dict['iss_position']['latitude']  # other latitude into int

# making the map as a type of plotting file, with long and latt
wmap = pg_o.Figure(data=pg_o.Scattergeo(lon=[ISS_pos_lon], lat=[
                   ISS_pos_lat], mode='markers', marker_color=3))

wmap.update_layout(title='THE ISS POSITION',
                   geo_scope='world')  # the world map

wmap.show()  # showing the map
wmap.show()  # (a second time as it sometimes breaks)

while True:  # loop
    pass  # keeping the cmd active
