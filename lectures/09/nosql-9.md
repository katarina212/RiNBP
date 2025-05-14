---
marp: true
theme: gaia
title: Raspodijeljene i nerelacijske baze podataka - Redis
description: Nikola Balić, Redis
paginate: true
---

# Redis i Key-Value Stores

### Akademska godina 2024/2025
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---
## Što je Redis?

### REmote DIctionary Server

- **In-memory baza podataka**
- **Key-value store**
- **Visoke performanse**
- **Podržava različite tipove podataka**
- **Često korišten kao cache**

---
## Redis vs MongoDB

### Različiti NoSQL pristupi

| Redis | MongoDB |
|-------|---------|
| In-memory | Disk-based |
| Key-value | Document |
| Jednostavnija struktura | Kompleksna struktura |
| Cache/Queue | Trajna pohrana |
| Brži | Veći kapacitet |

---
## Redis Tipovi Podataka

### Osnovni tipovi

- **Strings:** Najjednostavniji tip
- **Lists:** Linked lists
- **Sets:** Neuređeni skupovi
- **Sorted Sets:** Uređeni skupovi
- **Hashes:** Kolekcije key-value parova
- **Streams:** Append-only log strukture

---
## Redis Strings

### Osnovne operacije

```bash
# Postavljanje vrijednosti
SET user:1:name "Ana Horvat"
SET user:1:age "25"

# Dohvaćanje vrijednosti
GET user:1:name

# Inkrementiranje
SET counter 1
INCR counter
GET counter  # vraća "2"

# Postavljanje s istekom
SETEX session:token 3600 "abc123"
```

---
## Redis Lists

### Rad s listama

```bash
# Dodavanje na početak/kraj liste
LPUSH messages "Poruka 1"
RPUSH messages "Poruka 2"

# Dohvaćanje elemenata
LRANGE messages 0 -1

# Implementacija queue
LPUSH tasks "task:1"
RPOP tasks  # uzima zadnji element

# Implementacija stack
LPUSH stack "item:1"
LPOP stack  # uzima prvi element
```

---
## Redis Sets

### Neuređeni skupovi

```bash
# Dodavanje članova
SADD online:users "user:1"
SADD online:users "user:2"

# Provjera članstva
SISMEMBER online:users "user:1"

# Presjek skupova
SINTER online:users premium:users

# Unija skupova
SUNION team:a team:b
```

---
## Redis Sorted Sets

### Uređeni skupovi s bodovima

```bash
# Dodavanje s bodovima
ZADD leaderboard 100 "Ana"
ZADD leaderboard 95 "Marko"
ZADD leaderboard 98 "Ivan"

# Dohvaćanje ranga
ZRANK leaderboard "Ana"

# Top N igrača
ZREVRANGE leaderboard 0 2 WITHSCORES
```

---
## Redis Hashes

### Strukture objekata

```bash
# Postavljanje hash polja
HSET user:1 name "Ana Horvat" age "25" city "Split"

# Dohvaćanje jednog polja
HGET user:1 name

# Dohvaćanje svih polja
HGETALL user:1

# Inkrementiranje numeričkog polja
HINCRBY user:1 visits 1
```

---
## Redis Streams

### Event Sourcing i Messaging

```bash
# Dodavanje u stream
XADD sensors * temperature 25.5 humidity 60

# Čitanje iz streama
XREAD COUNT 2 STREAMS sensors 0

# Consumer grupe
XGROUP CREATE sensors group1 0
XREADGROUP GROUP group1 consumer1 COUNT 1 STREAMS sensors >
```

---
## Redis Pub/Sub

### Messaging sustav

```bash
# Pretplata na kanal
SUBSCRIBE news

# Objava na kanal
PUBLISH news "Nova vijest!"

# Pretplata na pattern
PSUBSCRIBE news:*

# Objava na specifični kanal
PUBLISH news:sport "Sportska vijest!"
```

---
## Redis kao Cache

### Caching strategije

```bash
# Cache-Aside Pattern
GET cache:user:1
# Ako nije u cacheu:
SET cache:user:1 "user_data"
EXPIRE cache:user:1 3600

# Write-Through
SET cache:user:1 "new_data"
# Istovremeno ažuriranje baze

# Cache Invalidation
DEL cache:user:1
```

---
## Redis Transactions

### Atomske operacije

```bash
# Početak transakcije
MULTI

# Naredbe u transakciji
SET user:1:balance 100
DECRBY user:1:balance 20
INCRBY user:2:balance 20

# Izvršavanje transakcije
EXEC

# Poništavanje transakcije
DISCARD
```

---
## Redis Persistence

### Opcije trajne pohrane

- **RDB (Redis Database):**
  - Point-in-time snapshots
  - Konfigurabilan interval
  - Manji overhead

- **AOF (Append Only File):**
  - Write-ahead log
  - Veća durability
  - Veći overhead

---
## Redis Cluster

### Distribuirani Redis

```bash
# Kreiranje clustera
redis-cli --cluster create \
  127.0.0.1:7000 127.0.0.1:7001 \
  127.0.0.1:7002 127.0.0.1:7003 \
  --cluster-replicas 1

# Provjera cluster info
CLUSTER INFO

# Provjera slotova
CLUSTER SLOTS
```

---
## Redis Security

### Osnovne sigurnosne prakse

- **Autentikacija:**
  ```bash
  CONFIG SET requirepass "complex_password"
  AUTH "complex_password"
  ```

- **SSL/TLS Encryption**
- **Network Security**
- **Access Control Lists (ACL)**

---
## Redis Use Cases

### Česti scenariji korištenja

- **Session Management**
- **Caching**
- **Real-time Analytics**
- **Queuing**
- **Rate Limiting**
- **Leaderboards**
- **Real-time Messaging**

---
## Praktični Primjer: Rate Limiting

### Implementacija

```bash
# Inkrementiranje brojača za IP
INCR "rate:ip:${ip}"
# Postavljanje isteka
EXPIRE "rate:ip:${ip}" 60

# Složeniji primjer s vremenskim prozorom
MULTI
ZADD "requests:${ip}" ${timestamp} ${request_id}
ZREMRANGEBYSCORE "requests:${ip}" 0 ${timestamp-60000}
ZCARD "requests:${ip}"
EXEC
```

---
## Redis Monitoring

### Praćenje performansi

```bash
# Info o memoriji
INFO memory

# Statistika naredbi
INFO stats

# Latency monitoring
LATENCY DOCTOR

# Slow log
SLOWLOG GET 10
```

---
## Redis Best Practices

### Optimizacija i održavanje

- **Memory Management:**
  - Praćenje memory usage
  - Implementacija eviction policies
  - Optimizacija struktura podataka

- **Performance:**
  - Pipelining naredbi
  - Izbjegavanje blokirajućih operacija
  - Pravilno particioniranje podataka

---
## Praktična Vježba

### Implementacija Chat sustava

1. **User Sessions:**
   - HSET za user podatke
   - EXPIRE za session timeout

2. **Chat Rooms:**
   - SADD za članove sobe
   - PUBLISH za poruke

3. **Message History:**
   - LPUSH za nove poruke
   - LTRIM za ograničenje povijesti

---
## Zaključak

### Kada koristiti Redis?

- **High-Speed Caching**
- **Session Management**
- **Real-time Analytics**
- **Message Broker**
- **Leaderboards/Counting**

---
## Pitanja?

### Sada je vrijeme za vaša pitanja!

- Nejasnoće oko Redisa?
- Use-case scenariji?
- Best practices?

---
## Hvala na Pažnji!

Kontakt informacije:
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko