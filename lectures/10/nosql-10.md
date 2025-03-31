---
marp: true
theme: default
paginate: true
---

# Raspodijeljene i nerelacijske baze podataka
# Graf baze podataka

IZVOR: Sullivan, D. (2015). NoSQL for mere mortals. Addison-Wesley Professional

---

## Sadržaj

- Uvod u graf baze podataka
- Teorija grafova i ključni koncepti
- Vrste grafova i njihova primjena
- Svojstva grafova i analiza
- Dizajniranje graf baza podataka
- Upitni jezici za graf baze
- Primjeri korištenja i implementacije

---

## Zašto su grafovi važni?

Graf baze podataka idealne su za sljedeće slučajeve:
- Modeliranje podataka u kemiji i biologiji
- Društvene mreže
- Web (povezanost stranica)
- Hijerarhijski podaci
- Mreže (prometne, komunikacijske, itd.)

![bg right:40% 80%](https://db-engines.com/en/ranking/graph+dbms)

---

## Graf baze podataka

- Temelje se na teoriji grafova
- Specijalizirane za analizu veza i poveznica između entiteta
- Primjenjive u mnogim područjima

**Ključna svojstva grafa:**
- Svaki vrh je jedinstven
- Svaki vrh ima skup ulaznih i izlaznih bridova
- Svaki vrh/brid ima skup svojstava
- Svaki brid ima oznaku koji definira vezu između dva vrha

---

## Što je graf?

- Matematički objekt koji se sastoji od:
  - vrhova (vertices) – ponekad se nazivaju i čvorovima
  - bridova (edges)

- Vrhovi mogu predstavljati "bilo što", npr.:
  - Gradove (povezani cestama)
  - Zaposlenike u tvrtki (radi s drugim zaposlenicima)
  - Električne mreže (spojene na druge mreže)
  - Proteine (interakcija s drugim proteinima)

---

## Graf - primjer

- Primjer jednostavnog grafa s dva vrha i jednim bridom
- Veze mogu biti:
  - Vidljive fizičke veze (ceste između gradova)
  - Kratke i manje vidljive (prijenos bakterija između osoba)
  - Bez fizičke veze (odnos šef-zaposlenik)

- Grafovi su izvrsni za modeliranje mreža svih vrsta

![bg right:40% 90%](../assets/graph.png)

---

## Modeliranje geografskih lokacija

**Vrhovi (čvorovi)**
- Geografske lokacije (gradovi, mjesta, raskrižja)
- Svojstva: naziv, koordinate, populacija, površina...

**Bridovi (veze)**
- Ceste koje povezuju lokacije
- Svojstva: duljina, godina izgradnje, ograničenje brzine...

---

## Modeliranje geografskih lokacija - pristupi

Ceste se mogu modelirati na dva načina:

1. Kao bridovi između vrhova (gradova)
   - Jednostavnije, fokus na udaljenosti
   - Manje detalja o samoj cesti

2. Kao posebni vrhovi povezani s drugim vrhovima
   - Složenije, omogućuje više detalja
   - Korisno kad trebamo podatke o samoj cesti (broj traka, lokacije prometnih nesreća...)

**Koji je "pravi" način?** Ovisi o potrebama aplikacije!

---

## Modeliranje zaraznih bolesti

- Vrhovi predstavljaju ljude
- Bridovi predstavljaju interakcije između ljudi

**Svojstva vrhova (ljudi):**
- Demografski podaci (dob, težina, lokacija...)
- Zdravstveni status:
  - Nije nikad bio inficiran
  - Nije inficiran sada ali je bio u prošlosti
  - Trenutno inficiran
  - Imun

**Svojstva bridova:**
- Tip kontakta
- Trajanje kontakta
- Vjerojatnost prijenosa

---

## Modeliranje konkretnih i apstraktnih entiteta

Grafovi su dobri za modeliranje apstraktnih odnosa (kao dio-od)

**Primjeri:**
- Oregon je dio USA, a provincija Quebec je dio Kanade
- Grad Portland je lociran u Oregonu, a grad Montreal u Quebecu

Ovakvi hijerarhijski odnosi predstavljaju poseban graf koji se naziva **stablo (tree)**

**Stablo ima:**
- Korijen (root)
- Svojstvo: svi vrhovi su spojeni na samo jedan vrh (odnos parent-child)

---

## Stabla

- Stabla su korisna za modeliranje hijerarhijskih odnosa
- Primjer: dijelovi automobila

```
Automobil
├── Motor
│   ├── Blok motora
│   ├── Klipovi
│   └── Svjećice
├── Karoserija
│   ├── Vrata
│   └── Stakla
└── Podvozje
    ├── Osovine
    └── Amortizeri
```

---

## Modeliranje društvenih mreža

- "Like" na društvenim mrežama može biti modeliran kao veza između osobe i objave
- Više ljudi može označiti s Like istu objavu
- Ljudi mogu imati više objava s različitim brojem Like oznaka

**Posebno svojstvo:**
U ovom primjeru postoji posebno svojstvo - bridovi idu samo od korisnika do objava. Ovakav graf se naziva **bipartitni graf** (bipartite graph).

---

## Prednosti graf baza podataka

- Graf BP pokazuju **eksplicitne veze** između entiteta
  - Vrhovi predstavljaju entitete i vezani su bridovima
  
- U relacijskim bazama podataka:
  - Veze nisu prikazane poveznicama
  - Entiteti dijele zajedničke atribute (ključeve)
  - Potrebno je koristiti JOIN operacije

- U graf BP se umjesto spajanja (JOIN) **prate bridovi** od vrha do vrha
  - Puno jednostavnija i brža operacija

---

## Pojednostavljeno modeliranje

- Kod relacijskih baza podataka modeliranje počinje definiranjem entiteta, atributa i veza
- Primjer društvene mreže u relacijskoj bazi (potrebne su pomoćne tablice za M:N veze):

![Modeliranje veze više-na-više u RBP](../assets/rbp.png)

---

## Višestruke veze između entiteta

- Primjer modeliranja transporta između entiteta u graf bazi podataka:

![Modeliranje veze više-na-više u graf BP](../assets/graph.png)

- Graf baze podataka prirodno podržavaju višestruke veze različitih tipova

---

## Terminologija graf BP - Vrh (vertex)

- Vrh predstavlja entitet označen jedinstvenim identifikatorom
  - Slično primarnom ključu ili rowkey-u u stupčastim BP
  
- Može predstavljati bilo koji entitet povezan s drugim entitetom:
  - Ljudi na društvenoj mreži
  - Gradovi povezani cestama
  - Poslužitelji u klasteru
  - Bilo koji drugi objekt iz stvarnog svijeta

---

## Terminologija graf BP - Brid (edge)

- Definira vezu između povezanih vrhova ili objekata

- Primjer:
  - U obiteljskom stablu vrhovi predstavljaju ljude a bridovi veze između njih (npr. "kćer od", "otac od")

- Također imaju svojstva koja se najčešće nazivaju "weight"
  - Primjer: u cestovnoj mreži weight bi mogla biti udaljenost između gradova

- Ne moraju svi grafovi imati svojstva za bridove

---

## Vrste bridova

**Usmjereni (directed)**
- Imaju smjer (npr. "roditelj od")
- Veza ima značenje samo u jednom smjeru

![bg right:40% 90%](../assets/graph.png)

**Neusmjereni (undirected)**
- Nemaju smjer 
- Npr. u cestovnoj mreži smjer ne mora biti potreban ako se traži samo povezanost između gradova
- Veza ima isto značenje u oba smjera

---

## Putanja (path)

- Niz vrhova s bridovima koji povezuju te vrhove

- **Usmjerena putanja:**
  - Ako je u pitanju usmjereni graf
  - Mora se pratiti smjer bridova

- **Neusmjerena putanja:**
  - Ako je u pitanju neusmjereni graf
  - Može se kretati u bilo kojem smjeru

- Važni jer sadržavaju informacije o povezanosti vrhova u grafu

- Čest problem: pronaći najkraći (optimalan) put između dva vrha

---

## Petlja (loop)

- Brid koji povezuje vrh na samog sebe

- **Primjer:**
  - U biologiji, proteini mogu imati interakciju s drugim proteinima iste vrste
  - Osoba na društvenoj mreži koja šalje poruke sama sebi
  
- U nekim grafovima petlje nemaju smisla
  - Na primjer u obiteljskom stablu

---

## Operacije na grafovima

- Osnovne operacije kao u ostalim BP:
  - Unos
  - Čitanje
  - Ažuriranje
  - Brisanje 

- Dodatne operacije specifične za grafove:
  - Unija grafova
  - Presjek grafova
  - Obilazak grafa

---

## Unija grafova

- Kombinirani skup vrhova i bridova dvaju ili više grafova

**Primjer:**
- Graf A
  - Vrhovi: 1, 2, 3 i 4
  - Bridovi: {1,2}, {1, 3}, i {1, 4}
  
- Graf B
  - Vrhovi: 1, 4, 5 i 6
  - Bridovi: {1, 4}, {4, 5}, {4, 6} i {5, 6}

---

## Unija grafova - rezultat

Unija grafova A i B je skup vrhova i bridova oba grafa:
- Vrhovi: 1, 2, 3, 4, 5 i 6
- Bridovi: {1, 2}, {1, 3}, {1, 4}, {4, 5}, {4, 6} i {5, 6}

![Unija grafova A i B](../assets/graph.png)

---

## Presjek grafova

- Skup vrhova i bridova koji su zajednički oba grafa

**Za prethodni primjer:**
- Vrhovi: 1, 4
- Bridovi: {1, 4}

---

## Obilazak grafa

- Proces posjećivanja svih vrhova u grafu na određeni način

**Najčešće metode obilaska:**
1. Pretraživanje u dubinu (DFS - Depth-First Search)
   - Započinje iz vrha i ide što dublje prije vraćanja
   
2. Pretraživanje u širinu (BFS - Breadth-First Search)
   - Posjećuje sve susjedne vrhove prije kretanja dalje

---

## Svojstva grafova i bridova

Nekoliko svojstava korisno za analizu i usporedbu grafova:

- Izomorfizmi (Isomorphisms)
- Redoslijed i veličina (Order and Size)
- Stupanj (Degree)
- Bliskost (Closeness)
- Pripadnost (Betweenness)

---

## Izomorfizam

- Dva grafa smatraju se izomorfnim ako:
  - Za svaki vrh u prvom grafu postoji odgovarajući vrh u drugom grafu
  - Za svaki brid između para vrhova u prvom grafu postoji odgovarajući brid u drugom grafu

- **Primjena:**
  - Društvene mreže
  - Epidemiologija
  - Detekcija uzoraka u skupu grafova

---

## Redoslijed i veličina (Order and Size)

- Mjere veličine grafa:
  - **Redoslijed grafa** = broj vrhova
  - **Veličina grafa** = broj bridova

- Važni za razumijevanje performansi:
  - Utječu na vrijeme i prostor potreban za izvođenje operacija
  - Za izvođenje operacija na malom grafu trebat će manje vremena nego za iste operacije na velikom grafu

---

## Stupanj (Degree)

- Broj bridova povezanih na vrh
- Jedan od načina mjerenja važnosti vrha u grafu

- **Značaj:**
  - Vrhovi s višim stupnjevima direktnije su povezani s drugim vrhovima
  - Važan pokazatelj kada se rješavaju problemi širenja informacija ili svojstava kroz mrežu
  - U društvenim mrežama, osobe s visokim stupnjem imaju više veza

---

## Bliskost (Closeness)

- Svojstvo vrha koje pokazuje koliko je vrh "daleko" od svih ostalih u grafu
- Važna mjera za razumijevanje:
  - Širenja informacija na društvenoj mreži
  - Širenja zarazne bolesti u zajednici
  - Kretanje materijala u distribucijskoj mreži

- **Primjena:**
  - Marketinški stručnjaci mogu ciljati ljude s visokim vrijednostima bliskosti za širenje vijesti o novom proizvodu
  - Informacije će se brže širiti mrežom ako započnu s nekim s visokom vrijednošću bliskosti

---

## Pripadnost (Betweenness)

- Mjera koliko je neki vrh "usko grlo" u mreži
- Pokazuje koliko je vrh važan za povezivanje različitih dijelova grafa

**Primjer:**
- Grad na rijeci koji ima mnogo cesta, ali samo jedan most
- Vrhovi koji tvore most imaju visoku vrijednost pripadnosti jer tvore usko grlo
- Ako bi se uklonili, graf bi ostao nepovezan

---

## Vrste grafova

- Usmjereni i neusmjereni grafovi (Directed and Undirected Graphs)
- Mrežni protok (Flow Network)
- Bipartitni grafovi (Bipartite Graph)
- Multigrafovi (Multigraph)
- Težinski graf (Weighted graph)

---

## Usmjereni i neusmjereni grafovi

**Usmjereni graf:**
- Bridovi imaju smjer (A → B)
- Veza od A do B ne implicira vezu od B do A

**Neusmjereni graf:**
- Bridovi nemaju smjer (A — B)
- Veza između A i B znači isto u oba smjera

---

## Mrežni protok (Flow Network)

- Nazivaju se i transportne mreže
- Usmjereni graf u kojem:
  - Svaki brid ima kapacitet
  - Svaki vrh ima skup ulaznih i izlaznih bridova
  
- Važno pravilo: zbroj kapaciteta ulaznih bridova ne smije biti veći od zbroja kapaciteta izlaznih bridova
  - Dvije iznimke: vrhovi "izvor" i "ponor"

- **Primjena:** modeliranje prometnih sustava, vodovodnih mreža, električnih mreža...

---

## Bipartitni grafovi (bigraf)

- Graf s dva različita skupa vrhova gdje je svaki vrh u jednom skupu povezan samo s vrhovima drugog skupa
- Nikada nema veza između vrhova istog skupa

**Koristi se za modeliranje:**
- Odnosa između objava na društvenim mrežama i ljudi
- Odnosa nastavnici-učenici
- Odnosa poslovi-kandidati
- Odnosa kupci-proizvodi

---

## Multigrafovi

- Graf s višestrukim bridovima između vrhova
- Omogućuje modeliranje različitih tipova veza između istih entiteta

**Primjer:**
- Tvrtka za dostavu koja koristi multigraf za određivanje najjeftinijeg načina dostave između gradova
- Višestruke veze predstavljaju različite opcije transporta (vlak, autobus, avion...)
- Svaki brid ima svojstva kao što su vrijeme, cijena, pouzdanost...

---

## Težinski graf (Weighted graph)

- Svaki brid ima dodijeljen broj (težinu) koji može predstavljati:
  - Cijenu
  - Kapacitet
  - Udaljenost
  - Vrijeme putovanja
  - Druge kvantitativne mjere

- Često se koristi kod optimizacije problema kao što je traženje najkraćeg puta
- **Dijkstrin algoritam:** jedan od najpoznatijih algoritama za traženje najkraćeg puta

---

## Dijkstrin algoritam

- Edsger Dijkstra: nizozemski znanstvenik poznat po doprinosu dizajnu softvera

> "Računarstvo nije ništa više o računalima nego što je astronomija o teleskopima."

- Idealan za:
  - Usmjeravanje paketa na Internetu
  - Traženje najučinkovitije rute za dostavu
  
- Performanse: vrijeme izvršavanja proporcionalno je kvadratu broja vrhova
  - Vrijeme potrebno za završetak algoritma eksponencijalno raste s brojem vrhova

---

## Dizajn graf baza podataka

- Pristup u dizajnu svake NoSQL BP temelji se na upitima i analizi podataka koja se očekuje od sustava
- Graf BP su primjerene za domenu problema koja se može opisati entitetima i odnosima među njima

**Od graf BP se očekuje rješavanje upita i analiza koji uključuju:**
- Identificiranje odnosa između entiteta
- Identificiranje zajedničkih svojstava bridova iz vrha
- Izračunavanje agregatnih svojstava bridova iz vrha
- Izračunavanje agregatnih vrijednosti svojstava vrhova

---

## Primjeri upita za graf BP

- Koliko skokova (bridova) je potrebno da se stigne od vrha A do vrha B?
- Koliko bridova između vrhova A i B ima trošak manje od 100?
- Koliko bridova je vezano na vrh A?
- Koja je centralna mjera vrha B?
- Je li vrh C usko grlo? Ako je, i ako se ukloni, koji dio grafa ostaje nepovezan?

---

## Dizajn graf BP za društvenu mrežu

**Primjer:** Društvena mreža za NoSQL programere

**Funkcionalnosti:**
- Prijava i odlazak sa stranice
- Praćenje objava drugih programera
- Postavljanje pitanja drugim ekspertima
- Predlaganje novih veza temeljem dijeljenih interesa
- Rangiranje članova temeljem broja veza, objava i odgovora

---

## Entiteti i svojstva

**Model definiran s dva osnovna entiteta:**
- Programeri
- Objave

**Svojstva programera:**
- Ime
- Lokacija
- Korištene NoSQL BP
- Godine iskustva
- Područje interesa (modeliranje podataka, optimizacija, sigurnost...)

**Svojstva objava:**
- Datum izrade
- Ključne riječi
- Tip objave (pitanje, novosti, savjeti...)
- Naslov
- Tijelo objave

---

## Odnosi između entiteta

1. **Programer – programer**
   - Veza "Follows" (prati)
   
2. **Programer – objava**
   - Veza "Created" (kreirana)
   
3. **Objava – programer**
   - Veza "CreatedBy" (kreirana od)
   
4. **Objava – objava**
   - Veza "ResponseTo" (odgovor na)

---

## Dizajn usmjeren upitima

- Ne postoji jedan ispravan način modeliranja graf BP za sve probleme
- Modeliranje ovisi o tipičnim upitima i načinu korištenja podataka

**Primjeri optimizacije:**
- Implementacija direktne veze između objave i programera (CreatedBy)
- Praćenje bridova i vrhova je jednostavna i brza operacija
- Veze objava-objava su korisne za modeliranje odgovora na pitanja

---

## Dizajn usmjeren upitima - primjer

**Primjer niti konverzacije:**

```
[Robert] -> Pitanje: "Postoji li brži put od Dijkstrinog algoritma za traženje najkraćeg puta?"
  |
  v
[Ana] -> Odgovor: "Za specifične slučajeve, da. A* je često brži za probleme s heuristikom..."
  |
  v
[Marko] -> Odgovor: "Bellman-Ford je bolji kad imaš negativne težine..."
  |
  v
[Robert] -> Zahvala: "Hvala svima na odgovorima!"
```

---

## Osnovni koraci dizajna graf BP

1. Identificirati upite koje želite izvoditi
2. Identificirati entitete u grafu
3. Identificirati odnose između entiteta
4. Preslikati upite specifične za domenu u apstraktnije upite grafa
5. Implementirati upite koristeći algoritme grafa za izračunavanje dodatnih svojstava čvorova

---

## Upitni jezici za graf

Postoji više različitih jezika za upite u graf bazama podataka:

- **Cypher** - deklarativni jezik sličan SQL-u za izradu upita
  - Koristi se za Neo4j graf BP
  
- **Gremlin** - jezik za obilazak grafa koji radi s više graf BP
  - Dio Apache TinkerPop projekta

---

## Cypher - primjeri

SQL je deklarativni jezik za rad s tablicama, Cypher je deklarativni jezik za rad s grafovima.

**Cypher podržava:**
- WHERE
- ORDER BY
- LIMIT
- UNION
- COUNT
- DISTINCT
- SUM
- AVG

---

## Cypher - primjeri sintakse

**Izrada vrhova:**
```cypher
CREATE (p:Programmer {name: 'Ana Horvat', location: 'Zagreb', 
                      experience: 5, interests: ['Modeliranje', 'Graf BP']})
```

**Izrada bridova:**
```cypher
MATCH (p1:Programmer {name: 'Ana Horvat'}), 
      (p2:Programmer {name: 'Ivan Kovač'})
CREATE (p1)-[:FOLLOWS]->(p2)
```

---

## Cypher - primjeri upita

**Dohvat svih programera:**
```cypher
MATCH (p:Programmer) 
RETURN p
```

**Dohvat svih veza za određenog programera:**
```cypher
MATCH (p:Programmer {name: 'Robert Smith'})-[r]-() 
RETURN r
```

---

## Gremlin - upiti za obilazak grafa

- Umjesto upita određivanjem kriterija za odabir vrhova (kao u Cypheru)
- Specificiraju se vrhovi i pravila za njihov obilazak

**Osnovni obilazak grafa:**
```gremlin
g.V().has('name', 'Robert').out('FOLLOWS').values('name')
```

Ovaj upit dohvaća sve programere koje Robert prati.

---

## Popularne graf baze podataka

- **Neo4j** - najpoznatija graf baza podataka, koristi Cypher
- **ArangoDB** - višemodalna baza koja podržava grafove, dokumente i ključ-vrijednost
- **Amazon Neptune** - upravljana graf baza u AWS-u
- **JanusGraph** - distribuirana graf baza podataka
- **OrientDB** - višemodalna baza s podrškom za grafove
- **TigerGraph** - skalabilna graf analitička platforma

---

## Zaključak

- Graf baze podataka odlične su za probleme gdje su odnosi između entiteta važni
- Idealne za složene upite koji bi zahtijevali mnoštvo JOIN operacija u relacijskim bazama
- Prirodno podržavaju kompleksne odnose i strukture podataka
- Omogućuju naprednu analizu veza između entiteta
- Podržavaju različite algoritme za analizu grafova

---

## Projekti - podsjetnik

- **ROKOVI**: na stranicama kolegija
- Predaja projekta u zadanim rokovima je uvjet za potpis!

**Dataset primjeri:**
- Vremenske prognoze: https://github.com/zonination/weather-us/blob/master/boston.csv
- New York taxi: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page