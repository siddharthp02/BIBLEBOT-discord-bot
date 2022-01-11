import discord 
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
	print('Bot is ready')

@client.event
async def on_message(message):
    replies = ['OH LORD AND SAVIOUR, THEE HATH BEEN SUMMONED','Praise Him by lifting your hands. Lift up your hands in the sanctuary, and bless the Lord.The lord has been summoned','But the hour comes, and now is, when the true worshippers shall worship the Father in spirit and in truth: for the Father seeks such to worship him. God is a Spirit: and they that worship him must worship him in spirit and in truth. FEAR NOT FOR GOD HAS BEEN SUMMONED','H But the LORD said to Samuel, Look not on his countenance, or on the height of his stature; because I have refused him: for the LORD sees not as man sees; for man looks on the outward appearance, but the LORD looks on the heart. FEAR NOT FOR THE LORD HAS BEEN CALLED UPON','That all the people of the earth may know that the LORD is God, and that there is none else. Yet alas, the lord is yet again called upon by mere mortals to fulfill their foolish desires.','And said, Naked came I out of my mother’s womb, and naked shall I return thither: the LORD gave, and the LORD has taken away; blessed be the name of the LORD','The LORD is my rock, and my fortress, and my deliverer; my God, my strength, in whom I will trust; my buckler, and the horn of my salvation, and my high tower.I beg thee my lord to spare your wisdom to us fools','O clap your hands, all you people; shout to God with the voice of triumph. For the LORD most high is terrible; he is a great King over all the earth. He shall come to answer thine needs','I will greatly praise the LORD with my mouth; yes, I will praise him among the multitude.OH LORD BLESS US WITH THINE GRACE','The fear of the LORD is the beginning of wisdom: a good understanding have all they that do his commandments: his praise endures for ever','DEAR LORD WE ARE NOTHING BUT SLUTS IN FRONT OF THINE GLORY, PLEASE ANSWER US WHORES']
    if '<@!716689653041725470>'  in message.content.split():
    	await message.channel.send(random.choice(replies))
    elif '<@716689653041725470>'  in message.content.split():
    	await message.channel.send(random.choice(replies))
    elif '<@561572502254387239>'  in message.content.split():
    	await message.channel.send('on this day a failure weeb child hath been calleth')
    elif '<@!561572502254387239>'  in message.content.split():
    	await message.channel.send('on this day a failure weeb child hath been calleth')
    elif '<@631474714761625611>'  in message.content.split():
    	await message.channel.send('LONELY ADI PIG HATH BEEN SUMMONED TO SPOUT MEANINGLESS SCAMS')
    elif '<@!631474714761625611>'  in message.content.split():
    	await message.channel.send('LONELY ADI PIG HATH BEEN SUMMONED TO SPOUT MEANINGLESS SCAMS')
    elif '<@!639057792891748362>'  in message.content.split():
    	await message.channel.send("He descended through the aureole in the sky minutes before the doomsday clock struck 12 only to be welcomed by a monstrous beast. He slayed the creature and sent it to hell and saved all of humanity from the fangs of the fiend")
    elif '<@639057792891748362>'  in message.content.split():
    	await message.channel.send("He descended through the aureole in the sky minutes before the doomsday clock struck 12 only to be welcomed by a monstrous beast. He slayed the creature and sent it to hell and saved all of humanity from the fangs of the fiend")	
    await client.process_commands(message)
	

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
	responses = [ 'It is certain ','It is decidedly so', 'Without a doubt', 'Yes definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes ','Signs point to yes',"Don't count on it",'My reply is no','My sources say no','Outlook not so good','Very doubtful','Reply hazy try again','Ask again later ','Better not tell you now','Cannot predict now','Concentrate and ask again']
	await ctx.send(f'{random.choice(responses)}')




client.run('NzkzNTM3NTc4OTMzNDIwMDgz.X-ttdg.pOUmOBlYN7nHfzVB8-oaPJTo5aY')