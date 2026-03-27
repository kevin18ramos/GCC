#!/bin/bash
set -e

systemctl daemon-reload
systemctl enable {{vm}}
systemctl start {{vm}}