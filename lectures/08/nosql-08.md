---
marp: true
theme: gaia
title: Odabrana poglavlja iz relacijskih baza podataka & Raspodijeljene i nerelacijske baze podataka - SAŽETAK
description: Nikola Balić - Ključni Koncepti
paginate: true
---

# SAŽETAK PREDAVANJA
## Odabrana poglavlja iz relacijskih baza podataka
## Raspodijeljene i nerelacijske baze podataka

### Akademska godina 2024/2025
Nikola Balić

---

<!-- Lecture 1: Odabrana poglavlja iz relacijskih baza podataka -->

# Tema 1: Uvod u Relacijske Baze Podataka

---

## Uvod: "Hrpa vs. Knjižnica"

- **Problem:** Podaci bez strukture = kaos.
- **Rješenje:** Baze = organizirana "knjižnica" za učinkovito pronalaženje informacija.
- **Cilj:** Brz i pouzdan pristup podacima.

---

## Uloga Baza Podataka u Doba AI/LLM

- **Temelj AI:** Baze su "gorivo" za AI/LLM (pohrana, upravljanje, kvaliteta).
- **Više od Pohrane:** Inteligentno upravljanje podacima za napredne AI sustave.
- **Kvaliteta Podataka:** Ključna za pouzdane AI modele.

---

## Zašto Relacijske Baze?

- **Strukturirani Podaci:** Idealne za jasno organizirane podatke.
- **Integritet:** PK, FK osiguravaju dosljednost i točnost.
- **SQL:** Standardni, moćan jezik za podatke.
- **Zrelost:** Provjerene, stabilne, široko korištene.

---

# Tema 2: Osnovni Koncepti Relacijskih Baza

---

## Tablice: Gradivni Blokovi

- **Organizacija:** Baza = skup **tablica**.
- **Entiteti:** Tablica = 1 tip entiteta (npr. Kupci, Proizvodi).
- **Struktura:** Redci (zapisi) & Stupci (atributi).

```
Tablica: Kupci
| ID_Kupca (PK) | Ime    | Prezime |
|---------------|--------|---------|
| 1             | Ana    | Ostojić |
```

---

## Ključevi: Identifikacija i Povezivanje

- **Primarni Ključ (PK):**
    - Jedinstveno identificira svaki redak.
    - Ne smije biti NULL.
- **Strani Ključ (FK):**
    - Stupac koji upućuje na PK u drugoj tablici.
    - Stvara veze (odnose) među tablicama.

---

## Odnosi (Relationships)

- **Svrha:** Povezuju tablice, smanjuju redundanciju.
- **Vrste:**
    - **1:1 (Jedan-prema-Jedan):** Rijetko (npr. `Korisnik`-`ProfilDetalji`).
    - **1:N (Jedan-prema-Mnogo):** Najčešći (npr. 1 `Kupac` - više `Narudžbi`).
    - **M:N (Mnogo-prema-Mnogo):** Preko **pomoćne (spojne) tablice** (npr. `Proizvodi` - `Narudžbe` -> `StavkeNarudzbe`).

---

# Tema 3: SQL Osnove

---

## SQL Struktura: `SELECT`, `FROM`, `WHERE`

- **`SELECT`:** Navodi stupce za prikaz.
    - `SELECT Ime, Prezime` ili `SELECT *`
- **`FROM`:** Navodi tablicu(e) izvora.
    - `FROM Kupci`
- **`WHERE`:** Filtrira retke po uvjetu.
    - `WHERE Grad = 'Split'`

---

## Primjeri Jednostavnih SQL Upita

```sql
-- Imena i prezimena svih kupaca
SELECT Ime, Prezime FROM Kupci;

-- Sve o proizvodu s ID-om 5
SELECT * FROM Proizvodi WHERE ID_Proizvoda = 5;

-- Nazivi proizvoda skupljih od 100
SELECT Naziv FROM Proizvodi WHERE Cijena > 100;
```

---

## Spajanje Tablica (`JOIN`)

- **Svrha:** Kombiniranje redaka iz 2+ tablica na temelju povezanog stupca (PK-FK).
- **`INNER JOIN`:** Vraća samo retke s podudaranjem u obje tablice.
    ```sql
    SELECT K.Ime, N.ID_Narudzbe
    FROM Kupci K JOIN Narudžbe N ON K.ID_Kupca = N.ID_Kupca;
    ```
- **Ostali:** `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN` (za zadržavanje redaka bez podudaranja).

---

# Tema 4: Normalizacija Baza Podataka

---

## Cilj Normalizacije

- **Smanjiti Redundanciju:** Eliminirati ponavljanje podataka.
    - Štedi prostor, olakšava ažuriranje.
- **Poboljšati Integritet:** Osigurati točne, konzistentne podatke.
    - Smanjuje anomalije (unos, ažuriranje, brisanje).
- **Olakšati Održavanje:** Jasnija, logičnija struktura.

---

## "Katastrofa Dupliciranih Podataka"

Bez normalizacije: Ime i adresa kupca ponavljaju se za svaku naručenu stavku.
- **Problemi:**
    - Teško ažuriranje (npr. promjena adrese).
    - Ako kupac nema narudžbi, gubimo podatke o njemu.
    - Veći utrošak prostora.
