from bs4 import BeautifulSoup
import requests


form_data={'Email': 'you@gmail.com', 'Passwd': 'your_password'}
post = "https://accounts.google.com/signin/challenge/sl/password"

with requests.Session() as s:
    soup = BeautifulSoup(s.get("https://mail.google.com").text)
    for inp in soup.select("#gaia_loginform input[name]"):
        if inp["name"] not in form_data:
            form_data[inp["name"]] = inp["value"]
    s.post(post, form_data)

    html = s.get("https://mail.google.com/mail/u/0/#inbox").content
    with open("1.html", 'a', encoding='utf-8') as file:
        file.write(html.decode('utf-8'))
    print(html)