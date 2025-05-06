---
marp: true
theme: gaia
title: Raspodijeljene i nerelacijske baze podataka - Raspodijeljene BP
description: Nikola Balić, Raspodijeljene baze podataka
paginate: true
---

# Napredne tehnike raspodjele podataka

### Akademska godina 2024/2025
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---
## Napredni koncepti raspodjele podataka

S obzirom da smo već pokrili:
- CAP teorem i ograničenja
- BASE vs. ACID modele
- Osnovne karakteristike NoSQL i njihovu skalabilnost
- Razlike u konzistentnosti između modela baza podataka

U ovom predavanju fokusiramo se na napredne provedbene strategije raspodjele podataka.

---
## Kratko ponavljanje: CAP teorem

**Consistency** (Konzistentnost): Svi čvorovi vide iste podatke u istom trenutku

**Availability** (Dostupnost): Sustav odgovara na svaki zahtjev

**Partition Tolerance** (Otpornost na mrežne particije): Sustav nastavlja rad unatoč prekidima komunikacije

**Ključno ograničenje:** Možemo garantirati samo 2 od 3 svojstva

---
## Kratko ponavljanje: BASE vs. ACID

### Različiti modeli konzistentnosti

**ACID** (Atomicity, Consistency, Isolation, Durability):
- Stroga konzistentnost
- Transakcije su atomarne - sve ili ništa
- Svaka transakcija vodi u validno stanje baze
- Tipično za relacijske baze podataka

---

**BASE** (Basically Available, Soft-state, Eventually consistent):
- Visoka dostupnost
- Podaci mogu biti privremeno nekonzistentni
- Konzistentnost se postiže "eventualno"
- Tipično za NoSQL baze podataka

---
## Kratko ponavljanje: Osnovne karakteristike NoSQL

### Prednosti za distribuirane sustave

**Skalabilnost:**
- Horizontalno skaliranje (scale-out)
- Jednostavna distribucija preko više čvorova
- Efikasno dodavanje novih čvorova

---

**Flexibilna shema:**
- Adaptacija na promjenjive poslovne zahtjeve
- Nije potrebna migracija sheme
- Različiti tipovi podataka istovremeno

**Performanse:**
- Optimizirano za specifične tipove podataka
- Manje kompleksnih JOIN operacija
- Mogućnost geo-distribucije podataka

---
## Kratko ponavljanje: Razlike u konzistentnosti

**Relacijske baze (Strong Consistency):**
- Svi čvorovi vide najnovije podatke
- Duža latencija
- Veći utjecaj mrežnih problema

---

**NoSQL pristupi:**
- **Eventual Consistency:** Podaci će biti konzistentni nakon određenog vremena
- **Causal Consistency:** Zadržava uzročno-posljedične veze između operacija
- **Read-your-writes Consistency:** Jamči vidljivost vlastitih pisanja
- **Session Consistency:** Konzistentnost unutar korisničke sesije

**Kompromis:** Veća konzistentnost = manja dostupnost i performanse

---
## Globalni vs. Lokalni pristup raspodjeli

### Konceptualno razlikovanje

**Globalni pristup:**
- Podaci distribuirani prema globalnoj strategiji
- Jedinstven pogled na shemu podataka
- Kompleksna koordinacija čvorova

---

**Lokalni pristup:**
- Autonomni lokalni čvorovi
- Podaci podijeljeni prema lokalnim potrebama
- Manji overhead koordinacije

---
## Federacija podataka vs. distribucija

### Evolucija pristupa

**Federacija:**
- Integracija postojećih autonomnih baza
- Heterogeni sustavi (različiti DBMS-i)
- Virtualni pristup podacima

---

**Distribucija:**
- Raspodjela jedinstvenog logičkog sustava
- Tipično homogeni DBMS-i
- Fizička raspodjela podataka

---
## Napredne strategije fragmentacije

### Poboljšanje performansi upita

1. **Vertikalna fragmentacija:**
   - Razdvajanje po stupcima
   - Paralelno izvođenje projekcija
   - Primjenjivo kod velikih tablica s različitim pristupnim obrascima

---
## Napredne strategije fragmentacije (nastavak)

### Poboljšanje performansi upita

2. **Derivirana horizontalna fragmentacija:**
   - Temeljeno na vezama između entiteta
   - Koordiniran pristup ovisnim entitetima
   - Optimizacija za JOIN operacije

---
## Tehnike replikacije u raspodijeljenim sustavima

### Napredne metode

