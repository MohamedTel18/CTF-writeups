#!/bin/bash

docker build -t 2025_pwn_directorhard .
docker run -it --rm  -p 1337:1337 2025_pwn_directorhard
