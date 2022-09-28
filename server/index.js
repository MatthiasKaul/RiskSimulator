import 'cross-fetch/dist/node-polyfill.js';
import PocketBase from 'pocketbase';
import express from 'express';
import cors from 'cors';

const client = new PocketBase('http://127.0.0.1:8090');
await client.admins.authViaEmail('admin@risk-simulator.de', 'RiskSimulator').catch((x) => console.log(x));

const app = express();

var corsOptions = {
    origin: "http://localhost:8081"
};

app.use(cors(corsOptions));

app.use(express.json());

app.use(express.urlencoded({ extended: true }));

app.get("/games", async (req, res) => {
    const records = await client.records.getFullList('games', 200 /* batch size */, {
        sort: '-created',
    });

    res.send(records);
});

app.post('/games', async (req, res) => {
    const data = {
        date: req.body.date
    };

    const record = await client.records.create('games', data);

    res.send(record);
});

app.get("/rounds", async (req, res) => {
    const records = await client.records.getFullList('rounds', 200 /* batch size */, {
        sort: '-created',
    });

    res.send(records);
});

app.post("/rounds", async (req, res) => {
    const data = {
        attackerName: req.body.attackerName,
        defenderName: req.body.defenderName,
        attackers: req.body.attackers,
        defenders: req.body.defenders,
        atkLosses: req.body.atkLosses,
        defLosses: req.body.defLosses,
        gameIdRef: req.body.gameIdRef
    };

    const records = await client.records.create('rounds', data);

    res.send(records);
});

// set port, listen for requests
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}.`);
});
