# RiskSimulator
Simulates Risk

[Click here](https://www.youtube.com/watch?v=dQw4w9WgXcQ) to learn more about the math behind the game!


# DB:

Start DB with:

```
.\db\pocketbase serve
```

Admin UI:

http://127.0.0.1:8090/_/

Credentials:

admin@risk-simulator.de

RiskSimulator

# Api:

Start with:

```
cd .\server\; node .\index.js  
```

http://localhost:8080/

## /games

Get:

Get all games

Returns: 
```
[
  {
    "id": "73ro8umvyguaby8",
    "created": "2022-09-28 18:51:13.060",
    "updated": "2022-09-28 18:51:13.060",
    "@collectionId": "279d09f1zo0wttn",
    "@collectionName": "games",
    "date": "2022-09-07 12:00:00.000",
    "@expand": {}
  }
]
```


Post:
Add new Game with request body e.g.:
```
{
  "date": "2022-09-07 12:00:00.000"
}
```

Returns e.g.:
```
{
  "id": "ti6drt099xhwdo6",
  "created": "2022-09-28 18:41:48.726",
  "updated": "2022-09-28 18:41:48.726",
  "@collectionId": "279d09f1zo0wttn",
  "@collectionName": "games",
  "date": "2022-09-07 12:00:00.000",
  "@expand": {}
}
```

## /rounds

Get:

Get all rounds

Returns:
```
[
  {
    "id": "2uv014efe6xr8tb",
    "created": "2022-09-28 18:52:19.178",
    "updated": "2022-09-28 18:52:19.178",
    "@collectionId": "517pidot9nhkd4d",
    "@collectionName": "rounds",
    "atkLosses": 2,
    "attackerName": "saming",
    "attackers": 12,
    "defLosses": 14,
    "defenderName": "marius",
    "defenders": 14,
    "gameIdRef": "73ro8umvyguaby8",
    "@expand": {}
  }
]
```

Post:

Add a new round with request body e.g.:#
```
{
  "attackerName": "saming",
  "defenderName": "marius",
  "attackers": 12,
  "defenders": 14,
  "atkLosses": 2,
  "defLosses": 14,
  "gameIdRef": "ti6drt099xhwdo6"
}
```

Returns:

```
{
  "id": "2uv014efe6xr8tb",
  "created": "2022-09-28 18:52:19.178",
  "updated": "2022-09-28 18:52:19.178",
  "@collectionId": "517pidot9nhkd4d",
  "@collectionName": "rounds",
  "atkLosses": 2,
  "attackerName": "saming",
  "attackers": 12,
  "defLosses": 14,
  "defenderName": "marius",
  "defenders": 14,
  "gameIdRef": "73ro8umvyguaby8",
  "@expand": {}
}
```