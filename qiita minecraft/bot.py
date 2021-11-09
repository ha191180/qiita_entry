#!/usr/bin/env python3
import sys

sys.path.append('/home/ubuntu/.local/lib/python3.8/site-packages')

import discord
from discord.ext import tasks
import psutil
import os
CHANNEL_ID = 0000 # your channel id
CLIENT_TOKEN = "YourDiscordClientToken"

svprocess = None
client = discord.Client()

@tasks.loop(seconds=10)
async def check_minecraft_status():
  is_run = False
  for proc in psutil.process_iter():
    try:
      if proc.name() == 'java':
        is_run = True
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
      pass
  if is_run:
    game = discord.Game("Minecraft")
    await client.change_presence(status=discord.Status.online, activity=game)
  else:
    await client.change_presence(status=discord.Status.idle, activity=None)

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')
  check_minecraft_status.start()

@client.event
async def on_message(message):
  ch = client.get_channel(CHANNEL_ID)
  if message.content == "/start":
    global svprocess 
    is_run = False
    print('Check existing server')
    for proc in psutil.process_iter():
      try:
        if proc.name() == 'java':
          is_run = True
      except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        await ch.send('Error1')
    if is_run:
      await ch.send('Server has been running already. Login the server and type /stop in Minecraft game.\n You can also use /kill command in discord to kill the process (I recommend /stop).')
    else:
      os.system('/home/ubuntu/run.sh')
#      svprocess = subprocess.Popen('/home/ubuntu/run.sh', shell=True,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#      logmsg = ''
#      while True:
#        line = svprocess.stdout.readline().decode().strip()
#        if line:
#          logmsg = line  
#        if not line and svprocess.poll() is not None:
#          print("[SERVER] Line ended. Is the server stopped?")
#          break  
      await ch.send("Wait a minute.")

  if message.content == '/isRun':
    is_run = False
    for proc in psutil.process_iter():
      try:
        if proc.name() == 'java':
          is_run = True
      except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        ch.send('No process. Server is Down.')
        pass
    if is_run:
      await ch.send('Server is Running.')
    else:
      await ch.send('Server is Down.')
  
  if message.content == '/kill':
    for proc in psutil.process_iter():
      try:
        if proc.name() == 'java':
          command = 'kill -KILL ' + str(proc.pid)
          os.system(command)
      except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    await ch.send('Kill confirmed.')

  if message.content == '/psaux':
    msg = ''
    for proc in psutil.process_iter():
      try:
        msg = msg + 'NAME: ' + proc.name() + ' \tPID: ' + str(proc.pid) + '\n'
      except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    print(msg)
    try:
      await ch.send(msg)
    except (Exception):
      await ch.send("Process list is too large. Extracted last 2000 char.\n" + msg[-1900:])

  if message.content == '/status':
    await ch.send(file=discord.File('/home/ubuntu/tmppictures/stat.png'))

    

    


client.run(CLIENT_TOKEN)

