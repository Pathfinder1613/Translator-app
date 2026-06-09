from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import ttk
import pyttsx3


window = tk.Tk()
window.title("Translator App")
window.geometry("700x500")

language_var = tk.StringVar()
language_var.set("Spanish") 

voice_var = tk.StringVar()
voice_var.set("Male")
volume_var = tk.DoubleVar()
volume_var.set(1.0)

languages = {
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Russian": "ru",
    "Italian": "it",
    "Portuguese": "pt",
    "Arabic": "ar",
    "Hindi": "hi"
}
quotes = (
    "Dread it. Run from it. Destiny arrives all the same.",
    "I know what it's like to lose.",
    "The hardest choices require the strongest wills.",
    "Perfectly balanced, as all things should be.",
    "I am inevitable.",
    "I finally rest and watch the sun rise.",
    "You're not the only one cursed with knowledge.",
    "All of that for a drop of blood.",
    "You should've gone for the head."
)

quote_var = tk.StringVar()
quote_var.set(quotes[0])

def speak_text(text):
    if text.strip():
        engine = pyttsx3.init()
        # Rate
        engine.setProperty("rate", rate_slider.get())
        # Volume
        engine.setProperty("volume", volume_var.get())
        # Voices
        voices = engine.getProperty("voices")

        if voice_var.get() == "Male":
            engine.setProperty("voice", voices[0].id)
        else:            
            engine.setProperty("voice", voices[1].id)  

        engine.say(text)
        engine.runAndWait()
        engine.stop()

def translate_text():
    english_text = english_inputText.get("1.0", "end-1c")
    target_lang = languages[language_var.get()]
    translator = GoogleTranslator(source="auto", target=target_lang)
    translated_text = translator.translate(english_text)
    translated_outputText.delete("1.0", "end")
    translated_outputText.insert("1.0", translated_text)

def load_quote(selected_quote):
    quote_var.set(selected_quote)
    english_inputText.delete("1.0", "end")
    english_inputText.insert("1.0", selected_quote)

main = ttk.Frame(window, padding=15)
main.grid(sticky="nsew")

for i in range(4):
    main.columnconfigure(i, weight=1, uniform="col")

ttk.Label(main, text="Language").grid(row=0, column=0, sticky="w")
ttk.Label(main, text="Voice").grid(row=0, column=1, sticky="w")
ttk.Label(main, text="Speed").grid(row=0, column=2, sticky="w")
ttk.Label(main, text="Volume").grid(row=0, column=3, sticky="w")

language_menu = ttk.OptionMenu(main, language_var, language_var.get(), *languages.keys())
language_menu.grid(row=1, column=0, sticky="ew", padx=5)

voice_menu = ttk.OptionMenu(main, voice_var, voice_var.get(), "Male", "Female")
voice_menu.grid(row=1, column=1, sticky="ew", padx=5)

rate_slider = ttk.Scale(main, from_=50, to=200, orient="horizontal")
rate_slider.set(125)
rate_slider.grid(row=1, column=2, sticky="ew", padx=5)

volume_slider = ttk.Scale(main, from_=0.0, to=1.0, orient="horizontal", variable=volume_var)
volume_slider.grid(row=1, column=3, sticky="ew", padx=5)

ttk.Label(main, text="Quote").grid(row=2, column=0, columnspan=4, sticky="w", pady=(15, 5))

quote_menu = ttk.OptionMenu(main, quote_var, quotes[0], *quotes, command=load_quote)
quote_menu.grid(row=3, column=0, columnspan=4, sticky="ew")

ttk.Label(main, text="English Text").grid(row=4, column=0, columnspan=4, sticky="w", pady=(15, 5))

english_inputText = tk.Text(main, height=5, wrap="word", relief="flat", bd=5)
english_inputText.grid(row=5, column=0, columnspan=4, sticky="nsew")
english_inputText.insert("1.0", quotes[0])

button_frame = ttk.Frame(main)
button_frame.grid(row=6, column=0, columnspan=4, pady=10, sticky="ew")

for i in range(3):
    button_frame.columnconfigure(i, weight=1)

ttk.Button(
    button_frame,
    text="🔊 Speak English",
    command=lambda: speak_text(english_inputText.get("1.0", "end-1c"))
).grid(row=0, column=0, sticky="ew", padx=5)

ttk.Button(
    button_frame,
    text="🌍 Translate",
    command=translate_text
).grid(row=0, column=1, sticky="ew", padx=5)

ttk.Button(
    button_frame,
    text="🔊 Speak Translation",
    command=lambda: speak_text(translated_outputText.get("1.0", "end-1c"))
).grid(row=0, column=2, sticky="ew", padx=5)

ttk.Label(main, text="Translated Text").grid(row=7, column=0, columnspan=4, sticky="w", pady=(10, 5))

translated_outputText = tk.Text(main, height=5, wrap="word", relief="flat", bd=5)
translated_outputText.grid(row=8, column=0, columnspan=4, sticky="nsew")

window.mainloop()