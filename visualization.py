import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    """Load the processed dataset from a given file path."""
    return pd.read_csv(file_path)

def plot_name_trend(name_trends, name, save_path=None):
    """Plot the trend of a specific name over time."""
    trend = name_trends[name_trends['name'] == name]
    plt.figure(figsize=(10, 6))
    plt.plot(trend['year'], trend['smoothed_count'], marker='o')
    plt.title(f"Trend for '{name}' Over Time")
    plt.xlabel('Year')
    plt.ylabel('Count')
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

def interactive_trend_plot(name_trends, name):
    """Create an interactive trend plot using Plotly."""
    trend = name_trends[name_trends['name'] == name]
    fig = px.line(trend, x='year', y='smoothed_count', title=f"Trend for '{name}' Over Time")
    fig.show()

def plot_correlation_matrix(correlation_data):
    """Plot a heatmap of the correlation matrix."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_data.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Name Trends and Historical Figures')
    plt.show()

def main():
    # Load data
    name_trends = load_data('data/processed/name_trends.csv')
    correlation_data = load_data('data/processed/correlation_data.csv')
    
    # Plot example trends
    plot_name_trend(name_trends, 'james', save_path='output/plots/james_trend.png')
    
    # Interactive trend plot
    interactive_trend_plot(name_trends, 'james')
    
    # Plot correlation matrix
    plot_correlation_matrix(correlation_data)

if __name__ == "__main__":
    main()
