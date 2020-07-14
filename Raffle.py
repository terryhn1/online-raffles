
import random
"""
The Raffle class is used as the Object that contains all the information in a raffle. 
"""

class Raffle:
    def __init__(self, name, email):
        self._name = name
        self._email = email
    
    def get_name(self):
        return self._name

    def get_email(self):
        return self._email


"""
The Raffle Bag class is used as the container for each raffle. 
The Raffle Bag should be able to add raffles. 
"""

class RaffleBag :
    def __init__(self, title):
        self._bag = list()
        self._title = title
    
    def add_raffles(self, name, email, num):
        #Given the name, create a raffle Object(s) accordingly to num and add it to the bag.
        # If the bag size is 0 before updates, then do not shuffle. Nothing is returned. 
        original_length = len(self._bag)
        count = 0

        while (count < num):
            newRaffle = Raffle(name, email)
            self._bag.append(newRaffle)
            count += 1
        if (original_length != 0):
            random.shuffle(self._bag)

        return
    
    def stringify(self):
        return [x.get_name() + "(" + x.get_email()[0:x.get_email().index('@')] +")" for x in self._bag]

    def print_bag(self):
        #Print the contents of the bag
        print("Prize: " + self._title)
        for i in self._bag:
            print(i.get_name())
        return

    def get_title(self):
        #print which bag is this referring to
        return self._title
    
    def size(self):
        return len(self._bag)

"""
This class contains all of the listings for raffles. 
In this, there should be enough raffle bags that there are prizes.
"""

class RaffleListing:
    def __init__(self):
        self._listing = list()
        
    def add_bag(self, bag):
        #Check for duplicates. If a bag with the same prize name is in, then do not do anything.
        for i in range(len(self._listing)):
            if self._listing[i].get_title() == bag.get_title():
                return
        self._listing.append(bag)
        return
    
    
    def get_bag(self, index):
        return self._listing[index]
    
    def get_listing(self):
        return self._listing


