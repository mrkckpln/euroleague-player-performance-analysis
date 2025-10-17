import pandas as pd
import numpy as np
from scipy import stats

def load_data():
    """Load the data for correlation analysis"""
    df = pd.read_csv('Euroleague_data/euroleague_players.csv')
    df['efficiency_rating'] = df['valuation']
    df = df[df['minutes_per_game'] >= 5]
    return df

def calculate_correlation_manual(x, y):
    """
    Calculate Pearson's correlation coefficient manually
    """
    # Calculate means
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # Calculate deviations from mean
    x_dev = x - x_mean
    y_dev = y - y_mean
    
    # Calculate the numerator (covariance)
    numerator = np.sum(x_dev * y_dev)
    
    # Calculate the denominator (product of standard deviations)
    x_std = np.sqrt(np.sum(x_dev ** 2))
    y_std = np.sqrt(np.sum(y_dev ** 2))
    denominator = x_std * y_std
    
    # Calculate correlation coefficient
    correlation = numerator / denominator
    
    return correlation

def main():
    # Load data
    df = load_data()
    
    # Get the variables
    x = df['minutes_per_game']
    y = df['efficiency_rating']
    
    # Calculate correlation using different methods
    manual_correlation = calculate_correlation_manual(x, y)
    pandas_correlation = x.corr(y)
    scipy_correlation = stats.pearsonr(x, y)[0]
    
    # Print results
    print("\nCorrelation Coefficient Calculation Results:")
    print(f"Manual calculation: {manual_correlation:.3f}")
    print(f"Pandas calculation: {pandas_correlation:.3f}")
    print(f"SciPy calculation: {scipy_correlation:.3f}")
    
    # Print interpretation
    print("\nInterpretation:")
    print(f"The correlation coefficient of {manual_correlation:.3f} indicates a {'strong' if abs(manual_correlation) > 0.5 else 'moderate'} {'positive' if manual_correlation > 0 else 'negative'} relationship")
    print("between playing time and efficiency rating.")
    
    # Print additional statistics
    print("\nAdditional Statistics:")
    print(f"Number of observations: {len(x)}")
    print(f"Mean minutes per game: {x.mean():.2f}")
    print(f"Mean efficiency rating: {y.mean():.2f}")
    print(f"Standard deviation of minutes: {x.std():.2f}")
    print(f"Standard deviation of efficiency: {y.std():.2f}")

if __name__ == "__main__":
    main() 