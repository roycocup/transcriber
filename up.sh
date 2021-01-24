#!/usr/bin/env bash

nice -10 docker-compose -p transcriber -f ./docker-compose.yml up ${@:1:99}
