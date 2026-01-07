from google.adk import Agent
import random

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]

game_state = {
    "round": 0,
    "max_rounds": 3,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False,
    "history": []
}

def validate_move(move: str, player: str) -> dict:
    if move not in VALID_MOVES:
        return {"valid": False, "reason": "Invalid move"}
    if move == "bomb":
        if player == "user" and game_state["user_bomb_used"]:
            return {"valid": False, "reason": "User already used bomb"}
        if player == "bot" and game_state["bot_bomb_used"]:
            return {"valid": False, "reason": "Bot already used bomb"}
    return {"valid": True}

def resolve_round(user_move: str, bot_move: str) -> str:
    if user_move == bot_move:
        return "draw"
    if user_move == "bomb":
        return "user"
    if bot_move == "bomb":
        return "bot"
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    return "user" if rules[user_move] == bot_move else "bot"

def update_game_state(user_move: str, bot_move: str, winner: str):
    game_state["round"] += 1
    if user_move == "bomb":
        game_state["user_bomb_used"] = True
    if bot_move == "bomb":
        game_state["bot_bomb_used"] = True
    if winner == "user":
        game_state["user_score"] += 1
    elif winner == "bot":
        game_state["bot_score"] += 1
    game_state["history"].append({
        "round": game_state["round"],
        "user_move": user_move,
        "bot_move": bot_move,
        "winner": winner
    })

referee_agent = Agent(name="RPS_Referee")

def reset_game_state():
    game_state["round"] = 0
    game_state["user_score"] = 0
    game_state["bot_score"] = 0
    game_state["user_bomb_used"] = False
    game_state["bot_bomb_used"] = False
    game_state["history"] = []

def run_game():
    print("Welcome to Rock–Paper–Scissors–Plus!")
    print("Best of 3 rounds")
    print("Moves: rock, paper, scissors, bomb\n")

    while game_state["round"] < game_state["max_rounds"]:
        print(f"\nRound {game_state['round'] + 1}")
        user_move = input("Enter your move: ").lower().strip()

        validation = validate_move(user_move, "user")
        if not validation["valid"]:
            print(f"Invalid input: {validation['reason']}")
            update_game_state("invalid", "invalid", "draw")
            continue

        bot_move = random.choice(
            ["rock", "paper", "scissors"]
            if game_state["bot_bomb_used"]
            else VALID_MOVES
        )

        winner = resolve_round(user_move, bot_move)
        update_game_state(user_move, bot_move, winner)

        print(f"User move: {user_move}")
        print(f"Bot move: {bot_move}")
        print(f"Round winner: {winner}")

    print("\nGame Over")
    print(f"Final Score → User: {game_state['user_score']} | Bot: {game_state['bot_score']}")

    if game_state["user_score"] > game_state["bot_score"]:
        print("Final Result: User Wins")
    elif game_state["bot_score"] > game_state["user_score"]:
        print("Final Result: Bot Wins")
    else:
        print("Final Result: Draw")

if __name__ == "__main__":
    while True:
        run_game()
        choice = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if choice != "yes":
            print("Thanks for playing!")
            break
        reset_game_state()
