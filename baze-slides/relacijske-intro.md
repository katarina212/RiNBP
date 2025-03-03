---
theme: gaia
paginate: true
marp: true
---

# Relacijske Baze Podataka: Osnove
## Uvodno Predavanje (45 minuta)

---
## Uvod (5 minuta)

- Otvaranje: "Zamislite knjižnicu gdje su knjige razbacane nasumično vs. one s jasnim sustavom"
- Zašto su baze podataka važne u našem svijetu vođenom podacima
- Budućnost i uloga baza podataka u dobu umjetne inteligencije i LLM-ova

---
## Osnovni Koncepti (12 minuta)

- Tablice: Gradivni blokovi
  - Primjer: Jednostavna baza podataka narudžbi kupaca
- Ključevi i Odnosi
  - Primarni ključevi: Jedinstveni identifikatori
  - Strani ključevi: Stvaranje veza
  - Vrste odnosa (jedan-prema-mnogima, itd.)
- Važnost dobro dizajnirane sheme

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

Vizualni prikaz odnosa Jedan-prema-Mnogo:

![Odnosi Jedan-prema-Mnogo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Relationship_one_to_many.svg/800px-Relationship_one_to_many.svg.png)

- **Jedan-prema-Mnogo (1:N):** Jedan kupac može imati više narudžbi.
- **Jedan-prema-Jedan (1:1):** (Rjeđe) Jedan kupac može imati jedan profil detalja.
- **Mnogo-prema-Mnogo (M:N):** (Složenije) Narudžba može sadržavati više proizvoda, a proizvod se može pojaviti u više narudžbi (koristi se pomoćna tablica).

---
## SQL Osnove (12 minuta)

- Osnovna struktura: `SELECT`, `FROM`, `WHERE`
- Jednostavni primjeri upita
- Interaktivna demonstracija: Izgradnja osnovnog upita
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
## Interaktivna Demonstracija (uživo!)

*Pitanje publici: Što biste željeli pitati bazu podataka o kupcima?*

*Primjer odgovora: Želim vidjeti email adrese svih kupaca.*

*SQL upit uživo:*
```sql
SELECT Email
FROM Kupci;
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

![INNER JOIN](https://www.sql-join.com/wp-content/uploads/2016/01/sql-inner-join.jpg)

---
## Principi Dizajna Baza Podataka (10 minuta)

- Osnove normalizacije (fokus na zašto je važno)
- Uobičajene zamke: "Katastrofa dupliciranih podataka"
- Indeksi: Kako ubrzavaju vašu bazu podataka
- Kratko spominjanje transakcija

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
## Transakcije (Kratko Spominjanje)

- **Što su?** Logičke jedinice rada koje se izvršavaju kao **cjelina**.
- **ACID svojstva:**
    - **Atomicity (Atomčnost):** Sve ili ništa.
    - **Consistency (Konzistentnost):** Održava integritet baze podataka.
    - **Isolation (Izolacija):** Transakcije se izvršavaju neovisno jedna o drugoj.
    - **Durability (Trajnost):** Promjene su trajne nakon potvrde transakcije.
- **Važne za osiguranje pouzdanosti** i **integriteta** podataka.

---
## Kontekst Stvarnog Svijeta (6 minuta)

- Kako relacijske baze podataka pokreću svakodnevne aplikacije
- Završne misli i poticaj za pitanja i odgovore

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

---
## Pitanja i Odgovori

- Imate li pitanja?
- Želite li da ponovimo neki koncept?
- Razgovarajmo!

---
## Hvala na Pažnji!

Kontakt informacije:
[vaš email]
[vaša web stranica/društvena mreža (opcionalno)]