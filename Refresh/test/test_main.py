from Refresh.src import main
import pytest

"""I don't remember how to setup the pytest.parametrize function. 
However, even though this appears to be a docstring, I am actually 
testing my new keyboard."""

def setup():
    return list(main.run())

def test_player_class():
    result = setup()
    assert isinstance(result, main.Player)

def test_player_has_amount():
    result = setup()
    assert result[0].amount == 0.0

def test_bet_amount_is_equal_to_all_players():
    result = setup()
    assert len(set([player.bet_amount for player in result])) == 1


