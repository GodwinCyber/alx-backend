import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';
import express from 'express';

const client = redis.createClient();
const clientGet = promisify(client.get).bind(client);
const clientSet = promisify(client.set).bind(client);

const queue = kue.createQueue();

const app = express();
const PORT = 1245;

const reserveSeat = async (number) => await clientSet('available_seats', number);

const getCurrentAvailableSeats = async () => await clientGet('available_seats');

let reservationEnabled = true;
reserveSeat(50);

/*======== ROUTES =======*/

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (!err) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });

  job.on('complete', () => console.log(`Seat reservation job ${job.id} completed`));
  job.on('failed', (err) => console.log(`Seat reservation job ${job.id} failed: ${err}`));
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();
    let availableSeats = parseInt(currentSeats, 10);

    if (isNaN(availableSeats)) {
      availableSeats = 0;
    }

    if (availableSeats <= 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      availableSeats -= 1;
      await reserveSeat(availableSeats);

      if (availableSeats === 0) {
        reservationEnabled = false;
      }

      done();
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
