
class CurrentBet:
    value: float

    def __init__(self, value: float = 1.0):
        self.value = round(value, 2)

class Player:
    amount: float
    bet_amount: CurrentBet

    def __init__(self, amount: float = 0.0):
        self.amount = round(amount, 2)
        # self.bet_amount = 0.0

    def bet_an_amount(self, bet_amount: CurrentBet):
        self.bet_amount = bet_amount
        self.amount -= self.bet_amount.value


def all_players_bet(players: list, bet_amount: CurrentBet):
    for player in players:
        player.bet_an_amount(bet_amount)


def run():
    current_bet = CurrentBet(1.25)

    p1 = Player(amount=10.34)
    p2 = Player(amount=8.95)

    list_of_players = [p1, p2]

    # all_players_bet(list_of_players, current_bet)

    return p1, p2


if __name__ == '__main__':
    run()