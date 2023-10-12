import mmap, random, pyttsx3

def speak(sentance):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[random.randint(0,1)].id)
    engine.setProperty('volume',random.randint(10, 100)) 
    engine.setProperty('rate', random.randint(1,200))
    engine.say(sentance)
    print(f"sentance: {sentance}")
    engine.runAndWait()
    return sentance

def read(wordList):
    with open(f"wordsDatabase/{wordList}", "r", encoding="utf-8") as file:
        mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        lines = mmapped_file.read().decode("utf-8").splitlines()
        mmapped_file.close()
    return lines