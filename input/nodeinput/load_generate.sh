#!/usr/bin/bash
node /usr/src/app/input.js & while [ 1 ]; do echo "Test"; sleep 0.1; done && fg
