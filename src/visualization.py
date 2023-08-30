import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def viz1(df):
    viz = px.box(df, x='Age', orientation='h',
              title="Passenger's Age Distribution - Boxplot")
    viz.update_layout(
    width=1100,  # Set the width to your desired value
    height=400,  # Set the height to your desired value
    )
    # Show the plot
    viz.show()
    return viz

def viz2(df):
    viz = px.histogram(df, x='Age', title="Passenger's Age Distribution - Histogram")
    viz.update_xaxes(title='Age')
    viz.update_yaxes(title='Count')

    # Show the plot
    viz.show()
    return viz

def viz3(df):
    
    transpcolors = ['#66B2FF','#FF9999']
    colors = ['#FF9999', '#66B2FF']
    
    # Create subplots with 1 row and 3 columns
    viz = go.Figure()

    # Create a pie chart for 'Transported'
    viz.add_trace(go.Pie(
        labels = ['Transported', 'NOT Transported'],
        values = df['Transported'].value_counts(),
        name = 'Transported',
        title = 'Transported',
        domain = {'x': [0, 0.3]},
        marker = dict(colors=transpcolors)
    ))

    # Create a pie chart for 'VIP'
    viz.add_trace(go.Pie(
        labels = ['NOT VIP', 'VIP'],
        values = df['VIP'].value_counts(),
        name = 'VIP',
        title = 'VIP',
        domain = {'x': [0.35, 0.65]},
        marker = dict(colors=colors)
    ))

    # Create a pie chart for 'CryoSleep'
    viz.add_trace(go.Pie(
        labels = ['NOT CryoSleep', 'CryoSleep'],
        values = df['CryoSleep'].value_counts(),
        name = 'CryoSleep',
        title = 'CryoSleep',
        domain = {'x': [0.7, 1]},
        marker = dict(colors=colors)
    ))

    # Update layout
    viz.update_layout(
        title = 'Pie Charts for Transported, VIP, and CryoSleep',
        grid = {'rows': 1, 'columns': 3},
    )

    # Show the plot
    viz.show()
    return viz

def viz4(df):
    column_sums = df[['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']].sum()

    # Create a bar chart
    bar_chart = px.bar(
        x=column_sums.index,  # Use column names as x-axis labels
        y=column_sums.values,  # Use column sums as y-axis values
        title="Total Expenses by Amenity",
        labels={'x': 'Amenity', 'y': 'Total Expense'}
    )
    bar_chart.show()
    return bar_chart