---
marp: true
theme: gaia
title: Odabrana poglavlja iz relacijskih baza podataka
description: Nikola Balić
paginate: true
---

# Odabrana poglavlja iz relacijskih baza podataka
## 2025

Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---
## Uvod

- "Hrpa vs. Knjižnica"
- Budućnost i uloga baza podataka u dobu umjetne inteligencije i LLM-ova

<!--
1. Za početak, zamislite dvije knjižnice. U prvoj, knjige su posvuda - na podu, na stolovima, nema nikakvog reda. Pronaći određenu knjigu je gotovo nemoguće, zar ne? A sada zamislite drugu knjižnicu, gdje je svaka knjiga uredno katalogizirana, smještena na policama prema sustavu, s karticama koje vam pomažu da je brzo pronađete. Baze podataka su upravo to - sustav za organizaciju i učinkovito pronalaženje informacija, poput dobro organizirane knjižnice, u usporedbi s kaosom prve knjižnice.
2. Baze podataka postaju još važnije jer one pohranjuju, upravljaju i osiguravaju kvalitetu tih podataka. Budućnost baza podataka nije samo pohrana, već i inteligentno upravljanje podacima kako bi se omogućio razvoj i primjena UI i LLM-ova.
-->

---
## Osnovni Koncepti

- Tablice: Gradivni blokovi
  - Primjer: Jednostavna baza podataka narudžbi kupaca
- Ključevi i Odnosi
  - Primarni ključevi: Jedinstveni identifikatori
  - Strani ključevi: Stvaranje veza
  - Vrste odnosa (jedan-prema-mnogima, itd.)

---
## Tablice: Gradivni Blokovi

- Baza podataka organizirana je u **tablice**.
- Svaka tablica pohranjuje podatke o **jednom tipu entiteta** (npr., kupci, proizvodi, narudžbe).
- Tablica se sastoji od **redaka (zapisa)** i **stupaca (atributa)**.

```
Tablica: Kupci

| ID_Kupca | Ime      | Prezime    | Email               |
|----------|----------|------------|---------------------|
| 1        | Ana      | Horvat     | ana.horvat@email.hr |
| 2        | Marko    | Kovačević  | marko.kovacevic@mail.com |
| 3        | Ivana    | Jurić      | ivana.juric@mail.net   |
```

---
## Ključevi i Odnosi

- **Primarni Ključ (PK):** Jedinstveno identificira svaki redak u tablici.
    - Osigurava **jedinstvenost** podataka.
    - Primjer: `ID_Kupca` u tablici `Kupci`.
- **Strani Ključ (FK):** Stupac u jednoj tablici koji upućuje na primarni ključ u drugoj tablici.
    - Stvara **odnose** između tablica.
    - Primjer: `ID_Kupca` u tablici `Narudžbe` (upućuje na `Kupci`).

---
## Vrste Odnosa

- **Jedan-prema-Mnogo (1:N):** Jedan kupac može imati više narudžbi.
- **Jedan-prema-Jedan (1:1):** (Rjeđe) Jedan kupac može imati jedan profil.
- **Mnogo-prema-Mnogo (M:N):** (Složenije) Narudžba može sadržavati više proizvoda, a proizvod se može pojaviti u više narudžbi (koristi se pomoćna tablica).

---
## SQL Osnove

- Osnovna struktura: `SELECT`, `FROM`, `WHERE`
- Jednostavni primjeri upita
- Demonstracija izgradnje baze podataka
- Spajanje tablica: Snaga odnosa
  - Brzi primjer spajanja kupaca i narudžbi

---
## SQL Struktura: SELECT, FROM, WHERE

- **SELECT:**  Navodi stupce koje želimo prikazati.
- **FROM:**   Navodi tablicu iz koje dohvaćamo podatke.
- **WHERE:**  Filtrira retke na temelju uvjeta.

```sql
-- Primjer: Dohvati imena kupaca iz tablice Kupci
SELECT Ime
FROM Kupci;
```

---
## Jednostavni SQL Upiti

