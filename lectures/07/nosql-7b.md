---
marp: true
theme: gaia
title: Raspodijeljene i nerelacijske baze podataka - SpacetimeDB
description: Nikola Balić, Raspodijeljene baze podataka
paginate: true
---

# SpacetimeDB

### Akademska godina 2024/2025
Nikola Balić
nikola.balic@gmail.com
github.com/nkkko

---
## Uvod

- **SpacetimeDB** je relacijska baza podataka koja **integrira aplikacijsku logiku** direktno u samu bazu
- Eliminira potrebu za zasebnim web ili game serverima
- Podržava više programskih jezika (C#, Rust)
- **WebAssembly moduli** - aplikacijski kod izvršava se unutar baze
- Optimizirana za **visoku propusnost i nisku latenciju** za multiplayer aplikacije poput igara

---
## Što je WebAssembly (WASM)?

- **Binarni format** niske razine za izvršavanje koda u web preglednicima i izvan njih
- Ključne karakteristike:
  - **Performanse**: Izvršava se blizu nativne brzine
  - **Sigurnost**: Sandbox okruženje, striktne memorijske granice
  - **Višejezičnost**: Može se generirati iz Rust, C++, C#, AssemblyScript, itd.
  - **Portabilnost**: Izvršava se na različitim platformama i arhitekturama
- U kontekstu SpacetimeDB: izolirana, sigurna izvršna okolina za serverski kod

---
## Ključni koncepti

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────────┐
│     Tablice     │◄───────►│    Reduceri     │◄───────►│  Subscription upiti │
│  (Rel. baza)    │         │   (WASM kod)    │         │    (WebSocket)      │
└─────────────────┘         └─────────────────┘         └─────────────────────┘
```

- **Tablice**: Relacijske tablice slične onima u PostgreSQL-u
- **Reduceri**: Atomske, transakcijske RPC funkcije definirane u WebAssembly modulu
- **Subscription upiti**: SQL upiti koji se izvršavaju preko WebSocket veze

---
## Arhitektura podataka

- **In-memory pohrana** - svi podaci u tablicama pohranjeni u memoriju
- **Trajnost** kroz Write-Ahead Log (WAL) nazvan Commitlog
- **Klijentske biblioteke** generiraju se automatski na temelju definiranih tablica i reducera
- **Subscription upiti** omogućuju klijentu pohranu parcijalne, ažurirane replike stanja servera
- **Ekstremno niska latencija** za čitanje na klijentu (lokalno iz replike)

---
## Write-Ahead Log (Commitlog u Spacetime)

- **Princip rada**:
  - Svaka promjena prvo se zapisuje u log datoteku na disk
  - Tek nakon potvrde zapisa, promjena se primjenjuje u memoriji
  - U slučaju pada sustava, stanje se rekonstruira ponovnim izvršavanjem zapisa iz loga
- **Prednosti**:
  - Atomarnost transakcija i osiguranje protiv gubitka podataka
  - Brzi oporavak nakon pada sustava
  - Optimizirano za sekvencijalni upis (visoka performansa)

---
## Definiranje podatkovnog modela

```rust
// Rust primjer
#[table(name = player_state, public)]
pub struct PlayerState {
    #[primary_key]
    player_id: Identity,
    name: String,
    health: u32,
    position: Position,
}
```

---
## Reduceri (Serverska logika)

```rust
// Rust primjer
#[reducer]
pub fn move_player(ctx: &ReducerContext, x: i32, y: i32) -> Result<(), String> {
    let sender_id = ctx.sender;

    // Pronađi igrača po primary key-u
    if let Some(mut player) = ctx.db.player_state().player_id().find(&sender_id) {
        // Ažuriraj poziciju
        player.position = Position { x, y };
        // Spremi promjene
        ctx.db.player_state().player_id().update(player);
        Ok(())
    } else {
        Err("Igrač nije pronađen".to_string())
    }
}
```

---
## Subscription upiti

- **Klijent** se pretplaćuje na podatke u bazi putem SQL upita
- **Inicijalni podaci** šalju se pri uspostavi pretplate
- **Inkrementalne promjene** šalju se automatski kod promjene podataka
- **WebSocket veza** koristi se za dvosmjernu komunikaciju

```typescript
// TypeScript primjer pretplate
conn.subscriptionBuilder()
    .onApplied(() => console.log("Pretplata uspostavljena"))
    .subscribe(["SELECT * FROM player_state WHERE health > 0"]);
```

---
## Autentifikacija

- Koristi **OpenID Connect** protokol
- `Identity` tip izračunava se iz `iss`/`sub` para pomoću BLAKE3 hash algoritma
---

```
┌────────────────────────────── 32 bajta ───────────────────────────┐
│                                                                    │
│  ┌────┬────┬───────────────────┬───────────────────────────────┐  │
│  │0xc2│0x00│ Checksum Hash(4B) │         ID Hash (26B)         │  │
│  └────┴────┴───────────────────┴───────────────────────────────┘  │
│          │                      │                                  │
│          └─ Prvi 4B od          └─ Prvih 26B od                   │
│             BLAKE3(0xc200||idHash)  BLAKE3(iss|sub)               │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

- Omogućuje integraciju s OIDC providerima poput Firebase Auth, Auth0, itd.

---
## Proizvodi i varijante

| Proizvod | Opis |
|----------|------|
| **SpacetimeDB Standalone** | Source available, single-node, self-hosted verzija |
| **SpacetimeDB Maincloud** | Hosted, managed-service, serverless cluster |
| **SpacetimeDB Enterprise** | Closed-source, klasterizirana verzija (na zahtjev) |

---
## Primjer instalacije

1. **Instalacija**: `curl -sSf https://install.spacetimedb.com | sh`
2. **Inicijalizacija modula**: `spacetime init --lang rust my_module`
3. **Definiranje sheme**: Tablice, reduceri, tipovi u izvornom kodu
4. **Build modula**: `spacetime build --project-path my_module`
5. **Objava**: `spacetime publish --project-path my_module my-database`
6. **Generiranje klijenta**: `spacetime generate --lang typescript ...`
7. **Razvoj klijenta**: Povezivanje, pretplata, pozivi reducera

---

| Aspekt | SpacetimeDB | MongoDB | Redis |
|--------|-------------|---------|-------|
| **Model podataka** | Relacijski | Dokumentni | Key-Value |
| **Aplikacijska logika** | Unutar baze | Izvan baze | Ograničena (Lua) |
| **Latencija čitanja** | Ekstremno niska (lokalno) | Niska | Vrlo niska |
| **Latencija pisanja** | Niska-srednja | Niska | Vrlo niska |
| **Tipovi klijenata** | Standardizirani | Vlastiti | Raznovrsni |
