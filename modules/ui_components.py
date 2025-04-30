import streamlit as st
from PIL import Image
import base64
import random
import io
import numpy as np

def load_css():
    """
    Load custom CSS to apply the retro gaming aesthetic.
    """
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
        
        /* Slider styling */
        .stSlider > div > div > div {
            background-color: var(--main-coral);
        }
        
        .stSlider > div > div > div > div {
            background-color: var(--main-yellow);
        }
        
        /* Dataframe styling */
        .dataframe {
            font-family: 'Space Mono', monospace;
            border: 2px solid var(--main-yellow);
        }
        
        .dataframe th {
            background-color: var(--main-coral);
            color: var(--light-text);
            padding: 8px;
            font-family: 'VT323', monospace;
            font-size: 16px;
            text-transform: uppercase;
        }
        
        .dataframe td {
            padding: 8px;
            border: 1px solid var(--main-yellow);
        }
        
        /* Form inputs */
        input, textarea {
            background-color: var(--dark-bg) !important;
            color: var(--light-text) !important;
            border: 2px solid var(--main-coral) !important;
            font-family: 'Space Mono', monospace !important;
        }
        
        /* Number input */
        .stNumberInput > div > div > input {
            background-color: var(--dark-bg) !important;
            color: var(--light-text) !important;
            border: 2px solid var(--main-yellow) !important;
            font-family: 'Space Mono', monospace !important;
        }
    </style>
    """, unsafe_allow_html=True)

def generate_pixel_background(width=40, height=40, colors=["#1e1e1e", "#2a2a2a"]):
    """
    Generate a simple pixel grid background.
    
    Args:
        width (int): Width of the background image
        height (int): Height of the background image
        colors (list): List of colors to use
        
    Returns:
        str: Base64 encoded PNG image string
    """
    img = Image.new('RGB', (width, height), colors[0])
    pixels = img.load()
    
    for i in range(0, width, 4):
        for j in range(0, height, 4):
            if random.random() > 0.7:  # 30% chance of a different colored pixel
                pixels[i, j] = tuple(int(colors[1].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    
    # Convert PIL Image to base64
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    
    return img_str

def add_bg_from_base64():
    """
    Apply a pixel art background to the Streamlit app.
    """
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

def pixel_container(title, content_function, color="#FFDE59"):
    """
    Create a pixel-bordered container with a specific title.
    
    Args:
        title (str): Container title
        content_function (function): Function to call inside the container
        color (str): Border color
    """
    st.markdown(f"""
    <div style="
        border: 4px solid {color};
        background-color: rgba(0,0,0,0.7);
        padding: 20px;
        margin: 20px 0;
        box-shadow: 5px 5px 0px rgba(0,0,0,0.5);
    ">
        <h3 style="color: {color}; margin-top: 0;">{title}</h3>
    """, unsafe_allow_html=True)
    
    content_function()
    
    st.markdown("</div>", unsafe_allow_html=True)

def pixel_card(title, value, subtitle=None, color="#FFDE59", icon=None):
    """
    Create a pixel-styled card for displaying key metrics.
    
    Args:
        title (str): Card title
        value (str): Main value to display
        subtitle (str, optional): Subtitle or additional info
        color (str): Border and accent color
        icon (str, optional): Icon emoji
    """
    icon_html = f'<span style="font-size: 24px; margin-right: 10px;">{icon}</span>' if icon else ''
    
    st.markdown(f"""
    <div style="
        border: 3px solid {color};
        padding: 15px;
        margin: 10px 0;
        background-color: rgba(0,0,0,0.5);
        text-align: center;
    ">
        <h4 style="font-size: 18px; margin-bottom: 10px; color: {color};">{icon_html}{title}</h4>
        <div style="font-family: 'VT323', monospace; font-size: 32px; margin: 10px 0; color: #F5F5F5;">
            {value}
        </div>
        {f'<p style="font-family: \'Space Mono\', monospace; font-size: 14px; margin: 5px 0; color: {color};">{subtitle}</p>' if subtitle else ''}
    </div>
    """, unsafe_allow_html=True)

def retro_button(label, color="#FFDE59"):
    """
    Create a pixel art styled button.
    
    Args:
        label (str): Button text
        color (str): Button color
        
    Returns:
        bool: True if button is clicked
    """
    button_html = f"""
    <div style="text-align: center; margin: 20px 0;">
        <button style="
            background-color: {color};
            border: none;
            color: black;
            padding: 10px 30px;
            font-family: 'VT323', monospace;
            font-size: 20px;
            cursor: pointer;
            box-shadow: 4px 4px 0px rgba(0,0,0,0.3);
        ">{label}</button>
    </div>
    """
    
    return st.button(label)

def game_header(title, subtitle=None):
    """
    Create a pixel-art style header with title and optional subtitle.
    
    Args:
        title (str): Main title text
        subtitle (str, optional): Subtitle text
    """
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="font-size: 50px; letter-spacing: 3px; text-shadow: 3px 3px 0px #FF6B6B;">{title}</h1>
        {f'<p style="font-family: \'Space Mono\', monospace; color: #FFDE59; font-size: 20px;">{subtitle}</p>' if subtitle else ''}
    </div>
    """, unsafe_allow_html=True)

