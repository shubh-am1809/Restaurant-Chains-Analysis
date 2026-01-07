import pandas as pd

df = pd.read_csv("dataset .csv")
df = df[['Restaurant Name', 'Aggregate rating', 'Votes']].dropna()
chain_counts = df['Restaurant Name'].value_counts()
chains = chain_counts[chain_counts > 1]

print("\nIdentified Restaurant Chains:\n")
print(chains.head(10))

chain_analysis = (
    df[df['Restaurant Name'].isin(chains.index)]
    .groupby('Restaurant Name')
    .agg(
        Outlet_Count=('Restaurant Name', 'count'),
        Average_Rating=('Aggregate rating', 'mean'),
        Total_Votes=('Votes', 'sum')
    )
    .sort_values(by='Outlet_Count', ascending=False)
)

print("\nRestaurant Chain Analysis:\n")
print(chain_analysis.head(10))

chain_analysis.reset_index().to_csv(
    "output/restaurant_chain_analysis.csv", index=False
)

print("\nResults saved to output/restaurant_chain_analysis.csv")
