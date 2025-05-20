---
marp: true
theme: gaia
title: Raspodijeljene i nerelacijske baze podataka - Column-Family Databases i InfluxDB
description: Nikola Balić, Stučaste baze podataka
paginate: true
style: |
  section {
    background-color: #fff;
  }
  section.title-slide {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }
  section.agenda {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 20px;
  }
  section.agenda ul {
    margin-top: 1em;
  }
  pre {
    overflow-x: auto;
    max-height: 400px;
    border-radius: 5px;
    background-color: #f5f5f5;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  pre, code {
    font-size: 0.8em;
  }
  table {
    font-size: 0.75em;
    width: 100%;
    max-width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
  }
  th, td {
    padding: 0.4em 0.6em;
    border: 1px solid #ddd;
  }
  th {
    background-color: #f0f0f0;
  }
  .table-container {
    width: 100%;
    overflow-x: auto;
  }
  p {
    font-size: 0.9em;
  }
  .highlight {
    color: #d32f2f;
    font-weight: bold;
  }
  .two-column {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 20px;
  }
  .diagram {
    text-align: center;
    margin: 0.5em 0;
  }
  .case-study {
    background-color: #f5f5f5;
    border-left: 5px solid #4caf50;
    padding: 0.5em 1em;
    margin: 1em 0;
  }
  img {
    max-width: 100%;
    display: block;
    margin: 0 auto;
  }
  img[alt="schema-compare"] {
    max-height: 300px;
  }
---

<!-- _class: title-slide -->
# Stučaste baze podataka

## Column-Family i Time-Series DB

#### Akademska godina 2024/2025
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---

<!-- _class: agenda -->
# Agenda

## Column-Family baze
- Problem skaliranja društvenih platformi
- Column vs Row orijentacija
- Bigtable i osnovni koncepti
- Moderne implementacije
- Primjeri iz prakse

## InfluxDB i Time-Series baze
- Specifičnosti vremenskih serija
- Evolucija InfluxDB-a
- Arhitektura i principi rada
- Primjeri primjene

---

# I. DIO: COLUMN-FAMILY BAZE PODATAKA

---

## Problem: Društvena platforma u krizi

**Scenarij:** Radite na rastućoj društvenoj platformi s 10M+ korisnika

<div class="case-study">
<strong>Simptomi:</strong>
<ul>
  <li>⚠️ <strong>Padovi sustava:</strong> Baza podataka se ruši tijekom vršnih sati</li>
  <li>⏱️ <strong>Spora izvedba:</strong> Generiranje feedova traje 10+ sekundi</li>
  <li>🔄 <strong>Problemi skaliranja:</strong> Svaki novi server dodaje složenost</li>
  <li>💰 <strong>Problemi s troškovima:</strong> Zahtjevi za pohranu rastu eksponencijalno</li>
</ul>
</div>

### Kako biste redizajnirali ovaj sustav?

---

## Zašto tradicionalne baze podataka nisu dovoljne

**Zahtjevi vaše društvene platforme:**
- Potrebno je pohraniti: Korisničke profile, objave, komentare, lajkove, praćenja
- Potrebno je posluživati: Personalizirane feedove, obavijesti, analitiku
- Potrebno je upravljati: Nepredvidivim rastom, sezonskim skokovima prometa

**Problemi s RDBMS-om za ovaj slučaj:**
- JOIN operacije postaju preskupe
- Promjene sheme su teške kako se funkcionalnosti razvijaju
- Vertikalno skaliranje doseže fizička ograničenja
- Nemoguće je učinkovito particionirati podatke preko više servera

---

## Rješenja iz stvarnog svijeta

<div class="two-column">
<div>

### Netflix
- Migrirali s Oracle-a na Cassandra-u
- 3+ bilijuna podatkovnih točaka dnevno
- Personalizacija za 200M+ pretplatnika
</div>
<div>

### Spotify
- Cassandra za 100M+ aktivnih korisnika
- 422M+ ukupnih pjesama
- Personalizirane playliste u stvarnom vremenu
</div>
</div>

<div class="case-study">

