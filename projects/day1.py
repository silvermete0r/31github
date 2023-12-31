import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
import seaborn as sns

def app():
    st.title('Day #1')
    st.subheader('Basketball Player Data Explorer 🏀')

    st.markdown("""
    This app analyze data about NBA Basketball Player Stats in Regular Seasons! Data taken from official resource using web scrapping!
    * **Python modules:** base64, pandas, streamlit.
    * **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/)
    * **Reference:** [Data Professor](https://github.com/dataprofessor)
    """)

    st.subheader('User Input Features')
    selected_year = st.selectbox('Year', list(reversed(range(1950,2024))))

    # Web scraping of NBA player stats
    @st.cache_data
    def load_data(year):
        url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
        html = pd.read_html(url, header = 0)
        df = html[0]
        raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
        raw = raw.fillna(0)
        player_stats = raw.drop(['Rk'], axis=1)
        return player_stats
    player_stats = load_data(selected_year)

    # Team Selection
    team_fullnames = {
        'ATL': 'Atlanta Hawks',
        'BOS': 'Boston Celtics',
        'BRK': 'Brooklyn Nets',
        'CHI': 'Chicago Bulls',
        'CHO': 'Charlotte Hornets',
        'CLE': 'Cleveland Cavaliers',
        'DAL': 'Dallas Mavericks',
        'DEN': 'Denver Nuggets',
        'DET': 'Detroit Pistons',
        'GSW': 'Golden State Warriors',
        'HOU': 'Houston Rockets',
        'IND': 'Indiana Pacers',
        'LAC': 'Los Angeles Clippers',
        'LAL': 'Los Angeles Lakers',
        'MEM': 'Memphis Grizzlies',
        'MIA': 'Miami Heat',
        'MIL': 'Milwaukee Bucks',
        'MIN': 'Minnesota Timberwolves',
        'NOP': 'New Orleans Pelicans',
        'NYK': 'New York Knicks',
        'OKC': 'Oklahoma City Thunder',
        'ORL': 'Orlando Magic',
        'PHI': 'Philadelphia 76ers',
        'PHO': 'Phoenix Suns',
        'POR': 'Portland Trail Blazers',
        'SAC': 'Sacramento Kings',
        'SAS': 'San Antonio Spurs',
        'TOR': 'Toronto Raptors',
        'UTA': 'Utah Jazz',
        'WAS': 'Washington Wizards'
    }
    sorted_unique_team = sorted(player_stats.Tm.unique())
    selected_team = st.multiselect('Team', sorted_unique_team, sorted_unique_team)
    with st.expander('Team Description'):
        st.json(team_fullnames)

    # Position Selection
    pos_fullnames = {
        'PG': 'Point Guard',
        'SG': 'Shooting Guard',
        'SF': 'Small Forward',
        'PF': 'Power Forward',
        'C': 'Center'
    }
    unique_pos = ['PG', 'SG', 'SF', 'PF', 'C']
    selected_pos = st.multiselect('Position', unique_pos, unique_pos)
    with st.expander('Position Description'):
        st.json(pos_fullnames)

    # Filtering Data
    df_selected_team = player_stats[(player_stats.Tm.isin(selected_team)) & (player_stats.Pos.isin(selected_pos))]

    # Display Data
    st.subheader(f'Display Player Stats of {team_fullnames[selected_team[0]] if len(selected_team)==1 else "Selected Teams"}' if len(selected_team)>0 else "No Teams Selected")
    st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
    st.dataframe(df_selected_team)

    # Download NBA Player Stats as CSV file
    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode() # string <-> bytes conversions
        href = f'<a href="data::file/csv;base64,{b64}" download="player_stats.csv">Download as CSV File</a>'
        return href
    
    st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)
    

    # Interesting Stats: Correlation Heatmap, Top 10 Best Players, Top 10 Defensive Players, Top 10 Rebouders, Favorite Player Stats
    selected_option = st.selectbox('Select Option', ['None', 'Correlation Heatmap', 'Top 10 Best Players', 'Top 10 Defensive Players', 'Top 10 Rebouders', 'Favorite Player Stats'])
    
    if selected_option == 'None':
        st.write('Please select an option from the dropdown menu.')

    if selected_option == 'Correlation Heatmap':
        st.header('Correlation Matrix Heatmap')
        df_selected_team.to_csv('data/output.csv', index=False)
        df = pd.read_csv('data/output.csv')
        df = df.select_dtypes(include=['float64'])
        corr = df.corr(method='spearman')
        plt.figure(figsize=(15, 15), dpi=300)
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True
        sns.heatmap(corr, mask=mask, cmap='viridis', annot=True, annot_kws={'size': 7}, fmt='.2f', linewidths=0.5)
        plt.tight_layout()
        st.pyplot()

    if selected_option == 'Top 10 Best Players':
        st.header('Top 10 Best Players by Points')
        df_selected_team.to_csv('data/output.csv', index=False)
        df = pd.read_csv('data/output.csv')
        df = df.sort_values(by=['PTS'], ascending=False)
        df = df.head(10)
        st.dataframe(df)

    if selected_option == 'Top 10 Defensive Players':
        st.header('Top 10 Defensive Players by STL')
        df_selected_team.to_csv('data/output.csv', index=False)
        df = pd.read_csv('data/output.csv')
        df = df.sort_values(by=['STL'], ascending=False)
        df = df.head(10)
        st.dataframe(df)
        
    if selected_option == 'Top 10 Rebouders':
        st.header('Top 10 Rebouders by TRB')
        df_selected_team.to_csv('data/output.csv', index=False)
        df = pd.read_csv('data/output.csv')
        df = df.sort_values(by=['TRB'], ascending=False)
        df = df.head(10)
        st.dataframe(df)

    if selected_option == 'Favorite Player Stats':
        with st.form(key='my_form'):
            player_name = st.text_input(label='Enter Player Name')
            submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            st.markdown(f'Player Stats for <code>{player_name}</code>', unsafe_allow_html=True)
            df_selected_team.to_csv('data/output.csv', index=False)
            df = pd.read_csv('data/output.csv')
            df = df[df['Player'].str.contains(player_name)]
            st.dataframe(df)