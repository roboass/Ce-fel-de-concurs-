import requests
import random
from bs4 import BeautifulSoup

limita_cuvinte = 15
animale = ["rechin", "urs", "cal", "marmota", "catel", "bou", "leu"]

while True:
    cuvant = input("Zi un cuvant: ")

    print("- Ce fel de %s?"%cuvant)

    r = requests.get("https://www.rimeaza.ro/cuvinte-care-rimeaza-cu-%s.html"%cuvant)
    soup = BeautifulSoup(r.content, 'html5lib')

    arr = []
    nr_cuvinte = 0

    for crti in soup.findAll("div", attrs = {"class" : "container_rime"}):
        for crtj in crti.findAll("a"):
            nr_cuvinte += 1
            if nr_cuvinte <= limita_cuvinte:
                arr.append(crtj.text)

    rima = random.choice(arr)
    for cuv in arr:
        if cuv in animale:
            rima = cuv
            break


    print("- De belit pula la %s"%rima)
    print("=====================================")
