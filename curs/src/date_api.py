"""Funcțiile pentru date din cursul 2, într-un singur fișier.

Într-un notebook din folderul de deasupra lui src/ (curs/):
    from src.date_api import cere_bm, cere_eurostat, cere_perechi

Dacă schimbi ceva aici, repornește kernelul (Restart), ca notebook-ul să ia
varianta nouă. Catalogul seturilor de date: data/CATALOG.md. În proiect, fișierul stă în proiect/src/.
"""
import requests
import pandas as pd

EUROSTAT = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
COMEXT = "https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/"


def cere_tot(url, parametri):
    """Toate valorile unei cereri la Banca Mondială, oricâte pagini ar avea."""
    meta = requests.get(url, params=parametri).json()[0]          # câte pagini sunt
    toate = []
    for pagina in range(1, meta["pages"] + 1):
        valori = requests.get(url, params={**parametri, "page": pagina}).json()[1]
        toate = toate + valori                                    # lipim valorile paginii
    return toate


def cere_bm(indicator, tari, ani="2022:2024"):
    """Un indicator al Băncii Mondiale, pentru o listă de țări: tara, an, valoare."""
    url = "https://api.worldbank.org/v2/country/" + ";".join(tari) + "/indicator/" + indicator
    valori = cere_tot(url, {"format": "json", "date": ani, "per_page": 1000})
    tabel = pd.json_normalize(valori)[["country.id", "date", "value"]]
    tabel.columns = ["tara", "an", "valoare"]
    return tabel


def cere_eurostat(dataset, parametri, pe="geo", adresa=EUROSTAT):
    """Un set Eurostat, ca tabel: un rând pentru fiecare valoare a dimensiunii `pe`.

    Pentru comerț (baza Comext) se dă adresa=COMEXT.
    """
    date = requests.get(adresa + dataset, params=parametri).json()
    if "value" not in date:                                       # răspuns fără date: eroare
        raise ValueError(f"{dataset}: răspunsul nu are date")

    numere = date["dimension"][pe]["category"]["index"]           # ce număr are fiecare cod
    valori = date["value"]                                        # ce valoare stă la fiecare număr
    if len(valori) > len(numere):
        raise ValueError("Mai fixează un filtru, de exemplu anul")

    tabel = []
    for cod, numar in numere.items():
        tabel.append({pe: cod, "valoare": valori.get(str(numar))})   # lipsă: None
    return pd.DataFrame(tabel)


def cere_perechi(dataset, filtre, tari, pe, fix="geo", adresa=EUROSTAT):
    """Perechi de țări: câte o cerere pentru fiecare țară din `tari`, ca la migrație în C2.

    `fix` este dimensiunea fixată pe rând (o țară pe cerere), `pe` cea care variază.
    """
    tabele = []
    for tara in tari:
        try:
            tabel = cere_eurostat(dataset, {**filtre, fix: tara}, pe=pe, adresa=adresa)
        except (ValueError, KeyError):
            print("fără date:", tara)                             # țara nu raportează
            continue
        tabel[fix] = tara                                         # notăm țara fixată
        tabele.append(tabel)
    return pd.concat(tabele)
