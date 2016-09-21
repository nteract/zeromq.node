# zmq-prebuilt &nbsp;&nbsp;[![Build Status](https://travis-ci.org/nteract/zmq-prebuilt.svg?branch=master)](https://travis-ci.org/nteract/zmq-prebuilt) &nbsp;[![Build status](https://ci.appveyor.com/api/projects/status/6u7saauir2msxpou?svg=true)](https://ci.appveyor.com/project/nteract/zmq-prebuilt) &nbsp;&nbsp;&nbsp;:package: stable: [![Build Status](https://travis-ci.org/nteract/zmq-prebuilt-testing.svg?branch=master)](https://travis-ci.org/nteract/zmq-prebuilt-testing) [![Build status](https://ci.appveyor.com/api/projects/status/ox85p208tsxw6vt1?svg=true)](https://ci.appveyor.com/project/nteract/zmq-prebuilt-testing)

[ØMQ](http://www.zeromq.org/) bindings for node.js.

## Installation

    $ npm install zmq-prebuilt

We rely on [`prebuild`](https://github.com/mafintosh/prebuild). Prepare to be amazed at the wonders of binaries.

## Developer Installation

To set up `zmq-prebuilt` for development, clone and fork this repository and make sure you have `git-lfs` installed.

If you are running on Linux or OS X, you will need to have `automake`, `autoconf` and `libtool`. These can be installed using `brew` on OS X.

On Winodws you'll need a C++ compiler, preferably [Visual Studio 2013](https://www.visualstudio.com/downloads/download-visual-studio-vs).

```
$ npm install
```

### Testing
You can run then run the test suite.


```
$ npm test
```

Or run some of the example applications.

```
$ node examples/subber.js
```

### Supported operating systems

* [X] OS X/Darwin 64-bit
* [X] Linux 64-bit
* [x] Windows (64-bit and 32-bit)

## Usage

Everywhere you used `require(zmq)` in your code base before, replace it with `zmq-prebuilt`.

## Examples

### Push/Pull

```js
// producer.js
var zmq = require('zmq-prebuilt')
  , sock = zmq.socket('push');

sock.bindSync('tcp://127.0.0.1:3000');
console.log('Producer bound to port 3000');

setInterval(function(){
  console.log('sending work');
  sock.send('some work');
}, 500);
```

```js
// worker.js
var zmq = require('zmq-prebuilt')
  , sock = zmq.socket('pull');

sock.connect('tcp://127.0.0.1:3000');
console.log('Worker connected to port 3000');

sock.on('message', function(msg){
  console.log('work: %s', msg.toString());
});
```

### Pub/Sub

```js
// pubber.js
var zmq = require('zmq-prebuilt')
  , sock = zmq.socket('pub');

sock.bindSync('tcp://127.0.0.1:3000');
console.log('Publisher bound to port 3000');

setInterval(function(){
  console.log('sending a multipart message envelope');
  sock.send(['kitty cats', 'meow!']);
}, 500);
```

```js
// subber.js
var zmq = require('zmq-prebuilt')
  , sock = zmq.socket('sub');

sock.connect('tcp://127.0.0.1:3000');
sock.subscribe('kitty cats');
console.log('Subscriber connected to port 3000');

sock.on('message', function(topic, message) {
  console.log('received a message related to:', topic, 'containing message:', message);
});
```

## Release

When making a release we'll want to do:

```
npm version minor && git push && git push --tags
```

Followed by waiting for the prebuilds to get uploaded for each OS, then finally running:

```
npm publish
```

After that you can push a commit to [`nteract/zmq-prebuilt-testing`](https://github.com/nteract/zmq-prebuilt-testing) to check if the binaries are packaged correctly.
