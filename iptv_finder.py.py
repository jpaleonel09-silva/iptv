import requests
import re

url = "https://multicanaishd.cloud/"

html = requests.get(url).text

links = re.findall(r'https?://[^\s]+\.m3u8', html)

arquivo = open("lista.m3u","w")

arquivo.write("#EXTM3U\n")

for i, link in enumerate(links):
    arquivo.write(f"#EXTINF:-1,Canal {i+1}\n")
    arquivo.write(link + "\n")

arquivo.close()

print("Lista IPTV criada!")