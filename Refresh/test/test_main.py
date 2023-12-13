from Refresh.src import main
import pytest

"""I don't remember how to setup the pytest.parametrize function. 
However, even though this initially appears to be a docstring, I 
am actually testing my new keyboard."""

"""def setup():
    return list(main.run())"""

result = main.run()
current_bet = main.CurrentBet(1.25)

def test_player_class(players=result):
    players_are_true = [isinstance(player, main.Player) for player in players]
    assert bool(set(players_are_true))

def test_player_has_amount(players=result):
    assert isinstance(players[0].amount, float)

def test_bet_amount_is_equal_to_all_players(players=result):
    assert len(set([player.bet_amount for player in players])) == 1

def test_all_players_bet_an_amount(players=result, bet=current_bet):
    initial_amounts = [player.amount for player in players]
    main.all_players_bet(players, bet)
    new_amounts = [player.amount for player in players]

    pair_of_old_new_values = list(zip(initial_amounts, new_amounts))
    assert float(sum(set([old - new for old, new in pair_of_old_new_values]))) == current_bet.value

    