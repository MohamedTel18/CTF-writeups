#!/bin/bash

docker build -t 2025_pwn_directoreasy .
docker run -it --rm  -p 1337:1337 2025_pwn_directoreasy
