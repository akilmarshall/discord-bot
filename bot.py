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
    # do not reply to the bot's own messages
    if message.author == client.user:
        return

    dice_regex = r'^(\d*)d(\d+)([\+-]\d+)?$'
    dice_match = re.match(dice_regex, message.content)
    if dice_match:
        number_of_dice_to_roll = dice_match.group(1)
        dice_number = int(dice_match.group(2))
        modifier = dice_match.group(3)
        # check that the dice number is valid
        if dice_number == 0:
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
            await message.channel.send(f'[{rolls}]+{modifier}={total + modifier}')
        else:
            await message.channel.send(f'[{rolls}]={total}')

with open('token') as f:
    token = f.readline().strip()
    client.run(token)