1. **Multi-master replikacija:**
   - Pisanje moguće na više čvorova
   - Rješavanje konflikata nakon pisanja
   - Potreba za sofisticiranim metodama detekcije i razrješavanja konflikata

---
## Tehnike replikacije u raspodijeljenim sustavima

### Napredne metode

2. **Quorum-based replikacija:**
   - Za pisanje potreban quorum čvorova (>50%)
   - Za čitanje potreban quorum
   - Matematički garantirana konzistentnost

---
## Consensus algoritmi u raspodijeljenim BP

### Temelj koordinacije

1. **Raft algoritam:**
   - Jedan čvor (lider) vodi cijeli proces
   - Jednostavan izbor lidera, kopiranje podataka i sigurnosna pravila
   - Lakši za razumijevanje nego Paxos


---

2. **Paxos:**
   - Klasični consensus algoritam
   - Kompleksnija implementacija
   - Teoretski dokazana korektnost

---
## Consensus algoritmi u raspodijeljenim BP (nastavak)

### Temelj koordinacije

3. **Zookeeper Atomic Broadcast (ZAB):**
   - Koristi ga Apache ZooKeeper
   - Slično Raft algoritmu
   - Koristi se u mnogim distribuiranim sustavima

---
## Bloom filteri u raspodijeljenim BP

```
      ┌────────────────┐
      │  0 1 0 0 1 0 1 │ Bloom filter
      └────────────────┘
               │
               ▼
┌───────┬───────┬───────┬───────┐
│ Shard1│ Shard2│ Shard3│ Shard4│
└───────┴───────┴───────┴───────┘
```

- Kompaktna struktura koja pamti "što je vjerojatno gdje"
- **False positive moguć, false negative nemoguć**
- **Drastično smanjuje nepotrebne mrežne upite**

---
## Particioniranje podataka u praksi

### Napredne tehnike - Hash particioniranje

```sql
-- Primjer hash particioniranja
CREATE TABLE Orders (
    OrderID int,
    CustomerID int,
    OrderDate date,
    ShipCountry varchar(50)
)
PARTITION BY HASH (CustomerID) PARTITIONS 4;
```

---
## Particioniranje podataka u praksi (nastavak)

### Napredne tehnike - List particioniranje

```sql
-- Primjer list particioniranja
CREATE TABLE Sales (
    RegionID int,
    ProductID int,
    SaleDate date,
    Amount decimal(10,2)
)
PARTITION BY LIST (RegionID) (
    PARTITION Europe VALUES IN (1, 2, 3),
    PARTITION Americas VALUES IN (4, 5),
    PARTITION Asia VALUES IN (6, 7, 8)
);
```

---
## Napredni mehanizmi za distribuirane transakcije

### Alternativne metode dvofaznom commit-u

1. **Saga pattern:**
   - Sekvencijalne lokalne transakcije
   - Kompenzacijske akcije za rollback
   - Eventualna konzistentnost

---
## Napredni mehanizmi za distribuirane transakcije (nastavak)

### Alternativne metode dvofaznom commit-u

2. **Optimistički pristup:**
   - Pretpostavka rijetkih konflikata
   - Provjera nakon izvršenja
   - Efikasniji kod niskog konflikta

---

3. **Višefazni commit:**
   - Trofazni commit protokol
   - Robusnost kod mrežnih particioniranja
   - Smanjenje blokiranja resursa

---
## Globalno jedinstveni identifikatori

### Ključni elementi raspodjele

1. **UUID/GUID:**
   - 128-bitni identifikatori
   - Globalno jedinstveni bez koordinacije
   - Veliki storage overhead

---
## Globalno jedinstveni identifikatori

### Ključni elementi raspodjele

2. **Snowflake ID:**
   - Razvijen od strane Twittera
   - Kombinirani timestamp, worker ID, sekvenca
   - Omogućava vremensko sortiranje

3. **ULID (Universally Unique Lexicographically Sortable Identifier):**
   - Kombinirani timestamp i random
   - Base32 enkodiranje

---
## Napredne tehnologije na serverless arhitekturi

### Moderne Cloud BP implementacije

1. **Amazon Aurora Serverless:**
   - Auto-skaliranje kapaciteta
   - Pay-per-use model
   - Kompatibilan s PostgreSQL/MySQL

---
## Moderne Cloud BP implementacije

2. **Azure Cosmos DB Serverless:**
   - Multi-model API
   - Globalna distribucija
   - Automatsko skaliranje

3. **Google Cloud Spanner:**
   - SQL + horizontalno skaliranje
   - Globalno distribuiran
   - Linearno skalabilna baza s ACID jamstvima

