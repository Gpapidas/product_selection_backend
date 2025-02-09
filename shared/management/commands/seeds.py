from django.core.management.base import BaseCommand

from products.seeders.db.seed_products import seed_products


class Command(BaseCommand):
    help = 'Seeds database'

    def handle(self, *args, **kwargs):
        seed_products()

        self.stdout.write("Database seeded successfully!\n")
