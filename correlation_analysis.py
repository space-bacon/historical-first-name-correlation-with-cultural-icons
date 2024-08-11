import pandas as pd
from scipy.stats import pearsonr, ttest_ind

def load_data(file_path):
    """Load the processed dataset from a given file path."""
    return pd.read_csv(file_path)

def cross_correlation(name_series, figure_year, max_lag=5):
    """Calculate cross-correlation between a name's popularity and a historical figure's prominence."""
    correlations = []
    for lag in range(-max_lag, max_lag + 1):
        shifted_series = name_series.shift(lag)
        correlation = shifted_series.corr(figure_year)
        correlations.append(correlation)
    return correlations

def test_statistical_significance(before, after):
    """Test if the difference in name popularity before and after a figure's prominence is significant."""
    stat, p_value = ttest_ind(before, after)
    return p_value < 0.05  # Returns True if significant

def correlate_with_figures(name_trends, historical_figures):
    """Correlate name trends with historical figures using statistical tests."""
    correlation_results = []

    for _, figure in historical_figures.iterrows():
        figure_name = figure['name']
        figure_year = figure['year_of_prominence']
        
        # Extract trends for the figure's name
        figure_trend = name_trends[name_trends['name'] == figure_name]
        
        # Perform Pearson correlation test between years and name counts
        corr, _ = pearsonr(figure_trend['year'], figure_trend['smoothed_count'])
        
        # Test statistical significance
        before = figure_trend[figure_trend['year'] < figure_year]['smoothed_count']
        after = figure_trend[figure_trend['year'] >= figure_year]['smoothed_count']
        significance = test_statistical_significance(before, after)
        
        correlation_results.append({
            'name': figure_name,
            'year_of_prominence': figure_year,
            'correlation_coefficient': corr,
            'statistically_significant': significance
        })

    return pd.DataFrame(correlation_results)

def save_data(df, file_path):
    """Save the correlation data to a specified file path."""
    df.to_csv(file_path, index=False)

def main():
    # Load processed data
    name_trends = load_data('data/processed/name_trends.csv')
    historical_figures_cleaned = load_data('data/processed/historical_figures_cleaned.csv')
    
    # Correlate with historical figures
    correlation_data = correlate_with_figures(name_trends, historical_figures_cleaned)
    
    # Save correlation data
    save_data(correlation_data, 'data/processed/correlation_data.csv')

if __name__ == "__main__":
    main()
