<h1>0x03. Queuing System in JS</h1>

<strong>Back-end JavaScript ES6 Redis NodeJS ExpressJS Kue</strong><br>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/bD8ATSAVbine9-zEXenwyw" title="Redis quick start" target="_blank">Redis quick start</a></li>
<li><a href="/rltoken/vFJSkoXkIvLqHzQgx8DVcw" title="Redis client interface" target="_blank">Redis client interface</a></li>
<li><a href="/rltoken/mRftfl67BrNvl-RM5JQfUA" title="Redis client for Node JS" target="_blank">Redis client for Node JS</a></li>
<li><a href="/rltoken/yTC3Ci2IV2US24xJsBfMgQ" title="Kue" target="_blank">Kue</a> <em>deprecated but still use in the industry</em></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/7yh7c3Zyy1RyUsdwlfsyDg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>How to run a Redis server on your machine</li>
<li>How to run simple operations with the Redis client</li>
<li>How to use a Redis client with Node JS for basic operations</li>
<li>How to store hash values in Redis</li>
<li>How to deal with async operations with Redis</li>
<li>How to use Kue as a queue system</li>
<li>How to build a basic Express app interacting with a Redis server</li>
<li>How to the build a basic Express app interacting with a Redis server and queue</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7</li>
<li>All of your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>js</code> extension</li>
</ul>

<h2>Required Files for the Project</h2>

<h3><code>package.json</code></h3>

<details>
<summary>
Click to show/hide file contents</summary>
<pre>
<code>
{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }
</code>
</pre>
</details>

<h3><code>.babelrc</code></h3>

<details>
<summary>
Click to show/hide file contents
</summary>
<pre>
<code> 
{
  "presets": [
    "@babel/preset-env"
  ]
}
</code>
</pre>
</details>

<h3>and&hellip;</h3>

<p>Don&rsquo;t forget to run <code>$ npm install</code> when you have the <code>package.json</code></p>
