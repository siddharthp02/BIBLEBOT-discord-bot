# discord-bots
Discord bot in python that will respond in bible quotes whenever a specific user is tagged.

## SETUP:

Create your own bot profile on discord developer portal. Give it all permissions.

Copy the bot token and replace at the end of the script where specified.

Invite bot to server.

## SET USER TO RESPOND TO

Run the python script
```
py bot.py
```
in linux.
```
python bot.py
```
in windows. 

It should say bot is ready.


To setup, first tag a user(in the same channel bot is in) that you want to set the bot to respond to.

Check your terminal, copy the user key within the content. Format <'@!lotsofnumbers'>. 

Uncomment the if condition line and replace the necessary part with the user key.

Now run the script again and the bot will now respond with a random line from the list whenever a user is tagged.
