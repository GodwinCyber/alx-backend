// Install node_redis using npm
// Using Babel and ES6, write a script named 0-redis_client.js.
// It should connect to the Redis server running on your machine:
// It should log to the console the message Redis client
// connected to the server when the connection to Redis works correctly
// It should log to the console the message Redis client not connected to
// the server: ERROR_MESSAGE when the connection to Redis does not work
// Requirements:
// To import the library, you need to use the keyword import

import { createClient } from 'redis';

const client = createClient()

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});
