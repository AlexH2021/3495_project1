#!/bin/sh
node input.js & while [ 1 ]; do echo "Test"; sleep 0.1; done &
