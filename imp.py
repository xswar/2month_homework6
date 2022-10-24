import os
import colorama
import tcolors
import envparse


envparse.env.read_envfile('options.env')

user_name = os.getenv('USER_NAME')
user_password = os.getenv('PASSWORD')

print(tcolors.Color.BLUE + colorama.Back.BLACK + user_name)
print(tcolors.Color.BLUE + colorama.Back.BLACK + user_password)



