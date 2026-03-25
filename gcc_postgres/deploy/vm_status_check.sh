#!/bin/bash
PID=$(cat process.pid)

if ps -p $PID > /dev/null
then
    echo "Running"
else
    echo "Stopped"
fi