// let’s use the client to store a hash value
// Create Hash:
// Using hset, let’s store the following:
//     The key of the hash should be HolbertonSchools
//     It should have a value for:
//         Portland=50
//         Seattle=80
//         New York=20
//         Bogota=20
//         Cali=40
//         Paris=2
//     Make sure you use redis.print for each hset
// Display Hash:
// Using hgetall, display the object stored in Redis. It should return the following:
// Requirements:
//     Use callbacks for any of the operation, we will look at async operations later

import { createClient, print } from "redis";

const client = createClient();

client.on("error", (err) => {
    console.log('Redis client not connected to the server:',err.toString());
});
client.on('connect', () => {
    console.log('Redis client connected to the server');

    const updateHashList = (hashField, hashValue, hashName) => {
        client.hset(hashName, hashField, hashValue, print);
    };

    const displayHashList = (hashName) => {
        client.hgetall(hashName, (err, reply) => {
            if (err) {
                console.error('Error fetching hash:', err);
            } else {
                console.log(reply);
            }
        });
    };
    const hashName = 'HolbertonSchools';
    const hashValue = {
        'Portland': 50,
        'Seattle': 80,
        'New York': 20,
        'Bogota': 20,
        'Cali': 40,
        'Paris': 2
    };
    for (const[field, value] of Object.entries(hashValue)) {
        updateHashList(field, value, hashName);
    }
    displayHashList(hashName);
});
