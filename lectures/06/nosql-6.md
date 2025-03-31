---
marp: true
theme: gaia
title: Raspodijeljene i nerelacijske baze podataka - Raspodijeljene BP
description: Nikola Balić, Raspodijeljene baze podataka
paginate: true
---

# Cloud i raspodijeljene baze podataka

### Akademska godina 2024/2025
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---
## Paralelne vs. Raspodijeljene BP

### Ključne razlike

**Paralelne BP:**
- Čvorovi fizički blizu
- Povezani brzim LAN-om
- Mala "cijena" komunikacije

**Raspodijeljene BP:**
- Geografski udaljeni čvorovi
- Komunikacija preko javne mreže
- Značajna "cijena" komunikacije

---
## Zašto Raspodijeljene BP?

### Izazovi tradicionalnih sustava

- **Relacijske BP nisu dizajnirane za distribuciju:**
  - JOIN operacije su "preskupe"
  - Teško horizontalno skaliranje
  - Visoki troškovi održavanja
  - Sporo izvršavanje upita

---
## Primjeri Raspodijeljenih BP

### Popularna rješenja

- **Apache Cassandra:**
  - NoSQL baza
  - Raspodijeljena arhitektura
  - Visoka dostupnost

- **Oracle RAC:**
  - Real Application Clusters
  - Shared-disk arhitektura
  - Više instanci jedne BP

- **Ostali:**
  - MySQL Cluster
  - PostgreSQL s Citus

---
## Poželjna Svojstva

### Ključni zahtjevi

1. **Neovisnost raspodijeljenih podataka:**
   - Transparentnost podataka
   - Skriveni detalji pohrane
   - Optimizirani upiti

2. **Raspodijeljena atomarnost transakcija:**
   - ACID svojstva
   - Atomske operacije
   - Konzistentnost podataka

---
## Arhitektura Raspodijeljenih BP

### Različiti pristupi

1. **Dijeljeno sve (Shared everything):**
   - Jedna neraspodijeljena BP
   - Svi resursi dijeljeni

2. **Dijeljena memorija (Shared memory):**
   - Teoretski model
   - Rijetko u praksi

3. **Dijeljen disk (Shared disk):**
   - Tipično za CloudDB
   - Zajednički pristup disku

4. **Dijeljenje ničega (Shared nothing):**
   - Svaki čvor samostalan
   - Komunikacija preko mreže

---
## Vrste Raspodijeljenih BP

### Homogene vs. Heterogene

**Homogene:**
- Ista verzija DBMS-a
- Identični zadaci
- Shared-nothing arhitektura

**Heterogene:**
- Različiti DBMS-i
- Različiti zadaci
- Kompleksna komunikacija

---
## Particioniranje i Sharding

### Strategije raspodjele podataka

```sql
-- Primjer horizontalnog particioniranja
CREATE TABLE Orders_2024
PARTITION OF Orders
FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');

-- Primjer shardinga po lokaciji
-- Shard 1: Europa
CREATE TABLE Orders_EU (
    CHECK (region = 'EU')
) INHERITS (Orders);

-- Shard 2: Azija
CREATE TABLE Orders_ASIA (
    CHECK (region = 'ASIA')
) INHERITS (Orders);
```

---
## MS SQL Server Raspodijeljenost

### Tehnološka rješenja

1. **Always On Availability Groups:**
   - Repliciranje BP
   - Automatski oporavak

2. **SQL Server Replication:**
   - Geografska distribucija
   - Master-slave model

3. **Distributed Partitioned Views:**
   - Horizontalno particioniranje
   - Transparentno usmjeravanje

4. **Stretch Database:**
   - Hibridno cloud rješenje
   - Azure integracija

---
## Primjer: MS SQL Distribucija

### E-commerce sustav

```sql
-- Kreiranje particije za elektroniku
CREATE PARTITION FUNCTION PF_Products(int)
AS RANGE RIGHT FOR VALUES (1000, 2000, 3000);

-- Kreiranje sheme za particioniranje
CREATE PARTITION SCHEME PS_Products
AS PARTITION PF_Products
TO (FG_Electronics, FG_Clothing, FG_Home);

-- Kreiranje particionirane tablice
CREATE TABLE Products (
    ProductID int,
    CategoryID int,
    Name nvarchar(100),
    Price decimal(10,2)
) ON PS_Products(CategoryID);
```

---
## Cloud Baze Podataka (CloudDB)

### Osnovne karakteristike

- **Administracija od "treće strane"**
- **Prednosti:**
  - Skalabilnost
  - Pouzdanost
  - Dostupnost
  - Jednostavna administracija

