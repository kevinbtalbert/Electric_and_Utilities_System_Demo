import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os

# Read the generated dataset (make sure to replace this path with the correct one on your machine)
df = pd.read_csv("/home/cdsw/CML-Assets/data/generated_utility_data_12_months.csv")

# Prepare the data for plotting
df['Billing Start Date'] = pd.to_datetime(df['Billing Start Date'])
df['Billing End Date'] = pd.to_datetime(df['Billing End Date'])
df['Month'] = df['Billing Start Date'].dt.month

# Pivoting the data for each customer's monthly readings
pivot_df = df.pivot_table(index=['Customer ID', 'Month'], 
                          values=['Previous Meter Reading', 'Current Meter Reading'], 
                          aggfunc='mean').reset_index()

# Average Monthly Consumption
avg_monthly_consumption = df.groupby('Month')['Usage (kWh)'].mean().reset_index()

# Calculate total consumption for each customer over the year
df['Total Consumption'] = df.groupby('Customer ID')['Usage (kWh)'].transform('sum')
top_consumers = df[['Customer ID', 'Total Consumption']].drop_duplicates().nlargest(5, 'Total Consumption')

# Initialize Dash app with external CSS for styling
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Layout of the app
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Meter Readings Over Time', children=[
            html.Div([
                html.H1("Customer Meter Readings Over Time", style={'textAlign': 'center', 'color': '#007BFF'}),
                html.P("Interactive dashboard displaying monthly meter readings.", style={'textAlign': 'center'}),
                html.Div([
                    dcc.Dropdown(
                        id='customer-dropdown',
                        options=[{'label': i, 'value': i} for i in df['Customer ID'].unique()],
                        value=df['Customer ID'].unique()[0],
                        style={'width': '50%', 'margin': 'auto'}
                    )
                ], style={'padding': '20px', 'textAlign': 'center'}),
                dcc.Graph(id='time-series-plot')
            ], style={'maxWidth': '1200px', 'margin': 'auto'})
        ]),
        dcc.Tab(label='Top Consumers', children=[
            html.Div([
                html.H1("Top Consumers by Total Consumption", style={'textAlign': 'center', 'color': '#007BFF'}),
                html.P("This tab shows the customers with the highest total consumption over the year.", 
                       style={'textAlign': 'center'}),
                dcc.Graph(
                    id='top-consumers-plot',
                    figure=px.bar(top_consumers, x='Customer ID', y='Total Consumption',
                                  title="Top 5 Consumers by Total Consumption")
                )
            ], style={'maxWidth': '1200px', 'margin': 'auto'})
        ]),
        dcc.Tab(label='Average Monthly Consumption', children=[
            html.Div([
                html.H1("Average Monthly Electricity Usage", style={'textAlign': 'center', 'color': '#007BFF'}),
                html.P("Analysis of average electricity usage per month across all customers.", style={'textAlign': 'center'}),
                dcc.Graph(
                    id='avg-monthly-consumption-plot',
                    figure=px.line(avg_monthly_consumption, x='Month', y='Usage (kWh)',
                                   title="Average Monthly Electricity Usage (kWh)")
                )
            ], style={'maxWidth': '1200px', 'margin': 'auto'})
        ]),
        dcc.Tab(label='Customer Charge Analysis', children=[
            html.Div([
                html.H1("Customer Charge vs Consumption Analysis", style={'textAlign': 'center', 'color': '#007BFF'}),
                html.P("Scatter plot showing the relationship between total charges and total consumption for each customer.", 
                       style={'textAlign': 'center'}),
                dcc.Graph(
                    id='charge-vs-consumption-plot',
                    figure=px.scatter(df.drop_duplicates('Customer ID'), x='Total Consumption', y='Total Charge', 
                                      hover_data=['Customer ID'], 
                                      title="Total Charge vs Total Consumption")
                )
            ], style={'maxWidth': '1200px', 'margin': 'auto'})
        ])
    ])
], style={'fontFamily': 'Arial, sans-serif'})

# Callback for updating the time series plot
@app.callback(
    Output('time-series-plot', 'figure'),
    [Input('customer-dropdown', 'value')]
)
def update_time_series(selected_customer_id):
    filtered_df = pivot_df[pivot_df['Customer ID'] == selected_customer_id]
    fig = px.line(filtered_df, x='Month', y=['Previous Meter Reading', 'Current Meter Reading'], 
                  title=f"Meter Readings for Customer ID: {selected_customer_id}")
    fig.update_layout(plot_bgcolor='white', paper_bgcolor='white')
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True, port=int(os.getenv('CDSW_APP_PORT')))
