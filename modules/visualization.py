import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import streamlit as st

def create_radar_chart(data, category_column, value_columns, title="Radar Chart"):
    """
    Creates a radar chart (polar plot) for comparing multiple entities.
    
    Args:
        data (DataFrame): The source data
        category_column (str): Column name containing entity names
        value_columns (list): List of columns containing values to plot
        title (str): Chart title
        
    Returns:
        plotly.graph_objects.Figure: The radar chart figure
    """
    fig = go.Figure()
    
    for entity in data[category_column].unique():
        entity_data = data[data[category_column] == entity]
        
        values = [entity_data[metric].values[0] for metric in value_columns]
        # Add the first value again to close the loop
        values.append(values[0])
        
        # Add the category names with the first one repeated at the end
        categories = value_columns + [value_columns[0]]
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=entity
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max([data[metric].max() for metric in value_columns]) * 1.1]
            )
        ),
        title=title,
        showlegend=True,
        legend=dict(font=dict(family="VT323", size=14)),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="VT323", color="#FFDE59"),
        height=600
    )
    
    return fig

def create_impact_certainty_matrix(data, x="Certainty (%)", y="Impact (1-10)", 
                                  color="Timeframe", size="Impact (1-10)", 
                                  hover_name="Factor", title="Impact vs Certainty Matrix"):
    """
    Creates a scatter plot for PESTLE analysis showing impact vs certainty.
    
    Args:
        data (DataFrame): The source data
        x (str): Column name for x-axis (default: "Certainty (%)")
        y (str): Column name for y-axis (default: "Impact (1-10)")
        color (str): Column name for color encoding (default: "Timeframe")
        size (str): Column name for point size (default: "Impact (1-10)")
        hover_name (str): Column name for hover text (default: "Factor")
        title (str): Chart title
        
    Returns:
        plotly.graph_objects.Figure: The scatter plot figure
    """
    fig = px.scatter(
        data,
        x=x,
        y=y,
        color=color,
        size=size,
        hover_name=hover_name,
        color_discrete_sequence=["#FFDE59", "#FF6B6B", "#4B64FF"],
        size_max=20,
        title=title
    )
    
    fig.update_layout(
        xaxis_title=x,
        yaxis_title=y,
        legend_title=color,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.2)',
        font=dict(family="VT323", color="#FFDE59"),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        height=500
    )
    
    # Add quadrant labels
    fig.add_annotation(x=75, y=8.5, text="HIGH IMPACT<br>HIGH CERTAINTY", showarrow=False, font=dict(family="VT323", size=14, color="#4DFF4D"))
    fig.add_annotation(x=75, y=2.5, text="LOW IMPACT<br>HIGH CERTAINTY", showarrow=False, font=dict(family="VT323", size=14, color="#FFDE59"))
    fig.add_annotation(x=55, y=8.5, text="HIGH IMPACT<br>LOW CERTAINTY", showarrow=False, font=dict(family="VT323", size=14, color="#FF6B6B"))
    fig.add_annotation(x=55, y=2.5, text="LOW IMPACT<br>LOW CERTAINTY", showarrow=False, font=dict(family="VT323", size=14, color="#4B64FF"))
    
    return fig

def create_bar_chart(data, x, y, color=None, text=None, title="Bar Chart", sort_by=None):
    """
    Creates a bar chart for comparing values across categories.
    
    Args:
        data (DataFrame): The source data
        x (str): Column name for x-axis categories
        y (str): Column name for y-axis values
        color (str, optional): Column name for color encoding
        text (str, optional): Column name for text display on bars
        title (str): Chart title
        sort_by (str, optional): Column name to sort by
        
    Returns:
        plotly.graph_objects.Figure: The bar chart figure
    """
    # Sort data if requested
    if sort_by:
        data = data.sort_values(sort_by, ascending=False)
    
    color_sequence = ["#FFDE59", "#FF6B6B", "#4B64FF", "#4DFF4D"]
    
    fig = px.bar(
        data,
        x=x,
        y=y,
        color=color,
        text=text,
        title=title,
        color_discrete_sequence=color_sequence
    )
    
    if text:
        fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
    
    fig.update_layout(
        xaxis_title=x,
        yaxis_title=y,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.2)',
        font=dict(family="VT323", color="#FFDE59"),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        height=400
    )
    
    return fig

def create_scatter_plot(data, x, y, color, size="Market Size (millions)", 
                       hover_name=None, hover_data=None, title="Scatter Plot"):
    """
    Creates a scatter plot for segment exploration.
    
    Args:
        data (DataFrame): The source data
        x (str): Column name for x-axis
        y (str): Column name for y-axis
        color (str): Column name for color encoding
        size (str): Column name for point size
        hover_name (str, optional): Column name for hover title
        hover_data (list, optional): List of columns to show on hover
        title (str): Chart title
        
    Returns:
        plotly.graph_objects.Figure: The scatter plot figure
    """
    fig = px.scatter(
        data,
        x=x,
        y=y,
        color=color,
        size=size,
        hover_name=hover_name if hover_name else color,
        hover_data=hover_data if hover_data else [size, y, x],
        size_max=30,
        title=title
    )
    
    fig.update_layout(
        xaxis_title=x,
        yaxis_title=y,
        legend_title=color,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.2)',
        font=dict(family="VT323", color="#FFDE59"),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        height=600
    )
    
    return fig

