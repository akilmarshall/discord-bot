import discord
import re
from random import choice
import requests
import pol_speech


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


def dice_roll(x: int):
    return choice(range(1, x + 1))


client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    # do not reply to the bot's own messages
    if message.author == client.user:
        return
    author_id = message.author.id
    dice_regex = r'^(\d*)d(\d+)([\+-]\d+)?$'
    if dice_match := re.match(dice_regex, message.content):
        number_of_dice_to_roll = dice_match.group(1)
        dice_number = int(dice_match.group(2))
        modifier = dice_match.group(3)
        # check that the dice number is valid
        if dice_number == 0 or dice_number == 1:
            await message.channel.send('A wise guy huh.')
            return

        rolls = str()
        total = 0

        if number_of_dice_to_roll:
            number_of_dice_to_roll = int(number_of_dice_to_roll)
            for _ in range(number_of_dice_to_roll):
                roll = dice_roll(dice_number)
                rolls += f'{roll}{"+" if _ < number_of_dice_to_roll - 1 else ""}'
                total += roll
        else:
            # only roll one dice
            roll = dice_roll(dice_number)
            total = roll
            rolls = f'{roll}'
        if modifier:
            # add the modifier
            modifier = int(modifier)
            if modifier > 0:
                await message.channel.send(f'[{rolls}]+{modifier}={total + modifier}')
            else:
                await message.channel.send(f'[{rolls}]-{-modifier}={total + modifier}')
        else:
            await message.channel.send(f'[{rolls}]={total}')

    if message.channel.name == 'dnd' and message.content.startswith('^'):
        # print(message.author.id)
        # await message.channel.send(message.content[1:])
        msg = message.content[1:]
        if msg[:5] == 'spell':
            head, tail = msg[:5], msg[6:]
            tail = tail.replace(' ', '-')
            a = api_request('spells', tail)
            await message.channel.send(format_spell_api(a))

    if message.content == 'wwps' or message.content == 'what would pol say?':
        await message.channel.send(pol_speech.pol_bot())


with open('token') as f:
    token = f.readline().strip()
    client.run(token)
