# OBSnake
__________________________________________________________________________________________
OBS python script that sends notifications to the discord server and the telegram channel whenever start translation button is pressed.
__________________________________________________________________________________________

Requirements:

1. OBS
2. Python 6.X (obs won't load scripts with any other version of python)
3. PIP package installer
4. Requests python library (python -m pip install requests)
5. Discord channel webhook
6. Telegram Bot API token
__________________________________________________________________________________________

<b><h3>How to use OBSnake:</h3></b>

1. Open Scripts menu in OBS: Instruments -> Scripts
2. Set the path to the python folder in python parameters tab
3. Go back to Scripts tab and add OBSnake file(obsnake.py) using '+' button
4. set script parameters:

 <b>Stream link</b>: link to the streaming platform's channel, e.g. https://wasd.tv/gafker
 
 <b>Description</b>: message text which will be delivered
 
 <b>Discord webhook URL.</b>: Where to get webhook https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks, leave empty if you dont want discord notifications
  
 <b>Telegram bot token</b> : Make sure that your bot is added in your channel. How to create a bot https://core.telegram.org/bots, leave empty if you dont want telegram notifications
  
 <b>Telegram channel name</b>: Channel name without @ symbol. e.g. if your channale name is @gafker use gafker in this field
 
 5. Hit start translation button

__________________________________________________________________________________________
 
