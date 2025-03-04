---
marp: true
theme: gaia
title: Odabrana poglavlja iz relacijskih baza podataka - 2. predavanje
description: Nikola Balić, Nerelacijske baze podataka - Uvod
paginate: true
---

# Odabrana poglavlja iz relacijskih baza podataka
## Predavanje 2: Uvod u NoSQL baze podataka

Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

[2/15]

---
## Ponovimo gradivo s prošlog predavanja

### Relacijske baze podataka - Temelji

- **Organizacija podataka:** Tablice, redci, stupci
- **Odnosi:** Primarni i strani ključevi, vrste odnosa
- **SQL:** Standardni upitni jezik
- **ACID svojstva:** Atomnost, Konzistentnost, Izolacija, Trajnost
- **Primjena:** Transakcijski sustavi, strukturirani podaci

---
## Zašto nam trebaju NoSQL baze podataka?

### Izazovi modernog doba

- **Volumen podataka:** Eksplozija količine podataka (Big Data)
- **Brzina podataka:** Potreba za brzim upisom i čitanjem (Real-time aplikacije)
- **Raznolikost podataka:** Nestrukturirani i polustrukturirani podaci (Dokumenti, JSON, Video, Slike)
- **Skalabilnost:** Potreba za horizontalnim skaliranjem sustava

---
## Usporedba: Relacijske vs. Nerelacijske baze podataka

| Značajka           | Relacijske baze podataka (SQL) | Nerelacijske baze podataka (NoSQL) |
|--------------------|---------------------------------|------------------------------------|
| Model podataka     | Tablični, strukturirani         | Različiti modeli (dokumentni, graf, ključ-vrijednost...) |
| Shema              | Fiksna shema                   | Fleksibilna ili bez sheme         |
| Skalabilnost       | Vertikalna (uglavnom)          | Horizontalna                       |
| Transakcije        | ACID                           | BASE (Eventual Consistency)       |
| Upitni jezik       | SQL                            | Različiti, specifični za tip       |
| Primjena           | Transakcijske aplikacije        | Web, Big Data, IoT, Mobile       |

---
## Što su to NoSQL baze podataka?

### "Not Only SQL" - Više od SQL-a

- **Alternativni pristupi** upravljanju podacima.
- **Nisu zamjena za relacijske baze podataka,** već nadopuna.
- **Optimizirane za specifične slučajeve upotrebe** gdje relacijske baze podataka nisu idealne.
- **Fokus na skalabilnost, fleksibilnost i performanse.**

---
## Tipovi NoSQL baza podataka - Detaljnije

- **Ključ-vrijednost (Key-Value):**
    - Jednostavna struktura: Ključ (jedinstveni identifikator) -> Vrijednost (bilo koji tip podataka).
    - Primjena: Cache, sesije, jednostavni upiti.
    - Primjeri: Redis, Memcached.
- **Dokumentne:**
    - Pohrana podataka kao dokumenata (JSON, XML).
    - Fleksibilna shema: Svaki dokument može imati različitu strukturu.
    - Primjena: CMS, katalozi proizvoda, mobilne aplikacije.
    - Primjeri: MongoDB, Couchbase.

---
## Tipovi NoSQL baza podataka - Detaljnije (nastavak)

- **Stupčaste (Column-Family):**
    - Podaci organizirani u stupce umjesto redaka.
    - Optimizirane za upite nad velikim skupovima podataka, agregacije.
    - Primjena: Analitika, vremenske serije, Big Data.
    - Primjeri: Cassandra, HBase.
- **Graf:**
    - Pohrana podataka kao čvorova i veza (grafova).
    - Optimizirane za odnose i mreže, analizu povezanosti.
    - Primjena: Društvene mreže, sustavi preporuke, otkrivanje prijevara.
    - Primjeri: Neo4j, Amazon Neptune.

---
## Primjena NoSQL baza podataka - Stvarni svijet

- **E-commerce:** Katalozi proizvoda (dokumentne), košarice (ključ-vrijednost), preporuke (graf).
- **Društvene mreže:** Profili, veze, aktivnosti (graf, dokumentne).
- **Gaming:**  Sesije, profili igrača, brzi pristup podacima (ključ-vrijednost).
- **IoT (Internet of Things):**  Pohrana senzorskih podataka (vremenske serije, stupčaste).
- **Analitika i Big Data:**  Obrada i analiza velikih nestrukturiranih podataka (stupčaste, dokumentne).

