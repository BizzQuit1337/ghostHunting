import random, time
import sharedFunctions as sf

def standardMode(lines):
    return ' '.join([lines[random.randint(0, len(lines) - 1)] for _ in range(random.randint(1, 5))])

def reverseMode(lines):
    line = ''
    for i in range(0, random.randint(1, 5)):
        line += ''.join(reversed(lines[random.randint(0, len(lines) - 1)]))
        line += ' '
    return line

def binary():
    if random.randint(1, 10)%2 == 0:
        return 'Yes'
    else:
        return 'No'
    


#sf.speak(binary)

#sf.speak(reverseMode(lines))

#sf.speak(standardMode(lines))