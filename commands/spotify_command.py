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
            artist = str(params[0])
            artist.replace('_',' ')
            track = str(params[1])
            track.replace('_',' ')

        except ValueError:
            await message.channel.send("Please, provide valid numbers")
            return

        global sp
        token = util.prompt_for_user_token(settings.SPOTIFY_USERNAME, scope='playlist-modify-private,playlist-modify-public', client_id=settings.SPOTIFY_CLIENT_ID, client_secret=settings.SPOTIFY_CLIENT_SECRET, redirect_uri=settings.SPOTIFY_REDIRECT_URI)
        print(token)

        if token:
            sp = spotipy.Spotify(auth=token)
            #get_wacken_tracks()

            wanted_track = sp.search(q='artist:' + artist + ' track:' + track, type='track')
            
            m = re.search("'track_number': 1, 'type': 'track', 'uri': 'spotify:track:(.+?)'}], 'limit", str(wanted_track))
            if m:
                extracted_id = m.group(1)
            #print(wanted_track)
            print("\nAdding: " + extracted_id+"\n")

            track_ids = [extracted_id]

            sp.trace = False
            results = sp.user_playlist_add_tracks(settings.SPOTIFY_USERNAME, settings.SPOTIFY_PLAYLIST_ID, track_ids)

        else:
            print ("Can't get token for", settings.SPOTIFY_USERNAME)