- **Normalizacija:** Razdvaja u tablice `Kupci`, `Proizvodi`, `Narudzbe`.

---

## Osnovne Normalne Forme (Ukratko)

- **1NF (Prva):** Svaka ćelija = 1 atomska vrijednost. Nema ponavljajućih grupa.
- **2NF (Druga):** U 1NF + svi ne-ključni atributi ovise o **cijelom** PK (važno za složene PK).
- **3NF (Treća):** U 2NF + nema tranzitivnih ovisnosti (ne-ključni atributi ne ovise o drugim ne-ključnim).

*Postoje i više: BCNF, 4NF, 5NF.*

---

# Tema 5: Indeksi

---

## Što su Indeksi?

- **Posebne Strukture:** Nad stupcima tablice za ubrzanje dohvata podataka.
- **Svrha:** Brži `SELECT` s `WHERE`, brži `JOIN`.
- **Analogija:** Kazalo u knjizi – brže pronalaziš stranicu (redak).

---

## Kako Indeksi Rade?

- Indeks = sortirana kopija vrijednosti stupca + pokazivači na retke.
- Baza pretražuje manji, sortirani indeks, pa direktno dohvaća retke.
- Obično koriste B-stablo strukturu.

---

## Zašto su Indeksi Važni i Trade-offs

- **Prednosti:**
    - **Drastično ubrzavaju `SELECT`** na velikim tablicama.
- **Nedostaci (Trade-offs):**
    - **Zauzimaju prostor.**
    - **Usporavaju `INSERT`, `UPDATE`, `DELETE`** (i indeksi se moraju ažurirati).
    - Pažljivo birati stupce za indeksiranje (česti u `WHERE`/`JOIN`).

---

# Tema 6: Primjeri Primjene i Zaključak (RBP)

---

## Primjeri Primjene Relacijskih Baza

- **Online Trgovine:** Kupci, proizvodi, narudžbe.
- **Bankarstvo:** Računi, transakcije.
- **CMS:** Članci, korisnici, komentari.
- **Računovodstvo:** Fakture, plaćanja.
- **HR Sustavi:** Zaposlenici, plaće.

---

## Ključne Prednosti RBP (Ponovimo)

- **Strukturiranost:** Jasna shema, tablice.
- **Integritet Podataka:** PK, FK, ograničenja.
- **SQL:** Moćan, standardiziran jezik.
- **Transakcije (ACID):** Pouzdanost operacija.
- **Zrelost i Pouzdanost:** Duga povijest.

---

## Zaključak (Relacijske Baze Podataka)

- **Temelj** modernog upravljanja strukturiranim podacima.
- Razumijevanje koncepata (tablice, ključevi, SQL, normalizacija) je **ključno**.
- Dobar dizajn = **performanse, integritet, održivost**.
- Ostaju **nezamjenjive** za mnoge primjene.

---

<!-- Lecture 2: Raspodijeljene i nerelacijske baze podataka - Uvodno predavanje -->

# Tema 7: Uvod u Raspodijeljene i Nerelacijske Baze Podataka (NoSQL)

---

## Zašto Istraživati Svijet Izvan RBP?

- **Eksplozija Podataka:** Volumen, brzina, raznolikost (V+V+V) izazov za RBP.
- **Ograničenja RBP:**
    - **Skalabilnost:** Teško horizontalno skaliranje.
    - **Fleksibilnost Sheme:** Kruta shema za brze promjene.
- **Potreba za Novim Rješenjima:** Big Data, Web 2.0, IoT, AI.

---

## NoSQL Revolucija

- **NoSQL = "Not Only SQL"** / "Non-Relational".
- **Karakteristike:**
    - **Nisu relacijske.**
    - **Shema-manje / Fleksibilna Shema.**
    - **Horizontalna Skalabilnost** (scale-out).
    - **Visoka Dostupnost** (replikacija, failover).
    - **Raznolikost Modela Podataka.**

---

## DIKW Piramida

- **Podatak (Data):** Sirove činjenice. (`38`)
- **Informacija (Information):** Obrađeni podaci s kontekstom. (`38°C`)
- **Znanje (Knowledge):** Primjena informacija, razumijevanje. (`Povišena temperatura = simptom`)
- **Mudrost (Wisdom):** Primjena znanja s prosuđivanjem. (`Ako 38°C -> ostati kući`)
- Baze: temelj za Informaciju, Znanje, Mudrost.

---

# Tema 8: Tipovi NoSQL Baza Podataka

---

## 1. Ključ-Vrijednost (Key-Value)

- **Model:** Parovi (jedinstveni ključ, vrijednost).
- **Vrijednost:** Bilo što (string, JSON, blob).
- **Operacije:** `GET(ključ)`, `PUT(ključ, vrijednost)`, `DELETE(ključ)`.
- **Karakteristike:** Izuzetno brze, visoko skalabilne.
- **Primjeri:** Redis, Memcached.
- **Upotreba:** Cache, korisničke sesije.

---

## 2. Dokumentne (Document-Oriented)

