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
## Od JSON-a do MongoDB-a

### Evolucija pohrane podataka

- **JSON kao temelj:** Prirodna evolucija iz XML-a
- **Document-Oriented pristup:** Fleksibilnost i skalabilnost
- **MongoDB:** Najpopularnija document-oriented baza podataka
- **BSON format:** Binary JSON - optimizirana verzija JSON-a

---
## Što je MongoDB?

### Osnovne karakteristike

- **Document-oriented baza podataka**
- **Schemaless dizajn:** Fleksibilna struktura dokumenata
- **Horizontalna skalabilnost**
- **Visoke performanse**
- **Bogat query jezik**

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
## MongoDB Schema Design

### Best Practices

- **Embedding vs Referencing**
- **Kada koristiti koji pristup?**
- **Modeliranje One-to-Many veza**
- **Modeliranje Many-to-Many veza**
- **Denormalizacija za performanse**

---
## Praktični primjer: Blog aplikacija

### Model podataka

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
## Update operacije detaljnije

### Različiti načini ažuriranja

```javascript
// Ažuriranje jednog dokumenta
db.users.updateOne(
  { name: "Ana Horvat" },
  { $set: { age: 26 } }
)

// Ažuriranje više dokumenata
db.users.updateMany(
  { city: "Split" },
  { $inc: { age: 1 } }
)

// Zamjena cijelog dokumenta
db.users.replaceOne(
  { name: "Ana Horvat" },
  { name: "Ana Novak", age: 26, city: "Zagreb" }
)
```

---
## Array Update Operatori

### Rad s poljima

```javascript
// Dodavanje u polje
db.users.updateOne(
  { name: "Ana Horvat" },
  { $push: { hobbies: "yoga" } }
)

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

// Pretraživanje po ugniježđenim objektima
db.orders.find({
  "shipping.address.city": "Split",
  "items.quantity": { $gt: 2 }
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
## Agregacijski Pipeline: Napredni Primjeri

### Kompleksna analiza podataka

```javascript
// Analiza prodaje po kategorijama i mjesecima
db.sales.aggregate([
  { $match: {
      date: {
        $gte: ISODate("2024-01-01"),
        $lt: ISODate("2025-01-01")
      }
    }
  },
  { $group: {
      _id: {
        category: "$category",
        month: { $month: "$date" }
      },
      totalSales: { $sum: "$amount" },
      avgOrder: { $avg: "$amount" },
      count: { $sum: 1 }
    }
  },
  { $sort: { "_id.month": 1, "totalSales": -1 } }
])
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

### Best Practices

- **Indeksi:**
  - Kreiranje indeksa za česte upite
  - Izbjegavanje nepotrebnih indeksa
  - Monitoring korištenja indeksa

- **Queries:**
  - Korištenje covered queries
  - Izbjegavanje regex bez prefiksa
  - Limitiranje rezultata

- **Schema Design:**
  - Pravilno modeliranje za use-case
  - Balansiranje između denormalizacije i normalizacije
  - Izbjegavanje preduboko ugniježđenih dokumenata

---
## Monitoring i Održavanje

### Alati i prakse

- **MongoDB Compass:**
  - Performance insights
  - Query optimization
  - Schema visualization

- **MongoDB Atlas:**
  - Cloud monitoring
  - Backup & restore
  - Scaling operations

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

### Ključne funkcionalnosti

- **Cluster Management:**
  - Automatsko skaliranje
  - Self-healing recovery
  - Backup i restore
  - Multi-region deployment

- **Sigurnost:**
  - Network isolation
  - IP whitelisting
  - VPC peering
  - End-to-end encryption

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

- **Realm:**
  - Backend as a Service
  - Serverless funkcije
  - Mobile sync

---
## Atlas Best Practices

### Optimizacija troškova i performansi

- **Cluster Sizing:**
  - Odabir pravog tier-a
  - Auto-scaling postavke
  - Resource limits

- **Monitoring:**
  - Performance Advisor
  - Real-time metrics
  - Custom alerts

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

---
## Pitanja?

### Sada je vrijeme za vaša pitanja!

- Nejasnoće oko MongoDB-a?
- Praktični problemi?
- Use-case scenariji?

---
## Hvala na Pažnji!

Kontakt informacije:
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko