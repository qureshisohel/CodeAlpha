from tkinter import *
import googletrans
import textblob
from tkinter import ttk,messagebox


root = Tk()
root.title('Sohel Qureshi')
#root.iconbitmap('googletrans.jpg')
root.geometry("950x300")

def translate_it():
    translated_text.delete(1.0,END)
    try:
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key
        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key    
                
        words = textblob.TextBlob(original_text.get(1.0,END))
        
        words = words.translate(from_lang=from_language_key,to=to_language_key)
        
        translated_text.insert(1.0,words)
            
    except Exception as e:
        messagebox.showerror("TRANSLATE",e)

def clear():
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)



#language_list = (1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

original_text = Text(root,height=10,width=40)
original_text.grid(row=0,column=0,pady=20,padx=10)

translate_button = Button(root,text="TRANSLATE!",font=("Helvetica",24),command=translate_it)
translate_button.grid(row=0,column=1,padx=10)

translated_text = Text(root,height=10,width=40)
translated_text.grid(row=0,column=2,pady=20,padx=10)

original_combo = ttk.Combobox(root,width=50,value=language_list)
original_combo.current(21)
original_combo.grid(row=1,column=0)


translated_combo = ttk.Combobox(root,width=50,value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1,column=2)


clear_button = Button(root,text="CLEAR",command=clear)
clear_button.grid(row=2,column=1)

root.mainloop()

