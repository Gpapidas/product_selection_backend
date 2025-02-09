from django.core.management import call_command
from django.core.management.base import BaseCommand

from users.seeders.test_db.seed_users import seed_test_users


class Command(BaseCommand):
    help = 'Seeds test database'

    def handle(self, *args, **kwargs):
        # Run the existing `seeds` command to populate base data
        call_command("seeds")

        seed_test_users()
        self.stdout.write("Test database seeded successfully!\n")
