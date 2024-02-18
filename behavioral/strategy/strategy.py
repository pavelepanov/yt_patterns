from abc import ABC, abstractmethod
from enum import Enum


class CandySellerMood(Enum):
    """ Mood of candy seller """
    GOOD = 1
    BAD = 2
    BETTER_STAY_AWAY = 3

class Strategy(ABC):
    """ Interface of strategy """

    @abstractmethod
    def check_mood_seller_candy(self, mood: CandySellerMood) -> bool:
        ...

    @abstractmethod
    def order_processing(self, money: int) -> str:
        ...

class GoodStrategy(Strategy):
    def check_mood_seller_candy(self, mood: CandySellerMood) -> bool:
        if (mood is CandySellerMood.GOOD or
            mood is CandySellerMood.BAD):
            return True
        return False

    def order_processing(self, money: int) -> str:
        return "The best candys for you!!!!"

class BadStrategy(Strategy):
    def check_mood_seller_candy(self, mood: CandySellerMood) -> bool:
        if (mood is CandySellerMood.BETTER_STAY_AWAY or
            mood is CandySellerMood.BAD):
            return True
        return False

    def order_processing(self, money: int) -> str:
        return "Take like liquorice stupid!"

class NormalStrategy(Strategy):
    def check_mood_seller_candy(self, mood: CandySellerMood) -> bool:
        return True

    def order_processing(self, money: int) -> str:
        if money < 5:
            return "Sorry, but no"
        elif money < 25:
            return "Give nice candys"
        elif money < 50:
            return "Give the best choco"
        else:
            return "Give THE BEST CANDYS IN THE WORLD"


class CandySeller:
    def __init__(self, strategy: Strategy, chief_mood: CandySellerMood) -> None:
        self._strategy = strategy
        self._chief_mood = chief_mood
        print(f"The start mood of the candy's seller: {chief_mood.name}")

    def get_chief_mood(self) -> CandySellerMood:
        return self._chief_mood

    def set_chief_mood(self, chief_mood: CandySellerMood) -> None:
        print(f"Now mood of the candy's seller: {chief_mood.name}")
        self._chief_mood = chief_mood

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def take_order(self, money: int) -> None:
        print(f"Client gives us {money} $")
        if self._strategy.check_mood_seller_candy(self._chief_mood):
            print(self._strategy.order_processing(money))
        else:
            print("Pretend the client didn't notice!")


barista = CandySeller(NormalStrategy(),
                      CandySellerMood.BETTER_STAY_AWAY)
barista.take_order(20)
barista.take_order(50)
barista.set_strategy(BadStrategy())
barista.take_order(40)
barista.take_order(200)
barista.set_strategy(GoodStrategy())
barista.take_order(40)
barista.set_chief_mood(CandySellerMood.GOOD)
barista.take_order(0)
