from gtts import gTTS
import os

t = ["Car","CNG","bappi","Lamp post"]
d =[20,30,50,10]
txt=[]
for i in range(0,len(t),1):
    res = '  '+str(d[i])+ 'মিটার সামনে '+ t[i]
    txt.append(res)

my_text ='  '.join(map(str, txt))
language = 'bn'
output = gTTS(text=my_text, lang=language,slow=False)
output.save("output.mp3")
os.system("start output.mp3")
