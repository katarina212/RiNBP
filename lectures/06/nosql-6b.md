---
marp: true
theme: default
paginate: true
---

# Raspodijeljene i nerelacijske baze podataka
# Vektorske baze podataka

Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---

## Sadržaj

- Uvod u vektorske baze podataka
- Vektorske ugradnje (embeddings)
- Arhitektura i principi vektorskih baza podataka
- Algoritmi za pretraživanje vektora
- Usporedba glavnih vektorskih baza podataka
- Primjene u AI i LLM sustavima
- Praktični primjeri korištenja
- Budućnost vektorskih baza podataka

---

## Što su vektorske baze podataka?

- **Specijalizirane NoSQL baze podataka** optimizirane za pohranu i pretraživanje vektorskih ugradnji (embeddings)
- **Vektorske ugradnje** su numeričke reprezentacije podataka u višedimenzionalnom prostoru
- Omogućuju **pretraživanje po sličnosti** umjesto po ključnim riječima ili točnim vrijednostima
- Ključne za moderne **AI i strojno učenje** aplikacije

![bg right:40% 80%](https://db-engines.com/en/ranking/vector+dbms)

---

## Zašto su vektorske baze podataka važne?

- **Eksplozija AI i LLM aplikacija**
  - Generativni AI modeli (ChatGPT, Claude, Llama)
  - Potreba za efikasnom pohranom konteksta i znanja

- **Pretraživanje po semantičkoj sličnosti**
  - Razumijevanje značenja, ne samo ključnih riječi
  - Multimodalno pretraživanje (tekst, slike, zvuk)

- **Skalabilnost za velike količine vektorskih podataka**
  - Milijuni ili milijarde vektora
  - Zahtjevi za brzim odgovorima u milisekundama

---

## Vektorske ugradnje (Embeddings)

**Što su vektorski embeddinzi?**
- Numeričke reprezentacije objekata u višedimenzionalnom prostoru (vektori)
- Slični objekti imaju slične vektorske reprezentacije (blizu u vektorskom prostoru)
- Tipično imaju 100-4000 dimenzija

**Tipovi embeddinga:**
- Tekstualni embeddinzi (dokumenti, rečenice, riječi)
- Slikovni embeddinzi
- Zvučni embeddinzi
- Multimodalni embeddinzi

---

## Kako nastaju vektorske ugradnje?

1. **Ulazni podaci** (tekst, slika, zvuk)
2. **Model za generiranje embeddings** (BERT, OpenAI, CLIP, itd.)
3. **Vektor** (numerička reprezentacija)
4. **Pohrana u vektorsku bazu** za brzo pretraživanje

---

## Princip pretraživanja po sličnosti

- **Mjere udaljenosti/sličnosti**:
  - Euklidska udaljenost (L2)
  - Kosinusna sličnost
  - Manhattanska udaljenost (L1)
  - Mahalanobisova udaljenost

- **kNN (k-nearest neighbors) pretraživanje**:
  - Pronalaženje k najbližih vektora upitnom vektoru
  - Složenost: O(n) za linearno pretraživanje

- **Problem**: Linearno pretraživanje nije praktično za velike baze podataka

---

## Algoritmi za efikasno pretraživanje vektora

**Aproksimativni algoritmi**:

- **LSH (Locality-Sensitive Hashing)**
  - Slični vektori će vjerojatno završiti u istim "bucketima"
  - Kompromis između točnosti i brzine

- **HNSW (Hierarchical Navigable Small World)**
  - Grafovska struktura za brzu navigaciju
  - Bolje performanse od LSH-a, ali zahtjevniji za izgradnju

- **IVF (Inverted File Index)**
  - Podjela prostora u clustere
  - Pretraživanje samo relevantnih clustera

---

## HNSW algoritam - primjer

- Višeslojni graf s "prečacima" za brzo pretraživanje
- Gornji slojevi: rijetke veze za velike skokove
- Donji slojevi: gušće veze za precizno pretraživanje
- Kompleksnost pretraživanja: O(log n)

---

## Komponente vektorske baze podataka

- **Indeksiranje**: Strukturiranje vektora za brzo pretraživanje (HNSW, IVF, FAISS)
- **Pohrana**: Optimizirana za vektore velikih dimenzija
- **Upitni mehanizam**: kNN pretraživanje, filtrirano pretraživanje
- **Metapodaci**: Dodatne informacije uz vektore
- **Skaliranje**: Distribuirano indeksiranje i pretraživanje
- **API**: Integracija s aplikacijama i AI sustavima

---

## Usporedba s tradicionalnim bazama podataka

| Značajka | Vektorske baze | Relacijske baze | Dokumentne baze |
|----------|---------------|-----------------|-----------------|
| **Model podataka** | Vektori | Tablice | Dokumenti |
| **Pretraživanje** | Po sličnosti | Po točnim vrijednostima | Po ključevima i indeksima |
| **Upitni jezik** | Vektorski upiti | SQL | Specifični za bazu |
| **Optimizirano za** | Semantičko pretraživanje | ACID transakcije | Fleksibilnost sheme |
| **Uobičajene primjene** | AI/ML, preporuke | Financije, ERP | Web aplikacije |

---

## Vodeće vektorske baze podataka

- **Pinecone**: Potpuno upravljana cloud vektorska baza
- **Weaviate**: Vektorska baza s podrškom za semantičko pretraživanje
- **Milvus**: Open-source vektorska baza za masivno skaliranje
- **Qdrant**: Vektorska baza s fokusom na filtriranje i metapodatke
- **pgvector**: Ekstenzija za PostgreSQL za vektorske operacije
- **Chroma**: Lightweight vektorska baza za AI aplikacije
- **Redis**: S modulima za vektorsko pretraživanje (RediSearch)
- **Vespa**: Vektorsko pretraživanje i organizacija podataka

---

## Arhitekturalne razlike

**Samostalne vektorske baze (Pinecone, Weaviate, Milvus, Qdrant)**:
- Specijalizirane za vektorske operacije
- Najbolje performanse za slučajeve čistog vektorskog pretraživanja
- Često upravljane kao cloud usluge

**Hibridne i ekstenzije (pgvector, Redis, Elasticsearch)**:
- Dodaju vektorske mogućnosti postojećim bazama podataka
- Omogućuju kombiniranje tradicionalnih i vektorskih upita
- Često korištene kada već postoji infrastruktura s ovim bazama

---

## Pegvector: Vektorsko proširenje za PostgreSQL

```sql
-- Instalacija ekstenzije
CREATE EXTENSION vector;

-- Kreiranje tablice s vektorskim stupcem
CREATE TABLE items (
  id bigserial PRIMARY KEY,
  embedding vector(384),  -- 384-dimenzionalni vektor
  content text,
  metadata jsonb
);

-- Kreiranje indeksa za brzo pretraživanje
CREATE INDEX ON items USING ivfflat (embedding vector_l2_ops)
  WITH (lists = 100);

-- Pretraživanje najsličnijih vektora
SELECT content, 1 - (embedding <=> '[0.1, 0.2, ...]') AS similarity
FROM items
ORDER BY embedding <=> '[0.1, 0.2, ...]'
LIMIT 5;
```

---

## Qdrant: Primjer API korištenja

```python
import qdrant_client as qc
from qdrant_client.http import models

# Spajanje na Qdrant
client = qc.QdrantClient(host="localhost", port=6333)

# Kreiranje kolekcije
client.create_collection(
    collection_name="documents",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)

# Dodavanje vektora
client.upload_points(
    collection_name="documents",
    points=[
        models.PointStruct(
            id=1, vector=[0.1, 0.2, ...],
            payload={"text": "Document content", "category": "article"}
        )
    ]
)

# Pretraživanje
results = client.search(
    collection_name="documents",
    query_vector=[0.1, 0.2, ...],
    limit=5,
    query_filter=models.Filter(must=[models.FieldCondition(key="category", match=models.MatchValue(value="article"))])
)
```

---

## Primjene vektorskih baza podataka

- **Pretraživanje po semantičkoj sličnosti**
  - Pronalaženje dokumenata sličnih upitu, bez obzira na ključne riječi

- **Retrieval Augmented Generation (RAG)**
  - Poboljšanje LLM odgovora s relevantnim dokumentima

- **Sustavi preporuka**
  - Pronalaženje sličnih proizvoda, filmova, sadržaja

- **De-duplikacija podataka**
  - Identificiranje sličnih ili duplikatnih sadržaja

- **Detekcija anomalija**
  - Pronalaženje odstupajućih vektora/podataka

---

## Retrieval Augmented Generation (RAG)


1. **Indeksiranje**: Dokumenti → vektorske ugradnje → vektorska baza
2. **Upitni proces**: Upit → vektorska ugradnja → pretraživanje relevantnih dokumenata
3. **Augmentacija**: Relevantni dokumenti dodani upitu LLM-u
4. **Generiranje**: LLM generira odgovor uz kontekst relevantnih dokumenata

Prednosti: specifični odgovori, manje halucinacija, ažurni podaci, privatnost

---

## RAG arhitektura - primjer koda

```python
from openai import OpenAI
from langchain.vectorstores import Weaviate
from langchain.embeddings import OpenAIEmbeddings

# Inicijalizacija
client = OpenAI()
embeddings_model = OpenAIEmbeddings()
vector_store = Weaviate(client=weaviate_client, embedding=embeddings_model)

# Korisnikov upit
query = "Koji su ključni događaji iz 2023. godine?"

# 1. Dohvati relevantne dokumente
query_embedding = embeddings_model.embed_query(query)
documents = vector_store.similarity_search_by_vector(query_embedding, k=3)

# 2. Izradi kontekst
context = "\n\n".join([doc.page_content for doc in documents])

# 3. Generiraj odgovor s kontekstom
prompt = f"""
Odgovori na sljedeće pitanje koristeći samo informacije iz navedenog konteksta.
Kontekst: {context}

Pitanje: {query}
"""

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
```

---

## Filtriranje i hibridno pretraživanje

- **Metapodaci uz vektore**
  - Kategorije, oznake, datumi, autori...
  - Omogućuju filtrirane upite

- **Hibridno pretraživanje**
  - Kombinacija vektorske sličnosti i tradicionalnog pretraživanja
  - Primjer: tekstualno + semantičko pretraživanje

```python
# Primjer filtriranog pretraživanja u Pinecone
results = index.query(
    vector=query_embedding,
    filter={"category": "science", "date": {"$gte": "2023-01-01"}},
    top_k=5
)
```

---

## Skaliranje vektorskih baza podataka

**Izazovi skaliranja**:
- Veliki broj vektora (milijarde)
- Visoke dimenzije (tisuće)
- Zahtjevi za niskom latencijom
- Potrebe za filterima i metapodacima

**Pristupi**:
- Horizontalno skaliranje (sharding)
- Distribuirano indeksiranje
- Napredne strategije particioniranja
- Kompresija vektora za uštedu prostora
- ANN (Approximate Nearest Neighbor) algoritmi

---

## Optimizacija performansi

- **Strategije indeksiranja**
  - HNSW parametri: `M` (maksimalne veze), `efConstruction`, `ef`
  - Balansiranje između brzine, memorije i točnosti

- **Dimenzionalnost**
  - Smanjenje dimenzija (PCA, t-SNE, UMAP)
  - Kompromis između informativnosti i efikasnosti

- **Kvantizacija**
  - Smanjenje preciznosti brojeva (npr. float32 → float16 ili int8)
  - Značajne uštede prostora uz minimalan gubitak točnosti

- **Denormalizacija metapodataka**
  - Brži filtrirani upiti
  - Memorijski tradeoff

---

## Usporedba performansi

| Baza podataka | Latencija (p95, ms) | Propusnost (QPS) | Max. vektora | Točnost (recall@10) |
|---------------|---------------------|------------------|--------------|---------------------|
| Pinecone      | 10-50               | 1000+            | Milijarde    | >90%                |
| Weaviate      | 20-100              | 500+             | Stotine milijuna | >90%           |
| pgvector      | 50-200              | 100+             | Milijuni     | >85%                |
| Qdrant        | 10-50               | 800+             | Milijarde    | >90%                |
| Milvus        | 5-30                | 2000+            | Milijarde    | >90%                |

*Napomena: Vrijednosti su okvirne i ovise o konfiguraciji, hardveru i slučaju korištenja*

---

## Sigurnosni aspekti

- **Privatnost podataka**
  - Vektorske ugradnje mogu sadržavati osjetljive informacije
  - Moguća rekonstrukcija originalnih podataka iz vektora

- **Autentikacija i autorizacija**
  - Granularna kontrola pristupa kolekcijama i vektorima
  - API ključevi i token-bazirani pristup

- **Enkripcija**
  - Enkripcija podataka u mirovanju i transportu
  - Izazov: efikasno pretraživanje enkriptiranih vektora

- **Regulatorna usklađenost**
  - GDPR, HIPAA, CCPA i ostale regulacije

---

## Praktični primjer 1: Sustav preporuka proizvoda

```python
# 1. Priprema podataka
product_descriptions = ["Smartphone with 6.1'' display", "Wireless earbuds", ...]
product_ids = [101, 102, ...]

# 2. Generiranje embeddings-a
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(product_descriptions)

# 3. Pohrana u vektorsku bazu
from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient("localhost", port=6333)
client.create_collection(
    collection_name="products",
    vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE)
)

# Dodavanje u bazu
points = [
    models.PointStruct(id=id, vector=embedding, payload={"description": desc})
    for id, embedding, desc in zip(product_ids, embeddings, product_descriptions)
]
client.upload_points("products", points=points)

# 4. Pretraživanje sličnih proizvoda
query = "wireless headphones with noise cancellation"
query_embedding = model.encode(query)
results = client.search("products", query_vector=query_embedding, limit=5)
```

---

## Praktični primjer 2: Chatbot koji koristi dokumentaciju

```python
# 1. Parsiranje dokumentacije
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

# Učitaj PDF
pdf_reader = PyPDF2.PdfReader('product_manual.pdf')
text = ""
for page in pdf_reader.pages:
    text += page.extract_text()

# Podijeli u chunkove
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_text(text)

# 2. Stvori embeddings i vektorsku bazu
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(texts=chunks, embedding=embeddings)

# 3. Implementacija odgovora na upite
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 4. Odgovaranje na upit
question = "How do I reset my device to factory settings?"
answer = qa_chain.run(question)
print(answer)
```

---

## Budući trendovi vektorskih baza podataka

- **Dublja integracija s LLM ekosustavom**
  - Specijalizirani AI agenati za rad s vektorskim bazama
  - Standardizacija RAG obrazaca

- **Optimizacija za specifične domene**
  - Vektorske baze za medicinske podatke, pravne dokumente, itd.
  - Domain-specific embedding modeli

- **Hibridni pristupi**
  - Fuzija grafovskih, relacijskih i vektorskih mogućnosti
  - Multi-modal pretraživanje (tekst, slike, audio)

- **Edge AI integracija**
  - Vektorske baze na edge uređajima (mobitelima, IoT)
  - Decentralizirani vektorski indeksi

---

## Izazovi i ograničenja

- **Kompleksnost indeksiranja**
  - Potrebno znanje za odabir pravih parametara
  - Izazovnost balansiranja performansi i točnosti

- **Cold-start problem**
  - Potrebni inicijalni podaci za efektivno pretraživanje
  - Izazov kod novih sustava

- **Semantički jaz**
  - Ograničenja embeddinga u hvatanju svih nijansi značenja
  - Kontekstualna ograničenja

- **Skalabilnost i troškovi**
  - Veliki indeksi zahtijevaju značajne resurse
  - Potreba za optimizacijom troškova

---

## Kako odabrati vektorsku bazu podataka?

**Ključni faktori za razmatranje:**

- **Volumen podataka**: Koliko vektora trebate pohraniti?
- **Dimenzionalnost**: Koliko dimenzija imaju vaši vektori?
- **Zahtjevi za latencijom**: Potrebno vrijeme odgovora?
- **Potrebe za skalabilnošću**: Očekujete li značajan rast?
- **Filtriranje i metapodaci**: Koliko su važni za vaš slučaj?
- **Infrastrukturna ograničenja**: On-premise vs. cloud?
- **Budget**: Samohostirano vs. upravljana usluga?
- **Integracijske potrebe**: S kojim se sustavima morate integrirati?

---

## Sažetak

- **Vektorske baze podataka** su specijalizirane za pohranu i pretraživanje vektorskih ugradnji
- Omogućuju **pretraživanje po sličnosti** umjesto po točnim vrijednostima
- Koriste napredne algoritme poput **HNSW i IVF** za brzo pretraživanje
- Ključne za moderne aplikacije: **RAG, preporuke, semantičko pretraživanje**
- Različite implementacije: **Pinecone, Weaviate, pgvector, Milvus, Qdrant**
- Budući trendovi uključuju **dublju integraciju s AI** i **specijalizaciju za domene**

---


**Dataset primjeri:**
- https://www.kaggle.com/datasets
- Vremenske prognoze: https://github.com/zonination/weather-us/blob/master/boston.csv
- New York taxi: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page