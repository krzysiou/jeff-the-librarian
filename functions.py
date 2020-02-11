async def silencer(message, username):

        if str(message.author) == username:
            await message.channel.send("Utkaj łeb Jobczyk!")