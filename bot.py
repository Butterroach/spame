import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import environ

load_dotenv()

TOKEN: str = environ["TOKEN"]
CHANNEL_PREFIX: str = environ["SPAM_CHANNEL_PREFIX"]
CHANGERS: list[str] = environ["CHANGERS"]
CASE_SENSITIVE_SPAM: bool = environ["CASE_SENSITIVE"] == "true"
UWU_PWEASE = ", please give me the 'manage messages' permission. I do not have the proper permissions to function properly."
spam: str = environ["DEFAULT_SPAM_MESSAGE"]
started_once: bool = False

intents = discord.Intents.default()
intents.message_content = intents.members = True
bot: commands.Bot = commands.Bot("6.28!", intents=intents)


async def clear_n_pin(message: discord.Message | commands.Context) -> bool:
    try:
        for msg in await message.channel.pins():
            await msg.unpin()
        await message.pin()
    except discord.Forbidden:
        await message.channel.send(f"{message.guild.owner.mention}{UWU_PWEASE}")
        return False
    return True


async def wrong_message_handle(message: discord.Message) -> bool:
    try:
        await message.delete()
    except discord.Forbidden:
        await message.channel.send(f"{message.guild.owner.mention}{UWU_PWEASE}")
    else:
        await message.channel.send(
            f"{message.author.mention}, you MUST send the current spam message __ONLY__. It is in my most recent pinned message!",
            delete_after=5,
        )


@bot.event
async def on_ready() -> None:
    print("haiiii :3")
    if not started_once:
        for channel in bot.get_all_channels():
            if channel.name.startswith(CHANNEL_PREFIX):
                bot_message: discord.Message = await channel.send(
                    f"The bot has restarted, and the spam message has been reset. The spam message is now set to:\n\n```\n{spam}\n```"
                )
                await clear_n_pin(bot_message)


@bot.event
async def on_message(message: discord.Message) -> None:
    await bot.process_commands(message)
    if not message.channel.name.startswith(
        CHANNEL_PREFIX
    ) or message.content.startswith(bot.command_prefix):
        return
    if message.type == discord.MessageType.pins_add and message.author == bot.user:
        print(".")
        await message.delete()
    if message.author.bot:
        return
    if CASE_SENSITIVE_SPAM:
        if message.content != spam:
            await wrong_message_handle(message)
        return
    if message.content.casefold() != spam.casefold():
        await wrong_message_handle(message)


@bot.command()
async def newspam(ctx: commands.Context, *, new_spam_message: str = None):
    global spam
    if str(ctx.author.id) not in CHANGERS:
        await ctx.reply("You're not a changer! You can NOT change the spam message!")
        return
    if new_spam_message is None:
        await ctx.reply("Provide something!")
        return
    spam = new_spam_message
    bot_message: discord.Message = await ctx.send(
        f"# A NEW SPAM MESSAGE HAS BEEN SET!\n\n```\n{spam}\n```"
    )
    await clear_n_pin(bot_message)


bot.run(TOKEN)
