import pandas as pd
import numpy as np

def normalize_metric(value, min_value, max_value, inverse=False):
    """
    Normalize a metric value to a 0-1 scale.
    
    Args:
        value (float): The raw metric value
        min_value (float): Minimum expected value
        max_value (float): Maximum expected value
        inverse (bool): If True, invert the normalization (1 becomes 0, 0 becomes 1)
        
    Returns:
        float: Normalized value between 0 and 1
    """
    # Ensure value is within bounds
    value = max(min_value, min(value, max_value))
    
    # Normalize to 0-1
    normalized = (value - min_value) / (max_value - min_value) if max_value > min_value else 0.5
    
    # Invert if needed (for metrics where lower is better)
    if inverse:
        normalized = 1 - normalized
    
    return normalized

def calculate_segment_score(segment_data, weights, metric_ranges=None):
    """
    Calculate an overall score for a market segment based on weighted metrics.
    
    Args:
        segment_data (dict): Dictionary of segment metric values
        weights (dict): Dictionary of metric weights (should sum to 100)
        metric_ranges (dict, optional): Dictionary of min/max values for each metric
        
    Returns:
        dict: Dictionary containing total score and breakdown by factor
    """
    # Default metric ranges if not provided
    if metric_ranges is None:
        metric_ranges = {
            "market_size": {"min": 50, "max": 10000, "inverse": False},
            "growth_rate": {"min": 0, "max": 50, "inverse": False},
            "profitability": {"min": 0, "max": 50, "inverse": False},
            "competitive_intensity": {"min": 1, "max": 100, "inverse": True},
            "market_accessibility": {"min": 1, "max": 100, "inverse": False},
            "ai_readiness": {"min": 1, "max": 100, "inverse": False},
            "sustainability_focus": {"min": 1, "max": 100, "inverse": False},
            "strategic_fit": {"min": 1, "max": 100, "inverse": False}
        }
    
    # Ensure weights sum to 100
    weight_sum = sum(weights.values())
    if weight_sum != 100:
        # Normalize weights to sum to 100
        weights = {k: (v / weight_sum) * 100 for k, v in weights.items()}
    
    # Normalize each metric
    normalized_scores = {}
    for metric, value in segment_data.items():
        if metric in metric_ranges:
            metric_range = metric_ranges[metric]
            normalized_scores[metric] = normalize_metric(
                value, 
                metric_range["min"], 
                metric_range["max"],
                metric_range["inverse"]
            )
    
    # Calculate weighted contributions
    contributions = {}
    for metric, normalized_score in normalized_scores.items():
        if metric in weights:
            weight = weights[metric] / 100  # Convert percentage to decimal
            contributions[metric] = normalized_score * weight
    
    # Calculate total score (0-100 scale)
    total_score = sum(contributions.values()) * 100
    
    return {
        "total_score": total_score,
        "normalized_scores": normalized_scores,
        "contributions": contributions,
        "weights": weights
    }

def calculate_opportunity_score(segment, max_values=None):
    """
    Calculate an opportunity score for a segment based on key metrics.
    
    Args:
        segment (Series or dict): Segment data containing key metrics
        max_values (dict, optional): Maximum values for normalization
        
    Returns:
        float: Opportunity score (0-100)
    """
    if max_values is None:
        max_values = {
            "Market Size (millions)": 5000,
            "CAGR (%)": 25,
            "Profitability (%)": 40,
            "Competitive Intensity": 100
        }
    
    # Default weights
    weights = {
        "Market Size (millions)": 0.3,  # 30%
        "CAGR (%)": 0.3,               # 30%
        "Profitability (%)": 0.3,      # 30%
        "Competitive Intensity": 0.1    # 10% (inverse)
    }
    
    # Calculate normalized and weighted scores
    score = (
        segment["Market Size (millions)"] / max_values["Market Size (millions)"] * weights["Market Size (millions)"] +
        segment["CAGR (%)"] / max_values["CAGR (%)"] * weights["CAGR (%)"] +
        segment["Profitability (%)"] / max_values["Profitability (%)"] * weights["Profitability (%)"] +
        (1 - segment["Competitive Intensity"] / max_values["Competitive Intensity"]) * weights["Competitive Intensity"]
    ) * 100
    
    return score

def rank_segments(segments_df, criteria=None, weights=None):
    """
    Rank market segments based on weighted criteria.
    
    Args:
        segments_df (DataFrame): DataFrame containing segment data
        criteria (list, optional): List of criteria columns to use
        weights (dict, optional): Dictionary of criterion weights
        
    Returns:
        DataFrame: Original DataFrame with added 'Opportunity Score' and 'Rank' columns
    """
    if criteria is None:
        criteria = [
            "Market Size (millions)", 
            "CAGR (%)", 
            "Profitability (%)", 
            "Competitive Intensity"
        ]
    
    if weights is None:
        weights = {
            "Market Size (millions)": 0.3,
            "CAGR (%)": 0.3,
            "Profitability (%)": 0.3,
            "Competitive Intensity": 0.1
        }
    
    # Get max values for normalization
    max_values = {
        criterion: segments_df[criterion].max() for criterion in criteria
    }
    
    # Calculate opportunity score for each segment
    segments_df["Opportunity Score"] = segments_df.apply(
        lambda row: calculate_opportunity_score(row, max_values), axis=1
    )
    
    # Rank segments by opportunity score
    segments_df["Rank"] = segments_df["Opportunity Score"].rank(ascending=False)
    
    return segments_df.sort_values("Opportunity Score", ascending=False)

