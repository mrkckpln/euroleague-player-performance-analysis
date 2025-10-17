import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

# Set style for better visualizations
plt.style.use('default')
sns.set_theme()

# Read the data
df = pd.read_csv('Euroleague_data/euroleague_players.csv')

# Create position categories based on statistics
def categorize_position(row):
    if row['total_rebounds_per_game'] > 5 and row['blocks_favour_per_game'] > 0.5:
        return 'Center'
    elif row['assists_per_game'] > 3:
        return 'Guard'
    elif row['total_rebounds_per_game'] > 3 and row['points_per_game'] > 10:
        return 'Forward'
    else:
        return 'Other'

df['position'] = df.apply(categorize_position, axis=1)

# Function to perform ANOVA analysis
def perform_anova_analysis(data, group_column, value_column, title_prefix):
    # Perform ANOVA test
    model = ols(f'{value_column} ~ {group_column}', data=data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    
    # Create box plot
    plt.figure(figsize=(12, 6))
    sns.boxplot(x=group_column, y=value_column, data=data)
    plt.title(f'{title_prefix} Distribution by {group_column}')
    plt.xlabel(group_column)
    plt.ylabel(value_column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'efficiency_by_{group_column.lower()}.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Perform post-hoc analysis
    mc = MultiComparison(data[value_column], data[group_column])
    posthoc = mc.tukeyhsd()
    
    # Create post-hoc plot
    plt.figure(figsize=(10, 6))
    posthoc.plot_simultaneous()
    plt.title(f'Tukey HSD Post-hoc Analysis - {group_column}')
    plt.tight_layout()
    plt.savefig(f'posthoc_analysis_{group_column.lower()}.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Calculate effect size (Eta-squared)
    ss_total = anova_table['sum_sq'].sum()
    eta_squared = anova_table['sum_sq'].iloc[0] / ss_total
    
    # Print analysis results
    print(f"\nANOVA Analysis of {value_column} by {group_column}:")
    print("\nANOVA Table:")
    print(anova_table)
    
    print(f"\nPost-hoc Analysis (Tukey HSD) for {group_column}:")
    print(posthoc.summary())
    
    print(f"\nGroup Statistics for {group_column}:")
    group_stats = data.groupby(group_column)[value_column].agg(['count', 'mean', 'std', 'min', 'max'])
    print(group_stats)
    
    print(f"\nEffect Size (Eta-squared) for {group_column}: {eta_squared:.3f}")
    
    return anova_table, posthoc, group_stats, eta_squared

# Perform ANOVA analysis for positions
position_anova = perform_anova_analysis(df, 'position', 'valuation_per_game', 'Efficiency Rating')

# Create violin plot for positions
plt.figure(figsize=(12, 6))
sns.violinplot(x='position', y='valuation_per_game', data=df)
plt.title('Efficiency Rating Distribution by Position (Violin Plot)')
plt.xlabel('Position')
plt.ylabel('Efficiency Rating per Game')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('efficiency_violin_plot_position.png', dpi=300, bbox_inches='tight')
plt.close() 