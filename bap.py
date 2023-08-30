from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime



today=str(datetime.date.today())
print(today)

t=today.split("-")
s=["breakfast", "lunch", "dinner"]

for i in s:
    print(f"this is {i}")
    html = urlopen(f"https://jeju-s.jje.hs.kr/jeju-s/food/{t[0]}/{t[1]}/{t[2]}/{i}")
    soup = BeautifulSoup(html, "html.parser")

    bap = soup.select("div:nth-child(2) > ul > li:nth-child(2) > dl > dd")
    print("="*50)

    for a in bap:
        bp=a.text.strip().split(" ")

    for b in bp:
        print(b)

    print("="*50)

