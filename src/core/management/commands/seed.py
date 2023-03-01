from django_seed import Seed
from core.models import Town, House, Person
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
    help = "Seed elements to database"

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            type=int,
            help='Number of elements to seed'
        )

    def handle(self, *args, **options):
        self.stdout.write("Seeding data")

        number = options.get('number', 10)

        seeder = Seed.seeder()
        seeder.add_entity(Town, number, {   
            'name': lambda x: seeder.faker.city(),
            'area': lambda x: seeder.faker.pydecimal(left_digits=5, right_digits=2, positive=True),
            'budget': lambda x: seeder.faker.pydecimal(left_digits=5, right_digits=2, positive=True),
        })

        seeder.add_entity(House, number, {
            'address': lambda x: seeder.faker.address(),
            'capacity': lambda x: seeder.faker.pyint(min_value=1, max_value=10, step=1),
            'levels': lambda x: seeder.faker.pyint(min_value=1, max_value=3, step=1),
        })

        seeder.add_entity(Person, number, {
            'age': lambda x: seeder.faker.pyint(min_value=1, max_value=100, step=1),
            'name': lambda x: seeder.faker.name(),
            'phone': lambda x: seeder.faker.phone_number(),
            'id' : lambda x : seeder.faker.pyint(min_value=1, max_value=100, step=1)
        })

        seeder.execute()
            