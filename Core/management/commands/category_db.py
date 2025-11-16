from django.core.management.base import BaseCommand
from Home.models import Category

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        categories = [
            { "name": "T-Shirts" },
            { "name": "Jeans" },
            { "name": "Sweaters" },
            { "name": "Jackets" },
            { "name": "Shirts" },
            { "name": "Pants" },
            { "name": "Hoodies" },
            { "name": "Shorts" }
        ]

        # Insert data
        for category in categories:
            if not Category.objects.filter(name=category["name"]).exists():  # Ensure title is unique
                Category.objects.create(**category)
            else:
                print(f"Category with title '{category['name']}' already exists. Skipping insert.")

        print("Static categories inserted successfully!")
