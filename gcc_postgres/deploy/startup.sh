#!/bin/bash
set -e

systemctl daemon-reload
systemctl enable {{repo}}
systemctl start {{repo}}