import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print(matches.head())
print(deliveries.head())


matches_2008 = matches[matches["season"] == 2008]

print("1. Total matches in 2008:")
print(len(matches_2008))


city_count = matches["city"].value_counts()

print("\n2. City with maximum number of matches:")
print(city_count.idxmax())
print(city_count.max())

print("\nCity with minimum number of matches:")
print(city_count.idxmin())
print(city_count.min())


print("\n3. Total matches city-wise:")
print(city_count)


toss_decisions = matches.groupby(
    ["toss_winner", "toss_decision"]
).size()

print("\n4. Toss decisions taken by each team:")
print(toss_decisions)


result_count = matches["result"].value_counts()

print("\n5. Normal matches:")
print(result_count["normal"])

print("Tied matches:")
print(result_count["tie"])


tie_matches = matches[matches["result"] == "tie"]

print("\n6. Teams involved in tied matches:")

for index, row in tie_matches.iterrows():
    print(row["team1"], "vs", row["team2"])


run_wins = matches[matches["win_by_runs"] > 0]

highest_runs = run_wins["win_by_runs"].max()

print("\n7. Highest winning margin:")
print(highest_runs)

print("Team:")
print(
    run_wins[
        run_wins["win_by_runs"] == highest_runs
    ]["winner"]
)

lowest_runs = run_wins["win_by_runs"].min()

print("\nLowest winning margin:")
print(lowest_runs)

print("Team:")
print(
    run_wins[
        run_wins["win_by_runs"] == lowest_runs
    ]["winner"]
)


print("\n8. Mean of win_by_runs:")
print(matches["win_by_runs"].mean())

print("\nMedian of win_by_runs:")
print(matches["win_by_runs"].median())

print("\nStandard deviation of win_by_runs:")
print(matches["win_by_runs"].std())


print("\n9. Venue with highest winning margin:")

print(
    run_wins[
        run_wins["win_by_runs"] == highest_runs
    ][["venue", "winner", "win_by_runs"]]
)

print("\nVenue with lowest winning margin:")

print(
    run_wins[
        run_wins["win_by_runs"] == lowest_runs
    ][["venue", "winner", "win_by_runs"]]
)


player_count = matches["player_of_match"].value_counts()

print("\n10. Players with more than 3 Player of the Match awards:")

print(
    player_count[player_count > 3]
)


six_deliveries = deliveries[
    deliveries["batsman_runs"] == 6
]

print("\n11. Deliveries where batsman scored a six:")

print(
    six_deliveries[
        [
            "match_id",
            "inning",
            "over",
            "ball",
            "batsman",
            "bowler",
            "batsman_runs"
        ]
    ]
)


delivery_data = deliveries.merge(
    matches[["id", "venue"]],
    left_on="match_id",
    right_on="id"
)

venue_runs = delivery_data.groupby(
    "venue"
)["total_runs"].sum()

venue_matches = matches.groupby(
    "venue"
)["id"].count()

average_runs_venue = venue_runs / venue_matches

print("\n12. Average runs per match at each venue:")
print(
    average_runs_venue.sort_values(
        ascending=False
    )
)


umpires = pd.concat([
    matches["umpire1"],
    matches["umpire2"],
    matches["umpire3"]
])

umpires = umpires.dropna()

umpire_count = umpires.value_counts()

maximum_umpire = umpire_count.max()

print("\n13. Umpire(s) with maximum number of matches:")

print(
    umpire_count[
        umpire_count == maximum_umpire
    ]
)


season_matches = matches[
    "season"
].value_counts().sort_index()

print("\n14. Total matches played in each season:")
print(season_matches)


delivery_season = deliveries.merge(
    matches[["id", "season"]],
    left_on="match_id",
    right_on="id"
)

season_runs = delivery_season.groupby(
    "season"
)["total_runs"].sum()

print("\n15. Total runs scored in each season:")
print(season_runs)


batsman_runs = deliveries.groupby(
    "batsman"
)["batsman_runs"].sum()

top_10_batsmen = batsman_runs.sort_values(
    ascending=False
).head(10)

print("\n16. Top 10 batsmen by total runs:")
print(top_10_batsmen)


wickets = deliveries[
    deliveries["player_dismissed"].notna()
]

