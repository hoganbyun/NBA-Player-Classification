import pandas as pd
import plotly.graph_objects as go

# This function creates radar plots. Classes refers to a list that contains the names of each player class,
# year refers to the season you want to look at and good/bad/average give you the option of which teams you want
# shown on the radar plot. You can choose a combination of any years. To view all years, enter "[0]"

def plot_radar(classes, years=[2015,2016,2017,2018,2019,2020], good=True, bad=True, average=False, semisup=True):
        
    model = ''
    if semisup == True:
        model = 'Semi-Supervised'
    else:
        model = 'Unsupervised'
        
    fig = go.Figure()
    # if all years selected
    if years == 0:
        good_df, bad_df, avg_df = gba_all_years(df)
    else:
        # get good/bad/avg for first year selected
        good_df, bad_df, avg_df = get_good_bad_avg(df, years[0])
        
        # get good/bad/avg for the rest of the years, if more than one selected 
        if len(years) > 1:
            for year in years[1:]:
                # get yearly stats
                temp_df = df[df['Player'].str.contains(f'{year}')]
                # get good/bad/avg for that year
                temp_g, temp_b, temp_a = get_good_bad_avg(temp_df, year)
                good_df += temp_g; bad_df += temp_b; avg_df += temp_a
            good_df = good_df / len(years); bad_df = bad_df / len(years); avg_df = avg_df / len(years)

    if good:
        fig.add_trace(go.Scatterpolar(
            r=good_df['Class'],
            theta=classes,
              fill='toself',
              name='Good Teams'
        ))
    if bad:
        fig.add_trace(go.Scatterpolar(
            r=bad_df['Class'],
            theta=classes,
              fill='toself',
              name='Bad Teams'
        ))
    if average:
        fig.add_trace(go.Scatterpolar(
            r=avg_df['Class'],
            theta=classes,
              fill='toself',
              name='Average Teams'
        ))
            
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
              visible=True
        )),
    showlegend=True,
    title=f"{years} NBA Team Composition: {model} Model"
    )
    fig.show()