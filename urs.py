import requests
import random
from bs4 import BeautifulSoup

cuvant = input("Zi un cuvant: ")

print("- Ce fel de %s?"%cuvant)

r = requests.get("https://www.rimeaza.ro/cuvinte-care-rimeaza-cu-%s.html"%cuvant)
soup = BeautifulSoup(r.content, 'html5lib')

arr = []

for crti in soup.findAll("div", attrs = {"class" : "container_rime"}):
    for crtj in crti.findAll("a"):
        arr.append(crtj.text)

rima = random.choice(arr)

print("- De belit pula la %s"%rima)
