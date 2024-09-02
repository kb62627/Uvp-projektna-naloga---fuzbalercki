# Analiza igralcev Premier lige leta 2022/23

## Uvod
Za projekt pri predmetu Uvod v programiranje sem izbrala analizo igralcev Premier lige. 

## Struktura projekta

### 1. Webscrape
Datoteka `webscrape.py`:
* Iz spletne strani izvleče podatke o igralcih
* Vse podatke shrani v eno CSV datoteko znotraj mape `statistika_igralcev.csv`

### 2. Analiza
Analiza podatkov se osredotoča na sledeče podatke o igralcih:
* Osebne podatke
* Položaj na igrišču
* Klub, s katerim je povezan
* Skupno število nastopov
* Skupen čas igranja
* Skupno število doseženih golov
* Skupno število asistenc
* Pričakovano število golov

S temi podatki sem nato izračunala in prikazala nekaj statističnih podatkov celotne lige.

## 3. Uporabljene knjižnice
* csv
* re
* os
* requests
* sys
* BeautifulSoup
* pandas
* matplotlib.pyplot
* seaborn