- **Model:** Podaci u **dokumentima** (JSON, BSON).
- **Kolekcije:** Grupe dokumenata (slično tablicama).
- **Fleksibilna Shema:** Dokumenti u kolekciji ne moraju imati istu strukturu.
- **Upiti:** Po sadržaju dokumenata, indeksiranje polja.
- **Primjeri:** MongoDB, Couchbase.
- **Upotreba:** CMS, e-trgovine, logiranje.

---

## 3. Stupčaste (Column-Family)

- **Model:** Podaci pohranjeni po **stupcima (column families)**.
- **Karakteristike:** Optimizirane za upite nad podskupom stupaca iz mnogo redaka. Skalabilne za Big Data.
- **Redak:** Ključ + obitelji stupaca. Stupac: ime, vrijednost, timestamp.
- **Primjeri:** Apache Cassandra, HBase.
- **Upotreba:** Analitika, vremenske serije, IoT.

---

## 4. Graf (Graph)

- **Model:** Fokus na **odnosima**. Struktura: **čvorovi** i **veze**.
- **Čvorovi:** Entiteti (osobe, proizvodi).
- **Veze:** Odnosi (PRIJATELJ_SA, KUPIO_JE). Mogu imati svojstva.
- **Karakteristike:** Efikasne za upite koji istražuju veze.
- **Primjeri:** Neo4j, Amazon Neptune.
- **Upotreba:** Društvene mreže, preporuke, detekcija prijevara.

---

## 5. Vektorske (Vector) - Ukratko

- **Model:** Pohrana, indeksiranje, pretraživanje **vektorskih ugradnji (embeddings)**.
- **Embeddings:** Numeričke reprezentacije podataka (tekst, slike) gdje slični objekti imaju bliske vektore.
- **Karakteristike:** Pretraživanje po semantičkoj sličnosti.
- **Ključne za AI/ML:** RAG za LLM-ove, preporuke.
- **Primjeri:** Pinecone, Weaviate, Milvus, Chroma, Qdrant.

---

# Tema 9: Prednosti i Nedostaci NoSQL Baza

---

## Prednosti NoSQL Baza

- **Skalabilnost (Horizontalna):** Lako "scale-out" na više servera.
- **Fleksibilnost Sheme:** Brži razvoj, prilagodba promjenama, raznoliki podaci.
- **Performanse (Specifične):** Optimizirane za određene modele/pristupe.
- **Visoka Dostupnost:** Često ugrađena replikacija i failover.

---

## Nedostaci NoSQL Baza

- **Konzistentnost:** Često "eventualna konzistentnost" (CAP teorem).
- **Manje Zrele (Relativno):** U usporedbi s RBP.
- **Nedostatak Standarda:** Nema jedinstvenog jezika poput SQL-a.
- **Transakcije:** Ograničena podrška za ACID preko više operacija.

---

## ACID Transakcije (Ponovimo)

Osiguravaju pouzdanost (tipično za RBP):
- **A - Atomicity:** Sve ili ništa.
- **C - Consistency:** Iz valjanog u valjano stanje.
- **I - Isolation:** Istovremene transakcije ne smetaju jedna drugoj.
- **D - Durability:** Potvrđene promjene su trajne.

*NoSQL: Često atomičnost samo na razini jednog dokumenta/zapisa.*

---

# Tema 10: Big Data Koncepti

---

## Eksplozija Količine Podataka

- **Eksponencijalni Rast:** Ogromne količine podataka se generiraju (društvene mreže, IoT, znanost).
- **Izazov:** Tradicionalni alati nedovoljni za obradu.
- **Big Data:** Veliki, složeni skupovi podataka i tehnologije za rad s njima.

![Data Growth](assets/datagrowth.png)

---

## Karakteristike Big Data (Originalna 3V)

- **Volume (Količina):** Ogromne količine (TB, PB, EB, ZB).
- **Variety (Raznolikost):**
    - **Strukturirani:** Organizirani (RBP).
    - **Polu-strukturirani:** Neka struktura (JSON, XML, logovi).
    - **Nestrukturirani:** Bez strukture (tekst, slike, video).
- **Velocity (Brzina):** Brzina generiranja i obrade (real-time).

---

## Proširene Karakteristike Big Data (5V+)

Uz 3V, često se spominju:
- **Veracity (Točnost):** Kvaliteta, pouzdanost podataka.
- **Value (Vrijednost):** Izvlačenje korisnih informacija.
- **Ostali 'V'-ovi:** Variability (promjenjivost), Validity (valjanost), Volatility (hlapljivost).

---

# Tema 11: Pohrana i Upravljanje Big Data

---

## Zašto RBP Nisu Uvijek Idealne za Big Data

- **Nestrukturirani Podaci:** RBP optimizirane za strukturirane.
- **Skalabilnost:** Teško horizontalno skaliranje.
- **Performanse JOIN-ova:** Presporo na ogromnim podacima.
- **Rigidnost Sheme:** Otežava rad s raznolikim, promjenjivim podacima.

---

## Ključne Tehnologije za Big Data

