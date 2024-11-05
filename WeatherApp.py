import tkinter as tk
from tkinter import font
import requests
h=500
w=600
def test_button(entry):
    print("The entry is: ",entry)
root=tk.Tk()
# 302d5c702784f4438e458adb2172fd12
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}&appid={API key} -->forecast
# https://api.openweathermap.org/data/2.5/weather?q={city name},{country code}&appid={API key} -->current
def format_weather(weather):
    try:
        name=weather['name']
        desc=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str="City: %s\nConditions: %s\nTemperature (°C): %s" % (name,desc,temp)
    except:
        final_str="There is a problem retrieving that information!"
    return final_str
def get_weather(city):
    weather_key='302d5c702784f4438e458adb2172fd12'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units': 'metric'}
    response=requests.get(url,params=params)
    weather = response.json()
    label['text']=format_weather(weather)
canvas=tk.Canvas(root, height=h,width=w)
canvas.pack()

background_image=tk.PhotoImage(file='landscape.png')
background_label=tk.Label(root, image=background_image)
background_label.place(relheight=1,relwidth=1)

frame1=tk.Frame(root, bg='#80c1ff', bd=5)
frame1.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.8, anchor='n')

entry=tk.Entry(frame1, bg='white',font=('@Meiryo UI',18))
entry.place(relwidth=0.6,relheight=1)
# relx=0.01,rely=0.10,
button=tk.Button(frame1, text="Get Weather", bg="white", font=('Elephant',15), command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relwidth=0.3, relheight=1)
# relx=0.65,rely=0.10,
frame2=tk.Frame(root,bg='#80c1ff',bd=10)
frame2.place(relx=0.5,rely=0.25,relheight=0.5,relwidth=0.80, anchor='n')

label=tk.Label(frame2, font=('Harrington',20), anchor='nw', justify='left',bd=4)
label.place(relwidth=1,relheight=1)

# button = tk.Button(frame, text="Test Button",bg="Yellow")
# button.place(relx=0,rely=0,relwidth=0.25,relheight=0.25)

# label=tk.Label(frame, text="This is a label", bg="Blue")
# label.place(relx=0.3,rely=0,relwidth=0.45,relheight=0.25)

# entry=tk.Entry(frame, bg="green")
# entry.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.25)
# print(tk.font.families())
root.mainloop()