### Instagram
- Cassandra obrađuje milijarde unosa vremenskih crta dnevno
- Omogućuje dostavu objava u gotovo stvarnom vremenu
- Podržava globalnu distribuciju sadržaja bez kašnjenja
</div>

---

## Row vs. Column Oriented Storage

<div class="diagram">
<img alt="schema-compare" src="/api/placeholder/800/300" />
</div>

### Fundamentalna razlika

**Row-oriented:**
```
[id:1, name:"Ana", email:"ana@email.com", dept:"HR"]
[id:2, name:"Ivan", email:"ivan@email.com", dept:"IT"]
```

**Column-oriented:**
```
id:    [1, 2]
name:  ["Ana", "Ivan"]
email: ["ana@email.com", "ivan@email.com"]
dept:  ["HR", "IT"]
```

---

## Row-Oriented Storage

<div class="two-column">
<div>

### Karakteristike
- **Pohranjuje** redak po redak
- **Optimizirano za:**
  - OLTP transakcije
  - Često pisanje
  - Dohvat kompletnih zapisa
</div>
<div>

### Prednosti
- ✅ Učinkovit unos i ažuriranje
- ✅ Jednostavno upravljanje transakcijama
- ✅ Efikasno kod dohvaćanja cijelog retka
- ✅ Jednostavno za implementirati
</div>
</div>

<div class="diagram">
<img alt="row-storage" src="/api/placeholder/600/200" />
</div>

---

## Column-Oriented Storage

<div class="two-column">
<div>

### Karakteristike
- **Pohranjuje** stupac po stupac
- **Optimizirano za:**
  - OLAP analitiku
  - Agregacije (SUM, AVG, COUNT)
  - Dohvat podskupova stupaca
</div>
<div>

### Prednosti
- ✅ Bolja kompresija podataka
- ✅ Učinkovitije čitanje podskupova stupaca
- ✅ Brže analitičke operacije
- ✅ Bolje skaliranje za velike podatke
</div>
</div>

<div class="diagram">
<img alt="column-storage" src="/api/placeholder/600/200" />
</div>

---

## OLTP vs OLAP: Usporedba

<div class="table-container">

| Karakteristika | OLTP | OLAP |
|----------------|------|------|
| **Primarna svrha** | Svakodnevne transakcije | Poslovna analitika |
| **Optimizacija** | Pisanje i čitanje pojedinačnih zapisa | Složeni upiti nad velikim skupovima podataka |
| **Veličina podataka** | Manji broj zapisa po upitu | Velike količine podataka |
| **Struktura podataka** | Normalizirane tablice | Denormalizirani, višedimenzionalni modeli |
| **Ažuriranje** | Često (stvarno vrijeme) | Periodično (batch) |
| **Performanse** | Brze transakcije (ms) | Duži upiti (s ili min) |
| **Shema** | Stabilna | Dinamična |
| **Primjeri primjene** | Transakcije, e-trgovina | Business Intelligence, predviđanje |
| **Preferirana pohrana** | Red-orijentirane BP | Stupac-orijentirane BP |
</div>

---

## Demonstracija SQL upita: Usporedba pristupa

### SELECT ime FROM emp WHERE ID_br=666

<div class="two-column">
<div>

**Row-oriented execution:**
```
1. Učitaj prvi blok (redci 1001-1003)
2. Provjeri uvjet ID_br=666 za svaki redak
3. Učitaj drugi blok (redci 1004-1006)
4. Provjeri uvjet ID_br=666 za svaki redak
5. Kada se pronađe redak, vrati 'ime'
```
</div>
<div>

**Column-oriented execution:**
```
1. Učitaj stupac ID_br
2. Pronađi pozicije gdje je ID_br=666
3. Učitaj samo te pozicije iz stupca 'ime'
```
</div>
</div>

### SELECT SUM(placa) FROM emp

<div class="two-column">
<div>

**Row-oriented execution:**
```
1. Učitaj sve blokove
2. Izvuci vrijednost plaće iz svakog retka
3. Izračunaj sumu
```
</div>
<div>

**Column-oriented execution:**
```
1. Učitaj samo stupac 'placa'
2. Izračunaj sumu
```
</div>
</div>

