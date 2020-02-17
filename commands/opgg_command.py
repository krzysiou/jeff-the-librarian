import commands.base_command
import requests 
from bs4 import BeautifulSoup 
from utils                  import get_emoji

class Opgg(commands.base_command.BaseCommand):

    def __init__(self):
        description = "Displays OPGG link"
        params = ["nickname"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            nick = str(params[0])
            nick.replace('_','+')
        except ValueError:
            await message.channel.send("Please, provide valid numbers")
            return

        url='https://eune.op.gg/summoner/userName='+ nick

        await message.channel.send(message.author.mention +"\n"
        +"*** Link: ***" + url
        )
