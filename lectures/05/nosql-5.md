---
marp: true
theme: gaia
title: Raspodijeljene i nerelacijske baze podataka - MongoDB
description: Nikola Balić, MongoDB
paginate: true
---

# MongoDB i Document-Oriented Databases

### Akademska godina 2024/2025
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---
## MongoDB — Lider NoSQL Svijeta

MongoDB je danas najpopularnija NoSQL baza podataka, sa 45.86% tržišnog udjela (2025.), daleko ispred konkurencije kao što su Amazon DynamoDB (10.67%) i Apache Cassandra (4.18%).

- **Prava tehnologija u pravom trenutku:** Prvi open-source release dolazi 2009., upravo kad web i mobilne aplikacije eksplodiraju i kad *cloud* postaje industrijski standard.
- MongoDB je odmah adresirao problem: **Skalabilnost i visoke performanse** za internet aplikacije s velikim i promjenjivim podatkovnim modelima
- MongoDB *developer-first* pristup

---
## Od JSON-a do Dokument pristupa

### Evolucija pohrane podataka

- **XML kao prethodnik:** Struktuirani podaci, ali često preopširan.
- **JSON kao prirodna evolucija:**
    - Lakši, čitljiviji format, sličan JavaScript objektima.
    - Postao *de facto* standard za web API-je i konfiguracije.
- **Potreba za fleksibilnošću:** Relacijske baze imaju krutu shemu; JSON nudi fleksibilnost.
- **Document-Oriented pristup:** Pohrana podataka u obliku dokumenata omogućavajući fleksibilnost i skalabilnost.

---
## MongoDB i BSON

### Specijalizirani pristup za baze podataka

- **MongoDB:** Vodeća *document-oriented* baza podataka.
- **BSON (Binary JSON):**
    - Binarni format za serijalizaciju JSON-like dokumenata.
    - Optimiziran za brzinu, prostor i efikasnost pretraživanja.
    - Dodaje dodatne tipove podataka (npr. `ObjectId`, `Date`, binarne podatke).

---

```json
// Primjer JSON i BSON dokumenta
{"hello": "world"} →

\x16\x00\x00\x00           // total document size
\x02                       // 0x02 = type String
hello\x00                  // field name
\x06\x00\x00\x00world\x00  // field value
\x00                       // 0x00 = type EOO ('end of object')
```

---
## Osnovne karakteristike MongoDB-a

- **Document-oriented baza podataka**
- **Schemaless dizajn:** Fleksibilna struktura dokumenata
- **Horizontalna skalabilnost**
- **Visoke performanse**
- **Bogat query jezik**

---
## Što znači "Schemaless"?

- **Fleksibilnost:** Dokumenti u istoj kolekciji *ne moraju* imati istu strukturu (ista polja i tipove podataka).
- **Primjer:** Jedan dokument korisnika može imati polje `middle_name`, dok drugi nema.
- **Evolucija aplikacije:** Lakše je dodavati nova polja bez migracije cijele baze.
- **Oprez:** Prevelika fleksibilnost može dovesti do nedosljednosti podataka.
- **Rješenje:** *Schema Validation* - Mogućnost definiranja pravila za strukturu dokumenata (opcionalno).

---
## MongoDB vs Relacijske baze

### Ključne razlike

| Relacijske BP | MongoDB |
|---------------|---------|
| Tablice | Kolekcije |
| Redci | Dokumenti |
| Stupci | Polja |
| JOIN | $lookup |
| Primarni ključ | _id polje |

---
## `$lookup` - MongoDB ekvivalent za JOIN

- Koristi se unutar **agregacijskog pipeline-a**.
- Omogućuje spajanje dokumenata iz dvije kolekcije.
- **Sintaksa:**
```javascript
{
  $lookup:
    {
      from: <kolekcija_za_spajanje>,
      localField: <polje_iz_trenutne_kolekcije>,
      foreignField: <polje_iz_druge_kolekcije>,
      as: <naziv_novog_polja_s_rezultatima>
    }
}
```

---
## MongoDB dokumenti

### Struktura i format

```json
{
  "_id": ObjectId("5f7d3b2e1c9d440000f5c7a1"),
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "country": "USA"
  },
  "hobbies": ["reading", "swimming"]
}
```

