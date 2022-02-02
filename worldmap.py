import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv('worldmap countries.csv')

data_country_count = data.set_index('country').to_dict()['count']

fig = go.Figure(data=go.Choropleth(
    locations = data['code'],
    z = data['count'],
    text = data['country'],
    colorscale = 'Earth',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = 'Countries',
))

fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Countries',
        showarrow = False
    )]
)

fig.show()