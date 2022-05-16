import pandas as pd
import pathlib
import random


def get_final_recs(track_id, n = 3):
    recs_df = pd.read_csv(str(pathlib.Path().parent.absolute()) + '/data/30_recs_per_track.csv')
    recs = recs_df[recs_df['track_id'] == track_id]
    
    track_names = list(eval(recs_df[recs_df['track_id'] == track_id].track_names.values[0]))
    track_links = list(eval(recs_df[recs_df['track_id'] == track_id].track_ids.values[0]))
    track_recs = dict(zip(track_links, track_names))

    track_recs = dict(random.sample(track_recs.items(), n))

    return track_recs

