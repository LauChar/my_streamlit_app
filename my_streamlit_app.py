import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Hello Wilders, welcome to my application!')

st.write('I enjoy discovering Streamlit possibilities.')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)

# st.write(df_weather)
df_weather

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

viz_correlation = sns.heatmap(df_weather.corr(),
                                center = 0,
                                cmap =sns.color_palette("vlag", as_cmap = True)
)

st.pyplot(viz_correlation.figure)

st.title("Hello Wilders, welcome to my application!")

name = st.text_input("Please give me your name:")
name_length = len(name)
st.write(f"Your name has {name_length} characters")