- **Distribuirani Datotečni Sustavi:** Npr. HDFS (Hadoop).
- **NoSQL Baze Podataka:** Za raznolike podatke, skalabilnost.
- **Okviri za Paralelnu Obradu:** Npr. Apache Spark, MapReduce.
- **Skladišta (Data Warehouses) i Jezera Podataka (Data Lakes).**
- **Cloud Computing Platforme:** Infrastruktura i usluge na zahtjev (AWS, Azure, GCP).

---

## Trenutno Stanje i Pretpostavke o Podacima

- **Promjena Paradigme:** Volumen (ZB), Variety (nestrukturirani dominiraju), Velocity (streaming), Izvori (IoT).
- **Moderne Pretpostavke:**
    - Format podataka: Često nepoznat/nepostojan.
    - Ažuriranja: Čitanje češće od pisanja (read-heavy).
    - Rast: Eksponencijalan.
    - Konzistentnost: Eventualna konzistentnost često prihvatljiva.

---

# Tema 12: CAP Teorem i BASE Model

---

## CAP Teorem (Brewer's Theorem)

U distribuiranom sustavu, **nemoguće je istovremeno garantirati sva 3**:
1.  **C - Consistency (Konzistentnost):** Svi čvorovi vide iste, najnovije podatke.
2.  **A - Availability (Dostupnost):** Sustav uvijek odgovara na zahtjeve.
3.  **P - Partition Tolerance (Particijska Tolerancija):** Sustav radi unatoč mrežnim prekidima.

**Implikacija:** Kod mrežne particije (P), morate birati između C i A.

---

## CAP Teorem: Odabir Kompromisa

![CAP Theorem Venn Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CAP_theorem_venn_diagram.svg/600px-CAP_theorem_venn_diagram.svg.png)

- **CP (Konzistentnost & Particijska Tolerancija):** Žrtvuje dostupnost (vraća grešku ako ne može osigurati C).
- **AP (Dostupnost & Particijska Tolerancija):** Žrtvuje strogu konzistentnost (može vratiti zastarjele podatke).
- **CA (Konzistentnost & Dostupnost):** Tradicionalne RBP na 1 čvoru. Nije za distribuirane.

*Većina distribuiranih sustava bira AP ili CP.*

---

## BASE Model (Alternativa ACID-u)

Opisuje svojstva NoSQL baza koje favoriziraju dostupnost:
- **B - Basically Available:** Sustav je uvijek dostupan.
- **S - Soft state:** Stanje sustava se može mijenjati (eventualna konzistentnost).
- **E - Eventually consistent:** Sustav će s vremenom postati konzistentan.

**ACID = stroga konzistentnost. BASE = dostupnost, skalabilnost, slabija konzistentnost.**

---

# Tema 13: Raspodijeljene Baze Podataka - Koncepti

---

## Što su Raspodijeljene Baze Podataka?

- **Definicija:** Podaci pohranjeni na **više fizičkih lokacija** (čvorova), korisnicima se čine kao jedinstvena baza.
- **Ciljevi:** Skalabilnost, visoka dostupnost, performanse, tolerancija na greške.

---

## Arhitektura Raspodijeljene Baze

- **Čvorovi (Nodes):** Računala u sustavu.
- **Klaster (Cluster):** Grupa povezanih čvorova.
- **Distribucija Podataka:**
    - **Fragmentacija (Sharding):** Podjela podataka.
    - **Replikacija:** Kopije podataka na više čvorova.
- **Mrežna Komunikacija & Katalog Podataka:** Ključni za rad.

---

## NoSQL Baze i Distribucija

- **Prirodno Distribuirane:** Mnoge NoSQL baze (Cassandra, HBase, MongoDB) dizajnirane za distribuciju.
- **Klaster Arhitektura:** Za horizontalno skaliranje i dostupnost.
- **Automatska Replikacija i Sharding:** Često ugrađeni mehanizmi.
- **Slijede CAP/BASE principe.**

---

# Tema 14: Denormalizacija

---

## Što je Denormalizacija?

- **Definicija:** **Namjerno dodavanje redundancije** (ponavljanja podataka) u normaliziranu bazu.
- **Cilj:** Poboljšati **performanse čitanja** žrtvujući neke prednosti normalizacije.
- **Kada:** Obično nakon normalizacije, kao strategija optimizacije za česte, skupe upite.
- **Nije loš dizajn** ako je kontrolirana.

---

## Razlozi za Denormalizaciju

- **Poboljšanje Performansi Upita:** Manje skupih JOIN-ova.
- **Pojednostavljenje Upita:** Lakši za pisanje i razumijevanje.
- **Brži Pristup:** Za specifične aplikacije/izvještaje.
- **Analitički Sustavi (OLAP):** Često koriste denormalizirane sheme (zvjezdaste, pahuljaste) jer je čitanje češće od pisanja.

---

## Uobičajene Strategije Denormalizacije

1.  **Dupliciranje Podataka:** Isti atributi u više tablica.
2.  **Predračunate Vrijednosti:** Pohrana suma, prosjeka itd.
3.  **Spajanje Tablica:** Kombiniranje često zajedno dohvaćanih tablica.
4.  **Pohrana Povijesnih Podataka (Snapshotting).**
5.  **Ugradnja (Embedding):** U dokumentnim bazama (npr. komentari unutar posta).

---

## Posljedice i Izazovi Denormalizacije

- **Povećana Redundancija:** Više prostora za pohranu.
- **Složenija Ažuriranja:** Promjena podatka na svim dupliciranim mjestima.
    - Rizik nekonzistentnosti.
- **Potencijalne Anomalije Podataka.**
- **Trade-off:** Brže čitanje vs. složenije pisanje i više prostora.

---

# Tema 15: Transakcije

---

## Što su Transakcije?

- **Definicija:** Niz operacija nad bazom kao **jedna, nedjeljiva logička jedinica**.
- **"Sve ili Ništa":**
    - Uspjeh svih operacija -> **COMMIT** (promjene trajne).
    - Neuspjeh bilo koje operacije -> **ROLLBACK** (baza se vraća u prethodno stanje).
- **Svrha:** Osigurati integritet i konzistentnost podataka.

---

## ACID Svojstva Transakcija (Detaljnije)

- **A - Atomicity:** "Sve ili ništa."
- **C - Consistency:** Iz valjanog u valjano stanje, poštujući pravila baze.
- **I - Isolation:** Istovremene transakcije ne ometaju jedna drugu.
- **D - Durability:** Potvrđene promjene su trajne i preživjet će padove sustava (npr. putem WAL).

---

## Razine Izolacije Transakcija

Stupanj izolacije jedne transakcije od drugih:
1.  **Read Uncommitted:** Najniža. Mogući *dirty reads* (čitanje nepotvrđenih promjena).
2.  **Read Committed:** Vidi samo potvrđene promjene. Sprječava *dirty reads*. Čest default.
3.  **Repeatable Read:** Ponovljena čitanja istog retka daju iste podatke.
4.  **Serializable:** Najviša. Kao da se transakcije izvršavaju serijski. Najbolja konzistentnost, najlošije performanse.

---

## Transakcije u NoSQL Svijetu

- **Ograničena Podrška:** Mnoge NoSQL baze nemaju tradicionalne ACID transakcije (posebno distribuirane).
- **Atomičnost na Razini Dokumenta/Zapisa:** Često za operacije nad 1 dokumentom.
- **Eventualna Konzistentnost:** Čest kompromis za dostupnost.
- **Saga Pattern:** Arhitektonski obrazac za upravljanje distribuiranim transakcijama (niz lokalnih transakcija + kompenzacije).
- **Neke NoSQL nude jača jamstva:** Npr. Neo4j (ACID), MongoDB (multi-dokument ACID unutar replica seta).

---

# Tema 16: SQL Programiranje

---

## Što je SQL Programiranje?

- **Proširenje SQL-a:** Ugrađivanje proceduralne logike direktno u bazu.
- **Objekti:** Stvaranje trajnih, ponovno upotrebljivih programskih jedinica.
- **Komponente:**
    - **Pohranjene Procedure (Stored Procedures)**
    - **Funkcije (User-Defined Functions - UDFs)**
    - **Okidači (Triggers)**

---

## Pohranjene Procedure

- **Svrha:** Enkapsulacija poslovne logike, performanse, sigurnost, modularnost.
- **Prednosti:** Jednom kompilirane, smanjuju mrežni promet, sigurnost (dozvole na proceduru).
- **Parametri:** Mogu biti ulazni (IN), izlazni (OUT), ulazno-izlazni (INOUT).

```sql
-- SQL Server primjer
CREATE PROC GetProductsByCategory (@CatID INT) AS
  SELECT PName, Price FROM Products WHERE CatID = @CatID;
-- Poziv: EXEC GetProductsByCategory @CatID = 1;
```

---

## Funkcije (User-Defined Functions - UDFs)

- **Svrha:** Izračuni, manipulacija podacima, vraćaju rezultat za SQL upite.
- **Vrste:**
    - **Skalarne:** Vraćaju 1 vrijednost (broj, string).
    - **Tablične (TVFs):** Vraćaju tablicu.
- **Ograničenja:** Obično ne mijenjaju stanje baze (bez DML nad trajnim tablicama).

---

## Okidači (Triggers)

- **Svrha:** Automatske akcije na DML događaje (`INSERT`, `UPDATE`, `DELETE`).
- **Upotreba:** Složena pravila integriteta, održavanje denormalizacije, audit.
- **Vrste:** `BEFORE` (prije DML), `AFTER` (nakon DML).
- **`inserted` / `deleted` pseudo-tablice:** Pristup podacima unutar okidača.
- **Oprez:** Mogu utjecati na performanse; koristiti pažljivo.

---

## Programske Strukture u SQL-u

- **Varijable:** `DECLARE @MojaVar INT; SET @MojaVar = 10;`
- **Uvjetovanja:** `IF @Uvjet THEN ... ELSE ... END IF;` (ovisno o dijalektu)
- **Petlje:** `WHILE @Brojac < 10 DO ... END WHILE;`
- **Kursori:** Iteracija kroz retke (koristiti oprezno, set-based je brže).
- **Upravljanje Greškama:** `TRY...CATCH` (npr. T-SQL).

---

# Tema 17: Pogledi (Views)

---

## Što je Pogled (View)?

