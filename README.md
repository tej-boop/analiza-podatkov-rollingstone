## Avtor
Teja Čižman

## Najbolj popularne pesmi v tednu 15. - 21. 10. 2021
Projektna naloga za predmet Programiranje 1: analiza podatkov s spletne strani rollingstone.com.
Analizirala bom 100 najbolj popularnih pesmi tretjega tedna v oktobru glede na lestvico
na spletni strani [Rolling Stone](https://www.rollingstone.com/charts/songs/2021-10-18/).

Za vsako pesem bom zajela sledeče podatke:
- naslov in izvajalca pesmi
- koliko tednov je že na lestvici
- število predvajanj ("streams")
- mesto, v kateri je pesem najbolj popularna (le ameriška mesta, saj je Rolling Stone osredotočen na ameriško občinstvo)
- glasbena založba, s katero izvajalec sodeluje

Delovne hipoteze:
- Ali bo imela pesem večje število predvajanj, če je več tednov na lestvici?
- Ali bodo na lestvici prevladovale pesmi, katerih izvajalci imajo pogodbe z glasbenimi založbami?

## CSV datoteka v repozitoriju
S pomočjo kode, napisane v prebery-pesmi.py, sem ustvarila CSV datoteko filmi.csv, ki je zajela sledeče podatke za vsako pesem:
- rank oziroma mesto na lestvici
- pevec
- koliko tednov je pesem že na lestvici najboljših 100 pesmi
- glasbena založba, s katero izvajalec sodeluje
- mesto, v katerem je pesem najbolj popularna
- število predvajanj v milijonih