---
## CRUD operacije u MongoDB-u

### Create, Read, Update, Delete

- **Create:** `insertOne()`, `insertMany()`
- **Read:** `find()`, `findOne()`
- **Update:** `updateOne()`, `updateMany()`
- **Delete:** `deleteOne()`, `deleteMany()`

---
## Primjer CRUD operacija

### Create
```javascript
db.users.insertOne({
  name: "Ana Horvat",
  age: 25,
  city: "Split"
})
```

### Read
```javascript
db.users.find({ city: "Split" })
```

---
## MongoDB Query Operators

### Najčešće korišteni operatori

- **Usporedba:** `$eq`, `$gt`, `$lt`, `$in`
- **Logički:** `$and`, `$or`, `$not`
- **Element:** `$exists`, `$type`
- **Array:** `$all`, `$elemMatch`
- **Agregacija:** `$group`, `$sum`, `$avg`

---
## Agregacijski Pipeline

### Obrada i transformacija podataka

```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: {
      _id: "$customer",
      totalSpent: { $sum: "$amount" }
    }
  },
  { $sort: { totalSpent: -1 } }
])
```

---
## Indeksi u MongoDB-u

### Optimizacija performansi

- **Single Field Index**
- **Compound Index**
- **Multikey Index** (za arrays)
- **Text Index**
- **Geospatial Index**

---
## Indeksi: Kreiranje i Analiza

- **Kako indeksi rade?** Obično koriste B-tree strukturu za brzo pronalaženje dokumenata.
- **Kreiranje indeksa:**
```javascript
// Jednostavni indeks (ascending)
db.users.createIndex( { "age": 1 } )

// Compound index (na više polja)
db.products.createIndex( { "category": 1, "price": -1 } ) // 1=asc, -1=desc

// Jedinstveni indeks (unique)
db.users.createIndex( { "email": 1 }, { unique: true } )
```

---
## Schema Design: Embedding vs. Referencing

- **Embedding (ugrađivanje):** Pohranjivanje povezanih podataka unutar istog dokumenta.
  - **Primjer:** Komentari unutar dokumenta posta.
  - **Prednosti:** Brži dohvat podataka (jedan upit), atomske operacije na dokumentu.
  - **Nedostaci:** Ograničenje veličine dokumenta (16MB), potencijalno veći dokumenti, duplikacija podataka ako se isti pod-dokument koristi na više mjesta.

---

- **Referencing (Referenciranje):** Pohranjivanje reference (obično `_id`) na dokument u drugoj kolekciji.
  - **Primjer:** Pohranjivanje `author_id` u postu, a detalji autora su u `users` kolekciji.
  - **Prednosti:** Manji dokumenti, nema duplikacije, lakše ažuriranje referenciranih podataka na jednom mjestu.
  - **Nedostaci:** Potrebni dodatni upiti (`$lookup`) za dohvat povezanih podataka (sporije čitanje).

---
## Schema Design: Modeliranje Veza

- **One-to-Few:**
  - **Embedding:** Gotovo uvijek najbolji izbor. Primjer: Adrese korisnika.
- **One-to-Many:**
  - **Embedding:** Dobro ako "mnogo" nije preveliko i podaci se čitaju zajedno (npr. komentari posta).
  - **Referencing:** Bolje ako "mnogo" može biti veliko ili se podaci često ažuriraju neovisno (npr. proizvodi i narudžbe).

---

- **Many-to-Many (Mnogo-na-mnogo):**
  - **Two-way Referencing:** Svaki dokument sadrži listu referenci na drugu stranu (npr. studenti i kolegiji - student ima listu `course_ids`, kolegij ima listu `student_ids`).
  - **One-way Referencing:** Jedna strana sadrži listu referenci (npr. post ima listu `tag_ids`).
  - **Embedding:** Rijetko, samo ako je jedna strana veze vrlo mala.

---
## Schema Design: Denormalizacija i Trade-offs

- **Denormalizacija:** Dupliciranje podataka u više dokumenata radi optimizacije čitanja.
  - **Primjer:** Pohranjivanje imena autora unutar svakog posta, iako postoji i u `users` kolekciji.
  - **Prednosti:** Smanjuje potrebu za `$lookup`, ubrzava čitanje.
  - **Nedostaci:** Povećava složenost ažuriranja (podatak treba ažurirati na više mjesta), veća potrošnja prostora, potencijalna nekonzistentnost.

