---
marp: true
theme: default
paginate: true
---

# Raspodijeljene i nerelacijske baze podataka
# Dokument baze podataka

IZVOR: Sullivan, D. (2015). NoSQL for mere mortals. Addison-Wesley Professional

---

## Sadržaj

- Uvod u dokument baze podataka
- Usporedba relacijskih i dokument baza podataka
- Dokumenti i JSON format
- Zbirke (Collections)
- Dizajn dokument baza podataka
- Horizontalno particioniranje (Sharding)
- Operacije na dokument bazama
- Primjer slučaja korištenja: TransGlobal Transport and Shipping

---

## Uvod u dokument baze podataka

- Vrsta NoSQL (nerelacijskih) baza podataka
- Podatke pohranjuje u fleksibilnom, polu-strukturiranom formatu - **dokument**
- Najpopularnije implementacije: MongoDB, Couchbase, Firestore, Amazon DocumentDB

![bg right:40% 80%](https://db-engines.com/en/ranking/document+store)

---

## Relacijske vs dokument baze podataka

Pet ključnih razlika:
1. Model podataka
2. Shema
3. Upiti
4. Skalabilnost
5. Integritet podataka i transakcije

---

## 1. Model podataka

**Relacijske baze podataka:**
- Koriste tabularni model
- Podaci organizirani u predefiniranoj shemi
- Tablice, redci i stupci
- Odnosi između entiteta izraženi preko stranih ključeva

**Dokument baze podataka:**
- Dokument-orijentirani podatkovni model
- Podaci pohranjeni kao fleksibilni i samostalni dokumenti
- Svaki dokument može imati svoju strukturu
- Odnosi mogu biti ugnježđeni unutar dokumenata

---

## 2. Shema

**Relacijske baze podataka:**
- Zahtijevaju fiksnu shemu
- Struktura i tipovi podataka definirani prije unosa podataka
- Promjena sheme često zahtijeva migracije ili operacije izmjene sheme

**Dokument baze podataka:**
- Fleksibilna shema ("schema-less" ili "schema-flexible")
- Svaki dokument može imati vlastitu strukturu
- Polja unutar dokumenata mogu varirati
- Lakša prilagodba promjenjivim zahtjevima bez potrebe za strogim migracijama

---

## 3. Upiti

**Relacijske baze podataka:**
- Koriste SQL jezik
- Omogućuju složene upite (JOIN, agregatne funkcije, filtriranje)
- Standardizirani pristup kroz SQL

**Dokument baze podataka:**
- Vlastiti jezik za upite ili API
- Upiti se izvode na razini dokumenta
- Mnoge dokument BP podržavaju napredne mogućnosti:
  - Indeksiranje
  - Pretraga teksta
  - Geoinformacijske upite

---

## 4. Skalabilnost

**Relacijske baze podataka:**
- Dizajnirane za vertikalno skaliranje
- Povećanje hardverskih resursa (procesor, memorija)
- Horizontalno skaliranje može biti složenije
- Zahtijeva tehnike particioniranja podataka

**Dokument baze podataka:**
- Prikladne za horizontalno skaliranje
- Mogu distribuirati podatke na više servera ili klastera
- Lako skaliranje dodavanjem novih čvorova u sustav
- Bolje rukovanje velikim količinama podataka i prometom

---

## 5. Integritet podataka i transakcije

**Relacijske baze podataka:**
- Ugrađena podrška za integritet podataka kroz ACID svojstva
- Omogućuju transakcije
- Osiguravaju da su operacije atomarne i konzistentne

**Dokument baze podataka:**
- Slabija konzistencija podataka
- Ne omogućuju striktno ACID transakcije, umjesto toga BASE
- Mnoge nude "eventual consistency" (konzistenciju u konačnici)
- Veći naglasak na dostupnost (availability) i toleranciju particije (partition tolerance)
- Prisjetite se BASE i CAP teorema

---

## Kompromisi redundancije

- **Niska redundancija:**
  - Dobra propusnost ažuriranja (potrebno zaključati samo nekoliko stavki)
  - Ažuriranje je brže i jednostavnije
  
- **Visoka redundancija:**
  - Bolje vrijeme izvršavanja upita (potrebno je pristupiti manjem broju blokova)
  - Upiti su brži i jednostavniji

**Problemi:**
- Redundantnost može voditi do nekonzistentnosti podataka
- Otključano čitanje podataka (ACID) može dati dojam nekonzistentnosti pohranjenih podataka

---

## Usporedba terminologije

**SQL BP:**
- Baza podataka → Tablice → Retci

**Dokument BP:**
- Baza podataka → Collections (Zbirke) → Documents (Dokumenti)

![Usporedba SQL i dokument baza](../assets/kupci.png)

---

## Dokument baze podataka - osnove

- Dokument je osnovna podatkovna jedinica
- Dokumenti su uređeni skupovi ključ-vrijednost parova
- Usporedivo s retkom u tablici, ali fleksibilnije

**Ključna razlika:**
Svaki dokument ne mora imati istu shemu!

---

## Što je Dokument? (u kontekstu dokument BP)

**JavaScript Object Notation (JSON) struktura:**
- Podaci organizirani u parovima ključ-vrijednost
- Dokument počinje `{` i završava s `}`
- Nazivi su stringovi poput `"customer_id"`
- Vrijednosti mogu biti:
  - Brojevi
  - Stringovi
  - Boolean (true/false)
  - Nizovi (`[ ]`)
  - Objekti (`{ }`)
  - NULL vrijednosti

---

## JSON primjer - zapis o kupcu

```json
{
  "customer_id": "C123456",
  "name": "Ana Horvat",
  "contact_info": {
    "email": "ana.horvat@example.com",
    "phone": "385-1-234-5678",
    "address": {
      "street": "Ilica 123",
      "city": "Zagreb",
      "postal_code": "10000",
      "country": "Croatia"
    }
  },
  "orders": [
    {
      "order_id": "O987654",
      "date": "2023-11-15",
      "items": [
        {"product_id": "P111", "name": "Laptop", "quantity": 1},
        {"product_id": "P222", "name": "Mouse", "quantity": 2}
      ]
    }
  ],
  "account_created": "2020-05-10",
  "loyalty_points": 250
}
```

---

## JSON i XML

Dokument baze podataka podržavaju različite formate:

**JSON:**
- Lakši za čitanje i pisanje
- Manje overhead-a
- Prirodna podržanost u JavaScript okruženjima
- Danas dominantan format

**XML:**
- Više metapodataka
- Strožija sintaksa
- Šira podrška za validaciju sheme
- Koristi se u nekim starijim sustavima

---

## Dokumenti i parovi Ključ-Vrijednost

**Prednost dokumenata u odnosu na K-V baze podataka:**
- Povezanim atributima upravlja se unutar jednog objekta
- Dokumenti mogu pohraniti više atributa u jednom objektu
- Lakša implementacija čestih zahtjeva (npr. filtriranje podataka)

**Primjer:**
U dokument BP jednim upitom možemo filtrirati korisnike s kupnjom u zadnjih 6 mjeseci i dohvatiti ID, imena i adrese. U K-V bazi to bi zahtijevalo više koraka i upita.

---

## Zbirke (Collections)

- Mogu se smatrati listom dokumenata
- Unutar iste kolekcije dokumenti ne moraju imati identičnu strukturu
- Preporuka: dokumenti unutar zbirke trebaju biti sličnog tipa

**Potencijalni problem:**
Filtriranje podataka prema različitim kriterijima. Možda je bolje napraviti više zbirki ovisno o očekivanoj količini podataka i načinu filtriranja.

---

## Ima li smisla stavljati različite tipove dokumenata u istu zbirku?

**Primjer:** Web trgovina s različitim tipovima proizvoda

**Informacije o svim proizvodima:**
- Naziv
- Kratki opis
- Skladište
- Dimenzija
- Težina
- Prosječna ocjena korisnika
- Prodajna cijena
- Nabavna cijena

---

## Informacije specifične za tipove proizvoda

**KNJIGE:**
- Autor
- Izdavač
- Godina izdanja
- Broj stranica

**CD:**
- Izvođač
- Producent
- Broj pjesama
- Ukupno vrijeme trajanja

**MALI KUĆANSKI APARATI:**
- Boja
- Snaga
- Stil

---

## Analiza upita za organizaciju podataka

**Tipični upiti:**
- Koji je prosječan broj kupljenih proizvoda od jednog kupca?
- Koji je raspon broja proizvoda kupljenih od strane kupaca?
- Kojih je 20 najpopularnijih proizvoda prema statistici kupaca?
- Kolika je prosječna vrijednost prodaje prema statistici kupaca?
- Koliko je tipova proizvoda prodano u zadnjih 30 dana?

**Zaključak:**
- Gotovo svi upiti odnose se na zajedničke podatke
- Samo jedan upit odnosi se na tipove proizvoda
- U ovom slučaju ima smisla staviti sve podatke u istu kolekciju
- Klijent će vjerojatno u budućnosti dodati još tipova proizvoda

---

## Definicija sheme

**Schemaless (bez sheme):**
- Fleksibilnost u strukturi dokumenata
- Nije potrebno unaprijed definirati strukturu
- Nema strogih ograničenja kao u relacijskim bazama

**Polymorphic schema (polimorfna shema):**
- Različite vrste dokumenata unutar iste zbirke
- Dokumenti s istim poljem "tip" imaju sličnu strukturu
- Korisno za modeliranje srodnih, ali različitih entiteta

---

## Osnovne operacije

- Ne postoji standardni jezik za manipulaciju podacima na dokument BP
- Svaka implementacija ima vlastiti API i sintaksu

**Osnovne operacije:**
- Unos (Insert)
- Brisanje (Delete)
- Ažuriranje (Update)
- Dohvat (Retrieve)
- Bulk Insert (masovni unos)

---

## Osnovne operacije - primjer

**Dvije kolekcije: Knjige (lijevo), Kupci (desno)**

```javascript
// Unos novog dokumenta
db.books.insert({
  title: "NoSQL za početnike",
  author: "Ivan Horvat",
  year: 2023,
  price: 299.99
})

// Dohvat s filtrom
db.customers.find({
  "address.city": "Zagreb"
})

// Ažuriranje
db.books.update(
  { title: "NoSQL za početnike" },
  { $set: { price: 249.99 } }
)

// Brisanje
db.customers.remove({ inactive: true })
```

---

## Terminologija dokument BP

**Osnovni termini:**
- **Dokument** - Skup uređenih ključ-vrijednost parova
- **Zbirka (kolekcija)** - Skupina dokumenata uobičajeno povezana za isti entitet
- **Ugrađeni dokument** - Dokument unutar dokumenta, omogućuje pohranu povezanih podataka u jednom dokumentu
- **Schemaless** - "Dvosjekli mač" - pruža fleksibilnost ali nema provjere podataka prije operacija
- **Polimorfična shema** - Više različitih "vrsta" dokumenata u istoj zbirci

---

## "Partitioning is a word that gets a lot of use in the NoSQL world—perhaps too much"

- CAP teorem (ponovimo):
  - Consistency (konzistentnost)
  - Availability (dostupnost)
  - Partition tolerance (tolerancija na particije)

- U kontekstu dokument BP se particioniranje odnosi na dijeljenje baze i raspodjelu različitih dijelova na različite poslužitelje

- **Horizontalno particioniranje** (tipično za NoSQL)
  - Dijeljenje po redcima (dokumentima)
  - Za razliku od vertikalnog (po stupcima)

---

## Horizontalno particioniranje ili Sharding

- Proces dijeljenja BP prema dokumentima
- Dijelovi (*shards*) su pohranjeni na različitim poslužiteljima
- Jedan *shard* može biti pohranjen na više poslužitelja kad je BP konfigurirana za repliciranje podataka

![bg right:40% 80%](../assets/v0.png)

---

## Razdvajanje podataka pomoću Shard Keys

- **Shard Key** je jedan ili više ključeva ili polja koji postoje u svim dokumentima u zbirci
- Određuje vrijednosti koje se koriste pri grupiranju dokumenata u različite shard-ove
- Algoritam particioniranja koristi shard key kao ulaz i određuje odgovarajući shard

**Tipovi podjele:**
- Range (raspon)
- Hash (hash vrijednost)
- Lista (eksplicitna lista vrijednosti)

---

## Normalizacija u dokument bazama

**Relacijske BP:**
- Normalizacija uklanja redundanciju
- Smanjuje anomalije ažuriranja
- Koristi JOIN operacije za povezivanje podataka

**Dokument BP:**
- Termin se ponekad koristi za opis dizajna dokumenata
- "Normalizirani dokumenti" impliciraju postojanje referenci prema drugim dokumentima za dodatne informacije
- Smanjuju redundanciju, ali povećavaju broj upita

---

## Denormalizacija

**Dizajniranje baza podataka podrazumijeva kompromise:**

- **Denormalizacija** u dokument BP često znači:
  - Ugnježđivanje povezanih podataka u jedan dokument
  - Povećanje redundancije podataka
  - Smanjenje potrebe za spajanjem više dokumenata
  
- **Prednosti:**
  - Brži upiti (sve na jednom mjestu)
  - Bolje performanse za čitanje
  
- **Nedostaci:**
  - Teže ažuriranje (potrebno ažurirati na više mjesta)
  - Veći rizik nekonzistentnosti

---

## Primjer slučaja korištenja

**Problem: TransGlobal Transport and Shipping (TGTS)**

- Posao je narastao i tvrtka transportira složenije i različitije isporuke
- Za sve spremnike potreban je osnovni skup polja:
  - Ime kupca, kontakt informacije
  - Izvorište, odredište
  - Sažetak sadržaja
  - Broj stavki u kontejneru
  - Indikator opasnog materijala
  - Datum isteka kvarljivih predmeta
  - Podaci za kontakt za isporuku

---

## Posebne vrste spremnika

**Opasni materijali:**
- Mora se priložiti sigurnosno-tehnički list (MSDS)
- Informacije za hitne službe koje će možda morati rukovati materijalima

**Kvarljiva hrana:**
- Podaci o inspekciji hrane
- Ime inspektora
- Agencija odgovorna za inspekciju
- Kontakt podaci agencije

---

## Analiza uzoraka upita

- 70%–80% upita dohvaća jedan zapis
  - Obično prema identifikatoru, imenu kupca, datumu otpreme i izvornom objektu
  
- Preostalih 20%–30% su sažeta izvješća
  - Pokazuju podskup uobičajenih informacija
  - Povremeno izvješća prema vrsti pošiljke (rijetko)

**Budući razvoj:**
- Značajno povećanje poslova u sljedećih 12-18 mjeseci
- Više vrsta tereta s posebnim informacijama
- Potreba za horizontalnim skaliranjem i fleksibilnom shemom

---

## Struktura: zbirka "Manifest"

**Osnovna polja:**
- Ime kupca
- Ime kontakta kupca
- Adresa kupca
- Broj telefona kupca
- Faks kupca
- E-pošta kupca
- Objekt za podrijetlo
- Odredišni objekt
- Datum otpreme
- Očekivani datum isporuke
- Broj stavki u spremniku

---

## Ugraditi (embed) ili ne?

**Pitanje:**
Treba li ugnijezditi podatke o kvarljivoj hrani i opasnim materijalima u glavni dokument ili ih izdvojiti?

**Analiza:**
- Prema uzorcima izvješća, podaci o kvarljivoj hrani rutinski se prijavljuju zajedno s ostalima
  - Odluka: ugraditi ove podatke u dokument

- Podaci o opasnim materijalima (MSDS) rijetko se koriste
  - Odluka: pohraniti u posebnu zbirku MSDS

---

## Odabir indeksa

**Uzorak korištenja:**
- 60%–65% operacija čitanja
- 35%–40% operacija pisanja

**Indeksi za čitanje:**
- Identifikator - za brz dohvat pojedinačnih manifesta
- Kombinirani indeks: ime klijenta + datum otpreme + mjesto podrijetla
  - Umjesto više pojedinačnih indeksa
  - Pokriva najčešće korištene upite

---

## Odvojene zbirke prema vrsti?

**Dilema:**
Treba li kreirati zasebne zbirke za svaku vrstu manifesta?

**Analiza:**
- Trenutno mali broj vrsta, ali u budućnosti mnogo više
- Tvrtka planira dodati usluge prijevoza smrznute robe

**Odluka:**
- Iznimka od pravila odvajanja po vrsti
- Nije poželjno upravljati velikim brojem kolekcija
- Korištenje jedne zbirke s polimorfnom shemom je bolje rješenje
- Tipove pratiti unutar dokumenata

---

## Projekti

**ROKOVI:**
- Temu odabrati do 1.5.2024.
- Obrane tema projekata od 14.5.2024 u terminima predavanja (DSE, utorkom u 8:15)
- Predaja finalne verzije projekta (u prihvatljivom obliku) - do 1.6.2024. - **Uvjet za potpis!**
- Obrane projekata od 28.5.

**Dataset primjeri:**
- https://www.kaggle.com/datasets
- Vremenske prognoze: https://github.com/zonination/weather-us/blob/master/boston.csv
- New York taxi: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page