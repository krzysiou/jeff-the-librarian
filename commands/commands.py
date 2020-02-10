#from commands.base_command import BaseCommand
import commands.base_command


# This is a convenient command that automatically generates a helpful
# message showing all available commands
class Commands(commands.base_command.BaseCommand):

    def __init__(self):
        description = "Displays this help message"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        from message_handler import COMMAND_HANDLERS
        msg = message.author.mention + "\n"

        # Displays all descriptions, sorted alphabetically by command name
        for cmd in sorted(COMMAND_HANDLERS.items()):
            msg += "\n" + cmd[1].description

        await message.channel.send(msg)
