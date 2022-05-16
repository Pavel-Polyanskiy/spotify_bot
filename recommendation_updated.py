import pandas as pd
import pathlib
import random


def get_final_recs_new(track_id, n = 3):
    recs_df = pd.read_csv(str(pathlib.Path().parent.absolute()) + '/data/30_recs_per_track.csv')
    id2track = pd.read_csv(str(pathlib.Path().parent.absolute()) + '/data/id2track.csv',index_col=0)

    recs = recs_df[recs_df['track_id'] == track_id]

    track_cluster = id2track[id2track.index == track_id].clust
    input_artist_name = id2track[id2track.index == track_id].artist

    track_names = list(eval(recs_df[recs_df['track_id'] == track_id].track_names.values[0]))

    track_links = list(eval(recs_df[recs_df['track_id'] == track_id].track_ids.values[0]))

    track_ids = [id.split('/')[-1] for id in track_links]

    final_ids = [name for name in track_ids if id2track[id2track.index == name].clust[0] == track_cluster[0]]
    final_links = ['https://open.spotify.com/track/' + id for id in final_ids]
    final_names = id2track.loc[final_ids]['full_name'].values.tolist()

    track_recs = dict(zip(final_links, final_names))
    if len(final_names)  >= n:
        track_recs = dict(random.sample(track_recs.items(), n))

    else: 
        track_recs = dict(random.sample(track_recs.items(), len(final_names)))

    return track_recs