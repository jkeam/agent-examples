#!/bin/bash

export OLLAMA_HOST=192.168.1.252
podman run -d --rm --name llama-server -it \
 --user 1001 \
 -v ~/.llama:/root/.llama:z \
 --network=host \
 -e OLLAMA_URL=http://$OLLAMA_HOST:11434 \
 docker.io/llamastack/distribution-starter:0.3.3 \
 --port 8321
