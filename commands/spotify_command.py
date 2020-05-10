import commands.base_command
import sys
import re
import spotipy
import spotipy.util as util
import settings
import base64
import requests

class Spotify(commands.base_command.BaseCommand):

    def __init__(self):
        description = "Adds track to a playlist on spotify (use '_' instead of spaces)"
        params = ["author","song"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:

            author = str(params[0])
            artist = author.replace('_',' ')
            song = str(params[1])
            track = song.replace('_',' ')

            print(artist + "  " + track)

        except ValueError:
            await message.channel.send("Please, provide valid numbers")
            return

        payload = {
            'grant_type': 'refresh_token',
            'refresh_token': settings.SPOTIFY_REFRESH_TOKEN
        }

        #encode

        message = settings.SPOTIFY_CLIENT_ID + ":" + settings.SPOTIFY_CLIENT_SECRET
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        response = requests.post(url="https://accounts.spotify.com/api/token", data=payload, headers={'Authorization': 'Basic '+base64_message})
        json_response = response.json()

        token = json_response["access_token"]

        if token:
            global sp
            sp = spotipy.Spotify(auth=token)

            wanted_track = sp.search(q='artist:' + artist + ' track:' + track, type='track')
            extracted_id = wanted_track["tracks"]["items"][0]["id"]
            print("\nAdding: " + extracted_id+"\n")

            track_ids = [extracted_id]

            sp.trace = False
            results = sp.user_playlist_add_tracks(settings.SPOTIFY_USERNAME, settings.SPOTIFY_PLAYLIST_ID, track_ids)

        else:
            print ("Can't get token for", settings.SPOTIFY_USERNAME)