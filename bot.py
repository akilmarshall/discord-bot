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

    dice_regex = r'^(\d*)d(\d+)(\+\d)?$'
    dice_match = re.match(dice_regex, message.content)
    if dice_match:
        number_of_dice_to_roll = dice_match.group(1)
        dice_number = int(dice_match.group(2))
        modifier = dice_match.group(3)
        if dice_number == 0:
            await message.channel.send('A wise guy huh.')
        else:
            if number_of_dice_to_roll:
                number_of_dice_to_roll = int(number_of_dice_to_roll)
                dice_rolls = str()
                dice_sum = 0
                for _ in range(number_of_dice_to_roll):
                    roll = dice_roll(dice_number)
                    dice_rolls += f'{roll}{"+" if _ < number_of_dice_to_roll - 1 else ""}'
                    dice_sum += roll 
                if modifier:
                    modifier = int(modifier)
                    await message.channel.send(f'[{dice_rolls}]+{modifier}={dice_sum + modifier}')
                else:
                    await message.channel.send(f'{dice_rolls}={dice_sum}')
            else:
                roll = dice_roll(dice_number)
                if modifier:
                    modifier = int(modifier)
                    await message.channel.send(f'{roll}+{modifier}={roll + modifier}')
                else:
                    await message.channel.send(f'{roll}')

with open('token') as f:
    token = f.readline().strip()
    client.run(token)