- **Virtualna Tablica:** Pohranjeni SQL upit koji se ponaša kao tablica. Ne pohranjuje podatke fizički (osim materijaliziranih).
- **Svrha:**
    - **Pojednostavljenje Složenih Upita.**
    - **Sigurnost:** Ograničavanje pristupa podacima.
    - **Logička Neovisnost Podataka.**
    - **Konzistentnost Prikaza Podataka.**

---

## Kreiranje i Korištenje Pogleda

```sql
-- Prikaz imena kupaca i ID-ova njihovih narudžbi
CREATE VIEW vw_KupciNarudzbe AS
SELECT K.Ime, K.Prezime, N.ID_Narudzbe
FROM Kupci K JOIN Narudžbe N ON K.ID_Kupca = N.ID_Kupca;

-- Korištenje pogleda
SELECT * FROM vw_KupciNarudzbe WHERE Ime = 'Ana';
```
- Podaci u pogledu su uvijek **ažurni** (upit se izvršava pri pristupu).

---

## Materijalizirani Pogledi

- **Fizička Pohrana:** **Fizički pohranjuju rezultate** upita.
- **Ažuriranje:** Podaci **nisu automatski ažurni**. Treba ih periodički **osvježavati (REFRESH)**.
- **Prednosti:** **Performanse** za složene upite/agregacije (rezultati pre-izračunati).
- **Nedostaci:** Zauzimaju prostor, podaci mogu biti zastarjeli, osvježavanje zahtjevno.

---

```sql
-- PostgreSQL primjer:
CREATE MATERIALIZED VIEW mv_MjesecniPromet AS
SELECT EXTRACT(MONTH FROM DatumNarudzbe) AS Mjesec, SUM(Iznos)
FROM Narudzbe GROUP BY Mjesec;
-- Osvježavanje: REFRESH MATERIALIZED VIEW mv_MjesecniPromet;
```

---

# Tema 18: DuckDB - Moderna Analitička SQL Baza

---

## Što je DuckDB?

- **Ugrađena (Embedded) Analitička (OLAP) Baza:** Radi unutar aplikacije (kao SQLite), ali za analitiku.
- **SQL Sučelje:** Standardni SQL + analitička proširenja.
- **Optimizirana za Brzinu:**
    - **Stupčano (Columnar) Skladištenje.**
    - **Vektorizirano Izvršavanje Upita.**
    - **Paralelizacija.**
- **Nula Konfiguracije, Open Source.**

---

## Ključne Značajke i Slučajevi Korištenja DuckDB-a

- **Jednostavnost:** Nema servera, biblioteka. Radi u memoriji ili s datotekama.
- **Direktno Čitanje Formata:** Čita CSV, Parquet, JSON bez uvoza.
    ```sql
    SELECT * FROM 'data.csv';
    ```
- **Integracija s Pandas (Python).**
- **Slučajevi Korištenja:** Interaktivna analiza, ETL, ugrađena analitika, lokalni razvoj.

---

## DuckDB vs. Ostale Baze

| Karakteristika     | DuckDB                  | SQLite          | PostgreSQL/MySQL | Cloud DW (BigQuery) |
|--------------------|-------------------------|-----------------|------------------|---------------------|
| **Primarna Svrha** | OLAP (Analitika)        | OLTP            | OLTP             | OLAP (Velika Skala) |
| **Arhitektura**    | Ugrađena                | Ugrađena        | Klijent-Server   | Cloud Servis        |
| **Skladištenje**   | Stupčano                | Redčano         | Redčano          | Stupčano            |
- **DuckDB:** Brza, lokalna, jednostavna analitika. Nije zamjena za OLTP ili masivna cloud skladišta.

---

# Tema 19: MongoDB - Dokumentna Baza Podataka

---

## Što je MongoDB?

- **Vodeća NoSQL Dokumentna Baza:** Podaci u fleksibilnim, JSON-sličnim dokumentima.
- **BSON (Binary JSON):** Interni, efikasniji format za pohranu; podržava više tipova.
- **Kolekcije:** Grupe dokumenata (kao tablice).
- **Fleksibilna Shema ("Schemaless"):** Dokumenti u kolekciji ne moraju imati istu strukturu.
    - *Opcionalno:* Schema Validation za kontrolu.

---

## Osnovne Karakteristike MongoDB-a

- **Dokumentni Model:** Prirodno mapiranje na objekte.
- **Upitni Jezik & Agregacijski Okvir:** Moćni alati za upite i transformacije.
- **Indeksi:** Za optimizaciju (jednostruki, složeni, tekstualni, geo...).
- **Horizontalna Skalabilnost:**
    - **Replikacija (Replica Sets):** Visoka dostupnost, redundancija.
    - **Sharding:** Distribucija podataka za veliki volumen/opterećenje.
- **MongoDB Atlas:** Potpuno upravljana cloud usluga.

---

## CRUD Operacije u MongoDB-u

- **Create:** `insertOne()`, `insertMany()`
- **Read:** `findOne({uvjet})`, `find({uvjet})` (vraća kursor)
- **Update:** `updateOne({uvjet}, {$set: {promjene}})`, `updateMany()`
    - Operatori: `$set`, `$inc`, `$push`, `$pull`.
- **Delete:** `deleteOne({uvjet})`, `deleteMany()`

---

