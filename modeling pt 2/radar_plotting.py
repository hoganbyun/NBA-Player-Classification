import pandas as pd
import plotly.graph_objects as go

# This function creates radar plots. Classes refers to a list that contains the names of each player class,
# year refers to the season you want to look at and good/bad/average give you the option of which teams you want
# shown on the radar plot

def plot_radar(classes, years=[2015,2016,2017,2018,2019,2020], good=True, bad=True, average=False, semisup=True):
        
    model = ''
    if semisup == True:
        model = 'Semi-Supervised'
    else:
        model = 'Unsupervised'
        
    fig = go.Figure()
    
    if good:
        # combine good teams for all years selected 
        good_df = pd.read_csv(f'results/radar_data/{model}/{years[0]}/good')
        if len(years) > 1:
            for year in years:
                good_df += pd.read_csv(f'results/radar_data/{model}/{year}/good')
            good_df = good_df / len(years)
        
        fig.add_trace(go.Scatterpolar(
            r=good_df['Class'],
            theta=classes,
              fill='toself',
              name='Good Teams'
        ))
    if bad:
        # combine bad teams for all years selected 
        bad_df = pd.read_csv(f'results/radar_data/{model}/{years[0]}/bad')
        if len(years) > 1:
            for year in years:
                bad_df += pd.read_csv(f'results/radar_data/{model}/{year}/bad')
            bad_df = bad_df / len(years)
          
        fig.add_trace(go.Scatterpolar(
            r=bad_df['Class'],
            theta=classes,
              fill='toself',
              name='Bad Teams'
        ))
    if average:
        # combine average teams for all years selected 
        avg_df = pd.read_csv(f'results/radar_data/{model}/{years[0]}/average')
        if len(years) > 1:
            for year in years:
                avg_df += pd.read_csv(f'results/radar_data/{model}/{year}/average')
            avg_df = avg_df / len(years)
            
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