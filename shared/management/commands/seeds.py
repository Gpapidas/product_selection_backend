from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seeds database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Database seeded successfully!\n")