---

- **Ključni Ustupci:**
  - **Embedding:** Optimizirano za čitanje, ali može otežati ažuriranje i ograničiti veličinu.
  - **Referencing:** Optimizirano za ažuriranje i konzistentnost, ali zahtijeva više upita za čitanje.
  - **Denormalizacija:** Optimizirano za čitanje, ali komplicira ažuriranje i povećava rizik nekonzistentnosti.

- **Pristup:** Odabrati modeliranje prema **najčešćim obrascima pristupa podacima (query patterns)**.

---
## Praktični primjer: Blog aplikacija

```javascript
// Post dokument
{
  "_id": ObjectId(),
  "title": "Uvod u MongoDB",
  "content": "MongoDB je NoSQL baza...",
  "author": {
    "_id": ObjectId(),
    "name": "Ana Horvat"
  },
  "comments": [
    {
      "_id": ObjectId(),
      "text": "Odličan članak!",
      "user": "Marko"
    }
  ],
  "tags": ["nosql", "mongodb", "database"]
}
```

---
## MongoDB Compass

### GUI alat za MongoDB

- **Vizualizacija podataka**
- **CRUD operacije kroz sučelje**
- **Agregacijski pipeline builder**
- **Performance insights**
- **Schema analysis**

---
## Replikacija i Sharding

### Skalabilnost i visoka dostupnost

- **Replica Set:** Automatska replikacija podataka
- **Sharding:** Horizontalno skaliranje
- **Load Balancing:** Distribucija opterećenja
- **Automatic Failover:** Visoka dostupnost

---
## Mehanizmi Skalabilnosti i Dostupnosti

- **Replica Set Detaljnije:**
  - **Primary:** Jedan član koji prima sve zapise (write operacije).
  - **Secondaries:** Više članova koji repliciraju podatke s Primary čvora. Mogu služiti za čitanje (read operacije).
  - **Arbiter (opcionalno):** Član koji ne pohranjuje podatke, ali sudjeluje u izboru novog Primary čvora (election) u slučaju pada trenutnog.
  - **Failover:** Automatski proces izbora novog Primary čvora ako trenutni postane nedostupan.

---

- **Sharding Detaljnije:**
  - **Shards:** Pojedinačni Replica Setovi koji pohranjuju dio ukupnih podataka.
  - **Shard Key:** Polje (ili više polja) u dokumentima koje određuje na koji Shard dokument pripada.
  - **Chunks:** Rasponi vrijednosti Shard Key-a; MongoDB automatski distribuira chunkove po Shardovima.
  - **Mongos:** Router proces koji prima upite od aplikacije i usmjerava ih na odgovarajuće Shardove.
  - **Config Servers:** Pohranjuju meta-podatke o clusteru (mapiranje chunkova na shardove).

---
## Sigurnost u MongoDB-u

### Osnovne sigurnosne prakse

- **Autentikacija i Autorizacija**
- **Role-Based Access Control (RBAC)**
- **Transport Layer Security (TLS/SSL)**
- **Encryption at Rest**
- **Audit Logging**

---
## Praktična vježba

### Implementacija Blog API-ja

1. **Postavljanje MongoDB okruženja**
2. **Kreiranje modela podataka**
3. **Implementacija CRUD operacija**
4. **Dodavanje indeksa**
5. **Implementacija pretraživanja**

---

```sh
docker run -d \
  --name demo-mongo \
  -p 27017:27017 \
  mongo:latest
```

```javascript
docker exec -it demo-mongo mongosh
```

```javascript
use myDemoDB
```

```javascript
db.users.insertOne({ name: "Alice", age: 25, joined: new Date() })
```

```javascript
db.users.find().pretty()
```

```javascript
db.users.deleteOne({ name: "Alice" })
```

---
## Array Update Operatori

### Rad s poljima

```javascript
// Dodavanje više vrijednosti
db.users.updateOne(
  { name: "Ana Horvat" },
  { $push: {
      hobbies: {
        $each: ["yoga", "painting"],
        $sort: 1
      }
    }
  }
)
```

