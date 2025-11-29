#!/bin/bash

# export INFERENCE_MODEL="meta-llama/Llama-3.1-3B-Instruct"
#  --env INFERENCE_MODEL=$INFERENCE_MODEL \
# export INFERENCE_MODEL="llama3.2:3b"
export OLLAMA_HOST=192.168.1.252
podman run -it \
 -d \
 --rm \
 -- name llama-server \
 --user 1001 \
 -v ~/.llama:/root/.llama:z \
 --network=host \
 -e OLLAMA_URL=http://$OLLAMA_HOST:11434 \
 docker.io/llamastack/distribution-starter:0.3.3 \
 --port 8321