---
## Prednosti NoSQL baza podataka - Zašto ih koristiti?

- **Skalabilnost:**  Horizontalno skaliranje, podnošenje velikog opterećenja.
- **Performanse:**  Brzi upis i čitanje podataka, optimizirane za specifične upite.
- **Fleksibilnost sheme:**  Prilagodljivost promjenama, brži razvoj.
- **Agilnost razvoja:**  Pogodnije za brze iteracije i promjene u aplikacijama.
- **Cijena:**  Često open-source i jeftinije za skaliranje od tradicionalnih RDBMS.

---
## Nedostaci NoSQL baza podataka - Na što treba paziti?

- **Konzistentnost:**  Eventual consistency (BASE) umjesto ACID.
- **Složenost upita:**  Nema standardni jezik poput SQL-a, specifični upitni jezici.
- **Alati i zrelost:**  Manje zrele tehnologije, manja zajednica u nekim slučajevima.
- **Sigurnost i zrelost ekosistema:**  Možda manje robusni sigurnosni mehanizmi u usporedbi s RDBMS.
- **Učenje i ekspertiza:**  Potrebno je novo znanje i vještine za rad s NoSQL bazama podataka.

---
## Distribuirane baze podataka - Prelazimo na veći opseg

- **Što su?** Baze podataka koje su raspoređene na **više računala (čvorova)**.
- **Zašto distribucija?**
    - **Skalabilnost:** Podnošenje ekstremno velikog opterećenja.
    - **Visoka dostupnost:** Otpornost na kvarove, kontinuirani rad.
    - **Geografska distribucija:**  Poboljšanje performansi i smanjenje latencije za korisnike diljem svijeta.

---
## CAP Teorem - Trokut kompromisa

- **Consistency (Konzistentnost):** Svi čvorovi vide istu verziju podataka u isto vrijeme.
- **Availability (Dostupnost):** Svaki zahtjev dobiva odgovor, bez garancije da je najnoviji.
- **Partition Tolerance (Tolerancija particije):** Sustav nastavlja raditi čak i ako se izgubi veza između čvorova.

**CAP teorem:**  U distribuiranom sustavu, moguće je istovremeno imati samo **dva od tri** svojstva.

![CAP Teorem](assets/cap-theorem.png)

---
## BASE - Alternativa ACID-u za distribuirane sustave

- **Basically Available (Osnovno dostupno):** Sustav je dostupan većinu vremena.
- **Soft state (Meko stanje):** Stanje sustava se može mijenjati tijekom vremena, bez potrebe za trenutnom konzistencijom.
- **Eventual consistency (Eventualna konzistentnost):**  Sustav će s vremenom postati konzistentan, ali ne odmah.

**BASE:** Fokus na **dostupnosti** i **performansama** u distribuiranom okruženju, uz kompromis u **strogoj konzistentnosti**.

---
## Zaključak - NoSQL i Distribuirane baze podataka

- **Raznolikost izbora:**  NoSQL nudi različite modele podataka za različite potrebe.
- **Skalabilnost i fleksibilnost:**  Ključni benefiti NoSQL i distribuiranih sustava.
- **Kompromisi:**  Nema "čarobnog štapića", treba razumjeti trade-offove (ACID vs. BASE, konzistentnost vs. dostupnost).
- **Praktično iskustvo:**  Kroz kolegij ćemo istražiti konkretne tehnologije i primjere.

---
## Pitanja?

### Otvoreni smo za diskusiju!

- Imate li pitanja o NoSQL bazama podataka?
- Želite li znati više o specifičnim tipovima?
- Kakva su vaša očekivanja od kolegija?

---
## Hvala na Pažnji!

Kontakt informacije:
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---
## Dodatni materijali

### Za one koji žele znati više

- **NoSQL Distilled** - Pramod J. Sadalage, Martin Fowler (Knjiga o NoSQL konceptima)
- **MongoDB: The Definitive Guide** - Kristina Chodorow (Detaljan vodič za MongoDB)
- **Online dokumentacija:**  Redis, Cassandra, Neo4j, MongoDB (i ostalih NoSQL baza podataka)