```sql
-- Dohvati sve stupce za kupca s ID-om 1
SELECT *
FROM Kupci
WHERE ID_Kupca = 1;
```

```sql
-- Dohvati imena i prezimena kupaca iz Zagreba (ako postoji stupac Grad)
SELECT Ime, Prezime
FROM Kupci
WHERE Grad = 'Zagreb';
```

---
## Demo: Izgradnje Baze Podataka

Koristimo `database.build` za brzu izgradnju primjera baze podataka:

*Primjer upita za `database.build`:*
```
Create a database for an online store with two tables:
'Kupci' (Customers) and 'Narudžbe' (Orders).
Use appropriate data types, and include primary and foreign key constraints.
```

---
## Spajanje Tablica (JOIN)

- Omogućuje kombiniranje podataka iz **dvije ili više tablica** na temelju **zajedničkog stupca** (obično strani i primarni ključ).
- Vrste JOIN-ova: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN` (i drugi, ovisno o sustavu).

---
## Primjer JOIN Upita

```sql
-- Dohvati imena kupaca i ID-ove njihovih narudžbi
SELECT Kupci.Ime, Narudžbe.ID_Narudžbe
FROM Kupci
INNER JOIN Narudžbe ON Kupci.ID_Kupca = Narudžbe.ID_Kupca;
```

Vizualizacija INNER JOIN:

![INNER JOIN](assets/innerjoin.png)

---
## Normalizacija Baza Podataka

- **Cilj:** Smanjiti **redundanciju (ponavljanje)** i **ovisnosti** podataka.
- **Zašto je važna?**
    - **Smanjuje prostor** za pohranu (nema dupliciranih podataka).
    - **Poboljšava integritet** podataka (manje šanse za nekonzistentnost).
    - **Olakšava održavanje** i **modifikaciju** baze podataka.

---
## "Katastrofa Dupliciranih Podataka"

*Zamislite tablicu Narudžbe bez normalizacije:*

```
Tablica: Narudžbe (nenormalizirana)

| ID_Narudžbe | Kupac_Ime | Kupac_Prezime | Proizvod_Naziv | Proizvod_Cijena | ... |
|-------------|-----------|---------------|----------------|-----------------|-----|
| 1           | Ana       | Horvat        | Laptop         | 1200            | ... |
| 1           | Ana       | Horvat        | Miš            | 25              | ... |
| 2           | Marko     | Kovačević     | Monitor        | 300             | ... |
| 2           | Marko     | Kovačević     | Tipkovnica     | 75              | ... |
```

- **Problem:** Informacije o kupcu se ponavljaju za svaku narudžbu.
- **Rješenje:** Normalizacija - odvojiti podatke o kupcima i narudžbama u zasebne tablice i povezati ih odnosom.

---
## Indeksi

- **Što su?** Posebne strukture podataka koje ubrzavaju dohvat podataka.
- **Kako rade?** Slično indeksu u knjizi - brzo pronalaze retke na temelju vrijednosti stupaca.
- **Zašto su važni?**
    - **Drastično ubrzavaju** upite, pogotovo na velikim tablicama.
    - **Ključni za performanse** baza podataka.
- **Nedostatak:** Zauzimaju dodatni prostor i usporavaju operacije upisa/ažuriranja.

---
## Primjeri Primjene

Relacijske baze podataka su **posvuda**:

- **Online trgovine:** Upravljanje proizvodima, narudžbama, kupcima.
- **Bankarstvo:** Transakcije, računi, korisnici.
- **Društvene mreže:** Profili, objave, veze.
- **Sustavi za upravljanje sadržajem (CMS):** Članci, korisnici, kategorije.
- **...i mnoge druge aplikacije!**

---
## Zaključak

- Relacijske baze podataka su **temelj modernog upravljanja podacima**.
- Razumijevanje osnovnih koncepata je **ključno** za rad s podacima.
- SQL je **standardni jezik** za interakciju s relacijskim bazama podataka.
- Dobar dizajn baze podataka je **važan za performanse i integritet**.
