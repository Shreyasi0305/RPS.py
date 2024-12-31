def player(prev_play, opponent_history=[]):
    """
    A player function to determine the next move based on the opponent's history.

    Args:
        prev_play (str): The opponent's previous move ("R", "P", or "S").
        opponent_history (list): Keeps track of the opponent's moves.

    Returns:
        str: The next move ("R", "P", or "S").
    """
    # Record the opponent's previous play
    if prev_play:
        opponent_history.append(prev_play)

    # Define the counter for each move
    counters = {"R": "P", "P": "S", "S": "R"}

    # If there is no history, play "R" by default
    if not opponent_history:
        return "R"

    # Count the frequency of each move
    move_counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        move_counts[move] += 1

    # Predict the opponent's next move as their most frequent move
    predicted_move = max(move_counts, key=move_counts.get)

    # Counter the predicted move
    return counters[predicted_move]
