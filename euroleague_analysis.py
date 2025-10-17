import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('default')
sns.set_theme()

def load_data():
    """
    Load Euroleague players data and perform initial preprocessing
    """
    print("Loading data file...")
    
    # Load the players data file
    players_df = pd.read_csv('Euroleague_data/euroleague_players.csv')
    
    print("Data loaded successfully!")
    return players_df

def preprocess_data(players_df):
    """
    Preprocess the data by cleaning and calculating additional metrics
    """
    print("Preprocessing data...")
    
    # Calculate shooting percentages (already in the dataset)
    # Calculate per game statistics (already in the dataset)
    
    # Handle missing values
    players_df = players_df.fillna(0)
    
    print("Data preprocessing completed!")
    return players_df

def descriptive_statistics(df):
    """
    Calculate and display descriptive statistics for key metrics
    """
    print("\nDescriptive Statistics:")
    
    # Select key metrics for analysis
    metrics = ['points_per_game', 'total_rebounds_per_game', 'assists_per_game', 
              'steals_per_game', 'blocks_favour_per_game', 'two_points_percentage',
              'three_points_percentage', 'free_throws_percentage']
    
    stats_df = df[metrics].describe()
    print(stats_df)
    
    return stats_df

def correlation_analysis(df):
    """
    Perform correlation analysis between key metrics
    """
    print("\nCorrelation Analysis:")
    
    # Select metrics for correlation analysis
    metrics = ['points_per_game', 'total_rebounds_per_game', 'assists_per_game', 
              'steals_per_game', 'blocks_favour_per_game', 'two_points_percentage',
              'three_points_percentage', 'free_throws_percentage']
    
    # Calculate correlation matrix
    corr_matrix = df[metrics].corr()
    
    # Create correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix of Player Statistics')
    plt.tight_layout()
    plt.savefig('correlation_matrix.png')
    plt.close()
    
    return corr_matrix

def regression_analysis(df):
    """
    Perform regression analysis to predict points per game
    """
    print("\nRegression Analysis:")
    
    # Prepare features and target
    features = ['total_rebounds_per_game', 'assists_per_game', 'steals_per_game', 
               'blocks_favour_per_game', 'two_points_percentage', 'three_points_percentage']
    X = df[features]
    y = df['points_per_game']
    
    # Add constant for statsmodels
    X = sm.add_constant(X)
    
    # Fit regression model
    model = sm.OLS(y, X).fit()
    print(model.summary())

    # Visual representation: Actual vs Predicted Points Per Game
    predicted_points = model.predict(X)
    plt.figure(figsize=(10, 6))
    plt.scatter(y, predicted_points, alpha=0.6)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)  # Reference line
    plt.xlabel('Actual Points Per Game')
    plt.ylabel('Predicted Points Per Game')
    plt.title('Regression Analysis: Actual vs Predicted Points Per Game')
    plt.tight_layout()
    plt.savefig('regression_actual_vs_predicted.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return model

def identify_outstanding_players(df):
    """
    Identify outstanding players based on multiple metrics
    """
    print("\nOutstanding Players Analysis:")
    
    # Calculate z-scores for key metrics
    metrics = ['points_per_game', 'total_rebounds_per_game', 'assists_per_game', 
              'steals_per_game', 'blocks_favour_per_game']
    
    z_scores = df[metrics].apply(stats.zscore)
    
    # Calculate overall performance score
    df['performance_score'] = z_scores.mean(axis=1)
    
    # Get top 10 players
    top_players = df.nlargest(10, 'performance_score')
    
    print("\nTop 10 Players by Overall Performance:")
    print(top_players[['player', 'points_per_game', 'total_rebounds_per_game', 
                      'assists_per_game', 'performance_score']])
    
    return top_players

if __name__ == "__main__":
    # Load and preprocess data
    players_df = load_data()
    processed_df = preprocess_data(players_df)
    
    # Perform analyses
    stats_df = descriptive_statistics(processed_df)
    corr_matrix = correlation_analysis(processed_df)
    regression_model = regression_analysis(processed_df)
    top_players = identify_outstanding_players(processed_df)
    
    # Save processed data
    processed_df.to_csv('processed_euroleague_data.csv', index=False)
    print("\nAnalysis completed and results saved!") 