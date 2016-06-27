"""
    Poker V 0.0.1
"""
import random
import sys

class Poker:

    def __init__(self,hands):
        self.hands = hands

    def run(self):
        return self.allmax(self.hands,max(self.hands,key=self.hand_rank))

    def allmax(self,hands,max):
        list = []
        for i in hands:
            if(self.hand_rank(max) == self.hand_rank(i)):
                list.append(i)
        return list

    def hand_rank(self,hand):
        ranks = self.card_ranks(hand)
        if self.straight(ranks) and self.flush(hand):
            return (8,max(ranks))
        elif self.kind(4,ranks):
            return (7,self.kind(4,ranks),self.kind(1,ranks))
        elif self.kind(3,ranks) and self.kind(2,ranks):
            return (6,self.kind(3,ranks),self.kind(2,ranks))
        elif self.flush(hand):
            return (5,ranks)
        elif self.straight(ranks):
            return (4,ranks)
        elif self.kind(3,ranks):
            return (3,self.kind(3,ranks),ranks)
        elif self.two_pair(ranks):
            return (2,self.two_pair(ranks),ranks)
        elif self.kind(2,ranks):
            return (1,self.kind(2,ranks),ranks)
        else:
            return (0,ranks)

    def card_ranks(self,hand):
        ranks = ["--23456789TJQKA".index(i) for i,s in hand]
        ranks.sort(reverse=True)
        return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks

    def straight(self,ranks):
        return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5


    def flush(self,hand):
        return len(set([s for n,s in hand])) == 1

    def kind(self,n,ranks):
        for i in ranks:
            if(ranks.count(i) == n):
                return i
        return None

    def two_pair(self,ranks):
        s = set()
        for i in ranks:
            if(ranks.count(i) == 2):
                s.add(i)
        if(len(s) == 2):
            return tuple(s)
        return None

    def test_poker(self):
        sf = "6C 7C 8C 9C TC".split()
        fk = "9D 9H 9S 9C 7D".split()
        fh = "TD TC TH 7C 7D".split()
        tp = "5S 5D 9H 9C 6S".split()
        s1 = "AS 2S 3S 4S 5C".split()
        s2 = "2C 3C 4C 5S 6S".split()
        ah = "AS 2S 3S 4S 6C".split()
        sh = "2S 3S 4S 6C 7D".split()
        self.hands = [s1,s2,ah,sh]
        assert self.run() == [s2]
        assert self.straight([9,8,7,6,5]) == True
        assert self.straight([9,8,8,6,5]) == False
        assert self.flush(sf) == True
        assert self.flush(fk) == False
        assert self.card_ranks(sf) == [10,9,8,7,6]
        assert self.card_ranks(fk) == [9,9,9,9,7]
        assert self.card_ranks(fh) == [10,10,10,7,7]
        fkranks = self.card_ranks(fk)
        tpranks = self.card_ranks(tp)
        assert self.kind(4,fkranks) == 9
        assert self.kind(3,fkranks) == None
        assert self.kind(2,fkranks) == None
        assert self.kind(1,fkranks) == 7
        assert self.two_pair(fkranks) == None
        assert self.two_pair(tpranks) == (9,5)
        assert self.hand_rank(sf) == (8,10)
        assert self.hand_rank(fk) == (7,9,7)
        assert self.hand_rank(fh) == (6,10,7)
        return "Test Passed!"

"""
    Start Poker
"""

print "\n Welcome! Poker V 0.0.1 \n"
print "\n - Every Hand Should Have 5 Cards!\n"
print "\n - Please Write Every Hand as the following example: '2S 3S 4S 6C 7D'\n"
print "\n - Enjoy!\n"
print "\n -------------------------------- \n"

while(1):
    hands_num = raw_input("\n How many hands you want to insert? ")
    hands = []

    for i in range(0,int(hands_num)):
        hands_string = raw_input("\n Please Enter Hands Number "+str(i+1)+" :")
        hands.append(hands_string.split())

    poker = Poker(hands)
    print "\n The Winner Hand is: "
    print poker.run()
    print "\n\n"
    result = raw_input(" Want to try it one more time. y/n ?")
    if (result == 'n'):
        sys.exit()
