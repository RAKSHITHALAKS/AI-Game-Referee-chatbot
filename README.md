# AI Game Referee – Rock Paper Scissors Plus

## Overview
This project implements a minimal AI game referee for a Rock–Paper–Scissors–Plus game.
The game runs in a simple CLI-based conversational loop and follows a best-of-3 format.

## Game Rules
1. Best of 3 rounds  
2. Valid moves: rock, paper, scissors, bomb  
3. Bomb can be used once per player  
4. Bomb beats all other moves  
5. Bomb vs bomb results in a draw  
6. Invalid input wastes the round  
7. Game ends automatically after 3 rounds  

## Architecture
1. Game state is stored in a persistent Python dictionary and not in the prompt  
2. Validation, game logic, and state updates are handled by explicit functions  
3. Google ADK is used to define the referee agent abstraction  
4. The CLI loop manages user interaction and deterministic execution  

## Tools / Functions
1. validate_move - validates user and bot moves  
2. resolve_round - determines the winner of each round  
3. update_game_state - updates game state across rounds  

## Tradeoffs
1. Bot move selection is random for simplicity  
2. Interaction is CLI-based instead of a UI  

## Improvements
1. Smarter bot strategy  
2. Better natural language input handling  
3. Automated tests  
