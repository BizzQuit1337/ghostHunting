from gtts import gTTS
import os, mmap, random, config

def buildSentance(wordList):
    with open(f"wordsDatabase/{wordList}", "r", encoding="utf-8") as file:
        mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        lines = mmapped_file.read().decode("utf-8").splitlines()
        mmapped_file.close()
    sentance = ' '.join([lines[random.randint(0, len(lines) - 1)][:-1] for _ in range(random.randint(1, 10))])
    return sentance

def generateAudio(sentance, fileName):
    tts = gTTS(text=sentance, lang="en")
    tts.save(f"audio/{fileName}")
    os.system(f"start audio/{fileName}")

counter = 0

while counter > config.limit:
    generateAudio(buildSentance(config.wordList), config.fileName)
    counter += 1
