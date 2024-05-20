import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%t,%C"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text.strip().split(",")
        if len(data) == 2:
            temperature, weather = data
            messagebox.showinfo("Weather", f"Weather: {weather}\nTemperature: {temperature}")
        else:
            messagebox.showerror("Error", "Failed to get weather information")
    else:
        messagebox.showerror("Error", "Failed to fetch weather data")

def get_city_facts(city):
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=true&explaintext=true&generator=search&gsrsearch={city}+landmarks&gsrlimit=2"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pages = data["query"]["pages"]
        facts = []
        for page_id in pages:
            title = pages[page_id]["title"]
            extract = pages[page_id]["extract"]
            facts.append((title, extract))
        return facts
    else:
        return None

def get_city_info():
    city = city_entry.get()
    if city:
        get_weather(city)
        facts = get_city_facts(city)
        if facts:
            for title, extract in facts:
                messagebox.showinfo("City Facts", f"{title}:\n{extract}")
        else:
            messagebox.showerror("Error", "Failed to get city facts")
    else:
        messagebox.showerror("Error", "Please enter a city")

app = tk.Tk()
app.title("Weather and City Facts App")

label = tk.Label(app, text="Enter city:")
label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_info_button = tk.Button(app, text="Get Weather and City Facts", command=get_city_info)
get_info_button.pack()

app.mainloop()