import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set style for better visualizations
plt.style.use('default')
sns.set_theme()

def load_and_prepare_data():
    """
    Load the data and prepare it for analysis
    """
    print("Loading data...")
    df = pd.read_csv('Euroleague_data/euroleague_players.csv')
    
    # Calculate efficiency rating using valuation column
    df['efficiency_rating'] = df['valuation']
    
    # Filter out players with very little playing time (less than 5 minutes per game)
    df = df[df['minutes_per_game'] >= 5]
    
    return df

def analyze_playing_time_efficiency(df):
    """
    Analyze and visualize the relationship between playing time and efficiency rating
    """
    # Create figure with multiple subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Scatter plot with regression line
    sns.regplot(data=df, x='minutes_per_game', y='efficiency_rating', 
                scatter_kws={'alpha':0.5}, line_kws={'color': 'red'}, ax=ax1)
    ax1.set_title('Playing Time vs Efficiency Rating')
    ax1.set_xlabel('Minutes Per Game')
    ax1.set_ylabel('Efficiency Rating')
    
    # Calculate correlation
    correlation = df['minutes_per_game'].corr(df['efficiency_rating'])
    ax1.text(0.05, 0.95, f'Correlation: {correlation:.2f}', 
             transform=ax1.transAxes, bbox=dict(facecolor='white', alpha=0.8))
    
    # Box plot of efficiency rating by playing time categories
    df['playing_time_category'] = pd.qcut(df['minutes_per_game'], q=4, 
                                        labels=['Low', 'Medium-Low', 'Medium-High', 'High'])
    sns.boxplot(data=df, x='playing_time_category', y='efficiency_rating', ax=ax2)
    ax2.set_title('Efficiency Rating Distribution by Playing Time')
    ax2.set_xlabel('Playing Time Category')
    ax2.set_ylabel('Efficiency Rating')
    
    # Rotate x-axis labels for better readability
    ax2.tick_params(axis='x', rotation=45)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('playing_time_efficiency_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Print statistical summary
    print("\nStatistical Summary:")
    print(f"Correlation coefficient: {correlation:.3f}")
    
    # Calculate average efficiency by playing time category
    category_stats = df.groupby('playing_time_category')['efficiency_rating'].agg(['mean', 'std', 'count'])
    print("\nEfficiency Rating by Playing Time Category:")
    print(category_stats)
    
    return correlation, category_stats

if __name__ == "__main__":
    # Load and prepare data
    df = load_and_prepare_data()
    
    # Perform analysis
    correlation, category_stats = analyze_playing_time_efficiency(df)
    
    print("\nAnalysis completed! Results have been saved to 'playing_time_efficiency_analysis.png'") 