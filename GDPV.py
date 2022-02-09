# GDPV 1.0 by SA ST
from requests import get
input("Welcome to GDPV! Press enter to continue!\n")
gd_player = input("Input a username or user id\n")
player_info = get("https://gdbrowser.com/api/profile/"+gd_player)