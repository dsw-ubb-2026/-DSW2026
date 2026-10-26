# Fluxuri de lucru pentru știința datelor · 2026

Materialele de seminar pentru cursul **Fluxuri de lucru pentru știința datelor** (Sociologie, UBB). Lecțiile sunt pe [courses.vladalexe.com](https://courses.vladalexe.com/data-science-workflows/).

## Cum îl folosești

1. Creează un folder al tău pentru curs, de exemplu `dsw`.
2. Alege **Code → Download ZIP**, dezarhivează arhiva în `dsw/` și redenumește folderul `DSW2026-main` în `curs`.
3. Deschide `dsw/` în VS Code și creează mediul virtual (pașii sunt în primul notebook):

```text
dsw/
├── .venv/      mediul Python
├── curs/       acest repo
└── proiect/    de la cursul 2: repo-ul echipei
```

**Windows (PowerShell):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r curs/requirements.txt
```

**macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r curs/requirements.txt
```

La fiecare curs nou descarci doar notebook-ul zilei în `curs/`. Nu descărca din nou arhiva întreagă peste `curs/`: îți poate suprascrie notebook-urile completate.

## Conținut

| Fișier | Curs |
|---|---|
| `01_introducere_si_datele_proiectului.ipynb` | C1. Jupyter, fișiere, JSON, primul contact cu SCI |
| `02_colectarea_datelor_prin_api.ipynb` | C2. Banca Mondială, Eurostat, migrația |

## Date

`data/country.csv` provine din [Social Connectedness Index (HDX)](https://data.humdata.org/dataset/social-connectedness-index), la nivel de țară. Descrierea setului: [Johnston, Kuchler, Kulkarni și Stroebel (2026)](https://doi.org/10.1016/j.dib.2026.112905). Fișierele din `exemple_curs1/` sunt fictive. Datele de la cursul 2 se colectează prin API și ajung în `data/c2/`.
