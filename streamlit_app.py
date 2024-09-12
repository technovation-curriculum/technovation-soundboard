import streamlit as st

def button_click(col):
    speech_container.audio(speechArr[col], format='audio/mpeg')

st.title("Soundboard App")
st.subheader(
    "Click on a person's name to hear a speech by that person"
)

names = ['Martin Luther King', 'Kamala Harris', 'Ketanji Brown Jackson']
imgArr = ['assets/mlk.jpg', 'assets/kamalaharris.png', 'assets/brownjackson.jpg']
speechArr = ['assets/mlk.mp3', 'assets/kamala.mp3', 'assets/brownjackson.mp3']

cols = st.columns(3)

for c in range(0, len(names)):
    cols[c].image(imgArr[c])
    cols[c].button(names[c], on_click=button_click, args=(c,), use_container_width=True)

speech_container = st.container(border=True)
speech_container.write('Audio:')
