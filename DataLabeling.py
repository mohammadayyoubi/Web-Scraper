import pandas as pd

# Load data
df = pd.read_csv('output.csv')

# Add an empty 'Label' column
df['Label'] = ''

# Manual labeling 
for i, row in df.iterrows():
    print(f"\nQuote {i+1}:\n{row['Quote']}")
    label = input("Label (positive/negative): ").strip().lower()
    while label not in ['positive', 'negative']:
        label = input("Please enter 'positive' or 'negative': ").strip().lower()
    df.at[i, 'Label'] = label

# Save labeled data
df.to_csv('labeled_quotes.csv', index=False)
print("Labeled data saved to labeled_quotes.csv")
