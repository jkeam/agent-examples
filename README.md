# Agent Examples

Examples of simple agents using Llamastack.

## Running

### Server

#### Local Model

Running ollama locally with Llamastack Server.

1. Serve model using ollama using one terminal

    ```shell
    nohup ./start-ollama.sh > ./start-ollama.log 2>&1 &
    # ollama run llama3.2:3b --keepalive 60m
    ollama run llama3.2:3b-instruct-fp16 --keepalive 60m
    ```

2. Wrap model with Llama Server in another terminal

    ```shell
    export OLLAMA_HOST="YOUR_IP_ADDRESS"
    podman run -d --rm --name llama-server -it \
     --user 1001 \
     -v ~/.llama:/root/.llama:z \
     --network=host \
     -e OLLAMA_URL=http://$OLLAMA_HOST:11434 \
     docker.io/llamastack/distribution-starter:0.3.3 \
     --port 8321
    ```

#### OpenAI Facade

Running Llamastack Server as a facade to OpenAI.

```shell
export OPENAI_API_KEY="YOUR_ACTUAL_OPENAI_API_KEY"
podman run -d --rm --name llama-server -it \
 --user 1001 \
 -v ~/.llama:/root/.llama:z \
 --network=host \
 -e OPENAI_API_KEY=$OPENAI_API_KEY \
 docker.io/llamastack/distribution-starter:0.3.3 \
 --port 8321
```

#### Verification

```shell
# test api endpoint
uv run llama-stack-client configure --endpoint http://localhost:8321 --api-key none
# see all models
uv run llama-stack-client models list
```

## References

1. Llama Stack Starter [run.yaml](https://github.com/llamastack/llama-stack/blob/a7c7c724679b2c19683925d78c33b63e79d2aff3/src/llama_stack/distributions/starter/run.yaml)
