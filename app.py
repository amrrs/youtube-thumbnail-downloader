import streamlit as st

st.title("Youtube Thumbnail Downloader")

st.text('Enter a Youtube Video Complete URL whose thumbnail you would like to download')

url = st.text_input(label = 'Enter a Youtube Video Complete URL')

if '&' in session_state.url:
    id = session_state.url[session_state.url.find('=') + 1:session_state.url.find('&')]
else:
    id = session_state.url[session_state.url.find('=') + 1:]

max_res = 'https://img.youtube.com/vi/'+id+'/maxresdefault.jpg'

st.text('Max Resolution Thubmnail - Right Click and Save it!!!')

st.image(max_res)
