db = db.getSiblingDB("main_db");
db.createCollection("main");
db.main.drop();

db.main.insertMany([
    {
        "text": "double, double toil and trouble"
    },
    {
        "text": "fire burn, and cauldron bubble"
    }
]);