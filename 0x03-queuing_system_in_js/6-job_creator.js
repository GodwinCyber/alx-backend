//     Create a queue with Kue
//     Create an object containing the Job data with the following format:
// {
//   phoneNumber: string,
//   message: string,
// }
//     Create a queue named push_notification_code, and create a job with the object created before
//     When the job is created without error, log to the console Notification job created: JOB ID
//     When the job is completed, log to the console Notification job completed
//     When the job is failing, log to the console Notification job failed

import kue from 'kue';
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '1234567890',
    message: 'Hello, this is a test message',
};
const job = queue.create('push_notification_code', jobData).save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    }
});
job.on('complete', () => {
    console.log('Notification job completed');
});
job.on('failed', (err, done) => {
    console.log('Notification job failed');
});
