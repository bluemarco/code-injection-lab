from fastapi import FastAPI
from uuid import uuid4

app = FastAPI()

status: str = ""


def set_status(stat: str) -> None:
    global status
    status = stat


def guess_the_number(num: int) -> str:
    stat: str = "incorrect"
    if num == int(uuid4()):
        stat = "correct"
    else:
        stat = "incorrect"

    set_status(stat)
    return stat


def give_reward() -> str:
    reward: float = 10_000_000.0
    global status

    if status == "correct":
        return f"Congrats! You won {str(reward)}."
    elif status == "incorrect":
        return "Please try again. Thank you for playing."
    else:
        return "Please try again. Thank you for playing."


@app.get("/")
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
