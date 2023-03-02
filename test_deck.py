from deck import Deck, Card 
import pytest 

def test_card():
    # Test creating a card to see if the card is correct is correctly created
    check = Card(5,'Hearts')
    assert check.rank == 5
    assert check.suite == 'Hearts'

    print ('Passed card test')
    pass
def test_card_operators():
    #Test comapring card rank to see if the operators are functioning correctly
    card1 = Card(8, 'Diamonds')
    card2 = Card(8,'Hearts')
    card3 = Card(3, 'Clubs')
    assert card1 == card2
    assert card3 < card1
    assert card1 != card3
    assert card2 > card3

    print ('Passed card operators test')

    def test_deck_lenght():

        #Test which create card deck to see if the right amount of cards are created
        check = Deck ()
        assert len (check) ==52

        print ('Passed deck lenght test')

        def test_deck():
            #Test creating card deck to see if the right amount of cards are created
            # and if len function returns the right amount of cards
            test_deck = Deck()
            assert len(test_deck) == 52

            #checkif the deck has the correct number of cards
            assert len (test_deck.cards) == 52

            #remove a card from teh deck and check if the len() function returns the correct number of cards
            test_deck.cards.pop()
            assert len(test_deck) == 51

            #add a card t the deck and check if the len() function returns the correct number of cards
            test_deck.cards.append(Card(rank =13, suite = 'Spades'))
            assert len (test_deck) == 52

            print ('Passed deck creation test')

            def test_sort():
                #Test sorting the card deck to see if the deck is sorted successfully
                test_deck = Deck ()
                test_deck.schuffle()

                test_deck.sort()
                previous_card = None
                for card in test_deck.cards:
                    if previous_card is not None:
                        assert previous_card.rank <=card.rank
                        previous_card = card

                        print ('Passed deck sorting test')

            def test_deck_take():
                # Test taking cards from the top of the card deck to seee if its taking the correct card
                check = Deck()
                assert check.take().rank == 13
                check.sort()
                assert check.take().rank == 12
                assert len(check) == 50

                print ('Passed deck take test')

            def test_deck_put():
                # Test putting cards in top of the card deck to see if it is putting the right cards
                check = Deck()
                card1 = Card(8, 'Diamonds')
                card2 = Card(8, 'Hearts') 
                card3 = Card(3, 'Clubs')
                check.put(card1)
                check.put(card2)
                check.put(card3)
                assert check.take().rank == 3
                assert check.take().rank == 8
                assert check.take().rank == 8
                assert len(check) == 52

                print ('Passed deck put test')

            if __name__=='__main__'
            pytest.main()  