---
## CloudDB vs. Raspodijeljene BP

### Usporedba karakteristika

| Aspekt | CloudDB | Raspodijeljene BP |
|--------|---------|-------------------|
| Infrastruktura | Pružatelj usluga | Vlastita |
| Skalabilnost | Automatska | Kompleksna |
| Dostupnost | Visoka | Zahtjevna |
| Cijena | Pay-as-you-go | Fiksni troškovi |

---
## Popularne CloudDB Platforme

### Relacijske:
- Amazon RDS
- Google Cloud SQL
- Azure SQL Database

### NoSQL:
- Amazon DynamoDB
- Google Cloud Firestore
- Azure Cosmos DB
- MongoDB Atlas

---
## Praktični Primjer: Bankovni Sustav (Prošireno)

### 1. Arhitektura sustava

```sql
-- Master baza (Zagreb)
CREATE DATABASE Bank_Master;
GO

-- Slave baze (Split, Rijeka)
CREATE DATABASE Bank_Split;
CREATE DATABASE Bank_Rijeka;

-- Tablice za transakcije
CREATE TABLE Transactions (
    TransactionID bigint IDENTITY(1,1),
    AccountID int,
    TransactionType varchar(20),
    Amount decimal(18,2),
    TransactionDate datetime2,
    BranchID int,
    Status varchar(20)
);

-- Particioniranje po regijama
CREATE TABLE Accounts_Zagreb
    CHECK (BranchID BETWEEN 1000 AND 1999)
    AS SELECT * FROM Accounts;

CREATE TABLE Accounts_Split
    CHECK (BranchID BETWEEN 2000 AND 2999)
    AS SELECT * FROM Accounts;
```

---
## Bankovni Sustav: Replikacija

### 2. Konfiguracija replikacije

```sql
-- Postavljanje publikacije
sp_addpublication
    @publication = 'BankTransactions',
    @description = 'Publikacija bankovnih transakcija',
    @sync_method = 'concurrent',
    @allow_push = 'true';

-- Dodavanje članaka
sp_addarticle
    @publication = 'BankTransactions',
    @article = 'Transactions',
    @source_owner = 'dbo',
    @source_object = 'Transactions';

-- Postavljanje pretplate
sp_addsubscription
    @publication = 'BankTransactions',
    @subscriber = 'SPLIT-SERVER',
    @destination_db = 'Bank_Split';
```

---
## Bankovni Sustav: Transakcije

### 3. Implementacija transakcija

```sql
-- Stored procedura za transfer
CREATE PROCEDURE TransferMoney
    @FromAccount int,
    @ToAccount int,
    @Amount decimal(18,2)
AS
BEGIN
    SET XACT_ABORT ON;
    BEGIN DISTRIBUTED TRANSACTION;

    BEGIN TRY
        -- Provjera stanja
        DECLARE @FromBalance decimal(18,2);
        SELECT @FromBalance = Balance
        FROM Accounts
        WHERE AccountID = @FromAccount;

        IF @FromBalance >= @Amount
        BEGIN
            -- Umanjenje s prvog računa
            UPDATE Accounts
            SET Balance = Balance - @Amount
            WHERE AccountID = @FromAccount;

            -- Dodavanje na drugi račun
            UPDATE Accounts
            SET Balance = Balance + @Amount
            WHERE AccountID = @ToAccount;

            -- Bilježenje transakcije
            INSERT INTO Transactions
            (AccountID, TransactionType, Amount, TransactionDate)
            VALUES
            (@FromAccount, 'TRANSFER_OUT', @Amount, GETDATE()),
            (@ToAccount, 'TRANSFER_IN', @Amount, GETDATE());

            COMMIT TRANSACTION;
        END
        ELSE
            THROW 50001, 'Nedovoljno sredstava', 1;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH
END;
```

---
## Praktični Primjer: E-commerce (Prošireno)

### 1. Sharding po kategorijama

```sql
-- Kreiranje sharding funkcije
CREATE PARTITION FUNCTION PF_Categories(int)
AS RANGE RIGHT FOR VALUES
(100, 200, 300, 400, 500);  -- ID rasponi za kategorije

-- Kreiranje sharding sheme
CREATE PARTITION SCHEME PS_Categories
AS PARTITION PF_Categories
TO (
    FG_Electronics,    -- Elektronika (1-100)
    FG_Clothing,       -- Odjeća (101-200)
    FG_Home,          -- Dom (201-300)
    FG_Sports,        -- Sport (301-400)
    FG_Books,         -- Knjige (401-500)
    FG_Other          -- Ostalo (501+)
);

-- Particionirana tablica proizvoda
CREATE TABLE Products (
    ProductID int,
    CategoryID int,
    Name nvarchar(100),
    Price decimal(10,2),
    Stock int,
    LastUpdated datetime2
) ON PS_Categories(CategoryID);
```

