import discord
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix='V', description="Vatsu destroys Tatsu.")


# https://stackoverflow.com/questions/35337299/python-datetime-to-float-with-millisecond-precision
def float_to_datetime(fl):
    return datetime.datetime.fromtimestamp(fl)


def datetime_to_float(d):
    return d.timestamp()


# Events
@bot.event
async def on_ready():
    print("VedgeBot load success.")


@bot.listen()
async def on_message(message):
    lowercase_message = message.content.lower()
    print(message.content)
    if message.author == bot.user:
        return
    if bot.user.mentioned_in(message):
        await message.reply(
            "I amv Vatsu, destroyer of Tatsu." +
            "\nIf I have problems pleave ping <@!741792119823401030> for help." +
            "\nI am not active very ovten. If I am not responding please be patient."
        )
    elif str(message.author) == "Tatsu#8792":
        content = str(message.content)
        if (content.contains("has leveled up")):
            if (content.startswith("<@!741792119823401030>")):
                await message.reply("Shut up Tatsu")
        # if (content.startswith("**Viewing rank card")):
        #     await message.reply(message.content)
        # message.author ==
    # if bot.user.mentioned_in(message):
    #     if "who" in lowercase_message and "are" in lowercase_message and "you" in lowercase_message:
    #         await message.reply(
    #             "I amv VedgeVog. Stealver of kneecapv. Typev `Vhelp` for commandv." +
    #             "\nIf I hav problemv pleave ping <@!741792119823401030> for hvlp."+
    #             "\nI am not activ very ovten. If I amv not revponding pleave be patience."
    #         )
    #     else:
    #         await message.reply(
    #             "I amv bot. Pleave type `Vhelp` for commandv." +
    #             "\nIf I hav problemv pleave ping <@!741792119823401030> for hvlp" +
    #             "\nI am not activ very ovten. If I amv not revponding pleave be patience."
    #         )


# https://stackoverflow.com/questions/66956261/check-if-message-reply-is-a-reply-type-message-discord-py
async def check_if_reply(ctx):
    if ctx.message.reference is not None:
        # https://stackoverflow.com/questions/61851174/how-to-get-message-by-id-discord-py
        replyMessage = await ctx.fetch_message(ctx.message.reference.message_id)
        return replyMessage
    return None


def escape_markdown(text):
    indices = [i for i, ltr in enumerate(text) if ltr == "`"]
    for num in reversed(indices):
        text = text[:num - 1] + "\\" + text[num:]
    return text


bot.run('ODk1MDEzMzg4MTc3MDAyNTI2.YVyYLA.jB_jYW-EwEydxxXGmRBSOPy6CNY')