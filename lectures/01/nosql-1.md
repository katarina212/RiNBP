---
marp: true
theme: gaia
title: Odabrana poglavlja iz relacijskih baza podataka
description: Nikola Balić, Uvodno predavanje
paginate: true
---

# Raspodijeljene i nerelacijske baze podataka

### Akademska godina 2024/2025

Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---
## Što ćemo učiti?

### Istražujemo svijet izvan Relacijskih Baza Podataka

- **Od monolitnih do distribuiranih sustava:**  Zašto nam trebaju drugačiji pristupi?
- **NoSQL revolucija:**  Upoznajemo različite tipove nerelacijskih baza podataka i njihovu primjenu.
- **Praktični primjeri:**  Rad s konkretnim tehnologijama i alatima.
- **Podatkovna znanost i budućnost podataka:** Kako se ove baze podataka uklapaju u širu sliku?

---
## Zašto je ovo važno?

### Podaci posvuda, ali kako ih kontrolirati?

- **Eksplozija podataka:**  Volumen, brzina, raznolikost - izazovi modernog doba.
- **Relacijske baze podataka nisu uvijek najbolje rješenje:**  Skalabilnost, fleksibilnost, performanse.
- **Potražnja na tržištu rada:**  Stručnjaci za NoSQL i distribuirane sustave su iznimno traženi.
- **Budućnost je u raznolikosti:**  Kombiniranje različitih pristupa za optimalna rješenja.

---
## Ciljevi kolegija

### Što ćete steći?

- **Razumijevanje:** Koncepata i arhitektura raspodijeljenih i nerelacijskih baza podataka.
- **Kompetencije:**  Praktične vještine rada s odabranim NoSQL tehnologijama.
- **Kritičko razmišljanje:**  Sposobnost odabira pravog tipa baze podataka za specifični problem.
- **Priprema za budućnost:**  Znanja i vještine relevantne za moderno podatkovno inženjerstvo i podatkovnu znanost.

---
## Organizacija kolegija

### Kako ćemo raditi?

- **Predavanja:**  Teorijske osnove, koncepti, primjeri iz prakse.
- **Laboratorijske vježbe:**  Praktični rad, implementacija, eksperimentiranje.
- **Projekt:**  Samostalna primjena stečenog znanja na konkretnom problemu.
- **Tekuće praćenje znanja:**  Kolokviji, projekt, usmeni ispit.
- **E-learning:**  Materijali, obavijesti, komunikacija.

---
## Obveze studenata (službene)

- Ispitu možete pristupiti **ako ste ispunili sve obveze**
- **Uvjeti za potpis i pristup polaganju ispita:**
    - uredno pohađanje predavanja (max. 30% izostanaka ili 4 puta)
        - *ne treba donositi ispričnice od liječnika*
    - uredno pohađanje svih laboratorijskih vježbi
        - *(riješeni svi zadaci u predviđenim rokovima)*

---
## Detalji o kolegiju

### Sve informacije na jednom mjestu

