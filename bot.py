import discord
import re
from random import choice

def dice_roll(x: int):
    return choice(range(1, x + 1))


client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    dice_regex = r"^(\d*)d(\d+)$"
    dice_match = re.match(dice_regex, message.content)
    if dice_match:
        number_of_dice_to_roll = dice_match.group(1)
        dice_number = int(dice_match.group(2))
        if dice_number == 0:
            await message.channel.send('A wise guy huh.')
        else:
            if number_of_dice_to_roll:
                number_of_dice_to_roll = int(number_of_dice_to_roll)
                dice_rolls = str()
                for _ in range(number_of_dice_to_roll):
                    dice_rolls += f'{dice_roll(dice_number)}{":" if _ < number_of_dice_to_roll - 1 else ""}'
                await message.channel.send(dice_rolls)
            else:
                await message.channel.send(f'{dice_roll(dice_number)}')

with open('token') as f:
    token = f.readline().strip()
    client.run(token)
