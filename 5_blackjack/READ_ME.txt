My first attempt at creating a game of Blackjack, using OOP. 

I already have a pretty good understanding of the rules of blackjack, however I struggled
with modelling the actual gameplay, as I was trying to perfect the 'flow' of the game.

I started with the card, deck and player classes, then somewhere along the way
realised I needed a dealer class, and then decided to add a table class in also. 

I hit a bit of a roadbump when I introduced the betting system, as I couldn't quite
get the correct inputs (at first), and subsiquently spent a lot of time perfecting 
the input values. I was trying to make the program fool-proof, but proved difficult to do.

I realised too late I should have been implementing Unit tests as I went. I won't make this
error on my next project.

The final issue I have had was setting the ACE value. This is a big aspect of the game
Blackjack, and I struggled particularly with the dealers ACE. Trying to tell a computer to 
think like a human is difficult. But I settled on playing the ACE if the dealers hand 
total is 1- not 21, and 2- lower than the opposing player.

Side note - I also had a few problems with the return value on the betting class. For some 
reason I was removing the betting account from it's self, and then minusing the belt also. 
Took a long time to figure out, and is possibly still bugging somewhere. 

Overall this project helped me immensly with my understanding of OOP, and class 
interoperability. 
It was fun, and stressful at times. 

Thank you for playing, and/or reading this too! 

Cheers!! 