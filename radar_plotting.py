import pandas as pd
import plotly.graph_objects as go

# list of good teams and bad teams (top and bottom 8)
good_2015 = ['GSW', 'SAS', 'CLE', 'TOR', 'OKC', 'LAC', 'ATL', 'BOS']
bad_2015 = ['PHI', 'LAL', 'BKN', 'PHX', 'MIN', 'NOP', 'NYK', 'SAC']

good_2016 = ['GSW', 'SAS', 'HOU', 'BOS', 'CLE', 'LAC', 'TOR', 'UTA']
bad_2016 = ['BKN', 'PHX', 'LAL', 'PHI', 'ORL', 'NYK', 'MIN', 'SAC']

good_2017 = ['HOU', 'TOR', 'GSW', 'BOS', 'PHI', 'CLE', 'POR', 'IND']
bad_2017 = ['PHX', 'MEM', 'DAL', 'ATL', 'ORL', 'SAC', 'CHI', 'BKN']

good_2018 = ['MIL', 'TOR', 'GSW', 'DEN', 'HOU', 'POR', 'PHI','UTA']
bad_2018 = ['NYK', 'PHX', 'CLE', 'CHI', 'ATL', 'WAS', 'NOP', 'MEM']

good_2019 = ['MIL', 'TOR', 'LAL', 'LAC', 'BOS', 'DEN', 'IND', 'HOU']
bad_2019 = ['GSW', 'MIN', 'CLE', 'DET', 'ATL', 'NYK', 'CHI', 'CHA']

good_2020 = ['UTA', 'PHI', 'PHO', 'LAC', 'MIL', 'BKN', 'LAL', 'DEN']
bad_2020 = ['MIN', 'DET', 'ORL', 'HOU', 'WAS', 'CLE', 'TOR', 'OKC']

# This function creates radar plots. Classes refers to a list that contains the names of each player class,
# year refers to the season you want to look at and good/bad/average give you the option of which teams you want
# shown on the radar plot

def plot_radar(df, classes, year, good=True, bad=True, average=False):
    top_5_df = pd.DataFrame(df.groupby('TEAM')['MIN'].nlargest()).reset_index()['level_1']
    
    temp = df.merge(top_5_df, left_index=True, right_on='level_1', how='inner').reset_index(drop=True)

    if year == 2015:
        good_teams = good_2015
        bad_teams = bad_2015
    elif year == 2016:
        good_teams = good_2016
        bad_teams = bad_2016
    elif year == 2017:
        good_teams = good_2017
        bad_teams = bad_2017
    elif year == 2018:
        good_teams = good_2018
        bad_teams = bad_2018
    elif year == 2019:
        good_teams = good_2019
        bad_teams = bad_2019
    elif year == 2020:
        good_teams = good_2020
        bad_teams = bad_2020
    else:
        return "Please enter a year between 2015 and 2020, inclusive"
    
    good_df = pd.DataFrame(temp[temp['TEAM'].isin(good_teams)]['Class'].value_counts().sort_index())
    good_df['Class'] = good_df['Class'] / 8
    good_df = good_df.drop(0)

    bad_df = pd.DataFrame(temp[temp['TEAM'].isin(bad_teams)]['Class'].value_counts().sort_index())
    bad_df['Class'] = bad_df['Class'] / 8
    bad_df = bad_df.drop(0)
    
    avg_df = temp.drop(temp[temp['TEAM'].isin(good_teams + bad_teams)].index)['Class'].value_counts().sort_index()
    avg_df = avg_df / 14
    avg_df = avg_df.drop(0)
    
    fig = go.Figure()
    
    if good:
        fig.add_trace(go.Scatterpolar(
            r=good_df['Class'],
            theta=classes[1:],
              fill='toself',
              name='Good Teams'
        ))
    if bad:
        fig.add_trace(go.Scatterpolar(
            r=bad_df['Class'],
            theta=classes[1:],
              fill='toself',
              name='Bad Teams'
        ))
    if average:
        fig.add_trace(go.Scatterpolar(
            r=avg_df,
            theta=classes[1:],
              fill='toself',
              name='Average Teams'
        ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
              visible=True,
              range=[0, 2]
        )),
      showlegend=True
    )

    fig.show()


# In[ ]:




