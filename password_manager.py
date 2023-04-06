import json
from tkinter import *
import random

window = Tk()
window.geometry('450x200')


def generate():
    password_e.delete(0, END)
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
    password = []
    for i in range(3):
        password.append(random.choice(alphabets))
    for i in range(2):
        password.append(random.choice(numbers))
    for i in range(2):
        password.append(random.choice(symbols))

    random.shuffle(password)

    password_e.insert(0, f'{"".join(password)}')


def add():
    email = email_e.get()
    website = website_e.get()
    password = password_e.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }
    if len(website) != 0 or len(password) != 0 or len(email) != 0:
        with open('data.json', 'r') as file:
            data = json.load(file)
            data.update(new_data)
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

    website_e.delete(0, END)
    password_e.delete(0, END)
def get():
    web = website_e.get()
    with open('data.json', 'r') as file:
        data = json.load(file)
        if web in data:
            email_e.delete(0, END)
            password_e.insert(0, data[web]['password'])
            email_e.insert(0, data[web]['email'])

emaill = Label(text='Email : ')
emaill.grid(column=0, row=2)
email_e = Entry(width=50)
email_e.grid(column=1, row=2)
email_e.insert(0, 'shree@gmail.com')

passwordl = Button(text="Password", command=generate)
passwordl.grid(column=0, row=1)
password_e = Entry()
password_e.grid(column=1, row=1)

websitel = Label(text="Website : ")
websitel.grid(column=0, row=0)
website_e = Entry(width=50)
website_e.grid(column=1, row=0)

submit = Button(text="submit", command=add)
submit.grid(column=1, row=3)

search = Button(text="Search", command=get)
search.grid(column=2, row=0)
window.mainloop()