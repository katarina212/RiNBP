---
marp: true
theme: gaia
title: Raspodijeljene i nerelacijske baze podataka - NoSQL Fundamentals
description: Nikola Balić, NoSQL Fundamentals
paginate: true
---

# NoSQL Database Fundamentals

### Akademska godina 2024/2025
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---
## Zašto NoSQL?

### Ključni razlozi za rast NoSQL baza podataka

- **Skalabilnost**
- **Cijena**
- **Fleksibilnost**
- **Dostupnost**

---
## Skalabilnost

### Vertikalna vs. Horizontalna

- **Scale Up:** 
  - Dodavanje resursa postojećem poslužitelju
  - Procesori, memorija, diskovi, mrežne kartice
  - Ograničenja fizičkog hardvera
  - Skupo

- **Scale Out:**
  - Dodavanje novih poslužitelja u klaster
  - Fleksibilnije
  - Teoretski neograničeno
  - NoSQL je dizajniran za ovaj pristup

---
## Izazovi vertikalnog skaliranja

### Problemi Scale Up pristupa

```
                   ┌─────────────┐
                   │             │
                   │   Server    │
                   │             │
                   └─────────────┘
                          ↓
┌─────────────────────────────────────────────┐
│                                             │
│              Veći server                    │
│                                             │
└─────────────────────────────────────────────┘
```

- **Tehnička ograničenja:** Maksimum RAM, CPU, disk
- **Prekidi u radu:** Nadogradnja često zahtijeva downtime
- **Eksponencijalni troškovi:** Cijena raste disproporcionalno

---
## Prednosti horizontalnog skaliranja

### Benefiti Scale Out pristupa

```
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│ Server 1│  │ Server 2│  │ Server 3│  │ Server 4│
└─────────┘  └─────────┘  └─────────┘  └─────────┘
      ↓            ↓            ↓            ↓
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│ Server 1│  │ Server 2│  │ Server 3│  │ Server 4│  │ Server 5│
└─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘
```

- **Linearna skalabilnost:** Dodavanje resursa prema potrebi
- **Visoka dostupnost:** Redundancija podataka
- **Kontinuirani rad:** Održavanje bez prekida usluge
- **NoSQL prednost:** Minimalne intervencije DBA

---
## Troškovi i licenciranje

### Ekonomski faktori

- **Relacijske baze podataka:**
  - Visoke cijene licenci (Oracle, MS SQL Server)
  - Različiti modeli licenciranja (po CPU, korisniku, poslužitelju)
  - Predvidljivi troškovi uz predvidljivo opterećenje

- **NoSQL baze podataka:**
  - Mnoge su open-source (MongoDB, Cassandra, Redis)
  - Pay-as-you-go modeli u cloudu
  - Prilagodljivi troškovi za varijabilno opterećenje

---
## Scenarij: Web aplikacija s promjenjivim opterećenjem

### Ekonomska prednost NoSQL-a

```
Promet                                     ▲
                           ▲               │
                           │               │
                           │               │
                   ▲       │       ▲       │
         ▲         │       │       │       │
         │         │       │       │       │
─────────────────────────────────────────────▶
         Jan      Apr      Jul     Oct     Dec
```

- **Sezonski vrhunci:** Praznici, promocije, događaji
- **Teško predviđanje:** Budući rast, viralnost
- **Prednost NoSQL cloud rješenja:** Plaćanje samo za korištene resurse

---
## Fleksibilnost sheme

### Rigidni vs. prilagodljivi model

- **Relacijske baze podataka:**
  - Fiksna shema (tablice, stupci)
  - ALTER TABLE operacije mogu biti skupe
  - Migracije često zahtijevaju downtime
  - Idealne za stabilne, dobro definirane podatke

- **NoSQL baze podataka:**
  - Schemaless ili fleksibilna shema
  - Dinamičko dodavanje novih polja
  - Brza prilagodba promjenama poslovnih zahtjeva

---
## Primjer: E-commerce katalog proizvoda

### Evolucija sheme podataka

**Relacijski pristup:**
```sql
-- Inicijalno
CREATE TABLE Products (
  ID INT, Name VARCHAR(100), Price DECIMAL(10,2)
);

-- Kasnije dodavanje polja
ALTER TABLE Products ADD COLUMN Weight DECIMAL(10,2);
ALTER TABLE Products ADD COLUMN Dimensions VARCHAR(50);
```

