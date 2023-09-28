import mmap, random, pyttsx3

def buildSentance(wordList):
    with open(f"wordsDatabase/{wordList}", "r", encoding="utf-8") as file:
        mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        lines = mmapped_file.read().decode("utf-8").splitlines()
        mmapped_file.close()
    sentance = ' '.join([lines[random.randint(0, len(lines) - 1)][:-1] for _ in range(random.randint(1, 5))])
    return sentance

def generateAudio(sentance):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[random.randint(0,1)].id)
    engine.setProperty('volume',random.random()) 
    engine.setProperty('rate', random.randint(1,200))
    engine.say(sentance)
    engine.runAndWait()

generateAudio(buildSentance('1000WordList.txt'))
