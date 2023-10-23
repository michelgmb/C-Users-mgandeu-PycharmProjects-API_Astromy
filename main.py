import streamlit as st
import requests


api_key ="PrwGEM5MNN1HkrQOMUhWGFtcBgI17JUyLKxM6gFo"
#https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY

url ='https://api.nasa.gov/planetary/apod?' \
     f'api_key={api_key}'

response = requests.get(url)
content = response.json()

print(content)
#print(content['explanation'])
st.set_page_config(layout="wide")
st.title(content['title'])
col1 = st.image(content['url'])
col2 = st.write(content['explanation'])