## Dizajn Sheme: Ugradnja vs. Referenciranje

- **Ugradnja (Embedding):** Povezani podaci unutar istog dokumenta.
    - **Primjer:** Komentari ugrađeni u post.
    - **Prednosti:** Brži dohvat (1 upit), atomske operacije.
    - **Nedostaci:** Veličina dokumenta (16MB), redundancija, teže ažuriranje.
- **Referenciranje (Linking):** Pohrana reference (`_id`) na dokument u drugoj kolekciji. Koristi `$lookup` (slično JOIN-u).
    - **Prednosti:** Manji dokumenti, nema redundancije.
    - **Nedostaci:** Potrebni dodatni upiti (`$lookup`), sporije.
**Odabir ovisi o obrascima pristupa podacima.**

---

# Tema 20: Napredne Tehnike Raspodjele Podataka

---

## Federacija Podataka vs. Distribucija

- **Federacija:** Integracija postojećih, autonomnih, često heterogenih baza. Virtualni pogled bez fizičkog premještanja.
- **Distribucija:** Raspodjela jedinstvenog logičkog sustava (obično homogenog DBMS-a) na više čvorova. Fokus na skalabilnost i dostupnost jedne baze.

---

## Napredne Strategije Fragmentacije (Sharding)

Fragmentacija = podjela baze na manje dijelove (shards) na različitim čvorovima.
1.  **Vertikalna Fragmentacija:** Dijeli tablicu po **stupcima**.
2.  **Derivirana Horizontalna Fragmentacija:** Fragmentacija jedne tablice temelji se na fragmentaciji **povezane tablice** (za lokalne JOIN-ove).

---

## Consensus Algoritmi (Paxos, Raft, ZAB)

Osiguravaju da se svi čvorovi u distribuiranom sustavu slože oko stanja, čak i kod grešaka. Ključni za konzistentnost.
- **Raft:** Lakši za razumijevanje/implementaciju. (Izbor lidera, replikacija loga).
- Koriste se za distribuirane logove, izbor lidera, održavanje konzistentnosti.

---

## Globalno Jedinstveni Identifikatori (GUIDs)

Generiranje jedinstvenih PK u distribuiranim sustavima:
1.  **UUID/GUID:** 128-bitni, globalno jedinstveni, neovisno generirani. Nisu sortirani.
2.  **Snowflake ID (Twitter):** 64-bitni (timestamp + worker ID + sekvenca). Približno sortirani po vremenu.
3.  **ULID:** Timestamp + random komponenta. Sortabilni, kraća string reprezentacija.

---

# Tema 21: Vektorske Baze Podataka

---

## Što su Vektorske Baze Podataka?

- **Specijalizirane NoSQL Baze:** Za pohranu i pretraživanje **vektorskih ugradnji (embeddings)**.
- **Embeddings:** Numeričke reprezentacije podataka (tekst, slike) u višedimenzionalnom prostoru. Slični objekti = bliski vektori. Generiraju se AI/ML modelima.
- **Pretraživanje po Sličnosti:** Umjesto po ključnim riječima. Koriste metrike (kosinusna sličnost, Euklidska udaljenost).

---

## Algoritmi za Pretraživanje Najbližih Susjeda (ANN)

Za brzo pretraživanje u velikim, visokodimenzionalnim prostorima (Approximate Nearest Neighbor):
- **HNSW (Hierarchical Navigable Small World):** Višeslojna grafovska struktura. Popularan.
- **IVF (Inverted File Index) / IVFADC:** Dijeli prostor u klastere; pretražuje relevantne. Često s Product Quantization (PQ) za kompresiju.
- **LSH (Locality-Sensitive Hashing):** Slični vektori u iste "kante".

---

## Primjene Vektorskih Baza

- **Semantičko Pretraživanje:** Po značenju, ne ključnim riječima.
- **Retrieval Augmented Generation (RAG):** Za LLM-ove; dohvat relevantnog konteksta iz baze za točnije odgovore.
- **Sustavi Preporuka:** Slični proizvodi, članci, filmovi.
- **Detekcija Anomalija, De-duplikacija Podataka.**
- **Multimodalno Pretraživanje:** Tekst leftrightarrow️ slika.

---

## Vodeće Vektorske Baze

- **Pinecone:** Cloud, jednostavnost, performanse.
- **Weaviate:** Open-source, graf veze, auto-generiranje vektora.
- **Milvus:** Open-source, visoko skalabilna.
- **Qdrant:** Open-source, fokus na filtriranje metapodataka.
- **Chroma:** Open-source, lagana, za lokalni razvoj (LangChain).
- **pgvector:** PostgreSQL ekstenzija (hibridni RBP-vektorski upiti).
- **Ostali:** Redis (RediSearch), Elasticsearch.

---

# Tema 22: Ključ-Vrijednost (Key-Value) Baze Podataka

---

## Ponovimo: Što su K-V Baze?

- **Model:** Najjednostavniji NoSQL. Par: jedinstveni **ključ** + **vrijednost**.
- **Vrijednost:** Bilo što (string, JSON, blob). Baza ne interpretira strukturu.
- **Operacije:** `PUT(ključ, vrijednost)`, `GET(ključ)`, `DELETE(ključ)`.
- **Karakteristike:** Izuzetno brze, visoko skalabilne, fleksibilne.

