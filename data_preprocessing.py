import pandas as pd

def load_data(file_path):
    """Load the dataset from a given file path."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean and preprocess the data."""
    df['name'] = df['name'].str.lower()
    df['name'] = df['name'].str.replace(r'[^a-z]', '', regex=True)  # Remove non-alphabetical characters
    df.dropna(subset=['name', 'year'], inplace=True)  # Drop rows with missing name or year

    # Remove outliers: Names that appear only once across all years
    name_counts = df['name'].value_counts()
    df = df[df['name'].isin(name_counts[name_counts > 1].index)]
    
    return df

def save_data(df, file_path):
    """Save the cleaned data to a specified file path."""
    df.to_csv(file_path, index=False)

def main():
    # Load raw data
    baby_names = load_data('data/raw/baby_names.csv')
    historical_figures = load_data('data/raw/historical_figures.csv')
    
    # Clean data
    baby_names_cleaned = clean_data(baby_names)
    historical_figures_cleaned = clean_data(historical_figures)
    
    # Save cleaned data
    save_data(baby_names_cleaned, 'data/processed/baby_names_cleaned.csv')
    save_data(historical_figures_cleaned, 'data/processed/historical_figures_cleaned.csv')

if __name__ == "__main__":
    main()
