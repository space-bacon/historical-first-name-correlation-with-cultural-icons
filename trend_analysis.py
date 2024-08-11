import pandas as pd
import statsmodels.api as sm

def load_data(file_path):
    """Load the processed dataset from a given file path."""
    return pd.read_csv(file_path)

def calculate_name_trends(df):
    """Calculate the frequency of each name by year, with smoothing."""
    name_trends = df.groupby(['year', 'name']).agg({'count': 'sum'}).reset_index()

    # Apply a simple moving average to smooth the trend
    name_trends['smoothed_count'] = name_trends.groupby('name')['count'].transform(lambda x: x.rolling(window=3, min_periods=1).mean())

    return name_trends

def transform_to_time_series(df):
    """Transform the name frequency data into a time series format."""
    time_series = df.pivot(index='year', columns='name', values='count').fillna(0)
    return time_series

def forecast_name_trend(time_series, name, steps=5):
    """Forecast future trends for a specific name using ARIMA model."""
    model = sm.tsa.ARIMA(time_series[name].dropna(), order=(5, 1, 0))
    model_fit = model.fit(disp=0)
    forecast = model_fit.forecast(steps=steps)
    return forecast

def save_data(df, file_path):
    """Save the trend data to a specified file path."""
    df.to_csv(file_path, index=False)

def main():
    # Load processed data
    baby_names_cleaned = load_data('data/processed/baby_names_cleaned.csv')
    
    # Calculate trends
    name_trends = calculate_name_trends(baby_names_cleaned)
    
    # Save trend data
    save_data(name_trends, 'data/processed/name_trends.csv')
    
    # Transform to time series for advanced analysis
    time_series = transform_to_time_series(name_trends)
    time_series.to_csv('data/processed/name_time_series.csv')

if __name__ == "__main__":
    main()
