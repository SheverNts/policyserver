# policyserver

Policy Server is a policy engine is written in python inspired by [OPA](https://github.com/open-policy-agent/opa) unlike OPA policy can be written in Python

## Usage
    ```bash
    $> policyserver --help
    positional arguments:
    {server}         sub-commands
        server         run server.

    optional arguments:
    -h, --help       show this help message and exit
    -v, --version    show program's version number and exit
    -l, --log-level  log level.
    ```
## Installation
Steps to Install Policy Server

* Pip Install Policy Server

    ```bash
    pip3 install policyserver
    ```

## Example
    * To start a server
    ```bash
    policyserver server -r examples/block_ssh/
    ```
    
    * Check the result of the policy based on user input 
    ```bassh
    cat << EOF > input.json
    {
    "user": "user1",
    "network": "192.0.2.0/17"
    }
    EOF
    >> curl -X POST  -d @input.json -H "Content-Type: application/json" http://localhost:8081/ps/v1/ssh/user_allow_network
    {"status":false}
    ```
## Setting up development environment

* Clone  Policy Server repo
    ```bash
    git clone https://github.com/SheverNts/policyserver.git
    ```
* Setup Virtual env
    ```bash
    virtulaenv -p $(which python3) policyserver

    cd policyserver
    source bin/activate
    pip3 install requirements_test.txt
    ```
