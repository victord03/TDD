
class CurrentBet:
    value: float

    def __init__(self, value: float = 1.0):
        self.value = round(value, 2)


class Player:
    amount: float
    bet_amount: CurrentBet

    def __init__(self, bet_amount: CurrentBet, amount: float = 0.0):
        self.amount = round(amount, 2)
        self.bet_amount = bet_amount


def run():
    current_bet = CurrentBet(1.25)

    p1 = Player(amount=10.34, bet_amount=current_bet)
    p2 = Player(amount=8.95, bet_amount=current_bet)

    return p1, p2


if __name__ == '__main__':
    run()