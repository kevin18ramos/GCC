#!/bin/bash
set -e

systemctl daemon-reload
systemctl disable {{vm}}
systemctl stop {{vm}}