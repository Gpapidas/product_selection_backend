from django.core.management import call_command
from django.db import connections
from django.test.runner import DiscoverRunner


class CustomTestRunner(DiscoverRunner):
    """
    Custom test runner that ensures the test database is used properly and is seeded before tests run.

    This test runner overrides the `setup_databases` method to:
    1. Use Django's automatically created test database.
    2. Run the `test_seeds` management command to seed the test database with initial data.

    Key Features:
    - The `setup_databases` method is guaranteed to run only once for the entire testing environment,
      ensuring all tests share the same seeded test database. This prevents redundant operations and improves performance.
    - The seeding logic is executed after the test database is created, ensuring all operations are safely performed
      on the test database and not the production database.

    Usage:
    - Set `TEST_RUNNER = 'shared.tests.runner.CustomTestRunner'` in your `settings.py`.
    - Run tests as usual: `python manage.py test`.

    Debugging:
    - To verify the test database is being used, check the name of the database via `connections['default'].settings_dict['NAME']`.
      The database name should start with `test_`.
    """

    def setup_databases(self, **kwargs):
        """
        Sets up the test databases and ensures the test database is used for seeding.
        """
        # Call the parent method to create the test database
        db_configs = super().setup_databases(**kwargs)

        # Ensure seeding happens in the test database
        print(f"Seeding test database: {connections['default'].settings_dict['NAME']}")
        call_command('test_seeds')

        return db_configs
