from collections import deque

def parse(inp):
    decks =  []
    for player in inp.split('\n\n'):
        cards = [int(card) for card in player.splitlines()[1:]]
        deck = deque(cards)
        decks.append(deck)
    return decks

def score(deck):
    score = 0
    for i, card in enumerate(reversed(deck)):
        score += (i+1) * card
    return score

def play_game(deck0, deck1):
    while deck0 and deck1:
        card0 = deck0.popleft()
        card1 = deck1.popleft()

        if card0 > card1:
            deck0.append(card0)
            deck0.append(card1)
        else:
            deck1.append(card1)
            deck1.append(card0)

    winner = deck1 if not deck0 else deck0
    return score(winner)

def play_game_rec(deck0, deck1):
    history = set()
    while deck0 and deck1:
        decks = (tuple(deck0), tuple(deck1))
        if decks in history:
            # Player 1 wins
            return False, deck0
        history.add(decks)

        card0 = deck0.popleft()
        card1 = deck1.popleft()
        len0 = len(deck0)
        len1 = len(deck1)

        if card0 <= len0 and card1 <= len1:
            sub_deck0 = deque(list(deck0)[:card0])
            sub_deck1 = deque(list(deck1)[:card1])
            player2_wins, _ = play_game_rec(
                    sub_deck0, sub_deck1)
        else:
            player2_wins = card1 > card0

        if not player2_wins:
            deck0.append(card0)
            deck0.append(card1)
        else:
            deck1.append(card1)
            deck1.append(card0)

    if deck0:
        return False, deck0
    else:
        return True, deck1

def part1(inp):
    decks = parse(inp)
    return play_game(*decks)

def part2(inp):
    decks = parse(inp)
    _, winning_deck = play_game_rec(*decks)
    return score(winning_deck)