---
## E-commerce: Upravljanje inventarom

### 2. Distribuirano praćenje zaliha

```sql
-- Kreiranje linked servera za svaku lokaciju
EXEC sp_addlinkedserver
    @server = 'WAREHOUSE-ZAGREB',
    @srvproduct = 'SQL Server';

EXEC sp_addlinkedserver
    @server = 'WAREHOUSE-SPLIT',
    @srvproduct = 'SQL Server';

-- Distribuirani view za zalihe
CREATE VIEW GlobalInventory AS
SELECT
    ProductID,
    Name,
    SUM(Stock) as TotalStock,
    MAX(LastUpdated) as LastUpdated
FROM (
    SELECT * FROM Products
    UNION ALL
    SELECT * FROM [WAREHOUSE-ZAGREB].Inventory.dbo.Products
    UNION ALL
    SELECT * FROM [WAREHOUSE-SPLIT].Inventory.dbo.Products
) as CombinedInventory
GROUP BY ProductID, Name;

-- Trigger za ažuriranje zaliha
CREATE TRIGGER trg_UpdateStock
ON Orders
AFTER INSERT
AS
BEGIN
    UPDATE p
    SET Stock = p.Stock - i.Quantity
    FROM Products p
    JOIN inserted i ON p.ProductID = i.ProductID
    WHERE p.CategoryID = i.CategoryID;
END;
```

---
## E-commerce: Obrada narudžbi

### 3. Distribuirana obrada narudžbi

```sql
-- Stored procedura za obradu narudžbe
CREATE PROCEDURE ProcessOrder
    @OrderID int,
    @CustomerID int,
    @Items OrderItemType READONLY
AS
BEGIN
    SET XACT_ABORT ON;
    BEGIN DISTRIBUTED TRANSACTION;

    BEGIN TRY
        -- 1. Provjera dostupnosti
        IF EXISTS (
            SELECT 1 FROM @Items i
            JOIN GlobalInventory g ON i.ProductID = g.ProductID
            WHERE i.Quantity > g.TotalStock
        )
        BEGIN
            THROW 50001, 'Proizvod nije dostupan', 1;
        END

        -- 2. Kreiranje narudžbe
        INSERT INTO Orders (
            OrderID, CustomerID, OrderDate, Status
        ) VALUES (
            @OrderID, @CustomerID, GETDATE(), 'PROCESSING'
        );

        -- 3. Dodavanje stavki
        INSERT INTO OrderItems (
            OrderID, ProductID, Quantity, Price
        )
        SELECT
            @OrderID,
            i.ProductID,
            i.Quantity,
            p.Price
        FROM @Items i
        JOIN Products p ON i.ProductID = p.ProductID;

        -- 4. Ažuriranje zaliha
        UPDATE p
        SET Stock = p.Stock - i.Quantity
        FROM Products p
        JOIN @Items i ON p.ProductID = i.ProductID;

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH
END;
```

---
## Optimizacija Performansi

### Best Practices

1. **Particioniranje:**
   - Prema geografskoj lokaciji
   - Prema vremenu
   - Prema poslovnoj logici

2. **Replikacija:**
   - Master-slave
   - Multi-master
   - Hibridni modeli

3. **Monitoring:**
   - Latencija
   - Throughput
   - Konzistentnost

---
## Praktična Vježba

### Implementacija raspodijeljenog sustava

1. **Postavljanje infrastrukture:**
   - Konfiguracija čvorova
   - Mrežno povezivanje
   - Sigurnosne postavke

2. **Particioniranje podataka:**
   - Definiranje strategije
   - Implementacija shardinga
   - Testiranje performansi

3. **Monitoring i održavanje:**
   - Praćenje metrika
   - Optimizacija upita
   - Backup strategije

---
## Zaključak

### Kada koristiti koji pristup?

- **CloudDB:**
  - Startups i male organizacije
  - Varijabilno opterećenje
  - Brza implementacija

- **Raspodijeljene BP:**
  - Velike organizacije
  - Specifični zahtjevi
  - Kontrola nad infrastrukturom

---
## Pitanja?

### Sada je vrijeme za vaša pitanja!

- Nejasnoće oko arhitekture?
- Praktični problemi?
- Use-case scenariji?

---
## Hvala na Pažnji!

Kontakt informacije:
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko