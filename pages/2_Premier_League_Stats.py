import streamlit as st
import pandas as pd

st.set_page_config(page_title="LaLiga Stats Player Wise", page_icon="📈")

st.title("Premier League Player Details")  
st.subheader("Filter to any team/player to see all their stats!")

a = st.selectbox("Select season", ["14-15", "15-16", "16-17", "17-18", "18-19", "19-20", "20-21", "21-22"], index=None)
match a:
    case "14-15":
        df = pd.read_csv('data/pl/players_epl_14-15.csv')

        team = st.selectbox("Select a team", df['team_title'].sort_values().unique(), index=None)
        player=st.selectbox("Select a player", df[df['team_title'] == team]['player_name'].sort_values().unique(), index=None)

        selected_players = df[(df['team_title'] == team) & (df['player_name'] == player)]

        if not selected_players.empty:
            st.write(f"Filtering results for Team: {team} and Player: {player}")
            # Display relevant properties, e.g., games, points, etc.
            st.dataframe(selected_players[['games', 'goals', 'assists', 'xG', 'xA', 'key_passes', 'yellow_cards', 'red_cards']])
        else:
            st.write("No players found with the given criteria.")
    case "15-16":
        df = pd.read_csv('data/pl/players_epl_15-16.csv')

        team = st.selectbox("Select a team", df['team_title'].sort_values().unique(), index=None)
        player=st.selectbox("Select a player", df[df['team_title'] == team]['player_name'].sort_values().unique(), index=None)

        selected_players = df[(df['team_title'] == team) & (df['player_name'] == player)]

        if not selected_players.empty:
            st.write(f"Filtering results for Team: {team} and Player: {player}")
            # Display relevant properties, e.g., games, points, etc.
            st.dataframe(selected_players[['games', 'goals', 'assists', 'xG', 'xA', 'key_passes', 'yellow_cards', 'red_cards']])
        else:
            st.write("No players found with the given criteria.")
    case "16-17":
        df = pd.read_csv('data/pl/players_epl_16-17.csv')

        team = st.selectbox("Select a team", df['team_title'].sort_values().unique(), index=None)
        player=st.selectbox("Select a player", df[df['team_title'] == team]['player_name'].sort_values().unique(), index=None)

        selected_players = df[(df['team_title'] == team) & (df['player_name'] == player)]

        if not selected_players.empty:
            st.write(f"Filtering results for Team: {team} and Player: {player}")
            # Display relevant properties, e.g., games, points, etc.
            st.dataframe(selected_players[['games', 'goals', 'assists', 'xG', 'xA', 'key_passes', 'yellow_cards', 'red_cards']])
        else:
            st.write("No players found with the given criteria.")
    case "17-18":
        df = pd.read_csv('data/pl/players_epl_17-18.csv')

        team = st.selectbox("Select a team", df['team_title'].sort_values().unique(), index=None)
        player=st.selectbox("Select a player", df[df['team_title'] == team]['player_name'].sort_values().unique(), index=None)

        selected_players = df[(df['team_title'] == team) & (df['player_name'] == player)]

        if not selected_players.empty:
            st.write(f"Filtering results for Team: {team} and Player: {player}")
            # Display relevant properties, e.g., games, points, etc.
            st.dataframe(selected_players[['games', 'goals', 'assists', 'xG', 'xA', 'key_passes', 'yellow_cards', 'red_cards']])
        else:
            st.write("No players found with the given criteria.")
    case "18-19":
        df = pd.read_csv('data/pl/players_epl_18-19.csv')

        team = st.selectbox("Select a team", df['team_title'].sort_values().unique(), index=None)
        player=st.selectbox("Select a player", df[df['team_title'] == team]['player_name'].sort_values().unique(), index=None)

        selected_players = df[(df['team_title'] == team) & (df['player_name'] == player)]

        if not selected_players.empty:
            st.write(f"Filtering results for Team: {team} and Player: {player}")
            # Display relevant properties, e.g., games, points, etc.
            st.dataframe(selected_players[['games', 'goals', 'assists', 'xG', 'xA', 'key_passes', 'yellow_cards', 'red_cards']])
        else:
            st.write("No players found with the given criteria.")
    case "19-20":
        df = pd.read_csv('data/pl/players_epl_19-20.csv')

        team = st.selectbox("Select a team", df['team_title'].sort_values().unique(), index=None)
        player=st.selectbox("Select a player", df[df['team_title'] == team]['player_name'].sort_values().unique(), index=None)

        selected_players = df[(df['team_title'] == team) & (df['player_name'] == player)]

        if not selected_players.empty:
            st.write(f"Filtering results for Team: {team} and Player: {player}")
            # Display relevant properties, e.g., games, points, etc.
            st.dataframe(selected_players[['games', 'goals', 'assists', 'xG', 'xA', 'key_passes', 'yellow_cards', 'red_cards']])
        else:
            st.write("No players found with the given criteria.")
    case "20-21":
        df = pd.read_csv('data/pl/players_la_epl_20-21.csv')

        team = st.selectbox("Select a team", df['team_title'].sort_values().unique(), index=None)
        player=st.selectbox("Select a player", df[df['team_title'] == team]['player_name'].sort_values().unique(), index=None)

        selected_players = df[(df['team_title'] == team) & (df['player_name'] == player)]

        if not selected_players.empty:
            st.write(f"Filtering results for Team: {team} and Player: {player}")
            # Display relevant properties, e.g., games, points, etc.
            st.dataframe(selected_players[['games', 'goals', 'assists', 'xG', 'xA', 'key_passes', 'yellow_cards', 'red_cards']])
        else:
            st.write("No players found with the given criteria.")
    case "21-22":
        df = pd.read_csv('data/pl/players_epl_21-22.csv')

        team = st.selectbox("Select a team", df['team_title'].sort_values().unique(), index=None)
        player=st.selectbox("Select a player", df[df['team_title'] == team]['player_name'].sort_values().unique(), index=None)

        selected_players = df[(df['team_title'] == team) & (df['player_name'] == player)]

        if not selected_players.empty:
            st.write(f"Filtering results for Team: {team} and Player: {player}")
            # Display relevant properties, e.g., games, points, etc.
            st.dataframe(selected_players[['games', 'goals', 'assists', 'xG', 'xA', 'key_passes', 'yellow_cards', 'red_cards']])
        else:
            st.write("No players found with the given criteria.")
    case _:
        st.write()