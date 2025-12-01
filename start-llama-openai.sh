#!/bin/bash

export OLLAMA_HOST=192.168.1.252
podman run -d --rm --name llama-server -it \
 --user 1001 \
 -v ~/.llama:/root/.llama:z \
 --network=host \
 -e OPENAI_API_KEY=$OPENAI_API_KEY \
 docker.io/llamastack/distribution-starter:0.3.3 \
 --port 8321
