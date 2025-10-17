import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better visualizations
plt.style.use('default')
sns.set_theme()

# Read the data
df = pd.read_csv('Euroleague_data/euroleague_players.csv')

# Create a figure with subplots for different statistics
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Distribution of Key Euroleague Statistics', fontsize=16)

# Points per game distribution
sns.histplot(data=df, x='points_per_game', bins=30, ax=axes[0,0], kde=True)
axes[0,0].set_title('Points per Game Distribution')
axes[0,0].set_xlabel('Points per Game')
axes[0,0].set_ylabel('Frequency')

# Rebounds per game distribution
sns.histplot(data=df, x='total_rebounds_per_game', bins=30, ax=axes[0,1], kde=True)
axes[0,1].set_title('Total Rebounds per Game Distribution')
axes[0,1].set_xlabel('Rebounds per Game')
axes[0,1].set_ylabel('Frequency')

# Assists per game distribution
sns.histplot(data=df, x='assists_per_game', bins=30, ax=axes[1,0], kde=True)
axes[1,0].set_title('Assists per Game Distribution')
axes[1,0].set_xlabel('Assists per Game')
axes[1,0].set_ylabel('Frequency')

# Blocks per game distribution
sns.histplot(data=df, x='blocks_favour_per_game', bins=30, ax=axes[1,1], kde=True)
axes[1,1].set_title('Blocks per Game Distribution')
axes[1,1].set_xlabel('Blocks per Game')
axes[1,1].set_ylabel('Frequency')

# Adjust layout and save
plt.tight_layout()
plt.savefig('statistics_distributions.png', dpi=300, bbox_inches='tight')
plt.close()

# Print summary statistics
print("\nSummary Statistics for Key Metrics:")
stats = df[['points_per_game', 'total_rebounds_per_game', 'assists_per_game', 'blocks_favour_per_game']].describe()
print(stats)

# Calculate additional distribution metrics
print("\nDistribution Analysis:")
for stat in ['points_per_game', 'total_rebounds_per_game', 'assists_per_game', 'blocks_favour_per_game']:
    print(f"\n{stat.replace('_', ' ').title()}:")
    print(f"Skewness: {df[stat].skew():.3f}")
    print(f"Kurtosis: {df[stat].kurtosis():.3f}")
    print(f"Median: {df[stat].median():.2f}")
    print(f"Mode: {df[stat].mode().iloc[0]:.2f}") 