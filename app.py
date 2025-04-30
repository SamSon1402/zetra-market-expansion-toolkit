import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from PIL import Image
import random
import plotly.express as px
import plotly.graph_objects as go
import base64

# Set page configuration
st.set_page_config(
    page_title="Zetra Market Expansion Toolkit",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply retro gaming aesthetic with custom CSS
def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=VT323&family=Space+Mono&display=swap');
        
        /* Main color scheme */
        :root {
            --main-yellow: #FFDE59;
            --main-coral: #FF6B6B;
            --pixel-blue: #4B64FF;
            --pixel-green: #4DFF4D;
            --dark-bg: #121212;
            --light-text: #F5F5F5;
        }
        
        /* Global styles */
        .stApp {
            background-color: var(--dark-bg);
            color: var(--light-text);
        }
        
        h1, h2, h3 {
            font-family: 'VT323', monospace;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--main-yellow);
            text-shadow: 2px 2px 0px rgba(0,0,0,0.8);
        }
        
        p, li, div {
            font-family: 'Space Mono', monospace;
        }
        
        /* Pixel-perfect UI elements */
        .stButton>button {
            border: 3px solid var(--main-coral);
            background-color: var(--dark-bg);
            color: var(--main-coral);
            font-family: 'VT323', monospace;
            font-size: 20px;
            padding: 5px 20px;
            transition: all 0.1s ease;
            box-shadow: 4px 4px 0px var(--main-coral);
        }
        
        .stButton>button:hover {
            transform: translate(2px, 2px);
            box-shadow: 2px 2px 0px var(--main-coral);
        }
        
        /* Custom dropdown and selectbox styling */
        .stSelectbox>div>div, .stMultiSelect>div>div {
            background-color: var(--dark-bg);
            border: 2px solid var(--main-yellow);
            color: var(--main-yellow);
            font-family: 'Space Mono', monospace;
        }
        
        /* Metric styling */
        .stMetric {
            background-color: rgba(0,0,0,0.3);
            border: 2px solid var(--pixel-blue);
            padding: 10px;
            border-radius: 0;
        }
        
        /* Container styling with pixel borders */
        .pixel-container {
            border: 4px solid var(--main-yellow);
            background-color: rgba(0,0,0,0.4);
            padding: 20px;
            margin: 10px 0;
        }
        
        /* Progress bar styling */
        .stProgress>div>div {
            background-color: var(--main-coral);
        }
        
        /* Tab styling */
        .stTabs button {
            font-family: 'VT323', monospace;
            font-size: 18px;
            color: var(--main-yellow);
        }
        
        .stTabs button[aria-selected="true"] {
            background-color: var(--main-coral);
            color: var(--light-text);
        }
    </style>
    """, unsafe_allow_html=True)

load_css()

# Function to generate pixelated background
def add_bg_from_base64():
    # Generate a simple pixel grid background
    def generate_pixel_background(width=40, height=40, colors=["#1e1e1e", "#2a2a2a"]):
        img = Image.new('RGB', (width, height), colors[0])
        pixels = img.load()
        for i in range(0, width, 4):
            for j in range(0, height, 4):
                if random.random() > 0.7:  # 30% chance of a different colored pixel
                    pixels[i, j] = tuple(int(colors[1].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        
        # Convert PIL Image to base64
        import io
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        return img_str
    
    bg_img = generate_pixel_background()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_img}");
            background-repeat: repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_base64()

# Generate synthetic data
@st.cache_data
def generate_industry_data():
    industries = [
        "Software & IT Services", "Manufacturing", "Healthcare", 
        "Financial Services", "Retail", "Energy & Utilities",
        "Telecommunications", "Education", "Professional Services",
        "Transportation & Logistics"
    ]
    
    data = []
    for industry in industries:
        market_size = np.random.randint(500, 10000)  # in millions
        growth_rate = np.random.uniform(1.5, 15.0)
        ai_adoption = np.random.uniform(10.0, 85.0)
        sustainability_focus = np.random.uniform(10.0, 90.0)
        profitability = np.random.uniform(5.0, 25.0)
        competition = np.random.uniform(10.0, 90.0)
        barriers_to_entry = np.random.uniform(10.0, 90.0)
        
        data.append({
            "Industry": industry,
            "Market Size (millions)": market_size,
            "Growth Rate (%)": growth_rate,
            "AI Adoption (%)": ai_adoption,
            "Sustainability Focus (%)": sustainability_focus,
            "Profitability (%)": profitability,
            "Competition Level (%)": competition,
            "Barriers to Entry (%)": barriers_to_entry
        })
    
    return pd.DataFrame(data)

@st.cache_data
def generate_segment_data():
    segments = []
    industries = [
        "Software & IT Services", "Manufacturing", "Healthcare", 
        "Financial Services", "Retail", "Energy & Utilities",
        "Telecommunications", "Education", "Professional Services"
    ]
    
    company_sizes = ["Small (10-50)", "Medium (51-500)", "Large (501-5000)", "Enterprise (5000+)"]
    regions = ["North America", "Europe", "Asia Pacific", "Latin America", "Middle East & Africa"]
    
    for industry in industries:
        for size in company_sizes:
            for region in regions:
                if random.random() > 0.3:  # Only generate some combinations to keep the data manageable
                    market_size = np.random.randint(50, 5000)  # in millions
                    cagr = np.random.uniform(1.0, 20.0)
                    profitability = np.random.uniform(3.0, 30.0)
                    competitive_intensity = np.random.uniform(10.0, 100.0)
                    tech_maturity = np.random.uniform(10.0, 100.0)
                    ai_readiness = np.random.uniform(10.0, 100.0)
                    sustainability_score = np.random.uniform(10.0, 100.0)
                    
                    segments.append({
                        "Industry": industry,
                        "Company Size": size,
                        "Region": region,
                        "Market Size (millions)": market_size,
                        "CAGR (%)": cagr,
                        "Profitability (%)": profitability,
                        "Competitive Intensity": competitive_intensity,
                        "Technology Maturity": tech_maturity,
                        "AI Readiness": ai_readiness,
                        "Sustainability Score": sustainability_score
                    })
    
    return pd.DataFrame(segments)

@st.cache_data
def generate_pestle_data():
    factors = {
        "Political": ["Regulatory Changes", "Trade Policies", "Political Stability", "Government Initiatives"],
        "Economic": ["Economic Growth", "Interest Rates", "Inflation", "Exchange Rates"],
        "Social": ["Demographic Shifts", "Consumer Behavior", "Work Culture", "Social Values"],
        "Technological": ["AI & Automation", "Cloud Computing", "Cybersecurity", "Digital Transformation"],
        "Legal": ["Data Protection", "Intellectual Property", "Compliance Requirements", "Contract Enforcement"],
        "Environmental": ["Sustainability Regulations", "Carbon Footprint", "Resource Scarcity", "Environmental Standards"]
    }
    
    data = []
    for category, items in factors.items():
        for item in items:
            impact = np.random.uniform(1.0, 10.0)
            certainty = np.random.uniform(50.0, 100.0)
            timeframe = random.choice(["Short-term", "Medium-term", "Long-term"])
            
            data.append({
                "Category": category,
                "Factor": item,
                "Impact (1-10)": impact,
                "Certainty (%)": certainty,
                "Timeframe": timeframe
            })
    
    return pd.DataFrame(data)

@st.cache_data
def generate_trends_data():
    trends = [
        "AI Integration in Business Processes",
        "Sustainable Business Operations",
        "Remote/Hybrid Work Models",
        "Data Privacy & Security Focus",
        "Personalized B2B Marketing",
        "Supply Chain Resilience",
        "Digital Transformation Acceleration",
        "Subscription-based Business Models",
        "Blockchain for B2B Transactions",
        "Customer Experience Prioritization"
    ]
    
    data = []
    for trend in trends:
        adoption = np.random.uniform(10.0, 90.0)
        impact = np.random.uniform(3.0, 10.0)
        investment = np.random.randint(10, 100)  # in billions
        time_to_mainstream = random.choice(["Already Mainstream", "1-2 Years", "3-5 Years", "5+ Years"])
        
        data.append({
            "Trend": trend,
            "Adoption Rate (%)": adoption,
            "Business Impact (1-10)": impact,
            "Global Investment (billions)": investment,
            "Time to Mainstream": time_to_mainstream
        })
    
    return pd.DataFrame(data)

# Load data
industry_data = generate_industry_data()
segment_data = generate_segment_data()
pestle_data = generate_pestle_data()
trends_data = generate_trends_data()

# Create the app structure
def main():
    # Sidebar navigation
    st.sidebar.markdown("<h1 style='text-align: center; color: #FFDE59;'>🎮 ZETRA QUEST 2025 🎮</h1>", unsafe_allow_html=True)
    
    # Add pixelated avatar
    st.sidebar.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <div style="
            width: 100px;
            height: 100px;
            margin: 0 auto;
            background: linear-gradient(45deg, #FF6B6B, #FFDE59);
            image-rendering: pixelated;
            border: 4px solid #FFDE59;
            box-shadow: 5px 5px 0px rgba(0,0,0,0.5);
        ">
            <div style="
                font-family: 'VT323', monospace;
                font-size: 42px;
                color: #121212;
                text-align: center;
                padding-top: 25px;
                font-weight: bold;
            ">Z</div>
        </div>
        <p style="font-family: 'VT323', monospace; font-size: 20px; margin-top: 10px;">ZETRA STRATEGIST</p>
        <p style="font-family: 'VT323', monospace; font-size: 16px; color: #FF6B6B;">PARIS HQ</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    nav_options = [
        "🏠 Home",
        "🔍 Market Overview",
        "🧩 Segment Explorer",
        "⚖️ Evaluation Tool",
        "🏆 Target Strategy"
    ]
    
    nav_selection = st.sidebar.radio("", nav_options, key="navigation")
    
    # "Power meter" in sidebar
    st.sidebar.markdown("<h3 style='text-align: center;'>SYSTEM POWER</h3>", unsafe_allow_html=True)
    power_level = 87  # Example value
    st.sidebar.progress(power_level/100)
    st.sidebar.markdown(f"""
    <div style='text-align: center; font-family: "VT323", monospace; font-size: 24px; color: #FFDE59;'>
        {power_level}%
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation handling
    if nav_selection == "🏠 Home":
        home_page()
    elif nav_selection == "🔍 Market Overview":
        market_overview()
    elif nav_selection == "🧩 Segment Explorer":
        segment_explorer()
    elif nav_selection == "⚖️ Evaluation Tool":
        evaluation_tool()
    elif nav_selection == "🏆 Target Strategy":
        target_strategy()

