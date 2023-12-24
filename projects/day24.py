import streamlit as st
import requests
from datetime import datetime

def format_time(time):
    return datetime.fromtimestamp(time).strftime('%Y-%m-%d')

def get_content(item_id):
    url = f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json'
    r = requests.get(url)
    content = r.json()
    return content

@st.cache_resource()
def get_top_stories():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)
    top_stories = r.json()[:30]
    list_top_stories = []
    for story in top_stories:
        content = get_content(story)
        data = {
            'title': content['title'],
            'url': f"https://news.ycombinator.com/item?id={content['id']}",
            'by': content['by'],
            'score': content['score'],
            'date': format_time(content['time'])
        }
        list_top_stories.append(data)
    return sorted(list_top_stories, key=lambda x: x['score'], reverse=True)

def app():
    colA, colB = st.columns([3, 5])
    colA.title('Day #24')
    colA.subheader('HackerNews Streamlit App')
    colA.markdown('''
        This app is a clone of [HackerNews](https://news.ycombinator.com/) in Streamlit UI.
                
        Reference: [HackerNews API](https://github.com/HackerNews/API)
    ''')
    colB.image('media/ycombinator-logo.png', width=250)
    st.write('---')
    
    st.markdown('<h3 style="color: yellow;">Top Stories</h3>', unsafe_allow_html=True)
    st.write('Choose how many stories you want to see:')
    num_stories = st.slider('', 1, 30, 10)

    with st.spinner('Loading...'):
        stories = get_top_stories()
        for idx, story in enumerate(stories[:num_stories]):
            st.markdown(f'''
                <h4 style="color: orange;">{idx+1}. {story['title']}</h4>
                <ul>
                    <li><b>Author:</b> <code>{story['by']}</code></li>
                    <li><b>Score:</b> <code>{story['score']}</code></li>
                    <li><b>Date:</b> <code>{story['date']}</code></li>
                </ul>
            ''', unsafe_allow_html=True)
            st.link_button('Read more', story['url'])
            st.write('---')