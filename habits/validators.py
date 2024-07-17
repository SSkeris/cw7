from datetime import timedelta

from rest_framework.exceptions import ValidationError


class ChoiceRewardValidator:
    """ Исключает одновременный выбор награды и приятной привычки. """

    def __init__(self, related_habit, reward):
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, habit):
        if habit.get(self.related_habit) and habit.get(self.reward):
            raise ValidationError(
                f'''Нельзя выбрать {self.related_habit} и {self.reward} одновременно, 
                выберите награду или приятную привычку.'''
            )


class DurationValidator:
    """ Проверяет длительность выполнения привычки, она не должна превышать 2 минут. """

    def __init__(self, duration):
        self.duration = duration

    def __call__(self, habit):
        max_duration = timedelta(minutes=2)
        if habit.get(self.duration) and habit.get(self.duration) > max_duration:
            raise ValidationError(f'Выполнение не может длиться более {max_duration}')
