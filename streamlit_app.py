import pandas as pd
import streamlit as st
import plotly.express as px

def supertype(x):
    output = x.split('—') #split at dash
    output = output[0].replace('Legendary', '').replace('World', '') #remove unimportant / outdated catergories in supertype
    return output.strip() #final clean

getYear = lambda x: int(x.split('-')[0])

def colorFull(x):
    if x == "['W']":
        return 'White'
    elif x == "['U']":
        return 'Blue'
    elif x == "['B']":
        return 'Black'
    elif x == "['R']":
        return 'Red'
    elif x == "['G']":
        return 'Green'
    elif x == "['CL']":
        return 'Colorless'
    elif x == "['MC']":
        return 'Multi-colored'
    else:
        return x

df = pd.read_csv('./top100salt.csv')

df['supertype'] = df['type'].apply(supertype)
df['year'] = df['date'].apply(getYear)

st.title('Magic the Gathering "Salt" Analysis')
st.write("Magic the Gathering is a popular trading card game produced by Wizards of the Coast. The game is renowned for its complextiy, and the ability for player to \
    play the way that they want. When a card is commonly used in a way that inspires annoyance in other players, that card is labeled as a 'salty' card. Every year, a  \
    popular Magic the Gathering site polls players on the top 100 cards that they think are the saltiest. The average score and count of votes for these cards give \
    these cards a salt score. Below is an analysis on common attributes between these cards.")

corrTable = px.imshow(df.corr(numeric_only=True), text_auto=True, height=800, width=800, template='ggplot2', aspect='auto', title='Correlation of Numerical Columns')
corrTable.update_layout(title_x=0.5)
st.plotly_chart(corrTable, use_container_width = True)

print('Done!')