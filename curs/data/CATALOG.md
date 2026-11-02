# Catalogul datelor

Date pe care le puteți aduce prin API pentru proiect, grupate după ce măsoară. Toate seturile Eurostat de mai jos răspund în format JSON-stat, deci merg cu funcțiile din `src/date_api.py` (`cere_eurostat`, `cere_perechi`); cele de la Banca Mondială merg cu `cere_bm`. Filtrele din tabel au fost verificate prin API (noiembrie 2026). Codurile pentru alte valori ale unui filtru (alt an, altă grupă de vârstă) se găsesc în [Eurostat Data Browser](https://ec.europa.eu/eurostat/databrowser/), căutând codul setului.

## De ce aceste date

Literatura despre Social Connectedness Index arată că legăturile dintre două locuri depind de distanță, de granițe, de limbă și istorie comună, de oamenii care s-au mutat dintr-un loc în altul, de schimburile dintre ele și de cât de asemănătoare sunt cele două locuri (vârstă, educație, venit). În plus, SCI vine din Facebook, deci contează și cât folosesc oamenii rețelele sociale.

- Bailey, Cao, Kuchler, Stroebel și Wong (2018), *Social Connectedness: Measurement, Determinants, and Effects*, Journal of Economic Perspectives.
- Bailey, Johnston, Kuchler, Russel, State și Stroebel (2020), *The Determinants of Social Connectedness in Europe*, SocInfo.
- Bailey, Gupta, Hillenbrand, Kuchler, Richmond și Stroebel (2021), *International Trade and Social Connectedness*, Journal of International Economics.

## 1. Perechi de țări

Un rând = o pereche de țări, ca în SCI pe țări. Atenție la sens: „din A în B” nu este același lucru cu „din B în A”.

| Ce măsoară | Set | Filtre | Exemplu: RO și IT |
|---|---|---|---|
| Migranți (stoc), după cetățenie | `migr_pop1ctz` | `sex=T, age=TOTAL, unit=NR` (alte grupe de vârstă la `age`) | cetățeni români în Italia |
| Imigranți pe an (flux), după cetățenie | `migr_imm1ctz` | `sex=T, age=TOTAL, agedef=COMPLET, unit=NR` | români sosiți în Italia: 46.439 (2015), 23.148 (2024) |
| Pasageri aerieni între țări | `avia_paocc` | `unit=PAS, tra_meas=PAS_CRD, schedule=TOTAL, freq=A`; `geo` = țara care raportează, `partner` = cealaltă | RO-IT: 4.717.400 pasageri (2024) |
| Turiști: nopți de cazare, după țara turistului | `tour_occ_ninraw` | `unit=NR, nace_r2=I551-I553`; `geo` = țara gazdă, `c_resid` = țara turistului | nopțile românilor în Italia: 4.075.029 (2024) |
| Comerț: exporturi și importuri | `DS-045409` (Comext, altă adresă, vezi mai jos) | `freq=A, product=TOTAL, flow=2` (export; `1` = import), `indicators=VALUE_IN_EUROS`; `reporter`, `partner` | exporturile României în Italia: 8,85 miliarde euro (2024) |

**Comerțul** vine din baza Comext, cu altă adresă decât restul Eurostat, dar în același format:
```python
from src.date_api import cere_eurostat, COMEXT

parametri = {"freq": "A", "reporter": "RO", "product": "TOTAL", "flow": "2",
             "indicators": "VALUE_IN_EUROS", "time": 2024}
comert = cere_eurostat("DS-045409", parametri, pe="partner", adresa=COMEXT)   # din src.date_api
```

## 2. Regiuni NUTS2

Un rând = o regiune. Se lipesc de SCI pe regiuni (`nuts2_2024.csv`), pe codul regiunii. Pentru o pereche de regiuni se poate construi o variabilă de asemănare, de exemplu diferența de vârstă medie dintre ele.

| Ce măsoară | Set | Filtre |
|---|---|---|
| Populația | `demo_r_pjangrp3` | `sex=T, age=TOTAL, unit=NR` (din cursul 2) |
| Densitatea | `demo_r_d3dens` | `unit=PER_KM2` (din cursul 2) |
| PIB pe locuitor | `nama_10r_3gdp` | `unit=PPS_EU27_2020_HAB` (din cursul 2) |
| Vârsta medie | `demo_r_pjanind2` | `indic_de=MEDAGEPOP, unit=YR` |
| Studii superioare, 25-64 ani (%) | `edat_lfse_04` | `isced11=ED5-8, age=Y25-64, sex=T, unit=PC` |
| Rata șomajului (%) | `lfst_r_lfu3rt` | `isced11=TOTAL, age=Y15-74, sex=T, unit=PC` |
| Folosesc rețelele sociale (% din persoane) | `isoc_r_iuse_i` | `indic_is=I_IUSNET, unit=PC_IND` |

Toate se cer pe tot nivelul cu `geoLevel=nuts2`, ca în cursul 2.

## 3. Țări

Un rând = o țară. Se lipesc de perechile de țări de două ori, o dată pentru fiecare capăt.

| Ce măsoară | Sursă | Cod |
|---|---|---|
| Folosesc rețelele sociale (% din persoane) | Eurostat `isoc_ci_ac_i` | `indic_is=I_IUSNET, ind_type=IND_TOTAL, unit=PC_IND` |
| Populația | Banca Mondială | `SP.POP.TOTL` |
| PIB pe locuitor (USD curenți) | Banca Mondială | `NY.GDP.PCAP.CD` |
| Utilizatori de internet (%) | Banca Mondială | `IT.NET.USER.ZS` |
| Remitențe primite (USD curenți) | Banca Mondială | `BX.TRF.PWKR.CD.DT` |
| Comerț (% din PIB) | Banca Mondială | `NE.TRD.GNFS.ZS` |
| Migranți internaționali (% din populație) | Banca Mondială | `SM.POP.TOTL.ZS` |

`cere_bm` aduce câte un indicator pe cerere: o cerere cu mai mulți indicatori deodată este refuzată de API.

## 4. Ce nu vine prin API

- **Limba comună, granița comună, legăturile istorice dintre țări**: baza GeoDist a [CEPII](https://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=6), un fișier de descărcat. Se pune în `data/raw/` al proiectului.
- **SCI pe județe (NUTS3)**: peste 40 MB, de pe [HDX](https://data.humdata.org/dataset/social-connectedness-index); nu se urcă pe GitHub.

## Coduri de verificat la lipire

Eurostat scrie Grecia `EL` și Regatul Unit `UK`; SCI și Banca Mondială scriu `GR` și `GB`. Valorile lipsă înseamnă că sursa nu are date, nu zero.