**NoSQL pristup (MongoDB):**
```javascript
// Inicijalno
db.products.insert({ name: "Laptop", price: 999.99 });

// Kasnije
db.products.insert({ 
  name: "Monitor", 
  price: 299.99, 
  weight: 5.4, 
  dimensions: "24x18x9",
  features: ["HDR", "4K", "HDMI 2.1"]
});
```

---
## Dostupnost podataka

### Očekivanja korisnika u digitalnom svijetu

- **24/7 pristup:** Korisnici očekuju stalnu dostupnost
- **Globalna publika:** Različite vremenske zone
- **Posljedice nedostupnosti:** 
  - Gubitak prihoda
  - Narušavanje povjerenja korisnika
  - Negativni PR

---
## Dostupnost u NoSQL bazama podataka

### Arhitektura za visoku dostupnost

```
         ┌─────────┐     ┌─────────┐     ┌─────────┐
         │ Node 1  │     │ Node 2  │     │ Node 3  │
         └─────────┘     └─────────┘     └─────────┘
               │               │               │
               └───────────────┼───────────────┘
                               │
                         ┌─────────────┐
                         │  Klijent    │
                         └─────────────┘
```

- **Distribuirani dizajn:** Podaci replicirani preko više čvorova
- **Automatski failover:** Ako jedan čvor padne, drugi preuzimaju
- **No Single Point of Failure:** Redundancija na više razina

---
## Upravljanje podacima u raspodijeljenim bazama

### Ključni zahtjevi

- **Trajna pohrana:** Podaci moraju opstati usprkos kvarovima
- **Konzistentnost:** Svi čvorovi moraju vidjeti iste podatke
- **Dostupnost:** Sustav mora odgovarati na zahtjeve

---
## Konzistentnost podataka

### Primjer distribucije sredstava

```
Alice ima 1000€ na računu

         ┌─────────┐          ┌─────────┐
         │ Server 1│          │ Server 2│
         │ Stanje: │          │ Stanje: │
         │  1000€  │          │  1000€  │
         └─────────┘          └─────────┘
                ↓                  ↑
                └──── Replikacija ─┘

Ako Alice podigne 200€, oba servera moraju ažurirati stanje na 800€
```

- **Izazov relacijskih baza:** Distribucija transakcija
- **Izazov NoSQL baza:** Balansiranje konzistentnosti i dostupnosti

---
## Two-Phase Commit

### Osiguravanje konzistentnosti u distribuiranim sustavima

```
   ┌────────────┐             ┌────────────┐
   │ Koordinator│             │ Sudionici  │
   └────────────┘             └────────────┘
         │                          │
         │─── 1. Pripremi se ──────▶│
         │                          │
         │◀── 2. Spreman/Odbijen ───│
         │                          │
         │─── 3. Commit/Rollback ──▶│
         │                          │
         │◀── 4. Potvrda ───────────│
```

- **Faza 1:** Koordinator pita sve čvorove jesu li spremni za commit
- **Faza 2:** Ako su svi spremni, izvršava se commit; inače rollback

---
## Eventual Consistency

### Kompromis za bolje performanse

```
Alice ima 1000€, podiže 200€ na Serveru 1

   ┌─────────┐               ┌─────────┐
   │ Server 1│               │ Server 2│
   │ Stanje: │               │ Stanje: │
   │   800€  │               │  1000€  │
   └─────────┘               └─────────┘
         │                        │
         │                        │
         └─── Replikacija (async)─┘
```

- **Privremena nekonzistentnost:** Server 2 nije odmah ažuriran
- **Eventulna konzistentnost:** Sustav će postati konzistentan
- **Prednost:** Brži odziv, veća dostupnost

---
## CAP teorem

### Fundamentalni kompromis

