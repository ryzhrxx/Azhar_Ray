import random

message = input('Pengguna: ')

def getReply(message):
    print('Bot: ' + message)

Balasan = ["hai!saya tahun ini berumur 19 tahun",
         "hai!saya tahun ini berumur 27 tahun",
         "hai!saya tahun ini berumur 14 tahun",
         "hai!saya tahun ini berumur 55 tahun",
         "hai!saya tahun ini berumur 45 tahun",
         "hai!saya tahun ini berumur 32 tahun"]

def getReply(message):
    if 'Hallo' in message:
        reply = "Hello, Ini BOT."
    elif 'halo,umur kamu berapa ?' in message:
        reply = random.choice(Balasan)
    else:
        reply = "Kata tidak di kenali"
    print('Bot: ' + reply)
	
while ('quit' not in message):
    message = input('Pengguna: ')
    getReply(message)