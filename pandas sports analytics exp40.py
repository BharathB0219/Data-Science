import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sports.csv", encoding='latin-1')
average_age = data['Age'].mean()
above_average_age_players = data[data['Age'] > average_age]['Name']
position_counts = data['Position'].value_counts()
plt.bar(position_counts.index, position_counts.values)
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.title('Distribution of Players Based on Positions')
plt.xticks(rotation=45)
plt.show()

print("Top 5 Goal Scorers:")
print(data.nlargest(5, 'Goals'))
print("\nTop 5 Highest Salaries:")
print(data.nlargest(5, 'Salary'))
print(f"\nAverage Age of Players: {average_age:.2f}")
print("\nPlayers Above Average Age:")
print(above_average_age_players)


'''
sample output
Top 5 Goal Scorers:
           Name  Age    Position  Goals   Salary
0  Lionel Messi   34     Forward     45  1000000
1       Ronaldo   36     Forward     40   900000
4        Robert   33     Forward     38   700000
3        Mbappe   22  Midfielder     35   750000
2        Neymar   29     Forward     30   800000

Top 5 Highest Salaries:
           Name  Age    Position  Goals   Salary
8        Beckar   22  Goalkeeper      6  4000000
0  Lionel Messi   34     Forward     45  1000000
1       Ronaldo   36     Forward     40   900000
2        Neymar   29     Forward     30   800000
3        Mbappe   22  Midfielder     35   750000

Average Age of Players: 29.78

Players Above Average Age:
0    Lionel Messi
1         Ronaldo
4          Robert
5          Andres
6            Luka
Name: Name, dtype: object
'''
