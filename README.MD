Absolutely, I can provide a `README.md` in Swedish for your project. Since the repository is for personal use among friends, I'll exclude the contributing section. Here's the adapted `README.md`:

# Enkelt API för Skadeberäkning till Eon 4

### API Endpoints
- `GET /injury_effects`: Beräkna effekter av skador.
  - Parametrar:
    - `injury_type` (sträng): Typ av skada (t.ex. 'Stickskada mot ben').
    - `damage` (heltal): Mängden skada som tillfogats.
    - `table_modifier` (heltal): Valbar modifierare för skadetabellen (ej obligatorisk).
    - `verbose` (True/False): För felsökning (ej obligatorisk).

### Exempel på anrop
```
curl --location 'http://localhost:5000/injury_effects?injury_type=Stickskada%20mot%20ben&damage=25&table_modifier=1&verbose=false'
