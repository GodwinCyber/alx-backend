// let’s copy the code from the previous exercise (1-redis_op.js)
// Using promisify, modify the function displaySchoolValue to use ES6 async / await
// Same result as 1-redis_op.js

import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', toString());
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
}

const getAsync = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
    try {
        const reply = await getAsync(schoolName);
        console.log(reply);
    } catch (err) {
        console.log('Error', err);
    }
}
const run = async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');

}
run();
