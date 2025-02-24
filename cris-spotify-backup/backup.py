import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import json

import os

load_dotenv()

TRACKS_JSON_FILE = 'tracks.json'

CHUNK_SIZE = 50
client_id = os.getenv('CLIEND_ID')
client_secret = os.getenv('CLIENT_SECRET')

all_tracks_list = []
dead_tracks_list = []


def chunked_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


if not os.path.isfile(TRACKS_JSON_FILE):
    with open('tracks.txt') as tracks_file:
        tracks = [x.strip().split("/")[-1] for x in tracks_file.readlines()]

    auth_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    all_tracks_result = []
    for chuck in chunked_list(tracks, CHUNK_SIZE):
        tracks_result = sp.tracks(tracks=chuck, market='CA')['tracks']
        all_tracks_result += tracks_result

    with open(TRACKS_JSON_FILE, 'w') as f:
        f.write(json.dumps(all_tracks_result))
else:
    with open(TRACKS_JSON_FILE, 'r') as f:
        all_tracks_result = json.loads(f.readline())

print(f'tracks loaded = {len(all_tracks_result)}')

for track_result in all_tracks_result:
    if not track_result['is_playable']:
        dead_tracks_list.append(track_result)
    all_tracks_list.append(track_result)


with open('out_all_tracks.txt', 'w') as f:
    for track in all_tracks_list:
        f.write(
            f'{track['name']} - {track['artists'][0]['name']}\n')

with open('out_dead_tracks.txt', 'w') as f:
    for track in dead_tracks_list:
        f.write(
            f'{track['name']} - {track['artists'][0]['name']}\n')
