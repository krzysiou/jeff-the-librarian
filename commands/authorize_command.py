import commands.base_command
import sys
import re
import spotipy
import spotipy.util as util
import settings

class Authorize(commands.base_command.BaseCommand):

    def __init__(self):
        description = "Authorize command."
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client):
        
        await message.author.send("Click the link below and authorize yourself on spotify website.")

        url='https://accounts.spotify.com/pl/authorize?scope=playlist-modify-private,playlist-modify-public&response_type=code&redirect_uri=https:%2F%2Flocalhost:8080&client_id='+settings.SPOTIFY_CLIENT_ID

        await message.author.send(url + '\n' +  message.author.mention)


