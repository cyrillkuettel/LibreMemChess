

def test_read_anki_deck():
    # todo
    deck = read_anki_deck("tests/test_deck.apkg")
    assert len(deck) == 2
    assert deck[0].front == "front1"
    assert deck[0].back == "back1"
    assert deck[1].front == "front2"
    assert deck[1].back == "back2"