---
## Terraformacija baze podataka

### Infrastruktura kao kod za DB

```hcl
# Primjer Terraform konfiguracije za DB cluster
resource "aws_rds_cluster" "distributed_db" {
  cluster_identifier      = "distributed-db"
  engine                  = "aurora-postgresql"
  engine_mode             = "serverless"
  master_username         = "admin"
  master_password         = var.db_password
  backup_retention_period = 7
  preferred_backup_window = "03:00-04:00"

  scaling_configuration {
    auto_pause               = true
    max_capacity             = 256
    min_capacity             = 2
    seconds_until_auto_pause = 300
  }
}
```

---
## Studija slučaja: Globalni e-commerce sustav

### 1. Specifikacija zahtjeva

**Izazovi:**
- Milijuni korisnika diljem svijeta
- 99.99% dostupnost
- Lokalna zakonska regulativa (GDPR, CCPA)
- Varijabilno opterećenje (sezone, promocije)

---

**Ključni pokazatelji:**
- Latencija transakcija < 200ms
- Konzistentnost košarica i narudžbi
- Eventualna konzistentnost kataloga

---
## Arhitekturni pristup

```
                     ┌─────────────────┐
                     │   Load Balancer │
                     └─────────────────┘
                              │
      ┌──────────────────────┼──────────────────────┐
      ▼                       ▼                      ▼
┌──────────┐            ┌──────────┐           ┌──────────┐
│ EU Region│            │ US Region│           │Asia Region│
├──────────┤            ├──────────┤           ├──────────┤
│ Products │◄──Sync────►│ Products │◄──Sync───►│ Products │
│          │            │          │           │          │
│ Users    │            │ Users    │           │ Users    │
│          │            │          │           │          │
│ Orders   │            │ Orders   │           │ Orders   │
└──────────┘            └──────────┘           └──────────┘
```

---
## Studija slučaja: Globalni e-commerce sustav

### 3. Implementacija raspodjele podataka

**Proizvodi:**
- Multi-master replikacija s odgođenom konzistencijom
- Regionalni cache s vremenski ograničenom valjanosti
- Globalni search index (Elasticsearch)

---
## Implementacija raspodjele podataka

**Korisnici:**
- Primarno regija korisnika s read-replica u drugim regijama
- GDPR sharding po geografskom području
- Lokalne kriptirane kopije osobnih podataka

**Narudžbe:**
- Single-master arhitektura po regiji
- Async replikacija za reporting
- Local-first pristup s globalnim ID-jevima

---
## Studija slučaja: Globalni e-commerce sustav

### 4. Mehanizmi konzistentnosti

**Inventory management:**
```javascript
// Pseudokod za rezervaciju inventara
transaction.begin()
try {
  // Lokalno smanjenje
  const inventory = db.inventory.findOne({productId: pid})
  if (inventory.quantity < quantity) throw new Error('Nedovoljno zaliha')

  db.inventory.update(
    {productId: pid},
    {$inc: {quantity: -quantity, reserved: +quantity}}
  )

  // Globalno obavještavanje
  messageQueue.publish('inventory.reserved', {
    productId: pid,
    quantity: quantity,
    regionId: 'eu-west',
    timestamp: Date.now()
  })

  transaction.commit()
} catch (err) {
  transaction.rollback()
  throw err
}
```

---
## Mehanizmi za oporavak od kvarova

**Samoobnavljanje sustava:**
- Automatska detekcija ispada čvorova
- Poluautomatsko povećanje replikatora za pogođenu regiju
- Sustav za bilježenje globalnog stanja (heartbeat)

**Disaster recovery:**
- Point-in-time recovery za sve regije
- Automatsko failover za regionalni ispad
- Topli standby za kritične komponente

---
## Praktični savjeti za implementaciju

### Zaključne napomene

1. **Inkrementalni pristup:**
   - Početi s manjim skupom podataka za distribuciju
   - Dizajnirati za inkrementalnu migraciju
   - Hibridni pristup često je najučinkovitiji

---
## Praktični savjeti za implementaciju

### Zaključne napomene

2. **Testiranje u produkcijskim uvjetima:**
   - Chaos engineering principi
   - Testiranje scenarija ispada čvorova
   - Simulacija mrežnih particioniranja

3. **Fleksibilni dizajn:**
   - Podržavati heterogene storage sustave
   - Pripremiti se za buduće promjene poslovnih zahtjeva
   - Dizajnirati za evoluciju arhitekture
