import crontab 
from crontab import CronTab
from gtts import gTTS
import random
from playsound import playsound

text="Is your mind wondering?"

array=["Are you on auto-pilot mode?","Have you been immersed in productive task?If yes, How long? Great keep going","Whats the most consequence thing you could right now do?","How full is your attentional space?"]
data=text+" "
add=array[random.randint(0,3)]
data+=add
data+=" Come on boy, lets get back to work."
print(data)
data_obj=gTTS(data,lang='en',slow=False)
data_obj.save("ReadAlert.mp3")
playsound("ReadAlert.mp3")