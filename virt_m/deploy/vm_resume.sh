#!/bin/bash
set -e

PID=$(systemctl show --property MainPID --value {{vm}})
kill -CONT $PID