---

## Kada Koristiti (i Ne Koristiti) K-V Baze?

**Idealne za:**
- **Caching:** Brzo čitanje često korištenih podataka (Redis).
- **Korisničke Sesije, Profili.**
- **Leaderboards, Redovi Poruka.**
**Manje pogodne za:**
- **Složene Upite i Relacije** (nema SQL JOIN-ova).
- **Strogu Konzistentnost** preko više ključeva.
- **Dubinsku Analitiku** po vrijednostima.

---

## Pohrana: In-Memory vs. On-Disk

- **In-Memory (Redis):**
    - RAM. **Prednosti:** Ekstremno brzo.
    - **Nedostaci:** Ograničen kapacitet, skuplje. Trajnost opcionalna (snapshot, AOF).
- **On-Disk (RocksDB):**
    - SSD/HDD. **Prednosti:** Veći kapacitet, jeftinije, trajno.
    - **Nedostaci:** Sporije od RAM-a.
- **Hibridni Pristupi:** RAM kao cache za "vruće" podatke.

---

## Skalabilnost: Replikacija i Particioniranje

- **Replikacija:** Kopije podataka na više čvorova (dostupnost, performanse čitanja).
    - Modeli: Master-Slave, Masterless.
- **Particioniranje / Sharding:** Podjela ključeva na više čvorova (kapacitet, propusnost).
    - Metode: Hash, Range, Consistent Hashing (minimizira premještanje kod promjene broja čvorova).

---

## Dizajn Ključeva i Pretraga po Vrijednosti

- **Dizajn Ključeva:** KRITIČAN! Konvencija (npr. `entitet:id:atribut`) za organizaciju, izbjegavanje kolizija, "pretragu" po prefiksu.
- **Pretraga po Vrijednosti:** Direktno nije efikasna. Rješenja:
    1. Filtriranje u aplikaciji (neučinkovito).
    2. Ručni Sekundarni Indeksi (dodatni K-V: `vrijednost -> originalni_ključ`).
    3. K-V Baze s Ugrađenim Indeksiranjem (RediSearch, DynamoDB GSI).

---

# Tema 23: SpacetimeDB - Relacijska Baza s Integriranom Logikom

---

## Što je SpacetimeDB?

- **Relacijska Baza + Integrirana Aplikacijska Logika:** Serverska logika (npr. za igre) piše se direktno u bazi.
- **Logika u WebAssembly (WASM):** Kod (Rust, C#) izvršava se kao sigurni WASM moduli unutar baze.
- **Nema Zasebnog Servera:** Klijenti komuniciraju direktno s bazom.
- **Optimizirana za Real-Time/Multiplayer.**
- **In-Memory + Trajnost (Commitlog/WAL).**

---

## Ključni Koncepti SpacetimeDB-a (1/2)

1.  **Tablice (Tables):** Relacijske, definirana shema, u memoriji.
    ```rust
    #[spacetimedb(table)] pub struct Player { #[primarykey] id: u64, ... }
    ```
2.  **Reduceri (Reducers):** WASM funkcije koje mijenjaju stanje baze (podatke u tablicama).
    - Atomske, transakcijske. Pozivaju ih klijenti (RPC).
    ```rust
    #[spacetimedb(reducer)] fn attack(ctx: Ctx, target_id: u64, dmg: i32) { ... }
    ```

---

## Ključni Koncepti SpacetimeDB-a (2/2)

3.  **Subscription Upiti:**
    - Klijenti se pretplaćuju na podatke SQL upitima (preko WebSocket-a).
    - Primaju inicijalno stanje + inkrementalne promjene.
    - **Lokalna Replika na Klijentu:** Ekstremno brza čitanja.
    ```typescript
    client.subscribe("SELECT * FROM Player", (data) => { /* ... */ });
    ```
4.  **WASM Moduli:** Kompajlirani kod reducera i definicija tablica.

---

## Arhitektura i Tok Podataka SpacetimeDB

1.  Klijent (WebSocket) -> Autentifikacija (OIDC).
2.  Klijent -> Pretplata (SQL) -> Inicijalni podaci + buduće promjene.
3.  Klijent -> Poziv Reducera (RPC).
4.  SpacetimeDB -> Izvršava WASM Reducer (atomska promjena Tablica).
5.  SpacetimeDB -> Promjene se šalju relevantnim pretplaćenim klijentima.
6.  SpacetimeDB -> Promjene se zapisuju u Commitlog (trajno).

---

# Tema 24: Zaključak

---

## Ključne Poruke Kolegija

1.  **Nema "Najbolje" Baze:** Izbor ovisi o zahtjevima ("Polyglot Persistence").
2.  **Razumijevanje Trade-offova:** Konzistentnost vs. Dostupnost (CAP), Normalizacija vs. Performanse (Denormalizacija).
3.  **SQL je i Dalje Važan.**
4.  **Podaci su "Gorivo" Modernih Aplikacija (posebno AI/LLM).**
5.  **Dizajn je Ključan** (RBP i NoSQL).
6.  **Budućnost je Raznolika i Hibridna.**
