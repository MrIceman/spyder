import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

file_name = '..'
df = pd.read_json(file_name)
df = df.loc[df['package'] .str.contains('consent')]

fig = px.scatter(df,
                 x="instability_rating",
                 y="abstraction_degree",
                 size=df["abstraction_degree"] + df["instability_rating"] + 1,
                 hover_name="name",
                 color='package',
                 size_max=15)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
