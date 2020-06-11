import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plots

plot = plots.get_plot()
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash Tutorials'),
    dcc.Graph(
        id="idss",
        figure=plot
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)