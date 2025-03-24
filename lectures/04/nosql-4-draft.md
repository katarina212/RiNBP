---
marp: true
theme: default
paginate: true
backgroundColor: #fff
---

# SQL Programiranje
### Pohranjene procedure, funkcije i okidači

---

# Sadržaj

1. Uvod u SQL programiranje
2. Pohranjene procedure
3. Funkcije
4. Okidači
5. Programske strukture u SQL-u
6. Integracija SQL programa u aplikacijsku arhitekturu
7. Razmatranja i najbolje prakse

---

# I. Uvod u SQL programiranje

---

## Što je SQL programiranje?

- SQL (Structured Query Language) je prvenstveno jezik za upite i upravljanje podacima
- SQL programiranje proširuje osnovne DML mogućnosti (SELECT, INSERT, UPDATE, DELETE)
- Omogućuje stvaranje trajnih, ponovno upotrebljivih objekata baze podataka
- Koristi se za ugrađivanje logike i automatizaciju procesa unutar baze podataka

---

## Zašto programirati u SQL-u?

- **Programabilnost baze podataka**: izvršavanje logike bliže izvorima podataka
- **Optimizacija upita**: kompiliranje i optimizacija od strane baze podataka
- **Agregirani podaci**: predizračun i pohrana zbirnih podataka
- **Složena izvješća**: generiranje naprednih izvješća iz više tablica
- **Primjena poslovnih pravila**: konzistentno očuvanje integriteta podataka
- **Poboljšana performansa**: smanjenje mrežnog prometa i brže izvođenje
- **Jednostavnije održavanje**: centralizirana logika

---

## Vrste SQL programa

- **Pohranjene procedure** (eng. Stored procedures): imenovane kolekcije SQL naredbi koje se pohranjuju i izvršavaju unutar baze podataka
- **Funkcije** (eng. Functions): slične procedurama, ali dizajnirane za vraćanje vrijednosti
- **Okidači** (eng. Triggers): automatski se izvršavaju kada se dogode specifični događaji u bazi podataka

---

# II. Pohranjene procedure

---

## Definicija i svrha

- Pohranjene procedure su imenovani skupovi prethodno kompiliranih SQL naredbi
- Pohranjene su direktno unutar sustava baze podataka
- Izvršavaju se pozivom njihovog imena
- Osnovna svrha: enkapsulacija ponovno upotrebljivih operacija baze podataka

---

## Prednosti korištenja pohranjenih procedura

- **Poboljšanje performansi**: kompilacija i optimizacija prilikom izvršavanja
- **Ponovna upotreba koda**: poziv iz više aplikacija ili dijelova aplikacije
- **Smanjeni mrežni promet**: šalje se samo poziv i rezultati, ne pojedinačni upiti
- **Poboljšana sigurnost**: korisnici mogu izvršavati procedure bez direktnog pristupa tablicama
- **Jednostavniji razvoj aplikacija**: enkapsulacija složene logike baze podataka
- **Lakše održavanje**: promjene u proceduri bez mijenjanja aplikacije

---

## Osnovna sintaksa (konceptualno)

```sql
CREATE PROCEDURE [dbo].[Naziv_Procedure]
    -- Parametri procedure
    @parametar1 tip_podatka, @parametar2 tip_podatka
AS
BEGIN
    -- SET NOCOUNT ON za sprječavanje dodatnih rezultata
    SET NOCOUNT ON;

    -- SQL naredbe
    INSERT INTO Tablica(Stupac1, Stupac2)
    VALUES(@parametar1, @parametar2);

    -- Dodatna logika...
END
GO
```

---

## Primjer procedure za distribuiranu banku

```sql
CREATE PROCEDURE [dbo].[Insert_Rn]
    @brojRacuna int, @iznos decimal(10,2)
AS
BEGIN
    SET NOCOUNT ON;

    if @brojRacuna % 2 = 0
    begin
        insert into BANKA_SH2.dbo.Racun(Broj_racuna, Iznos, Zadnja_promjena)
        values(@brojRacuna, @iznos, GETDATE());
    end
    else
    begin
        insert into [192.168.150.40].BANK_SH1.dbo.Racun(Broj_racuna, Iznos, Zadnja_promjena)
        values(@brojRacuna, @iznos, GETDATE());
    end
END
GO
```