---

```javascript
// Uklanjanje iz polja
db.users.updateOne(
  { name: "Ana Horvat" },
  { $pull: { hobbies: "swimming" } }
)
```

---
## Kompleksni upiti

### Napredni primjeri pretraživanja

```javascript
// Kombinacija uvjeta
db.users.find({
  $and: [
    { age: { $gte: 18, $lte: 30 } },
    { city: { $in: ["Split", "Zagreb"] } },
    { "address.country": "Croatia" }
  ]
})
```

---
## Text Search

### Pretraživanje teksta

```javascript
// Kreiranje text indeksa
db.posts.createIndex({ title: "text", content: "text" })

// Pretraživanje teksta
db.posts.find({
  $text: {
    $search: "mongodb nosql",
    $language: "croatian"
  }
})
```

---

```javascript
// Sortiranje po relevantnosti
db.posts.find(
  { $text: { $search: "mongodb" } },
  { score: { $meta: "textScore" } }
).sort({ score: { $meta: "textScore" } })
```

---
## Geospatial Queries

### Rad s lokacijskim podacima

```javascript
// Kreiranje 2dsphere indeksa
db.places.createIndex({ location: "2dsphere" })

// Pronalaženje lokacija u krugu
db.places.find({
  location: {
    $near: {
      $geometry: {
        type: "Point",
        coordinates: [16.4401, 43.5081] // Split koordinate
      },
      $maxDistance: 10000 // 10km radius
    }
  }
})
```

---
## Transactions u MongoDB-u

### Održavanje konzistentnosti podataka

```javascript
// Primjer transakcije
const session = db.getMongo().startSession();
session.startTransaction();

try {
  // Prebacivanje novca s jednog računa na drugi
  db.accounts.updateOne(
    { _id: fromAccountId },
    { $inc: { balance: -amount } },
    { session }
  );

  db.accounts.updateOne(
    { _id: toAccountId },
    { $inc: { balance: amount } },
    { session }
  );

  // Dodavanje zapisa transakcije
  db.transactions.insertOne({
    from: fromAccountId,
    to: toAccountId,
    amount: amount,
    date: new Date()
  }, { session });

  await session.commitTransaction();
} catch (error) {
  await session.abortTransaction();
  throw error;
} finally {
  session.endSession();
}
```

---
## Schema Validation

### Osiguravanje kvalitete podataka

```javascript
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email", "age"],
      properties: {
        name: {
          bsonType: "string",
          description: "must be a string and is required"
        },
        email: {
          bsonType: "string",
          pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
          description: "must be a valid email address"
        },
        age: {
          bsonType: "int",
          minimum: 18,
          description: "must be an integer >= 18"
        }
      }
    }
  }
})
```

---
## Change Streams

### Praćenje promjena u realnom vremenu

```javascript
// Otvaranje change stream-a
const changeStream = db.collection('users').watch();

// Praćenje promjena
changeStream.on('change', (change) => {
  console.log('Detected change:', change);

  if (change.operationType === 'insert') {
    console.log('New user:', change.fullDocument);
  } else if (change.operationType === 'update') {
    console.log('Updated fields:', change.updateDescription.updatedFields);
  } else if (change.operationType === 'delete') {
    console.log('Deleted document ID:', change.documentKey._id);
  }
});
```

---
## Praktični Primjer: E-commerce sustav

### Model podataka

```javascript
// Proizvod
{
  "_id": ObjectId(),
  "name": "Laptop XYZ",
  "price": 999.99,
  "category": "Electronics",
  "specs": {
    "cpu": "Intel i7",
    "ram": "16GB",
    "storage": "512GB SSD"
  },
  "inStock": 50,
  "tags": ["laptop", "electronics", "computers"]
}

// Narudžba
{
  "_id": ObjectId(),
  "user": {
    "_id": ObjectId(),
    "name": "Marko Marić",
    "email": "marko@example.com"
  },
  "items": [
    {
      "productId": ObjectId(),
      "name": "Laptop XYZ",
      "quantity": 1,
      "price": 999.99
    }
  ],
  "total": 999.99,
  "status": "processing",
  "shipping": {
    "address": {
      "street": "Ulica bb",
      "city": "Split",
      "country": "Croatia"
    },
    "method": "express",
    "tracking": "HR123456789"
  },
  "orderDate": ISODate("2024-03-31T10:00:00Z")
}
```