---

## Osnove Column-Family baza

**Temeljni koncept:** Podaci pohranjeni kao stupci unutar obitelji stupaca, adresirani prema ključu retka

```
┌─────────────────────────────────────────────┐
│ Ključ retka: "user_123"                     │
├─────────────────┬───────────────────────────┤
│ Obitelj stupaca:│ Obitelj stupaca:          │
│ profil          │ objave                    │
├─────────────────┼───────────────────────────┤
│ ime: "Ana"      │ 2023-01-01: "Prvi post"   │
│ email: "a@e.com"│ 2023-01-15: "Drugi post"  │
│ dob: "29"       │ 2023-02-01: "Treći post"  │
└─────────────────┴───────────────────────────┘
```

**Važno: Sparse Matrix** - Samo popunjena polja su pohranjena, prazna zauzimaju 0 prostora

---

## Terminologija Column-Family baza

### Različiti nazivi, slični koncepti

- **Column Family Databases**
- **Wide Column Stores**
- **Column-oriented Databases**
- **Bigtable Clones**

**Potencijalna konfuzija:** "Column-oriented" može se odnositi na:
1. Način fizičkog pohranjivanja podataka
2. Logički model višedimenzionalnih ključ-vrijednost parova

---

## Ključne komponente Column-Family DB

<div class="two-column">
<div>

### Glavne komponente
- **Keyspace:** Kontejner za column families (analog sheme)
- **Row Key:** Jedinstveni identifikator retka
- **Column Family:** Grupa povezanih stupaca
- **Column:** Najmanja jedinica pohrane (ime:vrijednost)
- **Timestamp:** Verzioniranje vrijednosti
</div>
<div>

### Osnovna struktura
```
Keyspace: "SocialApp"
  Table: "Users"
    Row: "user123"
      CF: "profile"
        Col: "name" → "Ana"
        Col: "email" → "a@e.com"
      CF: "posts"
        Col: "2023-01-01" → "Post 1"
```
</div>
</div>

---

## Row Key: Temelj skalabilnosti

- **Jedinstveni identifikator** za redak (npr. `user123`, `com.google.www`)
- **Analogno primarnom ključu** u relacijskoj bazi
- **Omogućuje:**
  - Brzo pronalaženje podataka (lookup)
  - Distribuciju podataka (sharding)
  - Sortiranje podataka za efikasne range scanove

**Važno:**
- Pohranjen leksikografski (abecedno): Ključno za grupiranje povezanih podataka
- Veličina (Bigtable): Uobičajeno 10-100 bajtova, max 64KB

---

## Column Families: Organizacijska jedinica

```
Column Family: profile
┌───────────┬───────────┬───────────┐
│ name:"Ana"│email:"a@e"│ age:"29"  │
└───────────┴───────────┴───────────┘

Column Family: posts
┌────────────────┬─────────────────┐
│2023-01:"Post 1"│2023-02:"Post 2" │
└────────────────┴─────────────────┘
```

**Funkcije column family:**
- **Grupiranje povezanih podataka**
- **Osnovna jedinica administracije**:
  - Kontrola pristupa
  - Konfiguracija kompresije
  - Postavke keširanja
  - Pravila garbage collection-a

**Fizički aspekt:** Stupci iste CF često su pohranjeni zajedno na disku (lokalitet)

---

## Primjer koda: Pristup podacima u Cassandra (CQL)

### Stvaranje strukture podataka
```sql
-- Stvaranje keyspace-a
CREATE KEYSPACE social_app
  WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};

-- Stvaranje tablice
CREATE TABLE social_app.users (
  user_id TEXT PRIMARY KEY,
  name TEXT,
  email TEXT,
  age INT
);

-- Stvaranje tablice s obitelji stupaca za objave
CREATE TABLE social_app.user_posts (
  user_id TEXT,
  post_date TIMESTAMP,
  content TEXT,
  likes INT,
  PRIMARY KEY (user_id, post_date)
) WITH CLUSTERING ORDER BY (post_date DESC);
```

---

## Primjer koda: CRUD operacije u Cassandra