---

## Parametri

- **Ulazni parametri**: vrijednosti koje se prosljeđuju proceduri tijekom izvršavanja
  - Primjer: `@brojRacuna`, `@iznos`
- **Izlazni parametri**: vrijednosti koje procedura vraća pozivatelju
  - Označeni sa `OUTPUT` ključnom riječi u definiciji

---

## Pozivanje pohranjenih procedura

```sql
-- Poziv procedure s imenovanjem parametara
EXEC Insert_Rn @brojRacuna = 12345, @iznos = 100.00;

-- Poziv procedure bez imenovanja parametara
EXEC Insert_Rn 12345, 100.00;

-- Poziv procedure s izlaznim parametrom
DECLARE @rezultat int;
EXEC Izracunaj_Saldo @racunID = 1001, @saldo = @rezultat OUTPUT;
SELECT @rezultat AS 'Trenutni saldo';
```

---

## Slučajevi korištenja

- **Izvođenje složenih, višekoračnih operacija**
  - Obrada narudžbe ili prijenos sredstava između računa
- **Osiguranje integriteta i konzistentnosti podataka**
  - Složena pravila validacije
- **Implementacija poslovnih pravila unutar baze podataka**
  - Centralizacija pravila za konzistentnu primjenu
- **Upravljanje podacima u distribuiranim okruženjima**
  - Usmjeravanje operacija na odgovarajući poslužitelj

---

# III. Funkcije

---

## Definicija i svrha

- Funkcije su objekti baze podataka koji sadrže SQL kod za izvođenje specifičnih izračuna
- Dizajnirane su za vraćanje vrijednosti
- Koriste se unutar SQL izraza i upita, slično ugrađenim funkcijama poput COUNT() ili AVG()
- Svrha: enkapsulacija izračuna ili logike dohvata podataka koji se mogu lako pozvati

---

## Vrste funkcija

- **Skalarne funkcije**
  - Vraćaju jednu vrijednost određenog tipa podataka
  - Primjeri: izračun poreza, formatiranje datuma

- **Tablične funkcije**
  - Vraćaju skup redaka (virtualnu tablicu)
  - Mogu se koristiti u JOIN klauzulama ili drugim dijelovima SQL upita

---

## Osnovna sintaksa (konceptualno)

**Skalarna funkcija**:
```sql
CREATE FUNCTION naziv_funkcije (parametar1 tip_podatka, ...)
RETURNS tip_podatka_za_povrat
AS
BEGIN
    -- Tijelo funkcije: izvođenje izračuna
    RETURN izračunata_vrijednost;
END;
```

**Tablična funkcija**:
```sql
CREATE FUNCTION naziv_funkcije (parametar1 tip_podatka, ...)
RETURNS TABLE
AS
RETURN (
    -- SQL upit koji definira tablicu za povrat
    SELECT stupac1, stupac2, ...
    FROM neka_tablica
    WHERE uvjet baziran na parametrima
);
```

---

## Prednosti i slučajevi korištenja

- **Enkapsulacija ponovno upotrebljive logike**
  - Definiranje jednom, korištenje na više mjesta

- **Pojednostavljenje složenih SQL upita**
  - Razbijanje složenih izračuna na manje, upravljivije jedinice

- **Izvođenje izračuna i transformacija podataka**
  - Posebno korisno kod skalarnih funkcija

- **Vraćanje skupova podataka temeljenih na ulaznim parametrima**
  - Filtrirani podaci koji se mogu koristiti u daljnjim upitima

---

# IV. Okidači

---

## Definicija i svrha

- Okidači su posebni SQL programi koji se automatski izvršavaju kao odgovor na određene događaje
- Događaji su obično DML operacije (INSERT, UPDATE, DELETE) na određenoj tablici
- Osnovna svrha: automatsko provođenje poslovnih pravila, održavanje integriteta podataka, revizija (audit)
- Omogućuju automatsku reakciju na promjene podataka

---

## Vrste okidača

- **BEFORE Okidači (pre)**
  - Izvršavaju se *prije* pokretajuće DML operacije
  - Koriste se za validaciju podataka ili sprječavanje operacije

- **AFTER Okidači (post)**
  - Izvršavaju se *nakon* uspješnog dovršetka DML operacije
  - Koriste se za reviziju, ažuriranje povezanih tablica

