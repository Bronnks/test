import random
import string
from django.utils import timezone

from django.core.management import BaseCommand
from faker import Faker

from achievements.models import Achievements, PlayerRanking
from players.models import Players, PlayerVehicles
from vehicles.models import Tank

fake = Faker()

class Command(BaseCommand):
    help = 'Заполняем базу данных'

    def handle(self, *args, **options):
        self.generate_players()
        self.generate_tank()
        self.generate_playervehicles()
        self.generate_achievements()
        self.generate_playerRanking()

        self.stdout.write(self.style.SUCCESS('Генерация базы данных выполнена успешно'))

    def generate_players(self, num_players=20):
        for _ in range(num_players):
            username = fake.user_name()
            email = fake.email()
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            date_joined = fake.date_time_between(start_date='-10y', end_date='now', tzinfo=timezone.get_current_timezone())
            Players.objects.create(username=username, email=email, password=password, date_joined=date_joined)

    def generate_tank(self, num_players=20):
        for _ in range(num_players):
            tank_name = fake.word()
            tank_type = random.choice(('легкий', "средний", "тяжелый", "поддержки", "уничтожения бронированных целей",
                                       "амфибия", "истребитель зенитных ракет", "разведчик"))
            tank_description = fake.sentence()
            damage_points = fake.pyint(min_value=0, max_value=1000)
            armor_points = fake.pyint(min_value=15, max_value=250)
            speed = fake.pyint(min_value=15, max_value=75)
            cost = fake.pyint(min_value=100000, max_value=1000000)
            Tank.objects.create(tank_name=tank_name, tank_type=tank_type, tank_description=tank_description,
                                damage_points=damage_points, armor_points=armor_points, speed=speed, cost=cost)

    def generate_playervehicles(self):
        for player in Players.objects.all():
            vehicle_id = random.choice(Tank.objects.all())
            experience_points = fake.pyint(min_value=1000, max_value=10000)
            PlayerVehicles.objects.create(player_id=player, vehicle_id=vehicle_id,
                                          experience_points=experience_points)

    def generate_achievements(self):
        for player in Players.objects.all():
            achievement_name = fake.word()
            achievement_description = fake.sentence()
            date_achieved = fake.date_time_between(start_date='-10y', end_date='now', tzinfo=timezone.get_current_timezone())
            Achievements.objects.create(player_id=player, achievement_name=achievement_name,
                                        achievement_description=achievement_description, date_achieved=date_achieved)

    def generate_playerRanking(self):
        for player in Players.objects.all():
            ranking_points = fake.pyint(min_value=1000, max_value=10000)
            PlayerRanking.objects.create(player_id=player, ranking_points=ranking_points)
