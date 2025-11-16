from django.core.management.base import BaseCommand
from Home.models import Feature

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        features = [
            {
                "title": "Regular Wrap Shirts",
                "image": "7_lc5kla.jpg"
            },
            {
                "title": "Bubble Hem Mini Skirts",
                "image": "8_mapllr.jpg"
            },
            {
                "title": "Mini Skirts",
                "image": "9_b8oq2u.jpg"
            },
            {
                "title": "Tube Top",
                "image": "11_wlhpor.jpg"
            },
        ]

        # Insert data
        for feature in features:
            if not Feature.objects.filter(title=feature["title"]).exists():  # Ensure title is unique
                Feature.objects.create(**feature)
            else:
                print(f"feature with title '{feature['title']}' already exists. Skipping insert.")

        print("Static features inserted successfully!")