- **INSTEAD OF Okidači**
  - Specifični za poglede (views)
  - Izvršavaju se *umjesto* DML operacije

---

## Pristup podacima unutar okidača

- Unutar okidača često trebate pristupiti podacima koji se mijenjaju
- SQL pruža dvije posebne "interne tablice" za tu svrhu:
  - `inserted` - sadrži kopije redaka koji se umeću ili nove vrijednosti ažuriranih redaka
  - `deleted` - sadrži kopije redaka koji se brišu ili stare vrijednosti ažuriranih redaka
- Upitom nad ovim tablicama možete pristupiti podacima i izvršiti potrebne akcije

---

## Primjer okidača

```sql
CREATE TRIGGER trg_AuditZaposlenici
ON Zaposlenici
AFTER UPDATE
AS
BEGIN
    INSERT INTO ZaposleniciLog (ID_zaposlenika, StaraPlaca, NovaPlaca, DatumPromjene)
    SELECT
        i.ID,
        d.Placa AS StaraPlaca,
        i.Placa AS NovaPlaca,
        GETDATE()
    FROM inserted i
    JOIN deleted d ON i.ID = d.ID
    WHERE i.Placa <> d.Placa;
END;
```

---

## Slučajevi korištenja

- **Provođenje složenih poslovnih pravila i ograničenja podataka**
  - Provjera da zbroj stavki narudžbe ne prelazi određeni limit

- **Revizija promjena podataka**
  - Automatsko bilježenje svih izmjena s informacijama tko, kada i što je mijenjao

- **Održavanje integriteta podataka u povezanim tablicama**
  - Automatsko ažuriranje povezanih tablica kada se promijeni glavna tablica

- **Izvođenje akcija na temelju modifikacija podataka**
  - Slanje obavijesti, ažuriranje agregatnih tablica

---

## Rekurzivni okidači

- Rekurzivni okidač je onaj čija akcija uzrokuje ponovno pokretanje istog okidača
- Primjer problema: "Okidač je rekurzivan jer ažuriranje plaće zaposlenika pokreće okidač ponovo, što dovodi do beskonačne petlje koja se ne završava."
- Važno je pažljivo dizajnirati okidače kako bi se izbjegla nenamjerna rekurzija
- Većina sustava baza podataka ima mehanizme za ograničenje dubine rekurzije

---

# V. Programske strukture u SQL-u

---

## Naredbe i blokovi

- SQL programiranje često uključuje izvršavanje više SQL naredbi kao jedne radne jedinice
- `BEGIN ... END` blok je osnovna konstrukcija za grupiranje skupa SQL naredbi
- Ovo omogućuje definiranje logičkog bloka koda unutar procedura, funkcija ili kontrolnih struktura

```sql
BEGIN
    -- Više SQL naredbi koje se izvršavaju kao logička cjelina
    SELECT @varijabla = COUNT(*) FROM Tablica;
    IF @varijabla > 0
        UPDATE Tablica SET Status = 'Aktivan';
END
```

---

## Kontrolne strukture

**IF-ELSE IF-ELSE struktura**
```sql
IF @uvjet1 = TRUE
    -- naredbe za prvi uvjet
ELSE IF @uvjet2 = TRUE
BEGIN
    -- više naredbi za drugi uvjet
    -- BEGIN...END potreban za više naredbi
END
ELSE
    -- naredbe ako ni jedan uvjet nije istinit
```

**WHILE petlja**
```sql
WHILE @brojac < 10
BEGIN
    SET @brojac = @brojac + 1;
    -- dodatne naredbe
END
```

---

## Varijable i kursori

**Varijable**
```sql
DECLARE @EmpName VARCHAR(50);
DECLARE @EmpSalary FLOAT;
SET @EmpName = 'Ivan Horvat';
```

**Kursori**
- Omogućuju obradu redak po redak rezultata upita
- Korisni za operacije koje se ne mogu jednostavno postići set-baziranim SQL operacijama
- Potencijalno manje učinkoviti od set-baziranih operacija za velike skupove podataka

---

## Primjer korištenja kursora

