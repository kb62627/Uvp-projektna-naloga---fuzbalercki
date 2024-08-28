from bs4 import BeautifulSoup
import pandas as pd
import sys
import re

def pridobi_podatke_igralcev(html_datoteka):
    try:
        # Poskusi prebrati datoteko z utf-8-sig kodiranjem
        with open(html_datoteka, 'r', encoding='utf-8-sig') as datoteka:
            vsebina = datoteka.read()
    except UnicodeDecodeError:
        try:
            # Če utf-8-sig ne uspe, poskusi z utf-8
            with open(html_datoteka, 'r', encoding='utf-8') as datoteka:
                vsebina = datoteka.read()
        except UnicodeDecodeError:
            # Če oba ne uspeta, poskusi z latin-1
            with open(html_datoteka, 'r', encoding='latin-1') as datoteka:
                vsebina = datoteka.read()
    
    # Ustvari BeautifulSoup objekt
    soup = BeautifulSoup(vsebina, 'html.parser')
    
    # Najdi vse vrstice tabele
    vrstice = soup.find_all('tr')
    
    if not vrstice:
        print("Ni najdenih <tr> elementov. Iskanje <table> elementov...")
        tabele = soup.find_all('table')
        if tabele:
            print(f"Najdenih {len(tabele)} <table> elementov.")
            for i, tabela in enumerate(tabele):
                print(f"Tabela {i+1} ima {len(tabela.find_all('tr'))} vrstic")
        else:
            print("Ni najdenih <table> elementov.")
            print("HTML struktura:")
            print(soup.prettify()[:1000])  # Izpiši prvih 1000 znakov polepšanega HTML-ja
        return None

    podatki_igralcev = []
    for vrstica in vrstice:
        stolpcki = vrstica.find_all(['th', 'td'])
        if len(stolpcki) > 1:  # Ensure it's a data row
            posamezni_igralec_podatki = {
                'Igralec': stolpcki[1].text.strip() if len(stolpcki) > 1 else '',
                'Nacionalnost': nacionalnost_enkrat(stolpcki[2].text.strip()) if len(stolpcki) > 2 else '',
                'Pozicija': stolpcki[3].text.strip() if len(stolpcki) > 3 else '',
                'Klub': stolpcki[4].text.strip() if len(stolpcki) > 4 else '',
                'Leto rojstva': stolpcki[6].text.strip() if len(stolpcki) > 6 else '',
                'Starost': stolpcki[5].text.strip() if len(stolpcki) > 5 else '',
                'Igre': stolpcki[7].text.strip() if len(stolpcki) > 7 else '',
                'Čas igranja': stolpcki[9].text.strip()  if len(stolpcki) > 9 else '',
                'Goli': stolpcki[11].text.strip() if len(stolpcki) > 11 else '',
                'Asistence': stolpcki[12].text.strip() if len(stolpcki) > 12 else '',
                'Pričakovani goli': stolpcki[19].text.strip() if len(stolpcki) > 19 else '',
                'Rumeni kartoni': stolpcki[17].text.strip() if len(stolpcki) > 17 else '',
                'Rdeči kartoni': stolpcki[18].text.strip() if len(stolpcki) > 18 else '',
            }
            
            podatki_igralcev.append(posamezni_igralec_podatki)
    
    # Create a DataFrame
    df = pd.DataFrame(podatki_igralcev)
    
    return df

def nacionalnost_enkrat(nacionalnost):
    # Odstrani vse male črke
    return re.sub(r'[a-z]', '', nacionalnost).strip()

# Pot do vaše HTML datoteke
pot_html_datoteke = 'lista_fuzbalerckou/usi.html'

try:
    # Pridobi podatke
    statistika_igralcev = pridobi_podatke_igralcev(pot_html_datoteke)

    if statistika_igralcev is not None:
        # Prikaži prvih nekaj vrstic DataFrame-a
        print(statistika_igralcev.head())

        # Po želji shrani v CSV datoteko
        statistika_igralcev.to_csv('statistika_igralcev.csv', index=False, encoding='utf-8-sig')
        print("Podatki uspešno pridobljeni in shranjeni v 'statistika_igralcev.csv'")
    else:
        print("Ni bilo pridobljenih podatkov. Prosimo, preverite HTML strukturo.")
except Exception as e:
    print(f"Prišlo je do napake: {e}")
    print("Verzija Python:", sys.version)
    print("Verzija BeautifulSoup:", BeautifulSoup.__version__)
    print("Verzija Pandas:", pd.__version__)
    


