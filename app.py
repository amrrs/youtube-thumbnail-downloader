import streamlit as st

st.title("Youtube Thumbnail Downloader")

st.text('Enter a Youtube Video Complete URL whose thumbnail you would like to download')

url = st.text_input(label = 'Enter a Youtube Video Complete URL')

id = url.split('=')[-1]

max_res = 'https://img.youtube.com/vi/'+id+'/maxresdefault.jpg'

st.text('Max Resolution Thubmnail - Right Click and Save it!!!')

st.image(max_res)
