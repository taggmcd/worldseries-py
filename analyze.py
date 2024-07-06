import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('worldSeries.csv')

# Group by Winning team and count the number of wins
wins = df.groupby('Winning team').size()

# Group by Losing team and count the number of losses
losses = df.groupby('Losing team').size()

# Combine wins and losses to get total appearances
appearances = wins.add(losses, fill_value=0)

# Find the team with the most wins
team_most_wins = wins.idxmax()
most_wins_count = wins.max()

# Find the team with the most losses
team_most_losses = losses.idxmax()
most_losses_count = losses.max()

# Find the team with the most appearances
team_most_appearances = appearances.idxmax()
most_appearances_count = appearances.max()

# Display the results
print(f"Team with the most wins: {team_most_wins} with {most_wins_count} wins")
print(f"Team with the most losses: {team_most_losses} with {most_losses_count} losses")
print(f"Team with the most appearances: {team_most_appearances} with {most_appearances_count} appearances")