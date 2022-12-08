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
    popular Magic the Gathering site called EDHRec.com polls players on the top 100 cards that they think are the saltiest. The average score and count of votes for these \
    cards give these cards a salt score. Below is an analysis on common attributes between these cards.")
st.write("From my personal expirience, I hypothesize that blue, low CMC, instants and/or soceries will be the saltiest. These cards frequently are used as a way to say 'NO', \
    as in \"I'm not going to let you do that, you can't have fun, rethink your plan\". This type of gameplay where you aren't achieving anything, but just stopping other \
    people from doing things is commonly aggravating to other players.")

st.header("Correlation of Numerical Components of Cards")

st.write("In the table below, 'score' refers to the score that the card was given on EDHRec. CMC is the converted mana cost, or how many resources the card costs to play. \
    Price is what the card costs to buy in USD, and the year is the year the card was first printed.")

corrTable = px.imshow(df.corr(numeric_only=True), text_auto=True, height=800, width=800, template='ggplot2', aspect='auto', title='Correlation Table')
corrTable.update_layout(title_x=0.5)
st.plotly_chart(corrTable, use_container_width = True)

st.write("As we can see from this table, there is only a significant correlation in between the CMC and the price, suggesting that cards with a lower CMC are often \
     more expensive. We can see that, to a lesser extent, cards with older first printing dates are more expensive to buy.")



st.header("Supertypes")

st.write("The following graph shows the frequency of the 'supertypes' of cards in the Top 100 list. Different types of cards perform different actions in the game, \
    ranging from cards that stay in the game until something removes them, to cards that are a one-time use, short effect.")

stvc = df['supertype'].value_counts()
barFig = px.bar(stvc, x=stvc.index, y=stvc.values, title="Count of Supertypes in the Top 100 Saltiest Cards", labels={'index': 'Supertype', 'y': 'Count'})
st.plotly_chart(barFig)

st.write("This chart shows that the most commonly appearing supertypes of cards are shared between Creature and Sorcery cards, two very different types of cards, \
    which is interesting. The lowest 2 are Lands and Artifact Creatures, which is intuivitive because lands do not commonly interact with other cards often and \
    artifact creatures are not printed as commonly as the other supertypes.")


st.header("Colors")

st.write("Finally, we will be looking at the color of these cards. In Magic: The Gathering, each color of card best generally supports a certain type of playstyle. \
    For example, blue cards often are reactive rather than aggressive. Having an insight into what colors give us the saltiest cards can also provide insight into \
    what playstyles are found to be annoying.")
st.write("White, blue, black, red, and green cards are printed at roughly the same frequency in each set, while multicolored (cards that require the player to be \
    playing with a combination of colors) are printed slightly less frequently, and colorless being printed much less frequently.")
st.write("The chart below shows how much the cards the fall under each color's category contribute to the whole. The whole is the sum of every salt score given, and each \
    card contributes it's salt score to it's respective color. As such, a card with a salt score of 3 will 'be worth' 3x as much as a card with a salt score of 1.")

df['coloridfull'] = df['colorid'].apply(colorFull)
pieFig = px.pie(df, values='score', names='coloridfull', color='coloridfull', title="Each Color's Share of Salt",
            color_discrete_map={
                'White': 'white',
                'Blue': 'blue',
                'Black': 'black',
                'Red': 'red',
                'Green': 'green',
                'Colorless': 'grey',
                'Multi-colored': 'gold'
            }, labels={'coloridfull': 'Color', 'score': 'Total Score'})
st.plotly_chart(pieFig)

st.write("As we can see, blue has by a measure of 10% the most saltiest cards. An interesting data point is dispite the frequency of printing of colorless cards, they \
    have one of the highest shares.")


st.header("Conclusion")
st.write("This data and the visualizations give us deep insight to some of the factors. First, we can see that my hypothesis was partially correct. Blue cards and sorcery\
    cards are two of the saltiest cards. However, CMC has only a -0.036 correlation with salt score, and there are only 9 instants (which allow for quick plays) in the\
    top 100 saltiest cards. From the data, we could say that a blue creature or sorcery would be more likely to salty than any other card.")

st.write("\n\n\nCreated by Thomas Pelowitz")
print('Done!')