def game_message(message, color="#FFDE59", highlight_text=None):
    """
    Create a game-style message box.
    
    Args:
        message (str): Message text
        color (str): Border color
        highlight_text (str, optional): Text to highlight in a different color
    """
    if highlight_text:
        message = message.replace(highlight_text, f'<span style="color: {color};">{highlight_text}</span>')
    
    st.markdown(f"""
    <div style="
        border: 4px solid {color};
        background-color: rgba(0,0,0,0.7);
        padding: 20px;
        margin: 20px 0;
        box-shadow: 5px 5px 0px rgba(0,0,0,0.5);
    ">
        <p style="font-family: 'VT323', monospace; font-size: 24px; color: #F5F5F5;">
            {message}
        </p>
    </div>
    """, unsafe_allow_html=True)

def feature_card(title, description, color, button_text="EXPLORE →"):
    """
    Create a feature highlight card with pixel styling.
    
    Args:
        title (str): Feature title
        description (str): Feature description
        color (str): Card border and accent color
        button_text (str): Text for the button
    """
    st.markdown(f"""
    <div style="
        border: 3px solid {color};
        padding: 15px;
        height: 200px;
        margin: 10px 0;
        background-color: rgba({int(color[1:3], 16)},{int(color[3:5], 16)},{int(color[5:7], 16)},0.1);
    ">
        <h3 style="color: {color};">{title}</h3>
        <p>{description}</p>
        <div style="position: absolute; bottom: 20px;">
            <button style="
                background-color: transparent;
                border: 2px solid {color};
                color: {color};
                font-family: 'VT323', monospace;
                padding: 5px 15px;
                cursor: pointer;
            ">{button_text}</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

def pixel_avatar(initials="Z", color_gradient=("#FF6B6B", "#FFDE59"), size=100, label="ZETRA STRATEGIST", subtitle="PARIS HQ"):
    """
    Create a pixelated avatar with initials.
    
    Args:
        initials (str): Initials to display in the avatar
        color_gradient (tuple): Gradient colors
        size (int): Avatar size in pixels
        label (str): Label below the avatar
        subtitle (str): Subtitle below the label
    """
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <div style="
            width: {size}px;
            height: {size}px;
            margin: 0 auto;
            background: linear-gradient(45deg, {color_gradient[0]}, {color_gradient[1]});
            image-rendering: pixelated;
            border: 4px solid {color_gradient[1]};
            box-shadow: 5px 5px 0px rgba(0,0,0,0.5);
        ">
            <div style="
                font-family: 'VT323', monospace;
                font-size: {size*0.42}px;
                color: #121212;
                text-align: center;
                padding-top: {size*0.25}px;
                font-weight: bold;
            ">{initials}</div>
        </div>
        <p style="font-family: 'VT323', monospace; font-size: 20px; margin-top: 10px;">{label}</p>
        <p style="font-family: 'VT323', monospace; font-size: 16px; color: #FF6B6B;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def power_meter(value, label="SYSTEM POWER", color="#FFDE59"):
    """
    Create a stylized power/progress meter.
    
    Args:
        value (float): Value between 0 and 100
        label (str): Meter label
        color (str): Accent color
    """
    st.markdown(f"<h3 style='text-align: center;'>{label}</h3>", unsafe_allow_html=True)
    st.progress(value/100)
    st.markdown(f"""
    <div style='text-align: center; font-family: "VT323", monospace; font-size: 24px; color: {color};'>
        {value}%
    </div>
    """, unsafe_allow_html=True)

def stats_footer(stats, border_color="#FFDE59"):
    """
    Create a stats footer with multiple metrics.
    
    Args:
        stats (dict): Dictionary of stat labels and values
        border_color (str): Border color
    """
    columns = len(stats)
    
    html = f"""
    <div style="
        display: flex;
        justify-content: space-between;
        margin-top: 40px;
        border-top: 2px dashed {border_color};
        padding-top: 20px;
    ">
    """
    
    for label, value in stats.items():
        html += f"""
        <div style="text-align: center;">
            <p style="color: {border_color}; font-family: 'VT323', monospace; font-size: 20px;">{label}</p>
            <p style="font-size: 28px; font-family: 'VT323', monospace;">{value}</p>
        </div>
        """
    
    html += "</div>"
    
    st.markdown(html, unsafe_allow_html=True)

def segment_card(segment_data, score_color="#FFDE59"):
    """
    Create a pixel-styled card for a market segment.
    
    Args:
        segment_data (dict): Dictionary with segment info
        score_color (str): Color based on score
    """
    # Determine color based on score
    if segment_data["Score"] >= 80:
        score_color = "#4DFF4D"  # Green
    elif segment_data["Score"] >= 70:
        score_color = "#FFDE59"  # Yellow
    else:
        score_color = "#FF6B6B"  # Red
    
    st.markdown(f"""
    <div style="
        border: 4px solid {score_color};
        padding: 15px;
        margin: 10px 0;
        background-color: rgba(0,0,0,0.5);
        text-align: center;
    ">
        <h3 style="font-size: 22px; margin-bottom: 10px;">{segment_data["Segment"]}</h3>
        <div style="font-family: 'VT323', monospace; font-size: 42px; margin: 15px 0; color: {score_color};">
            {segment_data["Score"]:.1f}
        </div>
        <p style="font-family: 'Space Mono', monospace; font-size: 14px; margin: 5px 0;">
            Market: ${segment_data["Market Size (millions)"]:.0f}M
        </p>
        <p style="font-family: 'Space Mono', monospace; font-size: 14px; margin: 5px 0;">
            Growth: {segment_data["Growth Rate (%)"]:.1f}%
        </p>
        <p style="font-family: 'Space Mono', monospace; font-size: 14px; margin: 5px 0;">
            Profit: {segment_data["Profitability (%)"]:.1f}%
        </p>
        <div style="margin-top: 15px;">
            <button style="
                background-color: {score_color};
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

def roi_metrics_card(metrics, color="#4DFF4D"):
    """
    Create a pixel-styled card for ROI metrics.
    
    Args:
        metrics (dict): Dictionary of ROI metrics
        color (str): Card accent color
    """
    st.markdown(f"""
    <div style="
        border: 4px solid {color};
        padding: 20px;
        margin: 20px 0;
        background-color: rgba(0,0,0,0.5);
        height: 400px;
    ">
        <h4 style="text-align: center; color: {color}; font-size: 24px; margin-bottom: 20px;">
            ROI METRICS
        </h4>
        
        <div style="margin-bottom: 20px;">
            <p style="font-family: 'VT323', monospace; font-size: 18px; margin-bottom: 5px;">BREAK-EVEN POINT</p>
            <div style="
                background-color: rgba({int(color[1:3], 16)},{int(color[3:5], 16)},{int(color[5:7], 16)},0.2);
                padding: 10px;
                font-family: 'Space Mono', monospace;
                font-size: 20px;
                text-align: center;
            ">{metrics["break_even_point"]}</div>
        </div>
        
        <div style="margin-bottom: 20px;">
            <p style="font-family: 'VT323', monospace; font-size: 18px; margin-bottom: 5px;">TOTAL INVESTMENT</p>
            <div style="
                background-color: rgba(255,107,107,0.2);
                padding: 10px;
                font-family: 'Space Mono', monospace;
                font-size: 20px;
                text-align: center;
            ">${metrics["total_investment"]:,.0f}</div>
        </div>
        
        <div style="margin-bottom: 20px;">
            <p style="font-family: 'VT323', monospace; font-size: 18px; margin-bottom: 5px;">PROJECTED 12-MONTH ROI</p>
            <div style="
                background-color: rgba(255,222,89,0.2);
                padding: 10px;
                font-family: 'Space Mono', monospace;
                font-size: 20px;
                text-align: center;
            ">{metrics["roi_percentage"]:.0f}%</div>
        </div>
        
        <div style="margin-bottom: 20px;">
            <p style="font-family: 'VT323', monospace; font-size: 18px; margin-bottom: 5px;">PROJECTED MARKET SHARE</p>
            <div style="
                background-color: rgba(75,100,255,0.2);
                padding: 10px;
                font-family: 'Space Mono', monospace;
                font-size: 20px;
                text-align: center;
            ">{metrics["market_share"]:.1f}%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def evaluation_result(score, title="SEGMENT SCORE", level_text=None):
    """
    Display evaluation results with pixel styling.
    
    Args:
        score (float): Evaluation score (0-100)
        title (str): Result title
        level_text (str, optional): Classification text
    """
    if level_text is None:
        level_text = 'HIGH POTENTIAL' if score >= 75 else 'MEDIUM POTENTIAL' if score >= 50 else 'LOW POTENTIAL'
    
    st.markdown(f"""
    <div style="
        text-align: center;
        margin: 20px 0;
        padding: 20px;
        border: 4px solid #FFDE59;
        background-color: rgba(0,0,0,0.5);
    ">
        <h3 style="color: #FFDE59;">{title}</h3>
        <p style="font-family: 'VT323', monospace; font-size: 72px; color: #FFDE59; text-shadow: 3px 3px 0px #FF6B6B;">
            {score:.1f}
        </p>
        <p style="font-family: 'Space Mono', monospace; font-size: 18px; color: #F5F5F5;">
            {level_text}
        </p>
    </div>
    """, unsafe_allow_html=True)

def pixelated_favicon(output_path="static/favicon.ico", size=32):
    """
    Generate a pixelated favicon for the application.
    
    Args:
        output_path (str): Path to save the favicon
        size (int): Size of the favicon in pixels
    """
    # Create a simple "Z" favicon with the Zetra colors
    img = Image.new('RGB', (size, size), "#121212")
    pixels = img.load()
    
    # Define a simple Z shape with pixels
    z_shape = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]
    
    # Scale to fit the icon size
    scale = size // len(z_shape)
    
    # Draw the Z with the Zetra colors
    for y, row in enumerate(z_shape):
        for x, pixel in enumerate(row):
            if pixel:
                for sy in range(scale):
                    for sx in range(scale):
                        if x * scale + sx < size and y * scale + sy < size:
                            # Gradient from coral to yellow
                            if y < len(z_shape) // 2:
                                pixels[x * scale + sx, y * scale + sy] = (255, 107, 107)  # Coral
                            else:
                                pixels[x * scale + sx, y * scale + sy] = (255, 222, 89)  # Yellow
    
    # Save the favicon
    img.save(output_path)
    
    return img