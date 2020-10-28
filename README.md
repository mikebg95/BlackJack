# BlackJack
Blackjack game made with Python and Tkinter

### How does the game work?
When opening the app, the player is asked for his/her name. After inserting the name, the user is automatically given 1000 chips to play with, and the info (name and chips) is shown on the screen.
Next, the player is asked what he/she would like to bet. Afterwards, the player and the dealer are dealt two cards each (the dealers second card is hidden). If the player has Blackjack, he is rewarded 2.5 times his/her bet, unless the dealer also has Blackjack (whereby the player simply gets bet back).
If the player does not have Blackjack, the player is presented with several options (hit, stand, double, or split), depending on the situation and the cards the player has (I'm still working on the split option).
When the players score is over 21, he/she loses; if not, it's the dealers turn. As long as the dealers score is under 17, it will hit another card. After both the player and the dealer are done (and none of them has a score over 21), their scores are compared. 
If it's a tie (a "push"), the player simply gets his/her bet back; if the dealer has a higher score, the player loses; if the player has a higher score, he/she gets twice his/her bet back.
After a round is finished, the player is asked to play another round. If the player doesn't have enough chips to play, he/she is asked to start a new game. 
