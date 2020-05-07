import commands.base_command
import sys
import re
import spotipy
import spotipy.util as util
import settings

class Spotify(commands.base_command.BaseCommand):

    def __init__(self):
        description = "Adds track to a playlist on spotify (use '_' instead of spaces)"
        params = ["artist","track"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            print(params[0] + "  " + params[1])

            artist = str(params[0])
            artist.replace('_',' ')
            track = str(params[1])
            track.replace('',' ')

            print(artist + "  " + track)

        except ValueError:
            await message.channel.send("Please, provide valid numbers")
            return

        global sp

        if settings.SPOTIFY_TOKEN:
            sp = spotipy.Spotify(auth=settings.SPOTIFY_TOKEN)

            wanted_track = sp.search(q='artist:' + artist + ' track:' + track, type='track')
            extracted_id = wanted_track["tracks"]["items"][0]["id"]
            print("\nAdding: " + extracted_id+"\n")

            track_ids = [extracted_id]

            sp.trace = False
            results = sp.user_playlist_add_tracks(settings.SPOTIFY_USERNAME, settings.SPOTIFY_PLAYLIST_ID, track_ids)

        else:
            print ("Can't get token for", settings.SPOTIFY_USERNAME)