import requests
from bs4 import BeautifulSoup
import random
import tkinter as tk
from tkinter import ttk

def fetch_quotes():
    url="http://quotes.toscrape.com/"
    response=requests.get(url)
    if response.status_code!=200:
        print(f'Failed to fetch the page\n{response.status_code}')
        return[]
    else:
        soup=BeautifulSoup(response.text, "html.parser")
        quotes_data=soup.find_all("div",class_="quote")
        quotes_list=[]

        for quote in quotes_data:
            text=quote.find("span", class_="text").text
            author=quote.find("small",class_="author").text
            quotes_list.append(f'{text}\n\nBy: {author}')
    return quotes_list

quotes=fetch_quotes()

def display_quote():
        if quotes:
            quote = random.choice(quotes)
            quote_label.config(text=quote)



app=tk.Tk()
app.title("Quote of the Day")
app.geometry("600x400")
app.configure(bg="#01796F")

frame=tk.Frame(app,background="#01796F")
frame.pack(expand=True)

quote_label=ttk.Label(frame,
    text="",
    wraplength=500,
    justify="center",
    font=("Palatino",18,"bold italic"),
    foreground="#F5F5F5",
    background="#01796F"
)

quote_label.pack(pady=20)

if quotes:
    display_quote()
else:
    quote_label.config(text="Failed to fetch quotes. Please check your internet connection.")

refresh_quote_button=ttk.Button(frame,text="Get Another Quote",command=display_quote)
refresh_quote_button.pack(pady=20, ipadx=10,ipady=5)
refresh_quote_button.configure(style="Custom.TButton")

style = ttk.Style()
style.configure("Custom.TButton", font=("Helvetica", 14), background="#F5F5F5", foreground="#01796F")

app.mainloop()