import streamlit as st
import requests 
import datetime as dt

def app():
    st.title('Day #8')
    st.subheader('Github Profile Data Analyzer Web App')
    st.markdown("""
        This app retrieves the list of repositories of any Github profile and displays the repository name, the number of stars and the language used in the repository.
        
        * **Python libraries:** `streamlit`, `requests`, `datetime`
        
        * **Data source:** [Github API](https://docs.github.com/en/rest)
    
        ---
    """)

    def time_format(time):
        time = dt.datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
        return time.strftime('%d %b %Y')

    def list_repos(username):
        response = requests.get(f'https://api.github.com/users/{username}/repos')
        repos = response.json()
        for id, repo in enumerate(repos):
            st.markdown(f"""
                ### {id+1}. {repo['name']}
                * **Owner:** {repo['owner']['login']}
                * **Description:** {repo['description']} 
                * **Language:** {repo['language']} 
                * **Number of Stars:** {repo['stargazers_count']} ⭐
                * **Number of Forks:** {repo['forks_count']} 🍴
                * **License:** {repo['license']['name'] if repo['license'] is not None else 'No License'} 📜
                * **Created At:** {time_format(repo['created_at'])}
                * **Last Updated At:** {time_format(repo['updated_at'])}
            """)
            st.link_button("Explore", repo['html_url'])
            st.write('---')
    
    def list_gists(username):
        response = requests.get(f'https://api.github.com/users/{username}/gists')
        gists = response.json()
        for id, gist in enumerate(gists):
            st.markdown(f"""
                ### {id+1}. {gist['description']}
                * **Owner:** {gist['owner']['login']}
                * **Created At:** {time_format(gist['created_at'])}
                * **Last Updated At:** {time_format(gist['updated_at'])}
            """)
            st.link_button("Explore", gist['html_url'])
            st.write('---')
    
    def show_github_profile(username):
        response = requests.get(f'https://api.github.com/users/{username}')
        profile = response.json()
        colA, colB = st.columns([2, 5])
        colA.image(profile['avatar_url'], width=250)
        colA.link_button('Explore', profile['html_url'])
        colB.markdown(f"""
            ### {profile['name']}
            * **Username:** {profile['login']}
            * **Location:** {profile['location']}
            * **Email:** {profile['email']}
            * **Bio:** {profile['bio']}
            * **Public Repositories:** {profile['public_repos']}
            * **Public Gists:** {profile['public_gists']}
            * **Followers:** {profile['followers']}
            * **Following:** {profile['following']}
            * **Created At:** {time_format(profile['created_at'])}
            * **Last Updated At:** {time_format(profile['updated_at'])}
        """)
    
    username = st.text_input('Enter Github Username', 'silvermete0r')

    if st.button('Submit'):
        response = requests.get(f'https://api.github.com/users/{username}')
        if response.status_code == 404:
            st.error('User not found')
        else:
            st.success(f'User {username} found in Github')
            with st.spinner('Loading Profile Data...'):
                show_github_profile(username)
                st.toast('Profile Data Loaded')
                _, col1, col2, _ = st.columns([5, 3, 2, 5])
                if col1.button('List Repositories'):
                    list_repos(username)
                if col2.button('List Gists'):
                    list_gists(username)