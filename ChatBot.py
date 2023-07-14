from tkinter import *
import tkinter as tk
import openai
from gtts import gTTS
from playsound import playsound
from deep_translator import GoogleTranslator
import os
openai.api_key = "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"
def playSound():
     translation = T.get("1.0","end-1c")
     language = voiceChoice.get()
     myObj = gTTS(text=translation,lang=language,slow=False)
     myObj.save("translated.mp3")
     playsound('translated.mp3')

def show():
    sourceLanguage = sourceChoice.get()
    targetLanguage = translatedChoice.get()
    message = translationField.get()
    translator = GoogleTranslator(source=sourceLanguage,target=targetLanguage)
    translation = translator.translate(message)
    T.config(state='normal')
    T.delete(1.0, tk.END)
    T.insert(tk.END,translation)
    T.config(state='disabled')
    #transLabel.config( text =  translation)

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# GUI interface
def display_response():
    input_text = chatBotField.get()
    response = generate_response(input_text)
    chatBotOutputField.config(state='normal')
    chatBotOutputField.delete(1.0, tk.END)
    chatBotOutputField.insert(tk.END, response)
    chatBotOutputField.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("OpenAI Chatbot")
root.geometry("1200x800")

voices =[ "en", "es","pt" ,"fr" , "zh-CN","zh-TW"]


options = [
 "afrikaans","albanian","amharic", "arabic" , "armenian", "assamese", "aymara","azerbaijani","bambara","basque","belarusian","bengali",
"bhojpuri","bosnian","bulgarian","catalan","cebuano","chichewa","chinese (simplified)","chinese (traditional)","corsican","croatian","czech",
"danish","dhivehi","dogri","dutch","english","esperanto","estonian","ewe","filipino","finnish","french","frisian","galician","georgian","german","greek","guarani",
"gujarati","haitian creole","hausa","hawaiian","hebrew","hindi","hmong","hungarian","icelandic","igbo","ilocano","indonesian","irish","italian",
"japanese","javanese","kannada","kazakh","khmer","kinyarwanda","konkani","korean","krio","kurdish (kurmanji)","kurdish (sorani)","kyrgyz",
"lao","latin","latvian","lingala","lithuanian","luganda","luxembourgish","macedonian","maithili","malagasy","malay","malayalam","maltese","maori",
"marathi","meiteilon (manipuri)","mizo","mongolian","myanmar","nepali","norwegian","odia (oriya)","oromo","pashto","persian","polish","portuguese",
"punjabi","quechua","romanian","russian","samoan","sanskrit","scots gaelic","sepedi","serbian","sesotho","shona","sindhi","sinhala","slovak",
"slovenian","somali","spanish","sundanese","swahili","swedish","tajik","tamil","tatar","telugu","thai","tigrinya","tsonga","turkish","turkmen","twi",
"ukrainian","urdu","uyghur","uzbek","vietnamese","welsh","xhosa","yiddish","yoruba","zulu"
]
  
sourceLabel = Label(root, text = "Source Language")
translatedLabel = Label(root, text = "Translated Language")
sourceLabel.grid(row = 1, column = 0, sticky = W, pady = 2)
translatedLabel.grid(row = 2, column = 0, sticky = W, pady = 2)

sourceChoice = StringVar()
sourceChoice.set( "English" )
SourceLangMenu = OptionMenu( root , sourceChoice , *options )
SourceLangMenu.grid(row = 1, column = 1, sticky = E)
 

translatedChoice = StringVar()
translatedChoice.set( "Spanish" )
translatedMenu = OptionMenu( root , translatedChoice , *options )
translatedMenu.grid(row = 2, column = 1, sticky = E)

translationField = tk.Entry(root, font=("Arial", 14))
messageLabel = Label( root , text = "Enter Message" )
messageLabel.grid(row = 3, column = 0, sticky = W, pady = 2)
translationField.grid(row = 3, column = 1, pady = 2, padx = 2, sticky = W)


T = Text(root, height = 5, width = 35,state='disabled')
translateButton = Button( root , text = "Translate" , command = show )
translateButton.grid(row = 3, column = 2, sticky = E)
#transLabel = Label( root , text = "Translated Message" )
T.grid(row = 4, column = 0, sticky = W, pady = 2)

voiceChoice = StringVar()
voiceChoice.set( "Voice" )
voicesMenu = OptionMenu( root , voiceChoice , *voices )
voicesMenu.grid(row = 4, column = 1, sticky = E)
playSoundButton = Button( root , text = "Play Sound" , command = playSound )
playSoundButton.grid(row = 4, column = 2, sticky = W, pady = 2)

chatBotField = tk.Entry(root, font=("Arial", 14))
chatInputLabel =  Label( root , text = "Enter Message" )
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=display_response)
submit_button.grid(row = 5, column = 2, sticky = W)
chatInputLabel.grid(row = 5, column = 0, sticky = W)
chatBotField.grid(row = 5, column = 1, sticky = W)

chatBotOutputField = tk.Text(root, font=("Arial", 12), state='disabled')
chatBotLabel =  Label( root , text = "Chat Bot A.I" )
chatBotLabel.grid(row = 12, column = 0)
chatBotOutputField.grid(row = 12, column = 3)

#root.configure(background='#476042')
root.mainloop()










