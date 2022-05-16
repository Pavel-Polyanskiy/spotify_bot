# %%
import pandas as pd
import numpy as np
import plotly.express as px
import pathlib
# %%
#from sklearn.preprocessing import MinMaxScaler


# %%
def get_track_visualization(artist, song_name):
    #loading data
    df_scaled = pd.read_csv(str(pathlib.Path().parent.absolute()) + '/data/data_scaled_visualization.csv', index_col = 0)
    columns = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness']

    #track id
    track_id = df_scaled[(df_scaled['artist'] == artist) & (df_scaled['song_name'] == song_name)].index[0]
    #vis
    df_for_vis = df_scaled[columns]
    df_vis = pd.DataFrame(dict(
        r = df_for_vis.loc[track_id],
        theta = df_for_vis.columns))
    fig = px.line_polar(df_vis, r = 'r', theta = 'theta', line_close = True)
    fig.update_traces(fill = 'toself')
    fig.update_layout(
        title={
            'text': f"{song_name} by {artist}",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(margin_t = 70)
    fig.update_layout(margin_b = 40)

    fig.update_layout(
        polar = dict(
            radialaxis = dict(range=[0, 1], showticklabels=False)))
    return fig