### Unos i dohvat podataka
```sql
-- Unos korisnika
INSERT INTO social_app.users (user_id, name, email, age)
VALUES ('user123', 'Ana Horvat', 'ana@email.com', 29);

-- Unos objava
INSERT INTO social_app.user_posts (user_id, post_date, content, likes)
VALUES ('user123', '2023-01-15 12:30:00', 'Moj prvi post!', 5);

-- Dohvat svih podataka o korisniku
SELECT * FROM social_app.users WHERE user_id = 'user123';

-- Dohvat posljednjih 10 objava korisnika
SELECT * FROM social_app.user_posts
WHERE user_id = 'user123'
LIMIT 10;
```

---

## Atomarno čitanje i pisanje

**Ključna karakteristika:**
- **Operacije na razini retka su atomarne**
- **Garantirano je da će se svi stupci u retku prilikom jedne operacije:**
  - Pročitati zajedno kao jedinica (ili nijedan)
  - Zapisati zajedno kao jedinica (ili nijedan)

**Važna ograničenja:**
- **Nema parcijalnih rezultata** unutar operacije na jednom retku
- **Transakcijska ograničenja:**
  - Atomične operacije samo na jednom retku
  - Ne podržava generalne transakcije preko više redaka ili tablica

---

## Bigtable: Početak column-family DB

### Google-ova revolucija koja je promijenila sve

- **Objavljen 2006. godine** kao znanstveni rad
- **"Bigtable: A Distributed Storage System for Structured Data"**
- **Utjecaj:** Inspirirao mnoge open-source implementacije
  - Apache HBase
  - Apache Cassandra (+ ideje iz Amazon Dynamo)
  - ScyllaDB, i druge...
- **Cilj:** Skaliranje do petabajta podataka
- **Dizajn:** Optimiziran za nisko-latentno, visoko-propusno okolinu

---

## Google-ova motivacija za razvoj Bigtable-a

### Zašto su razvili novu vrstu baze podataka?

**Potreba za obradom:**
- **Polustrukturirani podaci:**
  - Web indeksi (URL, sadržaj, meta)
  - Korisnički podaci (preference, pretraživanja)
  - Geografski podaci (lokacije, satelitske slike)

**Razmjeri:**
- Milijarde URL-ova
- Milijuni korisnika
- Terabajtne zbirke podataka

**Nijedna postojeća baza podataka nije mogla podržati ove zahtjeve**

---

## Bigtable Model Podataka: Definicija

### Trodimenzionalna sortirana mapa

<div class="two-column">
<div>

**Bigtable definicija:**
"Rijetka (sparse), distribuirana, perzistentna višedimenzionalna sortirana mapa."

**Indeksirana s:**
`(row:string, column:string, time:int64) → string`

**Karakteristike:**
- **"Sparse":** Većina ćelija je prazna
- **"Multidimensional":** Višestruke dimenzije za indeksiranje
</div>
<div>

**3D vizualizacija:**
```
     Column Families
     /       \
    /         \
Row Keys      Timestamps
    \         /
     \       /
      Values
```

**Vrijednost:**
- Niz bajtova (neinterpretiran od strane baze)
- Klijent određuje interpretaciju
</div>
</div>

---

## Bigtable: Primjer Web tablice

### Praktična primjena za indeksiranje web stranica

```
Row Key: "com.cnn.www"  (obrnuti URL)
┌──────────────────────┬────────────────────────────────┐
│ Column Family:       │ Column Family:                 │
│ contents:            │ anchor:                        │
├──────────────────────┼────────────────────────────────┤
│ t3: "<html>..."      │ cnnsi.com: "CNN Sports"        │
│ t2: "<html>..."      │ my.look.ca: "CNN.com"          │
└──────────────────────┴────────────────────────────────┘
```

**Ključne karakteristike:**
- **Row key:** Obrnuti URL - grupira srodne stranice (sve s iste domene)
- **CF "contents:":** Sadržaj stranice s vremenskom oznakom
- **CF "anchor:":** Linkovi koji upućuju na stranicu (kvalifikator = URL koji linka)

---

## Bigtable optimizacije: Tehnike za poboljšanje performansi

