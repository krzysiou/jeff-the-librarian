import commands.base_command
import requests 
from bs4 import BeautifulSoup 
from utils                  import get_emoji

class Opgg(commands.base_command.BaseCommand):

    def __init__(self):
        description = "Displays OPGG link"
        params = ["nickname1"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            nick1 = str(params[0])

            nick1.replace('_','+')
        except ValueError:
            await message.channel.send("Please, provide valid numbers")
            return

        url1='https://eune.op.gg/summoner/userName='+ nick1

        await message.channel.send(message.author.mention +"\n"
        +"** Link:   **" + url1
        )
