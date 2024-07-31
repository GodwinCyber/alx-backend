// Create an array that will contain the blacklisted phone numbers. Add in
// it 4153518780 and 4153518780 - these 2 numbers will be blacklisted by our jobs processor.
// Create a function sendNotification that takes 4 arguments: phoneNumber, message, job, and done:
//     When the function is called, track the progress of the job of 0 out of 100
//     If phoneNumber is included in the “blacklisted array”, fail the job with an Error
//     object and the message: Phone number PHONE_NUMBER is blacklisted
//     Otherwise:
//         Track the progress to 50%
//         Log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE
// Create a queue with Kue that will proceed job of the queue
// push_notification_code_2 with two jobs at a time.
// Requirements:
//     You only need one Redis server to execute the program
//     You will need to have two node processes to run each script at the same time
//     You muse use Kue to set up the queue
//     Executing the jobs list should log to the console the following:

import kue from 'kue';

const blacklistedNum = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
    const total = 100;

    job.progress(0, total);

    if (blacklistedNum.includes(phoneNumber)) {
        done(Error(`Phone number ${phoneNumber} is blacklisted`));
        return;
    }
    job.progress(50, total);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}
const queue = kue.createQueue();
const queueName = 'push_notification_code_2';

queue.process(queueName, 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});
