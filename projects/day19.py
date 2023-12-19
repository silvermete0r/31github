import streamlit as st
import instaloader

def get_profile_data(username):
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        data = profile._asdict()
        return data

    except instaloader.exceptions.ProfileNotExistsException:
        st.error('Profile not found.')
        return None
    
    except Exception as e:
        st.error(f'Error: {e}')
        return None

def app():
    st.title('Day #19')
    st.subheader('Instagram Analytics Web App')
    st.markdown('''
        This app uses the `instaloader` library to download Instagram profile data.
                
        Reference: [Instaloader](https://instaloader.github.io/)
    ''')
    st.write('---')

    st.markdown('### Input Instagram Username')
    username = st.text_input('Enter username: ')

    if st.button('Analyze'):
        if not username:
            st.warning('Please enter a username.')
            st.stop()

        with st.spinner('Analyzing..'):
            profile = get_profile_data(username)
            if not profile:
                st.stop()
            colA, colB = st.columns([2, 5])
            with colA:
                st.image(profile['profile_pic_url_hd'], width=200, caption='Profile Picture')
                st.caption(f"{profile['full_name']} | @{profile['username']}")
                colX, colY = st.columns(2)
                with colX:
                    st.write('Followers')
                    st.write(profile['edge_followed_by']['count'])
                with colY:
                    st.write('Following')
                    st.write(profile['edge_follow']['count'])
            with colB:
                st.write(profile['biography'])
            st.write('---')

            st.markdown('### Full Profile Data JSON')
            with st.container():
                st.json(profile)