<div class="two-column">
<div>

### Kompakcije
- **Minor:** Memtable → SSTable
- **Merging:** Spaja nekoliko SSTables
- **Major:** Spaja sve SSTables i uklanja obrisane podatke
</div>
<div>

### Caching i filteri
- **Scan Cache:** Često čitani retci
- **Block Cache:** SSTable blokovi
- **Bloom Filteri:** Brza provjera sadrži li SSTable podatak
</div>
</div>

### Napredne tehnike
- **Locality Groups:** Grupiranje column families za bolji lokalitet
- **Kompresija:** Po locality group
- **Commit Log:** Jedan log po serveru za bolje performanse
- **Nepromjenjivost SSTables-a:** Pojednostavljuje konkurentnost i dijeljenje

---

## Moderne Column-Family baze podataka

<div class="two-column">
<div>

### Apache Cassandra
- Pokreće Netflix, Apple, Instagram
- Decentralizirana P2P arhitektura
- Elastična skalabilnost
- CQL sučelje slično SQL-u
</div>
<div>

### ScyllaDB
- "Cassandra u C++" - 10x performanse
- Kompatibilna s Cassandra driverima
- Samopodešavanje
- Korisnici: Discord, Starbucks
</div>
</div>

### Amazon DynamoDB
- Potpuno upravljani NoSQL servis
- Višeregionalni, višestruki glavni čvorovi
- Automatsko skaliranje s latencijom <10ms
- Pay-per-use model bez održavanja

---

## Moderna studija slučaja: Discord

<div class="case-study">

### Discord-ov izazov skalabilnosti
- 300M+ registriranih korisnika
- 25+ milijardi poruka mjesečno
- 19M aktivnih servera

### ScyllaDB implementacija
1. Pohranjuje podatke o prisutnosti korisnika i poruke
2. Omogućuje značajke u stvarnom vremenu (indikatori tipkanja, status online)
3. Podržava i trenutni pristup i povijesno pretraživanje
4. Prilagođena strategija shardinga za ravnomjernu distribuciju
</div>

**Rezultat:** Sub-millisekunda latencija čak i pod ekstremnim opterećenjem

---

## Kada (NE) koristiti Column-Family BP

<div class="two-column">
<div>

### Dobri scenariji ✅
- Brza pohrana/dohvat po ključu
- Pisanje masovnih podataka
- Vremenske serije s poznatim uzorcima upita
- Platforme koje zahtijevaju horizontalno skaliranje
- Visoka dostupnost s geografskom distribucijom
</div>
<div>

### Loši scenariji ❌
- Kompleksne relacije između podataka
- Česti multi-row upiti bez pažljivog modeliranja
- Brojni ad-hoc upiti
- Potreba za strogim ACID transakcijama
- Mali volumen podataka
</div>
</div>

---

# II. DIO: TIME-SERIES BAZE PODATAKA

---

# InfluxDB: Baza podataka za vremenske serije

## Uvod u vremenske serije

**Što su vremenske serije?**
- Podaci gdje je vrijeme primarna dimenzija indeksiranja
- Svaki zapis ima vremensku oznaku (timestamp)
- Prirodno se akumuliraju kroz vrijeme
- Rijetko se ažuriraju nakon unosa

**Primjeri:**
- Podaci senzora (IoT)
- Metrike sustava (CPU, memorija)
- Financijski podaci (cijene dionica)
- Korisničke aktivnosti (klikovi, pregledi)

---

## InfluxDB ekosustav: Evolucija

<div class="two-column">
<div>

### Originalni TICK Stack
- **T**elegraf: Agent za prikupljanje
- **I**nfluxDB: Baza podataka
- **C**hronograf: Vizualizacija
- **K**apacitor: Obrada i alertiranje
</div>
<div>

### Moderna evolucija
- Chronograf često zamijenjen s Grafana
- Kapacitor u v3.0 zamijenjen ugrađenim Python VM & trigerima
- InfluxDB 3.0: Značajan redizajn
</div>
</div>

<div class="diagram">
<img alt="tick-stack" src="/api/placeholder/700/200" />
</div>

---

## Tehnološka evolucija InfluxDB-a

### Od Go do Rust-a

**InfluxDB 1.x & 2.x:**
- Napisane u Go
- Vlastiti jezik upita (Flux)
- Monolitna arhitektura

**InfluxDB 3.0: Nova generacija**
- Prepisana u Rust-u
- SQL kao standardno sučelje
- Razdvajanje compute i storage komponenti
- Optimizirana za cloud native okolinu

**Cilj:** Bolje performanse, skalabilnost, efikasnost

---

## Izazov: "Kriza kardinalnosti"

### Problem koji je ograničavao rast TSDB-ova

**Kardinalnost:** Broj jedinstvenih vremenskih serija (mjerenje + tagovi)

**Problem:**
- Visoka kardinalnost drastično smanjuje performanse
- Ograničava bogatstvo podataka (manje tagova)
- Povećava kompleksnost upita i pohrane

**Primjer visoke kardinalnosti:**
```
cpu_usage,host=server1,app=frontend,region=eu value=45.2
cpu_usage,host=server2,app=backend,region=us value=76.8
...
```
Svaka kombinacija tagova stvara novu vremensku seriju!

---

## Rješenje: InfluxDB 3.0 arhitektura

### Cilj: Rješavanje krize kardinalnosti

<div class="two-column">
<div>

**Arhitektura bazirana na object storage-u:**
- S3, MinIO, ili kompatibilni sustavi
- Apache Parquet format
- Razdvajanje compute & storage resursa
- Neovisno skaliranje komponenti
</div>
<div>

**Prednosti:**
- Isplativija dugoročna pohrana
- Bolje skaliranje s visoke kardinalnosti
- Jednostavnija integracija s analytics stogom
- Lakehouse kompatibilnost
</div>
</div>

<div class="diagram">
<img alt="influxdb-arch" src="/api/placeholder/700/200" />
</div>

---

## InfluxDB 3.0: SQL kao standard

### Napuštanje proprietary jezika

<div class="two-column">
<div>

**Flux jezik (InfluxDB 2.x):**
```
from(bucket: "metrics")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> mean()
```

**Problemi:**
- Strma krivulja učenja
- Manje resursa i alata
- Nedostatak podrške u ekosustavu
</div>
<div>

**SQL (InfluxDB 3.0):**
```sql
SELECT mean(value) FROM metrics.cpu
WHERE time >= now() - 1h
GROUP BY host;
```

**Prednosti:**
- Industrijski standard
- Šira dostupnost alata i znanja
- Lakša integracija s BI alatima
</div>
</div>

---

## InfluxDB 3.0: FDAP Stack

### Izgrađen na Apache open-source komponentama

**FDAP Akronim:**
- **F**light (Apache Arrow Flight SQL):
  - Efikasan RPC za SQL upite
  - Visoko performansni prijenos podataka

- **D**ataFusion:
  - Rust query engine
  - Koristi Arrow za in-memory obradu

- **A**rrow (Apache Arrow):
  - Brzi in-memory kolumnarni format
  - Standardizirani format između sustava

- **P**arquet (Apache Parquet):
  - Kolumnarni format za object storage
  - Kompatibilan s lakehouse arhitekturama

---

## Apache Parquet: Osnova moderne analitike

<div class="two-column">
<div>

### Karakteristike
- Optimiziran za analitiku
- Kolumnarna pohrana
- Bolja kompresija podataka
- Efikasno čitanje samo potrebnih stupaca
</div>
<div>

### Prednosti za InfluxDB
- Široko korišten format
- Interoperabilnost s Hadoop, Spark, Presto
- Podržava kompleksne tipove podataka
- Omogućuje evoluciju sheme
</div>
</div>

<div class="diagram">
<img alt="parquet-format" src="/api/placeholder/700/200" />
</div>

---

## InfluxDB 3.0: Operativni fokus

### Tri ključna područja izvrsnosti

<div class="two-column">
<div>

### 1. Ingestija
- Brz unos ogromnih količina podataka
- Podaci odmah dostupni za upite
- Optimizirani write path
- Batch i streaming unos
</div>