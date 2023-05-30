import requests

def get_match_details(league_id, season):
    url = f"https://www.openligadb.de/api/getmatchdata/{league_id}/{season}"
    response = requests.get(url)
    
    if response.status_code == 200:
        match_data = response.json()
        
        if match_data:
            for match in match_data:
                home_team = match['Team1']['TeamName']
                away_team = match['Team2']['TeamName']
                date = match['MatchDateTime']
                score_home_team = match['MatchResults'][0]['PointsTeam1']
                score_away_team = match['MatchResults'][0]['PointsTeam2']
                
                print("Match Details:")
                print(f"Home Team: {home_team}")
                print(f"Away Team: {away_team}")
                print(f"Date: {date}")
                print(f"Final Score: {score_home_team} - {score_away_team}")
                
                # Perform further analysis or processing as needed
                
        else:
            print("No match data found.")
    else:
        print("Failed to retrieve match data. Please try again later.")

# Usage
league_id = 123  # Replace with the ID of the league you want to analyze
season = "2021"  # Replace with the season you want to analyze
get_match_details(league_id, season)
