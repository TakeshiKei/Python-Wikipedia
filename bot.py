import discord
import asyncio
import pyttsx3
import speech_recognition as sr

# initialize text-to-speech engine
engine = pyttsx3.init()

# Discord client instance
client = discord.Client()

# function to convert text to speech


def speak(text):
    engine.say(text)
    engine.runAndWait()

# function to listen for speech input


async def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: {}".format(text))
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None

# function to handle voice channel events


@client.event
async def on_voice_state_update(member, before, after):
    if member == client.user:
        return

    if before.channel is None and after.channel is not None:
        # user has joined a voice channel
        await member.guild.system_channel.send("Hello! I'm here to help you.")

        while True:
            text = await listen()
            if text is not None:
                response = "I heard you say " + text
                await member.guild.system_channel.send(response)
                speak(response)

# start the Discord client
client.run('<MTA4NDgyMzQ5MDk5NTE3OTYwMw.G5nXBq.IPiYwb6x4GASt62X2HN84qqnYCtadloxCOGGPc>')
