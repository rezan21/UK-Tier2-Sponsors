import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output # for callbacks

import preprocessing
from plots import Plot

df = preprocessing.process()
plot = Plot(df)


# Launch the application:
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    # search and table
    html.Div(children=[
        dcc.Input(id="search_input", placeholder='Enter a value...', type='text',value=''),
        html.Div(dcc.Graph(id="table")),
    ]),

    # row of 2 barcharts
    html.Div(children=[
        html.Div(children=[
        html.Div(dcc.Graph(id="overall_bc")),
        dcc.Slider(id="overall_slider", marks={i:str(i) for i in range(2013,2021,1)} , min=2013, max=2020, step=1, value=2013, className="slider"),

        ]),

        html.Div(children=[
            html.Div(dcc.Graph(id="stack_bc")),
            dcc.Slider(id="stack_slider", marks={i:str(i) for i in range(1,21,4)} , min=1, max=20, step=1, value=5, className="slider"),
        ]),
    ], className="second-row")
    

    

    
    ], className="container")


# callbacks
@app.callback(Output("overall_bc", "figure"), [Input("overall_slider", "value")])
def overall_bc(year):
    return plot.overall_bc(year)

@app.callback(Output("stack_bc", "figure"), [Input("stack_slider", "value")])
def stack_bc(top):
    return plot.stack_bc(top)

@app.callback(Output("table", "figure"), [Input("search_input", "value")])
def search_tb(term):
    if term=="":
        return plot.search_tb("limited")
    else:
        return plot.search_tb(term)



server = app.server
if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8080, debug=True, use_reloader=True)