def calculate_roi(investment, revenue, periods):
    """
    Calculate ROI metrics based on investment and revenue projections.
    
    Args:
        investment (list): List of investment amounts by period
        revenue (list): List of revenue amounts by period
        periods (list): List of period labels
        
    Returns:
        dict: Dictionary of ROI metrics
    """
    total_investment = sum(investment)
    
    # Calculate profit/loss for each period
    profit = [revenue[i] - investment[i] for i in range(len(revenue))]
    cumulative_profit = [sum(profit[:i+1]) for i in range(len(profit))]
    
    # Find break-even point
    break_even_period = None
    for i, cum_profit in enumerate(cumulative_profit):
        if cum_profit >= 0:
            break_even_period = periods[i]
            break
    
    # Calculate ROI
    last_period_profit = cumulative_profit[-1] if cumulative_profit else 0
    roi_percentage = (last_period_profit / total_investment * 100) if total_investment > 0 else 0
    
    return {
        "total_investment": total_investment,
        "cumulative_profit": cumulative_profit,
        "break_even_period": break_even_period,
        "roi_percentage": roi_percentage,
        "profit_by_period": profit
    }

def calculate_market_entry_risk(segment_data):
    """
    Calculate market entry risk based on segment characteristics.
    
    Args:
        segment_data (dict): Dictionary containing segment metrics
        
    Returns:
        dict: Risk assessment by category and overall risk score
    """
    risk_factors = {}
    
    # Competition risk (higher competition = higher risk)
    if "competitive_intensity" in segment_data:
        competition = segment_data["competitive_intensity"]
        if competition < 40:
            risk_factors["competition"] = {"score": 1, "level": "Low"}
        elif competition < 70:
            risk_factors["competition"] = {"score": 2, "level": "Medium"}
        else:
            risk_factors["competition"] = {"score": 3, "level": "High"}
    
    # Market volatility risk (inverse of growth stability)
    if "growth_rate" in segment_data:
        growth = segment_data["growth_rate"]
        if growth > 20:
            risk_factors["volatility"] = {"score": 2, "level": "Medium"}  # High growth can be volatile
        elif growth > 5:
            risk_factors["volatility"] = {"score": 1, "level": "Low"}
        else:
            risk_factors["volatility"] = {"score": 3, "level": "High"}    # Stagnant markets are risky
    
    # Entry barrier risk
    if "market_accessibility" in segment_data:
        accessibility = segment_data["market_accessibility"]
        if accessibility > 70:
            risk_factors["entry_barriers"] = {"score": 1, "level": "Low"}
        elif accessibility > 40:
            risk_factors["entry_barriers"] = {"score": 2, "level": "Medium"}
        else:
            risk_factors["entry_barriers"] = {"score": 3, "level": "High"}
    
    # Calculate overall risk score (1-3 scale, where 1 is low risk and 3 is high risk)
    risk_scores = [factor["score"] for factor in risk_factors.values()]
    overall_risk = sum(risk_scores) / len(risk_scores) if risk_scores else 2
    
    risk_level = "Low" if overall_risk < 1.67 else "Medium" if overall_risk < 2.34 else "High"
    
    return {
        "factors": risk_factors,
        "overall_score": overall_risk,
        "overall_level": risk_level
    }

def prioritize_segments(segments_df, criteria_weights=None):
    """
    Create a prioritized list of segments based on multiple criteria.
    
    Args:
        segments_df (DataFrame): DataFrame containing segment data
        criteria_weights (dict, optional): Dictionary of criterion weights
        
    Returns:
        DataFrame: Prioritized segments with scores
    """
    if criteria_weights is None:
        criteria_weights = {
            "Market Size (millions)": 0.25,
            "CAGR (%)": 0.25,
            "Profitability (%)": 0.25,
            "Competitive Intensity": 0.15,
            "AI Readiness": 0.05,
            "Sustainability Score": 0.05
        }
    
    # Normalize numeric columns for scoring
    normalized_df = segments_df.copy()
    
    for column, weight in criteria_weights.items():
        if column in segments_df.columns:
            if column == "Competitive Intensity":  # Lower is better
                normalized_df[f"{column}_normalized"] = 1 - (segments_df[column] / segments_df[column].max())
            else:  # Higher is better
                normalized_df[f"{column}_normalized"] = segments_df[column] / segments_df[column].max()
    
    # Calculate priority score
    priority_score = 0
    for column, weight in criteria_weights.items():
        if f"{column}_normalized" in normalized_df.columns:
            priority_score += normalized_df[f"{column}_normalized"] * weight
    
    normalized_df["Priority Score"] = priority_score * 100
    
    # Clean up temporary columns
    for column in normalized_df.columns:
        if column.endswith("_normalized"):
            normalized_df.drop(column, axis=1, inplace=True)
    
    return normalized_df.sort_values("Priority Score", ascending=False)