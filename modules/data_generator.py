import pandas as pd
import numpy as np
import random

def generate_industry_data():
    """
    Generate synthetic data for industries including market size, growth rates,
    and other key metrics for visualization and analysis.
    
    Returns:
        DataFrame: Pandas DataFrame containing industry metrics
    """
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

def generate_segment_data():
    """
    Generate synthetic data for market segments with various criteria
    including company size, region, market metrics, etc.
    
    Returns:
        DataFrame: Pandas DataFrame containing segment data
    """
    segments = []
    industries = [
        "Software & IT Services", "Manufacturing", "Healthcare", 
        "Financial Services", "Retail", "Energy & Utilities",
        "Telecommunications", "Education", "Professional Services"
    ]
    
    company_sizes = ["Small (10-50)", "Medium (51-500)", "Large (501-5000)", "Enterprise (5000+)"]
    regions = ["North America", "Europe", "Asia Pacific", "Latin America", "Middle East & Africa"]
    
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
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

def generate_pestle_data():
    """
    Generate synthetic PESTLE analysis data with impact scores,
    certainty levels, and timeframes.
    
    Returns:
        DataFrame: Pandas DataFrame containing PESTLE factors
    """
    factors = {
        "Political": ["Regulatory Changes", "Trade Policies", "Political Stability", "Government Initiatives"],
        "Economic": ["Economic Growth", "Interest Rates", "Inflation", "Exchange Rates"],
        "Social": ["Demographic Shifts", "Consumer Behavior", "Work Culture", "Social Values"],
        "Technological": ["AI & Automation", "Cloud Computing", "Cybersecurity", "Digital Transformation"],
        "Legal": ["Data Protection", "Intellectual Property", "Compliance Requirements", "Contract Enforcement"],
        "Environmental": ["Sustainability Regulations", "Carbon Footprint", "Resource Scarcity", "Environmental Standards"]
    }
    
    data = []
    # Set random seed for reproducibility
    np.random.seed(43)
    random.seed(43)
    
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

def generate_trends_data():
    """
    Generate synthetic data for 2025 market trends including
    adoption rates, impact scores, and timeframes.
    
    Returns:
        DataFrame: Pandas DataFrame containing trend data
    """
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
    # Set random seed for reproducibility
    np.random.seed(44)
    random.seed(44)
    
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

def save_sample_data():
    """
    Save sample data to CSV files for offline use or testing.
    """
    industry_data = generate_industry_data()
    segment_data = generate_segment_data()
    pestle_data = generate_pestle_data()
    trends_data = generate_trends_data()
    
    industry_data.to_csv("data/industry_data.csv", index=False)
    segment_data.to_csv("data/segment_data.csv", index=False)
    pestle_data.to_csv("data/pestle_data.csv", index=False)
    trends_data.to_csv("data/trends_data.csv", index=False)
    
    return {
        "industry_data": industry_data,
        "segment_data": segment_data,
        "pestle_data": pestle_data,
        "trends_data": trends_data
    }

def load_data(use_cached=True):
    """
    Load data either from CSV files or generate fresh.
    
    Args:
        use_cached (bool): Whether to use cached CSV data if available
        
    Returns:
        dict: Dictionary containing all data DataFrames
    """
    try:
        if use_cached:
            industry_data = pd.read_csv("data/industry_data.csv")
            segment_data = pd.read_csv("data/segment_data.csv")
            pestle_data = pd.read_csv("data/pestle_data.csv")
            trends_data = pd.read_csv("data/trends_data.csv")
            
            return {
                "industry_data": industry_data,
                "segment_data": segment_data,
                "pestle_data": pestle_data,
                "trends_data": trends_data
            }
    except:
        # If files don't exist or there's an error, generate new data
        pass
    
    # Generate new data
    return {
        "industry_data": generate_industry_data(),
        "segment_data": generate_segment_data(),
        "pestle_data": generate_pestle_data(),
        "trends_data": generate_trends_data()
    }

if __name__ == "__main__":
    # When run directly, generate and save sample data
    save_sample_data()
    print("Sample data generated and saved.")