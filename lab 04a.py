import plotly.express as px
import pandas as pd
import dash
from dash import html, dcc, Input, Output

# use same gapminderDataFiveYear.csv as lab 03

app = dash.Dash(__name__)

# prepare data
df = pd.read_csv("gapminderDataFiveYear.csv")

year_options = []
for year in df["year"].unique():
    year_options.append({"label": str(year), "value": year})
    
# configure layout
app.layout = html.Div([
    html.H2("Select the year"),
    dcc.Dropdown(
            id='year_picker',
            options=year_options,
            value=df["year"].min()),
        dcc.Graph(id='graph_output')
])

@app.callback(
    Output('graph_output', 'figure'),
    Input('year_picker', 'value')
)

def update_graph(selected_year):
    filtered_df = df[df["year"] == selected_year]
    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp", size="pop", 
                    color="continent", hover_name="country",log_x=True, size_max=55)
    return fig

# execute program
if __name__ == '__main__':
    app.run(debug=True, port=8050)