"""
Temporary replacement of bot.py to develop the new api
"""
import discord

from modules import DiceRoller, LanguageModel

# Register chat commands as module objects
chat_commands = [DiceRoller(), LanguageModel()]


"""
def api_request(category: str, name: str) -> dict:
    # for example, category = 'spells', name = 'acid-arrow'
    # returns a dictionary
    api = 'https://www.dnd5eapi.co/api/'
    url = f'{api}{category}/{name}'
    r = requests.get(url)
    return r.json()


def format_spell_api(api_obj: dict) -> str:
    out = str()
    out += f'**Description:** {" ".join(api_obj["desc"])}\n'
    out += f'{" ".join(api_obj["higher_level"])}\n'
    out += f'**Range:** {api_obj["range"]}\n'
    out += f'**Components:** {api_obj["components"]}\n'
    out += f'**Material:** {api_obj["material"]}\n'
    out += f'**Ritual:** {api_obj["ritual"]}\n'
    out += f'**Duration:** {api_obj["duration"]}\n'
    out += f'**Concentration:** {api_obj["concentration"]}\n'
    out += f'**Casting Time:** {api_obj["casting_time"]}\n'
    out += f'**Level:** {api_obj["level"]}'
    return out
"""

client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    # do not reply to the bot's own messages
    if message.author == client.user:
        return
    for x in chat_commands:
        await x(message)
    """
    if message.channel.name == 'dnd' and message.content.startswith('^'):
        # print(message.author.id)
        # await message.channel.send(message.content[1:])
        msg = message.content[1:]
        if msg[:5] == 'spell':
            head, tail = msg[:5], msg[6:]
            tail = tail.replace(' ', '-')
            a = api_request('spells', tail)
            await message.channel.send(format_spell_api(a))
    elif message.content in ['+1 for the boyz', 'ya boi']:
        util.boy_win_counter.increase()
        await message.channel.send(f'Fall Boy Wins: {util.boy_win_counter.get_wins()}')
    elif message.content == 'my b':
        util.boy_win_counter.decrease()
        await message.channel.send(f'Fall Boy Wins: {util.boy_win_counter.get_wins()}')
    elif message.content == 'win count':
        await message.channel.send(f'{util.boy_win_counter.get_wins()}')
    """


with open('token') as f:
    token = f.readline().strip()
    client.run(token)
