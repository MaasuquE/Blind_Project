import pyttsx3
engine = pyttsx3.init()

t = ["Car", "CNG", "Ikra", "Lampost"]
d = [20, 30, 50, 10]
s = ["right", "left", "right", "left"]
txt = []
for i in range(0, len(t), 1):
    if s[i] == 'left':
        side = 'right'
    else:
        side = 'left'
    res = 'There is a {} on the {}  {} meters in front, Please move to {}.'.format(t[i], s[i], d[i], side)
    print(res)
    txt.append(res)

my_text = '  '.join(map(str, txt))

rate = engine.getProperty('rate')
engine.setProperty('rate', 115)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
engine.say(my_text)
engine.runAndWait()
