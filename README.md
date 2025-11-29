# Agent Examples

Examples of simple agents using Llamastack.

## Running

### Server

1. Serve model using ollama using one terminal

    ```shell
    nohup ./start-ollama.sh > ./start-ollama.log 2>&1 &
    # ollama run llama3.2:3b --keepalive 60m
    ollama run llama3.2:3b-instruct-fp16 --keepalive 60m
    ```

2. Wrap model with Llama Server in another terminal

    ```shell
    ./start-llama.sh
    ```

3. Verify

    ```shell
    # test model
    uv run llama-stack-client configure --endpoint http://localhost:8321 --api-key none
    # see all models
    uv run llama-stack-client models list
    ```
