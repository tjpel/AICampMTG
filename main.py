import pandas as pd
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
ctr = pd.crosstab(index=df['year'], columns=df['supertype'])

corrTable=px.imshow(df.corr(),text_auto=True,height=600,width=600,template='ggplot2',aspect='auto',title='<b>Pairwise Correlation of Columns</b>')
corrTable.update_layout(title_x=0.5)
corrTable.show()

stvc = df['supertype'].value_counts()
barFig = px.bar(stvc, x=stvc.index, y=stvc.values)
barFig.show()

df['coloridfull'] = df['colorid'].apply(colorFull)
pieFig = px.pie(df, values='score', names='coloridfull', color='coloridfull',
            color_discrete_map={
                'White': 'white',
                'Blue': 'blue',
                'Black': 'black',
                'Red': 'red',
                'Green': 'green',
                'Colorless': 'grey',
                'Multi-colored': 'gold'
            })
pieFig.show()