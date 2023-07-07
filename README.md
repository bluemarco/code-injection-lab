# Code Injection Lab  [![Semgrep](https://github.com/bluemarco/code-injection-lab/actions/workflows/semgrep.yml/badge.svg)](https://github.com/bluemarco/code-injection-lab/actions/workflows/semgrep.yml)
Guess the correct number and find a way to trick the app to win the game. Send a request to `/claim-reward` to verify if you won the game.

### Setup
To start the challenge server run the following commands:
```shell
$ docker build -t code-injection-lab . # Build the image
$
$ docker run -p 80:80 code-injection-lab # Start the server
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```