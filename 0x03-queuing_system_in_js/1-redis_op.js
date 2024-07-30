// Add two functions:
// setNewSchool:
// It accepts two arguments schoolName, and value.
// It should set in Redis the value for the key schoolName
// It should display a confirmation message using redis.print
// displaySchoolValue:
// It accepts one argument schoolName.
// It should log to the console the value for the key passed as argument
// At the end of the file, call:
// displaySchoolValue('Holberton');
// setNewSchool('HolbertonSanFrancisco', '100');
// displaySchoolValue('HolbertonSanFrancisco');

import { createClient, print } from "redis";

const client = createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
}

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, reply) => {
        console.log(reply);
    });
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
