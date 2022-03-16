from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import graph_functions as gf


app = Dash(__name__)

colors = {
    'background': '#FDFEFE',
    'text': '#17202A'
}

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

# Running cleaning stuff
exec(open("zhvi_cleaning.py").read())

#----------------APP STARTS HERE---------------------#
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1(
        children='Bust A Move!',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ),

    html.Div(children='Exploring Regional Mobility in the US\n', style={
        'textAlign': 'left',
        'padding' : 5,
        'color': colors['text']
    }),
    html.P("See 'high risk' counties:"),
    

    html.Div(children='''Our project explored the theory that the increasing availability 
    of remote working opportunities, partly as a consequence of the pandemic, 
    has led to migrations from major cities to smaller cities and towns in the western US 
    that are located close to nature/national parks. 
    Using historical housing price data as a proxy for recent regional mobility, 
    we were able to create a visualization that matches our theory and confirms 
    information in other news stories and research on this theory. ''',
    style={
        'textAlign': 'left',
        'color': colors['text'],
        'width' : '98%',
        'padding' :5
    }),

    html.Div(children='''Specifically, we plotted the change in estimated housing prices from 2019-2021 (using data from Zillow)
    to identify counties where the housing prices were on the rise (the redder counties). Our theory is that these 
    are the same counties that experienced
    inward migration from larger cities. We also think that these counties are closer to national parks/nature (black points on 
    the map). We show the race distribution of the selected county, a histogram of median income, 
    percent of the population in poverty, and where
    the currently selected county lies in this range. Additionally, we show the change in mobility across time for different types
    of activities within the selected county, using GPS activity from Google (this shows the change compared to the median value 
    from the 5-week baseline period Jan 3-Feb 6, 2020).''',
    style={
        'textAlign': 'left',
        'color': colors['text'],
        'width' : '98%',
        'padding' : 5
    }),

    html.Div(children='Click on a county on the map and use the toggle to view mobility and demographic data.',
    style={
        'textAlign': 'left',
        'color': colors['text'],
        'padding' :10, 
    }),
    html.Div([
            dcc.RadioItems(
                ['Full Map', 'High Risk'],
                value='Full Map',
                id='Filt',
                inline=True,
                style={'width': '15%'}
                )]),
    html.Div([
            dcc.Dropdown(
                ['Percent change in GPS activity by Category',
                'Distribution of Median Income and Poverty rate',
                'Race Distribution'],
                'Distribution of Median Income and Poverty rate',
                id='mobility_demo_toggle')],
                style={'width': '30%','float': 'right','display': 'inline-block'}),

    html.Div([
        
        dcc.Graph(
            id='zhvf',
            clickData={'points': [{'location': '30029'}]})],
            #figure=gf.create_chloropleth(counties, zhvi_county_inc_pop, natl_parks))], 
            style={'width': '55%'}),

    html.Div([dcc.Graph(
                id='mobility_demo',)],
                style={'width': '45%','display': 'inline-block'})
    
])

def make_side_graph(toggle_val, FIPS):
    '''
    Plot side graph based on toggle values
    '''

    if toggle_val == 'Percent change in GPS activity by Category':
        return gf.create_mobility_graph2(mobility, zhvi_county_inc_pop, FIPS)
    
    if toggle_val == 'Distribution of Median Income and Poverty rate':
        return gf.create_income_graph(zhvi_county_inc_pop, FIPS)
    
    if toggle_val == 'Race Distribution':
        return gf.create_pie_chart(zhvi_county_inc_pop, FIPS, race)

@app.callback(
    Output('zhvf', 'figure'),
    Input('Filt', 'value'),
    Input('zhvf', 'clickData'))
def update_map(Filt, clickData):
    if str(Filt) == 'High Risk':
        opacity = True
    else:
        opacity = False
    return gf.create_chloropleth(counties, zhvi_county_inc_pop, natl_parks, opacity)

@app.callback(
    Output('mobility_demo', 'figure'),
    Input('zhvf', 'clickData'),
    Input('mobility_demo_toggle', 'value'))
def update_graph_series(clickData, toggle):
    # Figure 2
    county = clickData['points'][0]['location']
    return make_side_graph(str(toggle), county)



'''
html.Div([
    dcc.Markdown(),
    html.Pre(id='click-data', style=styles['pre'])], 
    className='three columns')

@app.callback(
    Output('click-data', 'children'),
    Input('zhvf', 'clickData'),
    Input('mobility_demo_toggle', 'value'))
def display_click_data(clickData, toggle):
    return json.dumps(str(clickData['points'][0]['location'] + " " + toggle), indent=2)
'''

if __name__ == '__main__':
    app.run_server(debug=True)

