// Created a job creator, let’s add tests:
//     Import the function createPushNotificationsJobs
//     Create a queue with Kue
//     Write a test suite for the createPushNotificationsJobs function:
//         Use queue.testMode to validate which jobs are inside the queue
//         etc.
// Requirements:
//     Make sure to enter the test mode without processing the jobs before executing the tests
//     Make sure to clear the queue and exit the test mode after executing the tests

import createPushNotificationsJobs from "./8-job";

import kue from 'kue';
import sinon from "sinon";
import { expect } from "chai";

describe('createPushNotificationsJobs', () => {
    let queue;
    let consoleSpy;
  
    before(() => {
      queue = kue.createQueue();
      kue.Job.rangeByState('complete', 0, 1000, 'asc', (err, jobs) => {
        jobs.forEach((job) => {
          job.remove();
        });
      });
      queue.testMode.enter();
    });
  
    after(() => {
      queue.testMode.exit();
    });
  
    beforeEach(() => {
      consoleSpy = sinon.spy(console, 'log');
    });
  
    afterEach(() => {
      console.log.restore();
      queue.testMode.clear();
    });
  
    it('displays an error message if jobs is not an array', () => {
      expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
    });
  
    it('creates two new jobs to the queue', () => {
        const jobs = [
            {
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account'
            },
            {
            phoneNumber: '4153518781',
            message: 'This is the code 4562 to verify your account'
            }
      ];
  
      createPushNotificationsJobs(jobs, queue);
  
      expect(queue.testMode.jobs.length).to.equal(2);
      expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
      expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
      expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
      expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    });
  
    it('logs the correct messages for job events', (done) => {
      const jobs = [
        {
          phoneNumber: '4153518780',
          message: 'This is the code 1234 to verify your account'
        }
      ];
  
      createPushNotificationsJobs(jobs, queue);
  
      const job = queue.testMode.jobs[0];
      job.on('complete', () => {
        expect(consoleSpy.calledWith(`Notification job ${job.id} completed`)).to.be.true;
      });
  
      job.on('failed', (err) => {
        expect(consoleSpy.calledWith(`Notification job ${job.id} failed: ${err}`)).to.be.true;
      });
  
      job.on('progress', (progress) => {
        expect(consoleSpy.calledWith(`Notification job ${job.id} ${progress}% complete`)).to.be.true;
      });
  
      job.emit('complete');
      job.emit('failed', new Error('Failed to send'));
      job.emit('progress', 50);
  
      setImmediate(done);
    });
});
