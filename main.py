from fastapi import FastAPI
from os import environ

app = FastAPI()

status: str = ""
winner: bool = False


def set_winner():
    global winner
    winner = True


def guess_the_number(num: int) -> str:
    global status
    global winner

    winner = False
    stat: str = "incorrect"

    if num == int(environ['MAGIC_NUMBER']):
        stat = "correct"
    else:
        stat = "incorrect"

    status = stat
    return status


def give_reward() -> str:
    reward: float = 10_000_000.0
    global status

    if status == "correct" and winner:
        return f"Congrats! You won {str(reward)}."
    elif status == "incorrect":
        return "Please try again. Thank you for playing."
    else:
        return "Please try again. Thank you for playing."


@app.get("/")
def index():
    return "Code Injection Lab"


@app.get("/guess")
def guess(payload: str):
    response = {
        "msg": eval(f"guess_the_number({payload})")
    }
    return response


@app.get("/claim-reward")
def claim_reward():
    response = {
        "msg": give_reward()
    }
    return response