# Individual pages
def home_page():
    # Title with pixel art style
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="font-size: 50px; letter-spacing: 3px; text-shadow: 3px 3px 0px #FF6B6B;">ZETRA MARKET EXPANSION TOOLKIT</h1>
        <p style="font-family: 'Space Mono', monospace; color: #FFDE59; font-size: 20px;">PARIS HQ • LEVEL UP YOUR BUSINESS STRATEGY FOR 2025</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Game-style message box
    st.markdown("""
    <div style="
        border: 4px solid #FFDE59;
        background-color: rgba(0,0,0,0.7);
        padding: 20px;
        margin: 20px 0;
        box-shadow: 5px 5px 0px rgba(255,107,107,0.5);
    ">
        <p style="font-family: 'VT323', monospace; font-size: 24px; color: #F5F5F5;">
            WELCOME, ZETRA STRATEGIST! YOUR MISSION: IDENTIFY OPTIMAL B2B MARKET SEGMENTS FOR EXPANSION IN 2025.
            USE THE TOOLS IN THIS CONSOLE TO ANALYZE DATA, EVALUATE OPPORTUNITIES, AND FORMULATE YOUR STRATEGY FROM PARIS HQ.
            <span style="color: #FFDE59;">PRESS START TO BEGIN YOUR QUEST!</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature overview in a 2x2 grid
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            border: 3px solid #4B64FF;
            padding: 15px;
            height: 200px;
            margin: 10px 0;
            background-color: rgba(75,100,255,0.1);
        ">
            <h3 style="color: #4B64FF;">MARKET RADAR</h3>
            <p>Visualize market research and PESTLE analysis factors. Track emerging trends and industry shifts.</p>
            <div style="position: absolute; bottom: 20px;">
                <button style="
                    background-color: transparent;
                    border: 2px solid #4B64FF;
                    color: #4B64FF;
                    font-family: 'VT323', monospace;
                    padding: 5px 15px;
                    cursor: pointer;
                ">EXPLORE →</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="
            border: 3px solid #FF6B6B;
            padding: 15px;
            height: 200px;
            margin: 10px 0;
            background-color: rgba(255,107,107,0.1);
        ">
            <h3 style="color: #FF6B6B;">EVALUATION ENGINE</h3>
            <p>Calculate scores for potential market segments based on key metrics and custom parameters.</p>
            <div style="position: absolute; bottom: 20px;">
                <button style="
                    background-color: transparent;
                    border: 2px solid #FF6B6B;
                    color: #FF6B6B;
                    font-family: 'VT323', monospace;
                    padding: 5px 15px;
                    cursor: pointer;
                ">CALCULATE →</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            border: 3px solid #4DFF4D;
            padding: 15px;
            height: 200px;
            margin: 10px 0;
            background-color: rgba(77,255,77,0.1);
        ">
            <h3 style="color: #4DFF4D;">SEGMENT EXPLORER</h3>
            <p>Filter and analyze potential market segments based on multiple criteria and parameters.</p>
            <div style="position: absolute; bottom: 20px;">
                <button style="
                    background-color: transparent;
                    border: 2px solid #4DFF4D;
                    color: #4DFF4D;
                    font-family: 'VT323', monospace;
                    padding: 5px 15px;
                    cursor: pointer;
                ">DISCOVER →</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="
            border: 3px solid #FFDE59;
            padding: 15px;
            height: 200px;
            margin: 10px 0;
            background-color: rgba(255,222,89,0.1);
        ">
            <h3 style="color: #FFDE59;">STRATEGY BUILDER</h3>
            <p>Visualize and present your selected target segments and corresponding entry strategies.</p>
            <div style="position: absolute; bottom: 20px;">
                <button style="
                    background-color: transparent;
                    border: 2px solid #FFDE59;
                    color: #FFDE59;
                    font-family: 'VT323', monospace;
                    padding: 5px 15px;
                    cursor: pointer;
                ">STRATEGIZE →</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Start button
    st.markdown("""
    <div style="text-align: center; margin-top: 30px;">
        <button style="
            background-color: #FF6B6B;
            border: none;
            color: white;
            padding: 15px 40px;
            font-family: 'VT323', monospace;
            font-size: 28px;
            cursor: pointer;
            box-shadow: 5px 5px 0px rgba(0,0,0,0.3);
            margin: 20px auto;
        ">START MISSION</button>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats at the bottom
    st.markdown("""
    <div style="
        display: flex;
        justify-content: space-between;
        margin-top: 40px;
        border-top: 2px dashed #FFDE59;
        padding-top: 20px;
    ">
        <div style="text-align: center;">
            <p style="color: #FFDE59; font-family: 'VT323', monospace; font-size: 20px;">INDUSTRIES</p>
            <p style="font-size: 28px; font-family: 'VT323', monospace;">10</p>
        </div>
        <div style="text-align: center;">
            <p style="color: #FFDE59; font-family: 'VT323', monospace; font-size: 20px;">SEGMENTS</p>
            <p style="font-size: 28px; font-family: 'VT323', monospace;">78</p>
        </div>
        <div style="text-align: center;">
            <p style="color: #FFDE59; font-family: 'VT323', monospace; font-size: 20px;">METRICS</p>
            <p style="font-size: 28px; font-family: 'VT323', monospace;">24</p>
        </div>
        <div style="text-align: center;">
            <p style="color: #FFDE59; font-family: 'VT323', monospace; font-size: 20px;">TRENDS</p>
            <p style="font-size: 28px; font-family: 'VT323', monospace;">10</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def market_overview():
    st.markdown("<h1>ZETRA MARKET OVERVIEW & PESTLE ANALYSIS</h1>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🌐 INDUSTRY DATA", "🧭 PESTLE FACTORS"])
    
    with tab1:
        st.markdown("<h2>2025 INDUSTRY LANDSCAPE</h2>", unsafe_allow_html=True)
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Industries", "10", "Level 1")
        with col2:
            avg_market_size = int(industry_data["Market Size (millions)"].mean())
            st.metric("Avg Market Size", f"${avg_market_size}M", "+12%")
        with col3:
            avg_growth = round(industry_data["Growth Rate (%)"].mean(), 1)
            st.metric("Avg Growth Rate", f"{avg_growth}%", "+2.3%")
        with col4:
            avg_ai = round(industry_data["AI Adoption (%)"].mean(), 1)
            st.metric("Avg AI Adoption", f"{avg_ai}%", "+15.7%")
        
        # Industry comparison chart
        st.markdown("<h3>INDUSTRY COMPARISON</h3>", unsafe_allow_html=True)
        
        # Let user select metrics to view
        metrics = ["Market Size (millions)", "Growth Rate (%)", "AI Adoption (%)", 
                  "Sustainability Focus (%)", "Profitability (%)", "Competition Level (%)",
                  "Barriers to Entry (%)"]
        
        selected_metrics = st.multiselect(
            "SELECT METRICS TO COMPARE",
            metrics,
            default=["Market Size (millions)", "Growth Rate (%)"]
        )
        
        if selected_metrics:
            # Create radar chart with Plotly
            fig = go.Figure()
            
            for industry in industry_data["Industry"]:
                industry_data_filtered = industry_data[industry_data["Industry"] == industry]
                
                values = [industry_data_filtered[metric].values[0] for metric in selected_metrics]
                # Add the first value again to close the loop
                values.append(values[0])
                
                # Add the category names with the first one repeated at the end
                categories = selected_metrics + [selected_metrics[0]]
                
                fig.add_trace(go.Scatterpolar(
                    r=values,
                    theta=categories,
                    fill='toself',
                    name=industry
                ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, max([industry_data[metric].max() for metric in selected_metrics]) * 1.1]
                    )
                ),
                showlegend=True,
                legend=dict(font=dict(family="VT323", size=14)),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family="VT323", color="#FFDE59"),
                height=600
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Display data table with retro styling
            st.markdown("""
            <h3>RAW DATA</h3>
            <div style="border: 3px solid #FFDE59; padding: 10px; overflow-x: auto;">
            """, unsafe_allow_html=True)
            
            styled_df = industry_data[["Industry"] + selected_metrics]
            st.dataframe(styled_df, use_container_width=True)
    
    with tab2:
        st.markdown("<h2>PESTLE ANALYSIS DASHBOARD</h2>", unsafe_allow_html=True)
        
        # Filter by category
        categories = pestle_data["Category"].unique()
        selected_category = st.selectbox("SELECT CATEGORY", categories)
        
        filtered_pestle = pestle_data[pestle_data["Category"] == selected_category]
        
        # Impact vs Certainty scatter plot
        st.markdown("<h3>IMPACT VS CERTAINTY MATRIX</h3>", unsafe_allow_html=True)
        
        fig = px.scatter(
            filtered_pestle,
            x="Certainty (%)",
            y="Impact (1-10)",
            color="Timeframe",
            size="Impact (1-10)",
            hover_name="Factor",
            color_discrete_sequence=["#FFDE59", "#FF6B6B", "#4B64FF"],
            size_max=20
        )
        
        fig.update_layout(
            xaxis_title="Certainty (%)",
            yaxis_title="Impact (1-10)",
            legend_title="Timeframe",
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
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Impact by factor bar chart
        st.markdown("<h3>FACTOR IMPACT RANKING</h3>", unsafe_allow_html=True)
        
        # Sort by impact
        sorted_pestle = filtered_pestle.sort_values("Impact (1-10)", ascending=False)
        
        fig = px.bar(
            sorted_pestle,
            x="Factor",
            y="Impact (1-10)",
            color="Timeframe",
            color_discrete_sequence=["#FFDE59", "#FF6B6B", "#4B64FF"],
            text="Impact (1-10)"
        )
        
        fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
        
        fig.update_layout(
            xaxis_title="Factor",
            yaxis_title="Impact (1-10)",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0.2)',
            font=dict(family="VT323", color="#FFDE59"),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # 2025 Trends section
        st.markdown("<h3>2025 KEY TRENDS</h3>", unsafe_allow_html=True)
        
        # Trend adoption rates
        fig = px.bar(
            trends_data.sort_values("Adoption Rate (%)", ascending=False),
            x="Trend",
            y="Adoption Rate (%)",
            color="Time to Mainstream",
            color_discrete_sequence=["#4DFF4D", "#FFDE59", "#FF6B6B", "#4B64FF"],
            text="Adoption Rate (%)"
        )
        
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        
        fig.update_layout(
            xaxis_title="Trend",
            yaxis_title="Adoption Rate (%)",
            legend_title="Time to Mainstream",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0.2)',
            font=dict(family="VT323", color="#FFDE59"),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)

def segment_explorer():
    st.markdown("<h1>ZETRA SEGMENT EXPLORER</h1>", unsafe_allow_html=True)
    
    # Game-style intro
    st.markdown("""
    <div style="
        border: 4px solid #4DFF4D;
        background-color: rgba(0,0,0,0.7);
        padding: 20px;
        margin: 20px 0;
        box-shadow: 5px 5px 0px rgba(77,255,77,0.5);
    ">
        <p style="font-family: 'VT323', monospace; font-size: 24px; color: #F5F5F5;">
            SEGMENT EXPLORER ACTIVATED! FILTER THROUGH POTENTIAL B2B SEGMENTS USING THE CONTROLS BELOW.
            <span style="color: #4DFF4D;">FIND THE HIDDEN OPPORTUNITIES FOR YOUR EXPANSION QUEST!</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filters
    st.markdown("<h2>FILTER CONTROLS</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_industries = st.multiselect(
            "INDUSTRIES",
            segment_data["Industry"].unique(),
            default=[]
        )
    
    with col2:
        selected_sizes = st.multiselect(
            "COMPANY SIZES",
            segment_data["Company Size"].unique(),
            default=[]
        )
    
    with col3:
        selected_regions = st.multiselect(
            "REGIONS",
            segment_data["Region"].unique(),
            default=[]
        )
    
    # Numeric filters
    st.markdown("<h3>METRIC THRESHOLDS</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        min_market_size = st.slider(
            "MINIMUM MARKET SIZE (MILLIONS $)",
            int(segment_data["Market Size (millions)"].min()),
            int(segment_data["Market Size (millions)"].max()),
            int(segment_data["Market Size (millions)"].min())
        )
        
        min_growth = st.slider(
            "MINIMUM GROWTH RATE (%)",
            float(segment_data["CAGR (%)"].min()),
            float(segment_data["CAGR (%)"].max()),
            float(segment_data["CAGR (%)"].min())
        )
    
    with col2:
        min_profit = st.slider(
            "MINIMUM PROFITABILITY (%)",
            float(segment_data["Profitability (%)"].min()),
            float(segment_data["Profitability (%)"].max()),
            float(segment_data["Profitability (%)"].min())
        )
        
        max_competition = st.slider(
            "MAXIMUM COMPETITIVE INTENSITY",
            float(segment_data["Competitive Intensity"].min()),
            float(segment_data["Competitive Intensity"].max()),
            float(segment_data["Competitive Intensity"].max())
        )
    
    # Apply filters
    filtered_data = segment_data.copy()
    
    if selected_industries:
        filtered_data = filtered_data[filtered_data["Industry"].isin(selected_industries)]
    
    if selected_sizes:
        filtered_data = filtered_data[filtered_data["Company Size"].isin(selected_sizes)]
    
    if selected_regions:
        filtered_data = filtered_data[filtered_data["Region"].isin(selected_regions)]
    
    # Apply numeric filters
    filtered_data = filtered_data[
        (filtered_data["Market Size (millions)"] >= min_market_size) &
        (filtered_data["CAGR (%)"] >= min_growth) &
        (filtered_data["Profitability (%)"] >= min_profit) &
        (filtered_data["Competitive Intensity"] <= max_competition)
    ]
    
    # Results
    st.markdown(f"""
    <h2>SEGMENTS DISCOVERED: {len(filtered_data)}</h2>
    """, unsafe_allow_html=True)
    
    if len(filtered_data) > 0:
        # Segment scatter plot
        st.markdown("<h3>SEGMENT OPPORTUNITY MAP</h3>", unsafe_allow_html=True)
        
        plot_x = st.selectbox("X-AXIS METRIC", 
                           ["Market Size (millions)", "CAGR (%)", "Profitability (%)", 
                            "Competitive Intensity", "Technology Maturity", "AI Readiness", "Sustainability Score"],
                           index=0)
        
        plot_y = st.selectbox("Y-AXIS METRIC", 
                           ["Market Size (millions)", "CAGR (%)", "Profitability (%)", 
                            "Competitive Intensity", "Technology Maturity", "AI Readiness", "Sustainability Score"],
                           index=1)
        
        color_by = st.selectbox("COLOR BY", 
                             ["Industry", "Company Size", "Region"],
                             index=0)
        
        # Create scatter plot
        fig = px.scatter(
            filtered_data,
            x=plot_x,
            y=plot_y,
            color=color_by,
            size="Market Size (millions)",
            hover_name=color_by,
            hover_data=["Market Size (millions)", "CAGR (%)", "Profitability (%)"],
            size_max=30
        )
        
        fig.update_layout(
            title=f"{plot_y} vs {plot_x} by {color_by}",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0.2)',
            font=dict(family="VT323", color="#FFDE59"),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            height=600
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Top segments table
        st.markdown("<h3>TOP SEGMENTS</h3>", unsafe_allow_html=True)
        
        # Calculate opportunity score
        filtered_data["Opportunity Score"] = (
            filtered_data["Market Size (millions)"] / filtered_data["Market Size (millions)"].max() * 0.3 +
            filtered_data["CAGR (%)"] / filtered_data["CAGR (%)"].max() * 0.3 +
            filtered_data["Profitability (%)"] / filtered_data["Profitability (%)"].max() * 0.3 +
            (1 - filtered_data["Competitive Intensity"] / filtered_data["Competitive Intensity"].max()) * 0.1
        ) * 100
        
        # Display top 10 segments by opportunity score
        top_segments = filtered_data.sort_values("Opportunity Score", ascending=False).head(10)
        
        # Add a pixel-style border to the table
        st.markdown("""
        <div style="border: 3px solid #FFDE59; padding: 10px; overflow-x: auto;">
        """, unsafe_allow_html=True)
        
        display_cols = ["Industry", "Company Size", "Region", "Market Size (millions)", 
                        "CAGR (%)", "Profitability (%)", "Competitive Intensity", "Opportunity Score"]
        
        st.dataframe(
            top_segments[display_cols].style.format({
                "Market Size (millions)": "${:,.0f}M",
                "CAGR (%)": "{:.1f}%",
                "Profitability (%)": "{:.1f}%",
                "Competitive Intensity": "{:.1f}",
                "Opportunity Score": "{:.1f}"
            }),
            use_container_width=True
        )
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Save segments button
        st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <button style="
                background-color: #4DFF4D;
                border: none;
                color: black;
                padding: 10px 30px;
                font-family: 'VT323', monospace;
                font-size: 20px;
                cursor: pointer;
                box-shadow: 3px 3px 0px rgba(0,0,0,0.3);
            ">SAVE SELECTED SEGMENTS</button>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
            border: 4px solid #FF6B6B;
            background-color: rgba(0,0,0,0.7);
            padding: 20px;
            margin: 20px 0;
            text-align: center;
        ">
            <p style="font-family: 'VT323', monospace; font-size: 28px; color: #FF6B6B;">
                NO SEGMENTS MATCH YOUR CRITERIA!
            </p>
            <p style="font-family: 'Space Mono', monospace; font-size: 16px; color: #F5F5F5;">
                TRY ADJUSTING YOUR FILTERS TO DISCOVER MORE SEGMENTS.
            </p>
        </div>
        """, unsafe_allow_html=True)

def evaluation_tool():
    st.markdown("<h1>ZETRA SEGMENT EVALUATION TOOL</h1>", unsafe_allow_html=True)
    
    # Game-style intro
    st.markdown("""
    <div style="
        border: 4px solid #FF6B6B;
        background-color: rgba(0,0,0,0.7);
        padding: 20px;
        margin: 20px 0;
        box-shadow: 5px 5px 0px rgba(255,107,107,0.5);
    ">
        <p style="font-family: 'VT323', monospace; font-size: 24px; color: #F5F5F5;">
            EVALUATION ENGINE ACTIVATED! INPUT YOUR SEGMENT DATA AND ASSIGN WEIGHTS TO DETERMINE THE OPTIMAL TARGET.
            <span style="color: #FF6B6B;">YOUR STRATEGIC DECISIONS WILL AFFECT YOUR MARKET EXPANSION SUCCESS!</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create evaluation form
    st.markdown("<h2>SEGMENT INPUT</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        segment_name = st.text_input("SEGMENT NAME", "Enterprise Software - North America")
        
        market_size = st.number_input(
            "MARKET SIZE (MILLIONS $)",
            min_value=50,
            max_value=10000,
            value=2500
        )
        
        growth_rate = st.number_input(
            "GROWTH RATE (%)",
            min_value=0.0,
            max_value=50.0,
            value=12.5
        )
        
        profitability = st.number_input(
            "PROFITABILITY (%)",
            min_value=0.0,
            max_value=50.0,
            value=18.5
        )
        
        competitive_intensity = st.slider(
            "COMPETITIVE INTENSITY (1-100)",
            min_value=1,
            max_value=100,
            value=65
        )
    
    with col2:
        market_accessibility = st.slider(
            "MARKET ACCESSIBILITY (1-100)",
            min_value=1,
            max_value=100,
            value=75
        )
        
        ai_readiness = st.slider(
            "AI READINESS (1-100)",
            min_value=1,
            max_value=100,
            value=80
        )
        
        sustainability_focus = st.slider(
            "SUSTAINABILITY FOCUS (1-100)",
            min_value=1,
            max_value=100,
            value=70
        )
        
        strategic_fit = st.slider(
            "STRATEGIC FIT (1-100)",
            min_value=1,
            max_value=100,
            value=85
        )
    
    # Weight assignment
    st.markdown("<h2>EVALUATION WEIGHTS</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style="font-family: 'Space Mono', monospace; color: #F5F5F5;">
        Assign weights to each factor (total must equal 100%)
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        market_size_weight = st.slider(
            "MARKET SIZE WEIGHT (%)",
            min_value=5,
            max_value=40,
            value=20
        )
        
        growth_rate_weight = st.slider(
            "GROWTH RATE WEIGHT (%)",
            min_value=5,
            max_value=40,
            value=20
        )
    
    with col2:
        profitability_weight = st.slider(
            "PROFITABILITY WEIGHT (%)",
            min_value=5,
            max_value=40,
            value=15
        )
        
        competitive_weight = st.slider(
            "COMPETITIVE INTENSITY WEIGHT (%)",
            min_value=5,
            max_value=30,
            value=10
        )
    
    with col3:
        accessibility_weight = st.slider(
            "MARKET ACCESSIBILITY WEIGHT (%)",
            min_value=5,
            max_value=30,
            value=10
        )
        
        ai_weight = st.slider(
            "AI READINESS WEIGHT (%)",
            min_value=5,
            max_value=30,
            value=10
        )
    
    with col4:
        sustainability_weight = st.slider(
            "SUSTAINABILITY WEIGHT (%)",
            min_value=5,
            max_value=30,
            value=5
        )
        
        strategic_weight = st.slider(
            "STRATEGIC FIT WEIGHT (%)",
            min_value=5,
            max_value=30,
            value=10
        )
    
    # Calculate total weight
    total_weight = (market_size_weight + growth_rate_weight + profitability_weight + 
                   competitive_weight + accessibility_weight + ai_weight + 
                   sustainability_weight + strategic_weight)
    
    # Display total weight
    if total_weight != 100:
        st.markdown(f"""
        <div style="
            background-color: rgba(255,107,107,0.2);
            border: 2px solid #FF6B6B;
            padding: 10px;
            margin: 10px 0;
        ">
            <p style="font-family: 'VT323', monospace; color: #FF6B6B; font-size: 18px;">
                WARNING: TOTAL WEIGHT = {total_weight}%. PLEASE ADJUST TO EQUAL 100%.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Calculate button
    calculate_button = st.button("CALCULATE SCORE")
    
    if calculate_button and total_weight == 100:
        # Normalize inputs to 0-1 scale
        market_size_norm = market_size / 10000  # Assuming 10000M is max
        growth_rate_norm = growth_rate / 50     # Assuming 50% is max
        profitability_norm = profitability / 50  # Assuming 50% is max
        competitive_norm = 1 - (competitive_intensity / 100)  # Lower is better
        accessibility_norm = market_accessibility / 100
        ai_norm = ai_readiness / 100
        sustainability_norm = sustainability_focus / 100
        strategic_norm = strategic_fit / 100
        
        # Calculate weighted score
        weighted_score = (
            market_size_norm * market_size_weight / 100 +
            growth_rate_norm * growth_rate_weight / 100 +
            profitability_norm * profitability_weight / 100 +
            competitive_norm * competitive_weight / 100 +
            accessibility_norm * accessibility_weight / 100 +
            ai_norm * ai_weight / 100 +
            sustainability_norm * sustainability_weight / 100 +
            strategic_norm * strategic_weight / 100
        ) * 100
        
        # Display results
        st.markdown("<h2>EVALUATION RESULTS</h2>", unsafe_allow_html=True)
        
        # Pixel art score display
        st.markdown(f"""
        <div style="
            text-align: center;
            margin: 20px 0;
            padding: 20px;
            border: 4px solid #FFDE59;
            background-color: rgba(0,0,0,0.5);
        ">
            <h3 style="color: #FFDE59;">SEGMENT SCORE</h3>
            <p style="font-family: 'VT323', monospace; font-size: 72px; color: #FFDE59; text-shadow: 3px 3px 0px #FF6B6B;">
                {weighted_score:.1f}
            </p>
            <p style="font-family: 'Space Mono', monospace; font-size: 18px; color: #F5F5F5;">
                {'HIGH POTENTIAL' if weighted_score >= 75 else 'MEDIUM POTENTIAL' if weighted_score >= 50 else 'LOW POTENTIAL'}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Factor breakdown
        st.markdown("<h3>FACTOR BREAKDOWN</h3>", unsafe_allow_html=True)
        
        # Create data for the bar chart
        factors = [
            "Market Size", "Growth Rate", "Profitability", "Competitive Position",
            "Market Accessibility", "AI Readiness", "Sustainability", "Strategic Fit"
        ]
        
        normalized_scores = [
            market_size_norm * 100,
            growth_rate_norm * 100,
            profitability_norm * 100,
            competitive_norm * 100,
            accessibility_norm * 100,
            ai_norm * 100,
            sustainability_norm * 100,
            strategic_norm * 100
        ]
        
        weighted_contributions = [
            market_size_norm * market_size_weight,
            growth_rate_norm * growth_rate_weight,
            profitability_norm * profitability_weight,
            competitive_norm * competitive_weight,
            accessibility_norm * accessibility_weight,
            ai_norm * ai_weight,
            sustainability_norm * sustainability_weight,
            strategic_norm * strategic_weight
        ]
        
        weights = [
            market_size_weight,
            growth_rate_weight,
            profitability_weight,
            competitive_weight,
            accessibility_weight,
            ai_weight,
            sustainability_weight,
            strategic_weight
        ]
        
        # Create breakdown chart
        breakdown_df = pd.DataFrame({
            'Factor': factors,
            'Normalized Score': normalized_scores,
            'Weight': weights,
            'Contribution': weighted_contributions
        })
        
        # Sort by contribution
        breakdown_df = breakdown_df.sort_values('Contribution', ascending=False)
        
        fig = px.bar(
            breakdown_df,
            x='Factor',
            y='Contribution',
            text='Weight',
            color='Normalized Score',
            color_continuous_scale=['#FF6B6B', '#FFDE59', '#4DFF4D'],
            labels={'Contribution': 'Weighted Contribution', 'Weight': 'Weight (%)'}
        )
        
        fig.update_traces(texttemplate='%{text}%', textposition='outside')
        
        fig.update_layout(
            title="Factor Contribution to Overall Score",
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
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Save button
        st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <button style="
                background-color: #FFDE59;
                border: none;
                color: black;
                padding: 10px 30px;
                font-family: 'VT323', monospace;
                font-size: 20px;
                cursor: pointer;
                box-shadow: 3px 3px 0px rgba(0,0,0,0.3);
            ">SAVE EVALUATION RESULTS</button>
        </div>
        """, unsafe_allow_html=True)

def target_strategy():
    st.markdown("<h1>ZETRA TARGET SEGMENT STRATEGY</h1>", unsafe_allow_html=True)
    
    # Game-style intro
    st.markdown("""
    <div style="
        border: 4px solid #FFDE59;
        background-color: rgba(0,0,0,0.7);
        padding: 20px;
        margin: 20px 0;
        box-shadow: 5px 5px 0px rgba(255,222,89,0.5);
    ">
        <p style="font-family: 'VT323', monospace; font-size: 24px; color: #F5F5F5;">
            STRATEGY BUILDER ACTIVATED! VISUALIZE AND PRESENT YOUR TARGET SEGMENTS AND ENTRY STRATEGIES.
            <span style="color: #FFDE59;">PREPARE FOR THE FINAL BOSS: MARKET ENTRY!</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Example selected segments (normally would come from saved selections)
    selected_segments = pd.DataFrame({
        'Segment': [
            'Enterprise Software - North America',
            'Healthcare Tech - Europe',
            'FinTech - Asia Pacific'
        ],
        'Score': [82.5, 76.8, 71.3],
        'Market Size (millions)': [2500, 1800, 3200],
        'Growth Rate (%)': [12.5, 15.2, 18.6],
        'Profitability (%)': [18.5, 15.8, 14.2],
        'Competitive Intensity': [65, 55, 75],
        'Strategic Fit': [85, 80, 70]
    })
    
    # Display selected segments
    st.markdown("<h2>SELECTED TARGET SEGMENTS</h2>", unsafe_allow_html=True)
    
    # Create comparison chart
    fig = go.Figure()
    
    metrics = ['Score', 'Market Size (millions)', 'Growth Rate (%)', 
               'Profitability (%)', 'Competitive Intensity', 'Strategic Fit']
    
    for segment in selected_segments['Segment']:
        segment_data = selected_segments[selected_segments['Segment'] == segment]
        
        # Normalize values for radar chart
        values = []
        for metric in metrics:
            if metric == 'Score':
                values.append(segment_data[metric].values[0] / 100)  # Normalize to 0-1
            elif metric == 'Market Size (millions)':
                values.append(segment_data[metric].values[0] / 5000)  # Normalize to 0-1
            elif metric == 'Growth Rate (%)':
                values.append(segment_data[metric].values[0] / 25)  # Normalize to 0-1
            elif metric == 'Profitability (%)':
                values.append(segment_data[metric].values[0] / 25)  # Normalize to 0-1
            elif metric == 'Competitive Intensity':
                values.append(1 - segment_data[metric].values[0] / 100)  # Inverse and normalize to 0-1
            elif metric == 'Strategic Fit':
                values.append(segment_data[metric].values[0] / 100)  # Normalize to 0-1
        
        # Add the first value again to close the loop
        values.append(values[0])
        
        # Add the category names with the first one repeated at the end
        categories = metrics + [metrics[0]]
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=segment
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )
        ),
        showlegend=True,
        legend=dict(font=dict(family="VT323", size=14)),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="VT323", color="#FFDE59"),
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Segment scores
    st.markdown("<h2>SEGMENT SCORES</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    # Display segment cards with pixel art style
    for i, (idx, row) in enumerate(selected_segments.iterrows()):
        with [col1, col2, col3][i]:
            st.markdown(f"""
            <div style="
                border: 4px solid {'#4DFF4D' if row['Score'] >= 80 else '#FFDE59' if row['Score'] >= 70 else '#FF6B6B'};
                padding: 15px;
                margin: 10px 0;
                background-color: rgba(0,0,0,0.5);
                text-align: center;
            ">
                <h3 style="font-size: 22px; margin-bottom: 10px;">{row['Segment']}</h3>
                <div style="font-family: 'VT323', monospace; font-size: 42px; margin: 15px 0; color: {'#4DFF4D' if row['Score'] >= 80 else '#FFDE59' if row['Score'] >= 70 else '#FF6B6B'};">
                    {row['Score']:.1f}
                </div>
                <p style="font-family: 'Space Mono', monospace; font-size: 14px; margin: 5px 0;">
                    Market: ${row['Market Size (millions)']:.0f}M
                </p>
                <p style="font-family: 'Space Mono', monospace; font-size: 14px; margin: 5px 0;">
                    Growth: {row['Growth Rate (%)']:.1f}%
                </p>
                <p style="font-family: 'Space Mono', monospace; font-size: 14px; margin: 5px 0;">
                    Profit: {row['Profitability (%)']:.1f}%
                </p>
                <div style="margin-top: 15px;">
                    <button style="
                        background-color: {'#4DFF4D' if row['Score'] >= 80 else '#FFDE59' if row['Score'] >= 70 else '#FF6B6B'};
                        border: none;
                        color: black;
                        padding: 5px 15px;
                        font-family: 'VT323', monospace;
                        font-size: 16px;
                        cursor: pointer;
                    ">VIEW DETAILS</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Entry strategy section
    st.markdown("<h2>ENTRY STRATEGY BUILDER</h2>", unsafe_allow_html=True)
    
    # Strategy selection
    selected_segment = st.selectbox(
        "SELECT ZETRA SEGMENT FOR STRATEGY DEVELOPMENT",
        selected_segments['Segment']
    )
    
    # Strategy components
    st.markdown("<h3>STRATEGY COMPONENTS</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        entry_approach = st.selectbox(
            "MARKET ENTRY APPROACH",
            ["Direct Sales", "Channel Partners", "Acquisition", "Joint Venture", "Licensing"]
        )
        
        target_customers = st.multiselect(
            "TARGET CUSTOMER PROFILES",
            ["C-Suite Executives", "IT Decision Makers", "Department Heads", 
             "Operations Managers", "Finance Directors", "HR Leaders"],
            default=["C-Suite Executives", "IT Decision Makers"]
        )
        
        value_proposition = st.text_area(
            "VALUE PROPOSITION",
            "Our AI-powered solution optimizes business processes while reducing operational costs by 30% and increasing productivity by 25%."
        )
    
    with col2:
        competitive_advantages = st.multiselect(
            "COMPETITIVE ADVANTAGES",
            ["Advanced AI Capabilities", "Seamless Integration", "Cost Leadership", 
             "Superior User Experience", "Industry Expertise", "Data Security"],
            default=["Advanced AI Capabilities", "Superior User Experience"]
        )
        
        success_metrics = st.multiselect(
            "SUCCESS METRICS",
            ["Market Share", "Revenue Growth", "Customer Acquisition", 
             "Profitability", "Brand Recognition", "User Adoption"],
            default=["Market Share", "Revenue Growth"]
        )
        
        timeline = st.selectbox(
            "IMPLEMENTATION TIMELINE",
            ["Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026"]
        )
    
    # Strategy summary
    st.markdown("<h3>STRATEGY SUMMARY</h3>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="
        border: 4px solid #FFDE59;
        padding: 20px;
        margin: 20px 0;
        background-color: rgba(0,0,0,0.5);
    ">
        <h4 style="text-align: center; color: #FFDE59; font-size: 24px; margin-bottom: 20px;">
            ZETRA MARKET ENTRY STRATEGY: {selected_segment}
        </h4>
        
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
            <div style="width: 48%; margin-bottom: 15px;">
                <h5 style="color: #4B64FF; font-size: 18px;">ENTRY APPROACH</h5>
                <p style="font-family: 'Space Mono', monospace; font-size: 15px;">{entry_approach}</p>
            </div>
            
            <div style="width: 48%; margin-bottom: 15px;">
                <h5 style="color: #4B64FF; font-size: 18px;">TARGET CUSTOMERS</h5>
                <p style="font-family: 'Space Mono', monospace; font-size: 15px;">{", ".join(target_customers)}</p>
            </div>
            
            <div style="width: 48%; margin-bottom: 15px;">
                <h5 style="color: #4B64FF; font-size: 18px;">VALUE PROPOSITION</h5>
                <p style="font-family: 'Space Mono', monospace; font-size: 15px;">{value_proposition}</p>
            </div>
            
            <div style="width: 48%; margin-bottom: 15px;">
                <h5 style="color: #4B64FF; font-size: 18px;">COMPETITIVE ADVANTAGES</h5>
                <p style="font-family: 'Space Mono', monospace; font-size: 15px;">{", ".join(competitive_advantages)}</p>
            </div>
            
            <div style="width: 48%; margin-bottom: 15px;">
                <h5 style="color: #4B64FF; font-size: 18px;">SUCCESS METRICS</h5>
                <p style="font-family: 'Space Mono', monospace; font-size: 15px;">{", ".join(success_metrics)}</p>
            </div>
            
            <div style="width: 48%; margin-bottom: 15px;">
                <h5 style="color: #4B64FF; font-size: 18px;">IMPLEMENTATION TIMELINE</h5>
                <p style="font-family: 'Space Mono', monospace; font-size: 15px;">{timeline}</p>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 20px;">
            <button style="
                background-color: #FFDE59;
                border: none;
                color: black;
                padding: 10px 30px;
                font-family: 'VT323', monospace;
                font-size: 20px;
                cursor: pointer;
                box-shadow: 3px 3px 0px rgba(0,0,0,0.3);
            ">EXPORT STRATEGY</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Implementation roadmap
    st.markdown("<h3>IMPLEMENTATION ROADMAP</h3>", unsafe_allow_html=True)
    
    # Create timeline chart
    phases = ["Research & Planning", "Team Assembly", "Initial Market Entry", 
             "Scale Operations", "Expand Product Line"]
    
    phase_starts = [0, 1, 3, 6, 9]
    phase_durations = [1, 2, 3, 3, 3]
    
    # Create a Gantt-like chart
    fig = go.Figure()
    
    for i, phase in enumerate(phases):
        fig.add_trace(go.Bar(
            x=[phase_durations[i]],
            y=[phase],
            orientation='h',
            marker=dict(
                color=['#4B64FF', '#4DFF4D', '#FFDE59', '#FF6B6B', '#FF00FF'][i % 5],
                line=dict(width=2, color='#000000')
            ),
            text=f"{phase_durations[i]} months",
            textposition='inside',
            insidetextanchor='middle',
            width=0.6,
            base=phase_starts[i]
        ))
    
    fig.update_layout(
        title="Implementation Timeline (Months)",
        xaxis=dict(
            title="Timeline (Months)",
            showgrid=True,
            gridcolor='rgba(255,255,255,0.1)',
            tickvals=list(range(0, 13, 1)),
            range=[0, 12]
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
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Investment and ROI projection
    st.markdown("<h3>INVESTMENT & ROI PROJECTION</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Create sample financial data
        quarters = ["Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026", "Q3 2026"]
        investment = [800, 500, 300, 200, 150, 100]
        revenue = [0, 200, 600, 1200, 2000, 2800]
        profit = [-800, -300, 300, 1000, 1850, 2700]
        
        # Create financial chart
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
            title="Financial Projection ($000s)",
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
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # ROI metrics
        st.markdown("""
        <div style="
            border: 4px solid #4DFF4D;
            padding: 20px;
            margin: 20px 0;
            background-color: rgba(0,0,0,0.5);
            height: 400px;
        ">
            <h4 style="text-align: center; color: #4DFF4D; font-size: 24px; margin-bottom: 20px;">
                ROI METRICS
            </h4>
            
            <div style="margin-bottom: 20px;">
                <p style="font-family: 'VT323', monospace; font-size: 18px; margin-bottom: 5px;">BREAK-EVEN POINT</p>
                <div style="
                    background-color: rgba(77,255,77,0.2);
                    padding: 10px;
                    font-family: 'Space Mono', monospace;
                    font-size: 20px;
                    text-align: center;
                ">Q4 2025</div>
            </div>
            
            <div style="margin-bottom: 20px;">
                <p style="font-family: 'VT323', monospace; font-size: 18px; margin-bottom: 5px;">TOTAL INVESTMENT</p>
                <div style="
                    background-color: rgba(255,107,107,0.2);
                    padding: 10px;
                    font-family: 'Space Mono', monospace;
                    font-size: 20px;
                    text-align: center;
                ">$2,050,000</div>
            </div>
            
            <div style="margin-bottom: 20px;">
                <p style="font-family: 'VT323', monospace; font-size: 18px; margin-bottom: 5px;">PROJECTED 12-MONTH ROI</p>
                <div style="
                    background-color: rgba(255,222,89,0.2);
                    padding: 10px;
                    font-family: 'Space Mono', monospace;
                    font-size: 20px;
                    text-align: center;
                ">132%</div>
            </div>
            
            <div style="margin-bottom: 20px;">
                <p style="font-family: 'VT323', monospace; font-size: 18px; margin-bottom: 5px;">PROJECTED MARKET SHARE</p>
                <div style="
                    background-color: rgba(75,100,255,0.2);
                    padding: 10px;
                    font-family: 'Space Mono', monospace;
                    font-size: 20px;
                    text-align: center;
                ">8.5%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Final button
    st.markdown("""
    <div style="text-align: center; margin-top: 30px;">
        <button style="
            background-color: #4DFF4D;
            border: none;
            color: black;
            padding: 15px 40px;
            font-family: 'VT323', monospace;
            font-size: 28px;
            cursor: pointer;
            box-shadow: 5px 5px 0px rgba(0,0,0,0.3);
            margin: 20px auto;
        ">FINALIZE STRATEGY</button>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()