import re
import json
import csv

with open("100-najbolj-popularnih-pesmi.html", encoding="utf-8") as dat:
    vsebina = dat.read().replace("&amp;", "&")

vzorec = re.compile(
    r'rank">(?P<rank>\d+)</div>'
    r'.*?title"><p>(?P<naslov>.*?)</p></div>'
    r'.*?caption">(?P<pevec>.*?)</div>'
    r'.*?<small>Weeks on Chart</small>\n<span>(?P<tednov_na_lestvici>\d+)</span>'
    r'.*?label-text">(?P<glasbena_zalozba>.*?)</span>'
    r'.*?<li>(?P<top_mesto>.*?)</li>'
    r'.*?Song Streams</small>\n.*?<span>(?P<stevilo_predvajanj>.*?)</span>', re.DOTALL)

pesmi = []

for pesem in vzorec.finditer(vsebina):
    pesmi.append(pesem.groupdict())

# print(pesmi)

with open("filmi.csv", "w", encoding="utf-8") as dat:
    writer = csv.DictWriter(dat, [
        "rank",
        "naslov",
        "pevec",
        "tednov_na_lestvici",
        "glasbena_zalozba",
        "top_mesto",
        "stevilo_predvajanj"
    ], extrasaction="ignore")
    writer.writeheader()
    writer.writerows(pesmi)

# for i, ujemanje in enumerate(vzorec.finditer(vsebina), 1):
#     print(i, ujemanje.groupdict())