```sql
DECLARE @EmpID INT, @EmpName VARCHAR(50), @EmpSalary FLOAT;
DECLARE EmpCursor CURSOR FOR
SELECT ID, Ime, Placa FROM Zaposlenici;

OPEN EmpCursor;

FETCH NEXT FROM EmpCursor INTO @EmpID, @EmpName, @EmpSalary;

WHILE @@FETCH_STATUS = 0
BEGIN
    -- Povećanje plaće za 10%
    UPDATE Zaposlenici SET Placa = @EmpSalary * 1.1 WHERE ID = @EmpID;

    FETCH NEXT FROM EmpCursor INTO @EmpID, @EmpName, @EmpSalary;
END;

CLOSE EmpCursor;
DEALLOCATE EmpCursor;
```

---

# VI. Integracija SQL programa u aplikacijsku arhitekturu

---

## Troslojni arhitekturni model

- Često korišteni model za softversku arhitekturu:
  - **Prezentacijski sloj** (korisničko sučelje)
  - **Aplikacijski sloj** (poslovna logika)
  - **Podatkovni sloj** (pohrana i dohvat podataka)

- SQL programi imaju značajnu ulogu u podatkovnom sloju

---

## Uloga okidača i procedura

- SQL programi poput pohranjenih procedura nalaze se unutar podatkovnog sloja (RDBMS)
- Aplikacijski sloj može pozivati ove procedure za izvođenje podatkovnih operacija
- Primjer:
  ```csharp
  // Metoda poslovnog sloja koja koristi pohranjenu proceduru
  public void DodajProizvod(string naziv, decimal cijena, int kolicina)
  {
      using (SqlConnection conn = new SqlConnection(connectionString))
      {
          SqlCommand cmd = new SqlCommand("DodajProizvod", conn);
          cmd.CommandType = CommandType.StoredProcedure;
          cmd.Parameters.AddWithValue("@Naziv", naziv);
          cmd.Parameters.AddWithValue("@Cijena", cijena);
          cmd.Parameters.AddWithValue("@Kolicina", kolicina);
          conn.Open();
          cmd.ExecuteNonQuery();
      }
  }
  ```

---

# VII. Razmatranja i najbolje prakse

---

## Performanse SQL programa

- Dobro napisani SQL programi mogu poboljšati performanse
- Loše napisani ili pretjerano složeni programi mogu uzrokovati probleme s performansama
- Važno je optimizirati SQL kod, učinkovito koristiti indekse i izbjegavati nepotrebne operacije
- Kursore koristiti oprezno zbog njihovog potencijalnog utjecaja na performanse

---

## Održavanje i otklanjanje grešaka

- Upravljanje velikim brojem pohranjenih procedura, funkcija i okidača može postati složeno
- Važno je imati jasne konvencije imenovanja, dokumentaciju i kontrolu verzija
- Otklanjanje grešaka često uključuje korištenje alata specifičnih za bazu podataka
- Preporučljivo je testirati SQL programe u razvojnom okruženju prije implementacije u produkciju

---

## Sigurnosna razmatranja

- SQL injekcija je potencijalni sigurnosni rizik ako se ulazni parametri ne validiraju pravilno
- Koristiti parametrizirane upite ili druge sigurne prakse kodiranja
- Pažljivo upravljati dozvolama na pohranjenim procedurama i funkcijama
- Ograničiti pristup samo na potrebne operacije

---

## Kada koristiti pojedine vrste SQL programa

- **Pohranjene procedure**
  - Za enkapsulaciju složene poslovne logike
  - Za poboljšanje performansi često izvršavanih operacija
  - Za poboljšanje sigurnosti

- **Funkcije**
  - Za izračune koji se koriste unutar SQL izraza
  - Za vraćanje skupova redaka koji se koriste u daljnjim upitima

- **Okidači**
  - Za automatsko provođenje integriteta podataka
  - Za reviziju promjena
  - Za reakciju na događaje modifikacije podataka

---

# VIII. Zaključak

- SQL programiranje pruža moćne mogućnosti za proširenje funkcionalnosti relacijskih baza podataka
- Pohranjene procedure, funkcije i okidači ključni su objekti za enkapsulaciju logike, poboljšanje performansi i provođenje poslovnih pravila
- Razumijevanje kako učinkovito koristiti ove konstrukte ključno je za izgradnju robusnih, učinkovitih i održivih aplikacija
- SQL programi igraju vitalnu ulogu u modernim aplikacijskim arhitekturama

