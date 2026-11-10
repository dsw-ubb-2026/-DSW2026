# Fluxuri de lucru pentru știința datelor · 2026

Materialele de seminar pentru cursul **Fluxuri de lucru pentru știința datelor** (Sociologie, UBB). Lecțiile sunt pe [courses.vladalexe.com](https://courses.vladalexe.com/data-science-workflows/).

## Cum începi

1. Alege **Code → Download ZIP**, dezarhivează arhiva și redenumește folderul `DSW2026-main` în `dsw`.
2. Deschide `dsw` în VS Code și creează mediul virtual în terminal:

**Windows (PowerShell):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. În notebook alege **Select Kernel → Python Environments → .venv**.

## Structura

```text
dsw/
├── .venv/          mediul Python (îl creezi tu)
├── README.md
├── requirements.txt
├── curs/           notebook-urile de la curs, le completezi tu
└── proiect/        de la cursul 3: repo-ul echipei
```

- **`curs/`**: aici lucrezi la curs. Nu e repo Git și nu se urcă nicăieri.
- **`proiect/`**: de la cursul 3, repo-ul echipei pe GitHub. În `dsw/` rulezi o singură dată `git clone <adresa repo-ului echipei> proiect`. Doar aici se fac `pull`, `commit` și `push`.

## La fiecare curs

Descarci doar caietul zilei: îl deschizi aici, pe GitHub, apeși **Download raw file** și îl salvezi în `dsw/curs/`, lângă celelalte. Restul îl aduce caietul singur:
- C3 descarcă `src/date_api.py` în `curs/src/`, cu prima lui celulă;
- datele vin direct de la sursă (Eurostat, Banca Mondială, GISCO) sau de la adresa lor de aici, de pe GitHub;
- seturile de date pentru proiect sunt descrise în [`curs/data/CATALOG.md`](curs/data/CATALOG.md), care se citește aici, pe GitHub;
- C5 creează baza de date SQLite a cursului, `curs/data/dsw.db`, din tabelele din C3 și C4.

ZIP-ul se descarcă o singură dată, la primul curs. După curs, caietul complet înlocuiește aici varianta de seminar; dacă îl vrei, îl descarci la fel, după ce îți redenumești caietul tău (de exemplu `02_..._meu.ipynb`).

## Conținut

| Fișier | Curs |
|---|---|
| `curs/01_introducere_si_datele_proiectului.ipynb` | C1. Jupyter, fișiere, JSON, primul contact cu SCI |
| `curs/02_colectarea_datelor_prin_api.ipynb` | C2. Banca Mondială, Eurostat, migrația |
| `curs/03_surse_diverse_si_preprocesare.ipynb` | C3. Nomenclatorul NUTS, indicatorii într-un tabel, SCI pe regiuni, migrația curățată |
| `curs/04_curatarea_si_integrarea_datelor.ipynb` | C4. Cele cinci verificări ale curățării; integrarea cu `pivot` și `merge` |
| `curs/05_agregare_si_baze_de_date.ipynb` | C5. Baza de date SQLite, SQL, integrarea și agregarea |
| `curs/06_analiza_exploratorie.ipynb` | C6. Ipotezele H1-H4, harta, rețeaua și comunitățile |
| `curs/src/date_api.py` | funcțiile pentru date (Banca Mondială, Eurostat), de la C3 |
| `curs/data/CATALOG.md` | seturile de date pentru proiect, cu filtrele lor |

## Baza de date

De la cursul 5, tabelele cursului stau într-o bază de date SQLite: un singur fișier, `curs/data/dsw.db`, creat de caietul 05. Nu cere cont, parolă sau server.

## Date

`curs/data/country.csv` și `curs/data/nuts2_2024.csv` provin din [Social Connectedness Index (HDX)](https://data.humdata.org/dataset/social-connectedness-index), la nivel de țară și de regiune NUTS2. Descrierea setului: [Johnston, Kuchler, Kulkarni și Stroebel (2026)](https://doi.org/10.1016/j.dib.2026.112905). Fișierele din `curs/exemple_curs1/` sunt fictive. Datele aduse prin API (cursul 2) ajung în `curs/data/raw/`, neschimbate. Tabelele curate (de la cursul 3) ajung în `curs/data/processed/`, câte un fișier pe tabel. Nomenclatorul regiunilor vine de la [GISCO](https://gisco-services.ec.europa.eu/distribution/v2/nuts/nuts-2024-files.html).
