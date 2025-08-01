def calculate_risk(df):
    if df.empty:
        return "No Data"

    volatility = df['Close'].pct_change().std()
    if volatility > 0.03:
        return "High"
    elif volatility > 0.015:
        return "Medium"
    else:
        return "Low"