wickets = wickets[
    ~wickets["dismissal_kind"].isin([
        "run out",
        "retired hurt",
        "obstructing the field"
    ])
]

bowler_wickets = wickets.groupby(
    "bowler"
)["player_dismissed"].count()

bowler_wickets = bowler_wickets.sort_values(
    ascending=False
)

print("\n17. Total wickets taken by each bowler:")
print(bowler_wickets)


total_batsman_runs = deliveries.groupby(
    "batsman"
)["batsman_runs"].sum()

batsman_dismissals = deliveries[
    deliveries["player_dismissed"].notna()
]

batsman_dismissals = batsman_dismissals[
    ~batsman_dismissals["dismissal_kind"].isin([
        "retired hurt",
        "obstructing the field"
    ])
]

dismissal_count = batsman_dismissals.groupby(
    "player_dismissed"
).size()

batting_average = pd.DataFrame({
    "Runs": total_batsman_runs,
    "Dismissals": dismissal_count
})

batting_average["Dismissals"] = batting_average[
    "Dismissals"
].fillna(0)

batting_average["Batting Average"] = (
    batting_average["Runs"] /
    batting_average["Dismissals"].replace(0, np.nan)
)

top_10_average = batting_average.sort_values(
    "Batting Average",
    ascending=False
).head(10)

print("\n18. Top 10 batsmen by batting average:")
print(top_10_average)


toss_season = pd.crosstab(
    matches["season"],
    matches["toss_decision"]
)

toss_season.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Toss Decisions Across All Seasons")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.xticks(rotation=0)
plt.legend(title="Toss Decision")
plt.show()


teams = pd.unique(
    matches[["team1", "team2"]].values.ravel()
)

team_data = []

for team in teams:

    total_matches = (
        (matches["team1"] == team) |
        (matches["team2"] == team)
    ).sum()

    total_wins = (
        matches["winner"] == team
    ).sum()

    win_rate = (
        total_wins / total_matches
    ) * 100

    team_data.append([
        team,
        total_matches,
        total_wins,
        win_rate
    ])

team_stats = pd.DataFrame(
    team_data,
    columns=[
        "Team",
        "Total Matches",
        "Winning Matches",
        "Win Rate"
    ]
)

print("\n20. Total Matches vs Winning Matches vs Win Rate:")
print(team_stats)


x = np.arange(len(team_stats))
width = 0.35

plt.figure(figsize=(12, 6))

plt.bar(
    x - width / 2,
    team_stats["Total Matches"],
    width,
    label="Total Matches"
)

plt.bar(
    x + width / 2,
    team_stats["Winning Matches"],
    width,
    label="Winning Matches"
)

plt.xticks(
    x,
    team_stats["Team"],
    rotation=90
)

plt.xlabel("Team")
plt.ylabel("Number of Matches")
plt.title("Total Matches vs Winning Matches")
plt.legend()
plt.show()


plt.figure(figsize=(12, 6))

plt.bar(
    team_stats["Team"],
    team_stats["Win Rate"]
)

plt.xlabel("Team")
plt.ylabel("Win Rate (%)")
plt.title("Win Rate of All Teams")
plt.xticks(rotation=90)
plt.show()


winner_count = matches[
    "winner"
].value_counts()

print("\n21. Distribution of teams who won the matches:")
print(winner_count)


plt.figure(figsize=(12, 6))

plt.bar(
    winner_count.index,
    winner_count.values
)

plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.title("Distribution of Teams Who Won Matches")
plt.xticks(rotation=90)
plt.show()


toss_team = pd.crosstab(
    matches["toss_winner"],
    matches["toss_decision"]
)

print("\n22. Toss outcomes of all teams:")
print(toss_team)


toss_team.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Toss Outcomes of All Teams")
plt.xlabel("Team")
plt.ylabel("Number of Tosses")
plt.xticks(rotation=90)
plt.legend(title="Toss Decision")
plt.show()


top_5_teams = matches[
    "winner"
].value_counts().head(5)

print("\n23. Top 5 teams with most wins:")
print(top_5_teams)


plt.figure(figsize=(8, 5))

plt.bar(
    top_5_teams.index,
    top_5_teams.values
)

plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.title("Top 5 Teams With Most Wins")
plt.xticks(rotation=45)
plt.show()