def create_timeline_chart(phases, durations, title="Implementation Timeline"):
    """
    Creates a Gantt-like timeline chart for implementation planning.
    
    Args:
        phases (list): List of phase names
        durations (list): List of phase durations (in months)
        title (str): Chart title
        
    Returns:
        plotly.graph_objects.Figure: The timeline chart figure
    """
    # Calculate start positions (assuming sequential)
    starts = [0]
    for i in range(1, len(durations)):
        starts.append(starts[i-1] + durations[i-1])
    
    colors = ['#4B64FF', '#4DFF4D', '#FFDE59', '#FF6B6B', '#FF00FF']
    
    fig = go.Figure()
    
    for i, phase in enumerate(phases):
        fig.add_trace(go.Bar(
            x=[durations[i]],
            y=[phase],
            orientation='h',
            marker=dict(
                color=colors[i % len(colors)],
                line=dict(width=2, color='#000000')
            ),
            text=f"{durations[i]} months",
            textposition='inside',
            insidetextanchor='middle',
            width=0.6,
            base=starts[i]
        ))
    
    fig.update_layout(
        title=title,
        xaxis=dict(
            title="Timeline (Months)",
            showgrid=True,
            gridcolor='rgba(255,255,255,0.1)',
            tickvals=list(range(0, max(starts) + max(durations) + 1, 1)),
            range=[0, max(starts) + max(durations)]
        ),
        yaxis=dict(
            title="Phase",
            autorange="reversed"
        ),
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.2)',
        font=dict(family="VT323", color="#FFDE59")
    )
    
    return fig

def create_financial_projection(quarters, investment, revenue, profit, title="Financial Projection"):
    """
    Creates a combination bar and line chart for financial projections.
    
    Args:
        quarters (list): List of quarter labels
        investment (list): Investment amounts per quarter
        revenue (list): Revenue amounts per quarter
        profit (list): Profit/loss amounts per quarter
        title (str): Chart title
        
    Returns:
        plotly.graph_objects.Figure: The financial chart figure
    """
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=quarters,
        y=investment,
        name="Investment",
        marker_color="#FF6B6B"
    ))
    
    fig.add_trace(go.Bar(
        x=quarters,
        y=revenue,
        name="Revenue",
        marker_color="#4DFF4D"
    ))
    
    fig.add_trace(go.Scatter(
        x=quarters,
        y=profit,
        name="Profit/Loss",
        mode="lines+markers",
        line=dict(color="#FFDE59", width=3)
    ))
    
    fig.update_layout(
        title=f"{title} ($000s)",
        xaxis_title="Quarter",
        yaxis_title="Amount ($000s)",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.2)',
        font=dict(family="VT323", color="#FFDE59"),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        height=400,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig

def create_stacked_bar_chart(data, x, y, color, title="Stacked Bar Chart"):
    """
    Creates a stacked bar chart for showing breakdowns.
    
    Args:
        data (DataFrame): The source data
        x (str): Column name for x-axis categories
        y (str): Column name for y-axis values
        color (str): Column name for color encoding (stacking)
        title (str): Chart title
        
    Returns:
        plotly.graph_objects.Figure: The stacked bar chart figure
    """
    fig = px.bar(
        data,
        x=x,
        y=y,
        color=color,
        title=title
    )
    
    fig.update_layout(
        barmode='stack',
        xaxis_title=x,
        yaxis_title=y,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.2)',
        font=dict(family="VT323", color="#FFDE59"),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        height=400
    )
    
    return fig

def create_contribution_chart(factors, contributions, normalized_scores, weights, title="Factor Contribution"):
    """
    Creates a bar chart showing factor contributions to an overall score.
    
    Args:
        factors (list): List of factor names
        contributions (list): List of weighted contributions
        normalized_scores (list): List of normalized scores (0-100)
        weights (list): List of weights
        title (str): Chart title
        
    Returns:
        plotly.graph_objects.Figure: The contribution chart figure
    """
    df = pd.DataFrame({
        'Factor': factors,
        'Normalized Score': normalized_scores,
        'Weight': weights,
        'Contribution': contributions
    })
    
    # Sort by contribution
    df = df.sort_values('Contribution', ascending=False)
    
    fig = px.bar(
        df,
        x='Factor',
        y='Contribution',
        text='Weight',
        color='Normalized Score',
        color_continuous_scale=['#FF6B6B', '#FFDE59', '#4DFF4D'],
        labels={'Contribution': 'Weighted Contribution', 'Weight': 'Weight (%)'},
        title=title
    )
    
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    
    fig.update_layout(
        xaxis_title="Evaluation Factor",
        yaxis_title="Contribution to Score",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.2)',
        font=dict(family="VT323", color="#FFDE59"),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        height=500,
        coloraxis_colorbar=dict(title="Factor Score")
    )
    
    return fig

# Add custom Streamlit metric styling for retro gaming look
def retro_metric(label, value, delta=None, delta_color="normal"):
    """
    Creates a styled metric component with retro gaming aesthetic.
    
    Args:
        label (str): Metric label
        value (str/number): Metric value
        delta (str/number, optional): Delta value
        delta_color (str): Color direction ('normal', 'inverse', or 'off')
    """
    st.markdown(f"""
    <div style="
        border: 3px solid #FFDE59;
        padding: 10px;
        margin: 5px 0;
        background-color: rgba(0,0,0,0.5);
        text-align: center;
    ">
        <p style="font-family: 'VT323', monospace; font-size: 16px; margin: 0; color: #FFDE59;">
            {label}
        </p>
        <h3 style="font-family: 'VT323', monospace; font-size: 28px; margin: 5px 0;">
            {value}
        </h3>
        {f'''<p style="font-family: 'Space Mono', monospace; font-size: 14px; margin: 0; 
                        color: {'#4DFF4D' if delta_color == 'normal' else '#FF6B6B' if delta_color == 'inverse' else '#FFFFFF'};">
                {delta}
            </p>''' if delta else ''}
    </div>
    """, unsafe_allow_html=True)