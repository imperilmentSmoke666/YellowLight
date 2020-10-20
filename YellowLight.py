# imports
import requests

cash_app_url = 'https://cash.app/'

with open("usernames.txt", 'r') as fp:
    names = fp.readlines()

for name in names:
    check_user = cash_app_url + name.strip()
    r = requests.get(check_user)
    if r.status_code == 200:
        print("Username:", name, "is taken. link:", r.url)
        with open("taken.txt", 'a') as fp:
            fp.writelines(name)

    elif r.status_code == 404:
        print("Username:", name, "is free")
        with open("available.txt", 'a') as fp:
            fp.writelines(name)
    elif r.status_code == 429:
        print("Too many requests")
        quit()
    else:
        pass









