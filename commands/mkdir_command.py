import commands.base_command
import requests 
from bs4 import BeautifulSoup
from utils import get_emoji
import os

class Mkdir(commands.base_command.BaseCommand):

    def __init__(self):
        description = "Displays OPGG info of given summoner (use underscore instead of spaces)"
        params = ["nickname"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            name = str(params[0])
        except ValueError:
            await message.channel.send("Please, provide valid numbers")
            return

        route = "/users/krzysiektluszcz/Desktop/" + name
        if name != "":
            os.mkdir(route)