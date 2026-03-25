#!/bin/bash
nohup bash "$1" > output.log 2>&1 &
echo $! > process.pid