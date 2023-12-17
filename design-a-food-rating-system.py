from collections import defaultdict
from sortedcontainers import SortedList


class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.__food_to_cuisine = {}
        self.__food_to_rating = {}
        self.__cusine_to_rating = defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.__cusine_to_rating[cuisine].add((-rating, food))
            self.__food_to_cuisine[food] = cuisine
            self.__food_to_rating[food] = rating


    def changeRating(self, food: str, newRating: int) -> None:
        old_rating = self.__food_to_rating[food]
        cuisine = self.__food_to_cuisine[food]
        self.__cusine_to_rating[cuisine].remove((-old_rating, food))
        self.__food_to_rating[food] = newRating
        self.__cusine_to_rating[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        print(self.__cusine_to_rating[cuisine][0][1])
        return self.__cusine_to_rating[cuisine][0][1]