![bg right:50% 80%](https://miro.medium.com/v2/resize:fit:1400/1*rxTP-_STj-QRDt1X9fdVlA.png)

- **Consistency (Konzistentnost)**
- **Availability (Dostupnost)**
- **Partition Tolerance (Otpornost na particioniranje)**

"U distribuiranom sustavu možete imati samo dva od tri svojstva"

---
## CAP teorem u praksi

### Primjer: A+P (AP sustavi)

```
   ┌─────────┐   Mrežna     ┌─────────┐
   │ Server 1│   particija  │ Server 2│
   │ Stanje: │   (prekid)   │ Stanje: │
   │   800€  │ X─────────X  │  1000€  │
   └─────────┘              └─────────┘
```

- **Dostupnost:** Sustav nastavlja odgovarati na zahtjeve
- **Partition Tolerance:** Sustav nastavlja raditi usprkos prekidu
- **Nekonzistentnost:** Server 1 i Server 2 prikazuju različite podatke

---
## CAP teorem u praksi

### Primjer: C+P (CP sustavi)

```
   ┌─────────┐   Mrežna     ┌─────────┐
   │ Server 1│   particija  │ Server 2│
   │ Stanje: │   (prekid)   │ Stanje: │
   │   ???   │ X─────────X  │   ???   │
   └─────────┘              └─────────┘
```

- **Konzistentnost:** Sustav osigurava da svi čvorovi vide iste podatke
- **Partition Tolerance:** Sustav nastavlja raditi usprkos prekidu
- **Nedostupnost:** Neki zahtjevi će biti odbijeni do ponovnog spajanja

---
## ACID vs. BASE

### Dva pristupa konzistentnosti podataka

**ACID (Relacijske BP):**
- **Atomicity:** Transakcija je sve ili ništa
- **Consistency:** Transakcija prelazi iz jednog valjanog stanja u drugo
- **Isolation:** Transakcije su izolirane jedna od druge
- **Durability:** Potvrđene promjene su trajne

**BASE (NoSQL BP):**
- **Basically Available:** Sustav odgovara na većinu zahtjeva
- **Soft state:** Stanje sustava može se mijenjati s vremenom
- **Eventually consistent:** Sustav će s vremenom postati konzistentan

---
## BASE: Basically Available

### Dostupnost kao prioritet

- **Načelna dostupnost:** Sustav je uvijek dostupan za upite
- **Parcijalni kvarovi:** Dio sustava može biti nedostupan
- **Primjer:** NoSQL baza na 10 poslužitelja; ako jedan otkaže, 90% upita i dalje uspijeva

```
  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
  │Node 1│  │Node 2│  │Node 3│  │Node 4│  │Node 5│
  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘
  
  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
  │Node 6│  │Node 7│  │Node 8│  │Node 9│  │Node10│
  └──────┘  └──X───┘  └──────┘  └──────┘  └──────┘
               ↑
            Kvar
```

---
## BASE: Soft State

### Fleksibilnost stanja sustava

- **Promjenjivo stanje:** Stanje sustava može se mijenjati s vremenom
- **"Istjecanje" podataka:** Podaci mogu postati nevažeći ako se ne osvježe
- **Kontinuirano ažuriranje:** Noviji podaci zamjenjuju stare
- **Optimistički pristup:** Pretpostavka da će ažuriranja rijetko stvarati konflikte

---
## BASE: Eventually Consistent

### Naknadna konzistentnost

- **Privremena nekonzistentnost:** Kratki periodi kada različiti čvorovi vide različite podatke
- **Mehanizmi replikacije:** Osiguravaju da će svi čvorovi eventualno imati iste podatke
- **Brzina synchronizacije:** Ovisi o mrežnoj latenciji, opterećenju sustava i drugim faktorima
- **Trade-off:** Žrtvovanje trenutne konzistentnosti za veću dostupnost i performanse

---
## Optimizacija izbora baze podataka

### Kako odabrati pravu bazu podataka?

1. **Analiza zahtjeva aplikacije:**
   - Potrebna konzistentnost?
   - Važnost dostupnosti?
   - Očekivano opterećenje?
   
2. **Tipovi podataka i upita:**
   - Strukturirani vs. polustrukturirani podaci
   - Jednostavni upiti vs. kompleksni joins
   
3. **Skalabilnost i budući rast:**
   - Predviđeni rast podataka
   - Očekivana brzina rasta korisnika

---
## NoSQL tipovi baza podataka

### Glavni modeli podataka

- **Ključ-vrijednost:** Jednostavno mapiranje (Redis, DynamoDB)
- **Dokumentne:** Fleksibilni JSON dokumenti (MongoDB, Couchbase)
- **Stupčaste:** Optimizirane za stupce podataka (Cassandra, HBase)
- **Graf:** Čvorovi i veze (Neo4j, JanusGraph)
- **Vektorske:** Za duboko učenje (Pinecone, Weaviate)

---
## Ključ-vrijednost baze podataka

### Jednostavnost i brzina

```
┌─────────────┬────────────────────────┐
│    Ključ    │       Vrijednost       │
├─────────────┼────────────────────────┤
│ user:1001   │ {"name": "Ana Horvat"} │
├─────────────┼────────────────────────┤
│ session:xyz │ {"valid_until": "..."} │
├─────────────┼────────────────────────┤
│ counter:hit │ 42768                  │
└─────────────┴────────────────────────┘
```

- **Jednostavnost:** Parovi ključ-vrijednost
- **Performanse:** Vrlo brze operacije dohvata po ključu
- **Primjene:** Sesije, keš, brojači, postavke

---
## Dokumentne baze podataka

### Fleksibilnost strukture

```json
{
  "_id": "123",
  "name": "Ana Horvat",
  "email": "ana@example.com",
  "orders": [
    { "id": "ord1", "items": ["laptop", "mouse"], "total": 1200 },
    { "id": "ord2", "items": ["keyboard"], "total": 150 }
  ],
  "address": {
    "street": "Vukovarska 123",
    "city": "Split"
  }
}
```

- **Ugniježđeni podaci:** Kompleksna struktura u jednom dokumentu
- **Fleksibilna shema:** Dokumenti iste kolekcije mogu imati različitu strukturu
- **Upiti po atributima:** Moguće pretraživanje po svim poljima

---
## Stupčaste baze podataka

### Optimizacija za analitiku

```
Column Family: "user_profile"
┌────┬────────┬────────┬───────┬─────────┐
│ ID │  Name  │ Email  │ City  │ Country │
├────┼────────┼────────┼───────┼─────────┤
│ 1  │ Ana    │ a@e.com│ Split │ Croatia │
│ 2  │ Marko  │ m@e.com│ Zagreb│ Croatia │
└────┴────────┴────────┴───────┴─────────┘

Column Family: "user_orders"
┌────┬───────────┬────────────┐
│ ID │ Order_Ids │ Last_Order │
├────┼───────────┼────────────┤
│ 1  │ [5,8,12]  │ 2023-06-12 │
│ 2  │ [3,7]     │ 2023-05-30 │
└────┴───────────┴────────────┘
```

- **Column families:** Grupiranje povezanih stupaca
- **Rijetke matrice:** Efikasna pohrana za milijune stupaca
- **Analitičke operacije:** Optimizirane za agregacije po stupcima

---
## Graf baze podataka

### Mreže povezanih podataka

```
    ┌───────┐       FOLLOWS      ┌───────┐
    │ Ana   │─────────────────→ │ Marko │
    └───────┘                   └───────┘
        ↑                           │
        │                           │
    FOLLOWS                      FOLLOWS
        │                           │
        │                           ↓
    ┌───────┐        LIKES       ┌───────┐
    │ Ivana │←─────────────────  │ Petar │
    └───────┘                    └───────┘
```

- **Čvorovi i veze:** Prirodno modeliranje odnosa
- **Optimizacija putanja:** Brzo pretraživanje povezanosti
- **Primjene:** Društvene mreže, preporuke, znanje, prijevare

---
## Zaključak

### Glavni takeaways

1. **NoSQL nije zamjena, već nadopuna relacijskih baza**
2. **Razlozi za NoSQL: skalabilnost, cijena, fleksibilnost, dostupnost**
3. **CAP teorem: kompromis između konzistentnosti i dostupnosti**
4. **BASE vs. ACID: različiti pristupi konzistentnosti**
5. **Odabir baze podataka ovisi o specifičnim zahtjevima aplikacije**

---
## Pitanja?

### Sada je vrijeme za vaša pitanja!

- Nejasnoće oko koncepata?
- Primjeri iz prakse?
- Specifični scenariji primjene?

---
## Hvala na Pažnji!

Kontakt informacije:
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko