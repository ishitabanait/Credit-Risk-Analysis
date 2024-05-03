import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

def automated_EDA(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path, low_memory=False)
    
    # Display data shape and column count
    data_shape = data.shape
    data_info = data.info()

    # Display warning for columns with mixed types
    mixed_types_columns = data.select_dtypes(include=['object']).columns

    # Handle missing data by filling with mode for categorical features
    categorical_data = data.select_dtypes(include=['object']).columns
    for feature in categorical_data:
        mode_value = data[feature].mode()[0]
        data[feature] = data[feature].fillna(mode_value)

    # Display missing data counts
    missing_data_counts = data.isnull().sum()

    # Generate descriptive statistics
    descriptive_statistics = data.describe()

    # Generate correlation matrix for numeric columns
    corr = data.select_dtypes(include=['float64', 'int64']).corr()

    # Create Dash app
    app = dash.Dash(__name__)

    # Define app layout
    app.layout = html.Div([
        html.H1("Exploratory Data Analysis Dashboard"),

        html.H2("Dataset Information"),
        html.P(f"Data Shape: {data_shape}"),
        html.P(f"Column Count: {len(data.columns)}"),
        html.P("Column Types:"),
        html.Pre(data_info),

        html.H2("Correlation Matrix"),
        dcc.Graph(id='heatmap', figure=px.imshow(corr, labels=dict(x="Numeric Features", y="Numeric Features"))),

        html.H2("Distribution Plots"),
        dcc.Dropdown(id='feature-dropdown', options=[{'label': col, 'value': col} for col in data.select_dtypes(include=['float64', 'int64']).columns], value=data.select_dtypes(include=['float64', 'int64']).columns[0]),
        dcc.Graph(id='distribution-plot'),

        html.H2("Boxplots"),
        dcc.Dropdown(id='boxplot-feature-dropdown', options=[{'label': col, 'value': col} for col in data.select_dtypes(include=['float64', 'int64']).columns], value=data.select_dtypes(include=['float64', 'int64']).columns[0]),
        dcc.Graph(id='boxplot'),

        html.H2("Pairwise Plots"),
        dcc.Dropdown(id='pairplot-x-dropdown', options=[{'label': col, 'value': col} for col in data.select_dtypes(include=['float64', 'int64']).columns], value=data.select_dtypes(include=['float64', 'int64']).columns[0]),
        dcc.Dropdown(id='pairplot-y-dropdown', options=[{'label': col, 'value': col} for col in data.select_dtypes(include=['float64', 'int64']).columns], value=data.select_dtypes(include=['float64', 'int64']).columns[1]),
        dcc.Graph(id='pairplot'),

        html.H2("Categorical Data Distribution"),
        dcc.Dropdown(id='cat-feature-dropdown', options=[{'label': col, 'value': col} for col in data.select_dtypes(include=['object']).columns], value=data.select_dtypes(include=['object']).columns[0]),
        dcc.Graph(id='cat-distribution-plot')
    ])

    # Define callback to update distribution plot
    @app.callback(
        Output('distribution-plot', 'figure'),
        [Input('feature-dropdown', 'value')]
    )
    def update_distribution_plot(selected_feature):
        fig = px.histogram(data, x=selected_feature, nbins=20, title=f'Distribution of {selected_feature}')
        return fig

    # Define callback to update boxplot
    @app.callback(
        Output('boxplot', 'figure'),
        [Input('boxplot-feature-dropdown', 'value')]
    )
    def update_boxplot(selected_feature):
        fig = px.box(data, y=selected_feature, title=f'Boxplot of {selected_feature}')
        return fig

    # Define callback to update pairwise plot
    @app.callback(
        Output('pairplot', 'figure'),
        [Input('pairplot-x-dropdown', 'value'),
         Input('pairplot-y-dropdown', 'value')]
    )
    def update_pairplot(selected_x_feature, selected_y_feature):
        fig = px.scatter(data, x=selected_x_feature, y=selected_y_feature, title='Pairwise Plot')
        return fig

    # Define callback to update categorical distribution plot
    @app.callback(
        Output('cat-distribution-plot', 'figure'),
        [Input('cat-feature-dropdown', 'value')]
    )
    def update_categorical_distribution_plot(selected_cat_feature):
        value_counts = data[selected_cat_feature].value_counts()
        fig = px.bar(x=value_counts.index, y=value_counts.values, labels={'x': f'Count of {selected_cat_feature}', 'y': 'Count'})
        return fig

    # Run the app
    app.run_server(debug=True)

# Call the function with the file path
automated_EDA("C:/Users/91942/Desktop/loan/loan_clean.csv")