from functionClass import *
from discord_bot import *

if __name__ == '__main__':
    with open('token.txt','r') as my_file:
        token = my_file.read()
    bot.run(token)
