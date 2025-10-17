import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm

# Set style for better visualizations
plt.style.use('default')
sns.set_theme()

# Read the data
df = pd.read_csv('Euroleague_data/euroleague_players.csv')

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Scatter plot with regression line
sns.regplot(data=df, x='points_per_game', y='valuation_per_game', 
            scatter_kws={'alpha':0.5}, line_kws={'color': 'red'}, ax=ax1)
ax1.set_title('Relationship between Points and Efficiency')
ax1.set_xlabel('Points per Game')
ax1.set_ylabel('Efficiency Rating per Game')

# Calculate correlation and p-value
correlation, p_value = stats.pearsonr(df['points_per_game'], df['valuation_per_game'])
ax1.text(0.05, 0.95, f'Correlation: {correlation:.3f}\nP-value: {p_value:.3e}', 
         transform=ax1.transAxes, bbox=dict(facecolor='white', alpha=0.8))

# Residual plot
X = sm.add_constant(df['points_per_game'])
model = sm.OLS(df['valuation_per_game'], X).fit()
residuals = model.resid
sns.scatterplot(x=df['points_per_game'], y=residuals, ax=ax2, alpha=0.5)
ax2.axhline(y=0, color='r', linestyle='--')
ax2.set_title('Residual Plot')
ax2.set_xlabel('Points per Game')
ax2.set_ylabel('Residuals')

# Print detailed statistical analysis
print("\nStatistical Analysis of Points vs Efficiency:")
print("\nCorrelation Analysis:")
print(f"Pearson Correlation Coefficient: {correlation:.3f}")
print(f"P-value: {p_value:.3e}")
print(f"R-squared: {correlation**2:.3f}")

print("\nRegression Analysis:")
print(model.summary())

# Calculate additional statistics
print("\nAdditional Statistics:")
print("\nPoints per Game:")
print(df['points_per_game'].describe())
print("\nEfficiency Rating per Game:")
print(df['valuation_per_game'].describe())

# Save the plot
plt.tight_layout()
plt.savefig('efficiency_points_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# Create a new figure for distribution of residuals
plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True)
plt.title('Distribution of Residuals')
plt.xlabel('Residual Value')
plt.ylabel('Frequency')
plt.savefig('residuals_distribution.png', dpi=300, bbox_inches='tight')
plt.close() 