---
## Performance Optimization

- **Indeksi:**
  - Kreiranje indeksa za česte upite
  - Izbjegavanje nepotrebnih indeksa
  - Monitoring korištenja indeksa

- **Queries:**
  - Korištenje covered queries
  - Izbjegavanje regex bez prefiksa
  - Limitiranje rezultata

---

- **Schema Design:**
  - Pravilno modeliranje za use-case
  - Balansiranje između denormalizacije i normalizacije
  - Izbjegavanje preduboko ugniježđenih dokumenata

---
## Monitoring i Održavanje

- **MongoDB Compass:**
  - Performance insights
  - Query optimization
  - Schema visualization

- **MongoDB Atlas:**
  - Cloud monitoring
  - Backup & restore
  - Scaling operations

---

- **Mongosh:**
  - Administrative tasks
  - Query debugging
  - Performance analysis

---
## MongoDB Atlas

### Cloud Database as a Service

- **Što je Atlas?**
  - Potpuno upravljana cloud usluga za MongoDB
  - Automatsko skaliranje i održavanje
  - Globalna distribucija podataka
  - Integrirani monitoring i alerting

---
## Atlas Mogućnosti

- **Cluster Management:**
  - Automatsko skaliranje
  - Self-healing recovery
  - Backup i restore
  - Multi-region deployment

- **Sigurnost:**
  - Network isolation
  - IP whitelisting
  - VPC peering, End-to-end encryption

---
## Atlas Setup

### Postavljanje prvog clustera

```javascript
// 1. Kreiranje besplatnog clustera
// Odabir M0 Free Tier opcije
// Odabir cloud providera (AWS, GCP, Azure)
// Odabir regije (npr. eu-central)

// 2. Konfiguracija mrežnog pristupa
// Dodavanje IP adrese: 0.0.0.0/0 (development)
whitelist: ["193.198.xxx.xxx"] // PMF IP

// 3. Kreiranje database korisnika
{
  "username": "pmfst_user",
  "password": "******",
  "roles": ["readWrite"]
}
```

---
## Atlas Connection

### Povezivanje s aplikacijom

```javascript
// Connection string format
mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/myDatabase

// Primjer Node.js connection
const { MongoClient } = require('mongodb');

const uri = "mongodb+srv://pmfst_user:******@cluster0.xxxxx.mongodb.net/myDatabase";
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

async function connect() {
  try {
    await client.connect();
    console.log("Connected to MongoDB Atlas");
  } catch (error) {
    console.error("Connection error:", error);
  }
}
```

---
## Atlas Search

### Full-text pretraživanje

```javascript
// 1. Kreiranje Atlas Search indeksa
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "description": {
        "type": "string",
        "analyzer": "lucene.croatian"
      }
    }
  }
}

// 2. Pretraživanje s Atlas Search
db.products.aggregate([
  {
    $search: {
      "text": {
        "query": "laptop gaming",
        "path": "description",
        "fuzzy": {
          "maxEdits": 1
        }
      }
    }
  },
  {
    $limit: 10
  }
])
```

---
## Atlas Services

### Dodatne usluge

- **Charts:**
  - Interaktivne vizualizacije
  - Real-time dashboards
  - Embedding u aplikacije

- **Data Lake:**
  - Analiza podataka na S3/GCS
  - Federated queries
  - BI integracija

---
## Atlas optimizacija troškova i performansi

- **Cluster Sizing:**
  - Odabir pravog tier-a
  - Auto-scaling postavke
  - Resource limits

- **Monitoring:**
  - Performance Advisor
  - Real-time metrics
  - Custom alerts

---

- **Backup Strategy:**
  - Continuous backup
  - Point-in-time recovery
  - Cross-region backup

---
## Zaključak

### Zašto MongoDB?

- **Fleksibilnost schema-less dizajna**
- **Horizontalna skalabilnost**
- **Jednostavnost korištenja**
- **Bogat ekosustav**
- **Velika zajednica korisnika**
