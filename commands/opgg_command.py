import commands.base_command
import requests 
from bs4 import BeautifulSoup 
from utils                  import get_emoji

class Opgg(commands.base_command.BaseCommand):

    def __init__(self):
        description = "Displays OPGG link"
        params = ["nickname1","nickname2","nickname3","nickname4","nickname5"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            nick1 = str(params[0])
            nick2 = str(params[1])
            nick3 = str(params[2])
            nick4 = str(params[3])
            nick5 = str(params[4])

            nick1.replace('_','+')
            nick2.replace('_','+')
            nick3.replace('_','+')
            nick4.replace('_','+')
            nick5.replace('_','+')
        except ValueError:
            await message.channel.send("Please, provide valid numbers")
            return

        url1='https://eune.op.gg/summoner/userName='+ nick1
        url2='https://eune.op.gg/summoner/userName='+ nick2
        url3='https://eune.op.gg/summoner/userName='+ nick3
        url4='https://eune.op.gg/summoner/userName='+ nick4
        url5='https://eune.op.gg/summoner/userName='+ nick5

        await message.channel.send(message.author.mention +"\n"
        +"** Link:   **" + url1 + "\n"
        +"** Link:   **" + url2 + "\n"
        +"** Link:   **" + url3 + "\n"
        +"** Link:   **" + url4 + "\n"
        +"** Link:   **" + url5 + "\n"
        )