- **E-learning sustav:** [https://elearning.pmfst.unist.hr/](https://elearning.pmfst.unist.hr/)
    - Kolegij: **Raspodijeljene i nerelacijske baze podataka**
    - Kratica: **RINBP25**
    - Lozinka: **RINBP25**

---
## Elementi za tekuće praćenje znanja 1/2

- **Pismeni dio ispita:**
    - **1.dio**
        - SQL
        - kolokvij se odnosi na gradivo koje se do tada obrađivalo na vježbama (boduje se na ljestvici 0-100%)
    - **2.dio**
        - NoSQL
        - Odrađivanje svih obveza na vježbama
        - Samostalna izrada projekta (NoSQL baze podataka) na odabranu temu

---
## Elementi za tekuće praćenje znanja 2/2

- **Usmeni ispit**
    - **Uvjet za izlazak:** položen pismeni ispit
    - **Obrana projekta**
    - **Ocjena se kreira prema:**
        - Ocjeni kolokvija - 1.dio
        - Projektu (složenosti i obrani projekta) – 2.dio

---
## Ispitni termini

- Za izlazak na ispit student mora odraditi **sve predviđene obveze**
    - Dolasci, odrađivanje vježbi u zadanim rokovima
- Ispit se može polagati **najviše 4 puta** u jednoj akademskoj godini
    - 4. put student može polagati komisijski ispit pred ispitnim povjerenstvom od tri člana
    - na komisijskom ispitu student polaže i pismeni i usmeni dio ispita bez obzira na rezultate kolokvija i eventualnu položenost pismenog dijela ispita

---
## Baze podataka

- **Baza podataka** je organizirana zbirka podataka spremljena prema specifičnim pravilima.
- **Podatak**: skup vrijednosti kvalitativnih ili kvantitativnih svojstava koji opisuju određeni objekt, fenomen...
- **Piramida**
    - „DIKW (data, information, knowledge, wisdom)"

```
Mudrost
Znanje
Informacija
Podatak
```

---
## Primjer

- 38
- 38°C
- Povišena tjelesna temperatura
- Ostajem kući

```
Mudrost
Znanje
Informacija
Podatak
```
---
## Podatak i informacija

- Podatak je predstavljen brojem, znakom, slikom, zvukom ili nekim drugim oblikom zapisa, u obliku koji osigurava pristup, pohranu, obradu ili prijenos podatka posredstvom čovjeka ili računala.
- **Podatak sam po sebi nema značenje.**
- **Tek nakon obrade podatak poprima značenje i postaje informacija.**

---
## Razvoj područja NoSQL baza podataka

- **Rast i raznolikost podataka:** Tradicionalne relacijske baze podataka nisu uvijek optimalne za sve vrste podataka i opterećenja.
- **Web 2.0 i Big Data:** Potreba za skalabilnijim i fleksibilnijim rješenjima.
- **Cloud computing:**  Omogućuje lakšu distribuciju i skaliranje baza podataka.
- **Pojava novih paradigmi:**  Ključ-vrijednost, dokumentne, graf, stupčaste baze podataka.

---
## Karakteristike NoSQL baza podataka

- **Nisu relacijske:** Ne koriste tablice i SQL u tradicionalnom smislu.
- **Shema-manje (Schema-less):** Fleksibilnost u strukturi podataka, nema fiksnih shema.
- **Skalabilnost:** Dizajnirane za horizontalno skaliranje i rad s velikim količinama podataka.
- **Visoka dostupnost:** Otpornost na greške i osiguravanje kontinuiranog rada.
- **Raznolikost modela podataka:** Prilagođene različitim potrebama i tipovima podataka.

---
## Tipovi NoSQL baza podataka

- **Ključ-vrijednost (Key-Value):** Jednostavne, brze, skalabilne (Redis, Memcached).
- **Dokumentne:** Pohrana podataka u obliku dokumenata (JSON, XML), fleksibilne sheme (MongoDB, Couchbase).
- **Stupčaste (Column-Family):** Optimizirane za upite nad velikim skupovima podataka (Cassandra, HBase).
- **Graf:** Pohrana i analiza povezanih podataka (Neo4j, Amazon Neptune).
- **Vektorske baze podataka:** Optimizirane za pohranu i pretraživanje vektorskih ugradnji (Pinecone, Weaviate).

---
## Prednosti NoSQL baza podataka

- **Skalabilnost i performanse:**  Bolje performanse i skaliranje za specifične slučajeve upotrebe.
- **Fleksibilnost:**  Prilagodljivost promjenjivim zahtjevima i strukturama podataka.
- **Razvojna brzina:**  Brži razvoj aplikacija zbog fleksibilnosti shema.
- **Pogodnost za određene tipove podataka:**  Bolje performanse za dokumente, grafove, itd.

---
## Nedostaci NoSQL baza podataka

- **Složenost konzistentnosti:**  Teže osigurati ACID svojstva u distribuiranom okruženju.
- **Manje zrele tehnologije:**  Relativno novije tehnologije u usporedbi s relacijskim bazama podataka.
- **Raznolikost:**  Veliki broj različitih NoSQL sustava, teže standardizirati znanje.
- **Nema standardni jezik:**  Nema jedinstvenog jezika poput SQL-a, svaki sustav ima svoj upitni jezik ili API.

---
## ACID Transakcije

- **Atomicity (Atomičnost):** Transakcija se izvršava u cijelosti ili se ne izvršava uopće ("sve ili ništa").
- **Consistency (Konzistentnost):** Transakcija održava integritet baze podataka, prelazeći iz jednog valjanog stanja u drugo.
- **Isolation (Izolacija):**  Transakcije se izvršavaju izolirano jedna od druge, bez međusobnog ometanja.
- **Durability (Trajnost):** Kada je transakcija potvrđena (commit), promjene su trajne i neće se izgubiti ni u slučaju pada sustava.

---
## Primjeri primjene NoSQL baza podataka

- **Web aplikacije i mobilne aplikacije:**  Skalabilnost, brzina, fleksibilnost.
- **Big Data i analitika:**  Obrada velikih količina nestrukturiranih podataka.
- **Internet of Things (IoT):**  Pohrana podataka s senzora i uređaja.
- **Društvene mreže:**  Upravljanje grafovima veza i interakcija.
- **Gaming industrija:**  Brzi pristup podacima za online igre.

---
## Vektorske baze podataka

- **Vektorske ugradnje?** Numerički prikazi podataka (tekst, slike, zvuk) u višedimenzionalnom prostoru.
- **Zašto su važne?**
    - **Sličnost pretraživanja:** Pronalaženje sličnih podataka na temelju vektorske udaljenosti.
    - **Umjetna inteligencija i strojno učenje:** Ključne za aplikacije poput prepoznavanja slika, obrade prirodnog jezika, sustava preporuke.
- **Primjeri:** Pinecone, Weaviate, Milvus, Chroma, Qdrant

---
## Zaključak

- NoSQL baze podataka **nisu zamjena** za relacijske baze podataka, već **nadopuna**.
- Pravi izbor baze podataka ovisi o **specifičnim zahtjevima** projekta.
- Razumijevanje NoSQL paradigmi je **ključno** za moderne programere i podatkovne stručnjake.
- Kolegij će vas **pripremiti za rad** s raznolikim sustavima za upravljanje podacima.

---
## Pitanja?

### Sada je vrijeme za vaša pitanja!

- Nejasnoće oko organizacije kolegija?
- Zainteresiranosti i očekivanja?
- Bilo što drugo vezano za kolegij?

---
## Hvala na Pažnji!

Kontakt informacije:
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko