---
marp: true
theme: gaia
title: Raspodijeljene i nerelacijske baze podataka - Column-Family Databases
description: Nikola Balić, Column-Family Databases
paginate: true
---

# Column-Family Databases

### Akademska godina 2024/2025
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---
## Uvod u Wide Column Stores

### Big Data izazovi

- **Very Large Databases (VLDB):** 
  - Milijarde redaka
  - Desetci tisuća stupaca
  
- **Zašto su potrebne?**
  - Google, Facebook, Amazon, Yahoo!
  - Skala tradicionalno nezamisliva za relacijske BP
  - Analitike, IoT, senzorski podaci, logovi

---
## Row vs. Column Oriented Storage

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

### Karakteristike

- **Pohranjuje redak po redak**
- **Optimizirano za:**
  - OLTP (Online Transaction Processing)
  - Često pisanje
  - Dohvat kompletnih zapisa
  
- **Prednosti:**
  - Učinkovit unos/ažuriranje zapisa
  - Jednostavno upravljanje transakcijama
  - Efikasno kod dohvaćanja cijelog retka

---
## Column-Oriented Storage

### Karakteristike

- **Pohranjuje stupac po stupac**
- **Optimizirano za:**
  - OLAP (Online Analytical Processing)
  - Analitiku
  - Agregacije (SUM, AVG, COUNT)
  
- **Prednosti:**
  - Bolja kompresija podataka
  - Učinkovitije čitanje podskupa stupaca
  - Brže analitičke operacije

---
## Demonstracija SQL upita 1

### SELECT ime FROM emp WHERE ID_br=666

**Row-oriented execution:**
```
1. Učitaj prvi blok (redci 1001-1003)
2. Provjeri uvjet ID_br=666 za svaki redak
3. Učitaj drugi blok (redci 1004-1006)
4. Provjeri uvjet ID_br=666 za svaki redak
5. Kada se pronađe redak, vrati vrijednost 'ime'
```

**Column-oriented execution:**
```
1. Učitaj stupac ID_br
2. Pronađi pozicije gdje je ID_br=666
3. Učitaj samo te pozicije iz stupca 'ime'
```

---
## Demonstracija SQL upita 2

### SELECT SUM(placa) FROM emp

**Row-oriented execution:**
```
1. Učitaj sve blokove
2. Izvuci vrijednost plaće iz svakog retka
3. Izračunaj sumu
```

**Column-oriented execution:**
```
1. Učitaj samo stupac 'placa'
2. Izračunaj sumu
```

Koje je učinkovitije? 🤔

---
## Terminologija Column-Family baza

### Različiti nazivi, slični koncepti

- **Column Family Databases**
- **Wide Column Stores**
- **Column-oriented Databases**
- **Bigtable Clones**

**Konfuzija:** "Column-oriented" može se odnositi na:
1. Način fizičkog pohranjivanja podataka
2. Logički model višedimenzionalnih ključ-vrijednost parova

---
## Osnovna struktura

### Glavni koncepti

```
┌─────────────────────────────────────────────┐
│ Row Key: "user1"                            │
├─────────────────┬───────────────────────────┤
│ Column Family:  │ Column Family:            │
│ profile         │ posts                     │
├─────────────────┼───────────────────────────┤
│ name: "Ana"     │ 2023-01-01: "Prvi post"   │
│ email: "a@e.com"│ 2023-01-15: "Drugi post"  │
│ age: "29"       │ 2023-02-01: "Treći post"  │
└─────────────────┴───────────────────────────┘
```

- **Sparse Matrix:** Samo popunjena polja su pohranjena
- **Multidimensional Map:** Organizacija kao višestruka mapa

---
## Ključne komponente

### Anatomija Column Family baze podataka

- **Keyspace:** Kontejner za column families (analog sheme)
- **Row Key:** Jedinstveni identifikator retka
- **Column Family:** Grupa povezanih stupaca
- **Column:** Najmanja jedinica pohrane (ime:vrijednost)
- **Timestamp:** Verzioniranje vrijednosti

---
## Row Key

### Dizajn i karakteristike

- **Jedinstveni identifikator** za redak
- **Analogno primarnom ključu** u relacijskoj bazi
- **Omogućuje:** 
  - Brzo pronalaženje podataka
  - Distribuciju podataka (sharding)
  - Sortiranje podataka
  
- **Pohranjen leksikografski** (važno za fizičku organizaciju)

---
## Column Families

### Organizacijska jedinica

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

- **Grupiranje povezanih podataka**
- **Osnovna jedinica administracije**
- **Fizički pohranjeni zajedno** na disku
- **Definirani pri stvaranju tablice,** ali mogu se dodati naknadno

---
## Stupci i vremenske oznake

### Atomska jedinica podataka

**Struktura stupca:**
- **Ime stupca:** Identifikator (string)
- **Vrijednost:** Binarni podatak
- **Vremenska oznaka (timestamp):** Verzioniranje podataka

**Primjeri:**
```
"name:Ana:1577836800"
"name:Ana Horvat:1609459200"  // novija verzija
```

---
## Atomarno čitanje i pisanje

### Transakcijska svojstva

- **Operacije na razini retka su atomarne**
- **Garantirano je da će se svi stupci u retku:**
  - Pročitati zajedno kao jedinica (ili nijedan)
  - Zapisati zajedno kao jedinica (ili nijedan)
  
- **Nema parcijalnih rezultata**
- **Izazov:** Transakcije preko više redaka

---
## Bigtable: Početak column-family DB

### Google's Revolucija

- **Objavljen 2006. godine**
- **Citiran rad:** "Bigtable: A Distributed Storage System for Structured Data"
- **Utjecaj:** Inspirirao mnoge open-source implementacije
- **Cilj:** Skaliranje do petabajta podataka
- **Dizajn:** Optimiziran za nisko-latentno, visoko-propusno okolinu

---
## Google's Motivacija

### Zašto su razvili Bigtable?

- **Polustrukturirani podaci:** 
  - Web indeksi (URL, sadržaj, meta)
  - Korisnički podaci (preference, pretraživanja)
  - Geografski podaci (lokacije, satelitske slike)

- **Zahtjevi:** 
  - Milijarde URL-ova
  - Milijuni korisnika 
  - Terabajtne zbirke

---
## Bigtable Model Podataka

### Trodimenzionalna mapa

```
(row:string, column:string, timestamp:int64) → string
```

**Primjer Web tablice:**
- **Row key:** "com.cnn.www" (obrnuti URL)
- **Column family:** "contents:" (sadržaj stranice)
- **Column family:** "anchor:" (linkovi koji pokazuju na ovu stranicu)
- **Timestamp:** verzije u vremenu

---
## Bigtable Arhitektura

### Distribuirani sustav

![width:800px](https://miro.medium.com/v2/resize:fit:1400/1*8ioFXR_TP_XDBz7VF8rbIw.png)

- **Tablet serveri:** Upravljaju podskupom podataka
- **Master server:** Koordinira tablet servere
- **Chubby:** Distributed lock service za koordinaciju

---
## Apache HBase i Cassandra

### Open-source implementacije

**HBase:**
- Direktna implementacija Bigtable koncepta
- Dio Hadoop ekosustava
- Tight integration s HDFS
- Master-slave arhitektura

**Cassandra:**
- Kombinira koncepte Bigtable i Amazon Dynamo
- Decentralizirana arhitektura (peer-to-peer)
- Linear scalability
- Eventual consistency model

---
## Usporedba Column-Family i Key-Value baza

### Strukturalne razlike

**Key-Value:**
```
key1 → value1
key2 → value2
```

**Column-Family:**
```
row1 → {cf1:col1→val1, cf1:col2→val2, cf2:col1→val3}
row2 → {cf1:col1→val4, cf2:col2→val5}
```

**Column-Family = Key-Value + struktura + vremenske oznake**

---
## Usporedba s Relacijskim BP

### Ključne razlike

| Relacijske BP | Column-Family BP |
|---------------|------------------|
| Fiksna shema | Fleksibilna shema |
| JOIN operacije | Denormalizirani podaci |
| Kompleksna ACID | Eventual consistency |
| Vertikalni scale | Horizontalni scale |
| Upiti po više kriterija | Upiti fokusirani na key |

---
## Smjernice za dizajn

### Best Practices

1. **Denormalizacija umjesto JOIN-ova**
2. **Pažljiv odabir row key-a:**
   - Ravnomjerna distribucija
   - Optimizacija pristupa
3. **Organizacija column families:**
   - Zajedno pohraniti podatke koji se zajedno koriste
4. **Upravljanje verzijama:**
   - Kontrolirati broj verzija
   - Konfigurirati garbage collection
5. **Izbjegavanje kompleksnih podatkovnih struktura**

---
## CASE STUDY: Analiza kupaca

### TransGlobal Transport and Shipping (TGTS)

**Zahtjevi:**
- Praćenje obrazaca narudžbi
- Pohrana povijesnih podataka
- Analiza trendova
- Machine learning nad podacima

**Podaci:**
- Narudžbe dostave
- Evidencije kupaca
- Novinski članci, bilteni industrije
- Povijesni podaci

---
## TGTS: Model podataka

### Column Family dizajn

**Customers (CF):**
- Row key: customer_id
- Columns: name, address, industry, market_category...

**Orders (CF):**
- Row key: order_id
- Columns: customer_id, date, status, total...

**Indices (CF):**
- Orders by customer: customer_id → [order_id1, order_id2...]
- Items by order: order_id → [item_id1, item_id2...]
- Ships by route: route_id → [ship_id1, ship_id2...]

---
## Slučajevi korištenja Column-Family DB

### Idealne primjene

1. **Time-series data:** IoT senzori, logovi, metrike
   
2. **Financijske analize:**
   - Detekcija prijevara
   - Analiza tržišta
   
3. **Personalizacija i preporuke:**
   - Korisnički profili
   - Ponašanja i preference
   
4. **Event sourcing sustavi:**
   - Pohrana povijesti promjena
   - Audit trail

---
## Kada NE koristiti Column-Family BP

### Ograničenja

1. **Kompleksne relacije** između podataka
2. **Česti multi-row upiti** bez pažljivog modeliranja
3. **Aplikacije s brojnim ad-hoc upitima**
4. **Potreba za strogim ACID transakcijama**
5. **Mali volumen podataka**

---
## Zaključak

### Prednosti i nedostaci

**Prednosti:**
- Skalabilnost do petabajta podataka
- Visoke performanse za analitičke upite
- Fleksibilna shema
- Efikasna pohrana velikih količina podataka

**Nedostaci:**
- Veća kompleksnost modeliranja
- Ograničena podrška za transactions
- Nije optimalna za sve tipove upita
- Zahtijeva pažljiv dizajn ključeva

---
## Pitanja?

### Sada je vrijeme za vaša pitanja!

- Nejasnoće oko koncepta column-family?
- Razlike između različitih implementacija?
- Primjeri iz prakse?

---
## Hvala na Pažnji!

Kontakt informacije:
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko