# Imports
import requests
import pandas as pd
import plotly.express as px

# Grab the json file and shove it into txt
resp = requests.get('http://api.open-notify.org/iss-now.json')
txt = resp.json()

# Place the data in a dataframe
data = {'Lat': [txt['iss_position']['latitude']],
        'Long': [txt['iss_position']['longitude']]}
iss_df = pd.DataFrame(data)

# Display it on a plot.
fig = px.scatter_geo(iss_df, lat='Lat', lon='Long')
fig.update_layout(title='World map', title_x=0.5)
fig.show()
