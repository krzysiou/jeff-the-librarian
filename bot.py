import sys

import settings
import discord
import message_handler
import random

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from events.base_event              import BaseEvent
import events
from multiprocessing                import Process
from utils import get_emoji


this = sys.modules[__name__]
this.running = False

sched = AsyncIOScheduler()

def main():

    print("Starting up...")
    client = discord.Client()

    @client.event
    async def on_ready():
        if this.running:
            return

        this.running = True

        game = discord.Game(name=settings.NOW_PLAYING)
        if settings.NOW_PLAYING:
            await client.change_presence(activity=game)
        n_ev = 0
        for ev in BaseEvent.__subclasses__():
            event = ev()
            sched.add_job(event.run, 'interval', (client,), 
                          minutes=event.interval_minutes)
            n_ev += 1
        sched.start()
        print("Done")

    async def common_handle_message(message):
        text = message.content
        if text.startswith(settings.COMMAND_PREFIX) and text != settings.COMMAND_PREFIX:
            cmd_split = text[len(settings.COMMAND_PREFIX):].split()
            try:
                await message_handler.handle_command(cmd_split[0].lower(), 
                                      cmd_split[1:], message, client)
            except:
                print("Error while handling message", flush=True)
                raise

    @client.event
    async def on_message(message):
        if str(message.author.id) in settings.BLACKLIST:
            await message.channel.send(settings.QUOTES[random.randrange(0,3)]+"\n"+message.author.mention)
            await common_handle_message(message)
        else:
            await common_handle_message(message)
            if message.content.startswith(get_emoji(":trophy:")+f"** Nickname: **"):
                await message.delete(delay=30)
            # if message.content.startswith("'stalk") or message.content.startswith("'live") or message.content.startswith("'commands") or message.content.startswith("'random"):
            #     await message.delete()
            if message.content.startswith(get_emoji(":game_die:")+"** Gamemode: **"):
                await message.delete(delay=30)
            if message.content.startswith("Insufficient parameters!") or message.content.startswith("Command List:") or message.content.startswith(get_emoji(":game_die:")+f" **You rolled**") or message.content.startswith("Player is not in game at the moment."):
                await message.delete(delay=10)
    
    @client.event
    async def on_typing(channel, user, when):
        if user.id in settings.BLACKLIST:
            await channel.send("O nie... Jobczyk coś pisze..." + user.mention)

    @client.event
    async def on_message_edit(before, after):
        await common_handle_message(after)

    client.run(settings.BOT_TOKEN)

if __name__ == "__main__":
    main()
