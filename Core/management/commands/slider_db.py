from django.core.management.base import BaseCommand
from Home.models import Slider

class Command(BaseCommand):
    help = 'Creates Slider objects'

    def handle(self, *args, **options):
        slider = [
            {
                'id' : 1,
                'title' : "Men's",
                'collection' : 'Collections',
                'year' : 2025,
                'description' : 'lorem sfsfj sfsfjsafk afksajf asfj sajf sjkfjsf',
                'image' : 'image/slider/1-Photoroom.png',
                'status' : 'active',
            },
            {
                'id': 2,
                'title': "Women's",
                'collection': 'Collections',
                'year': 2025,
                'description': 'lorem sfsfj sfsfjsafk afksajf asfj sajf sjkfjsf',
                'image': 'image/slider/2-Photoroom.png',
                'status' : 'inactive',
            },
        ]
        for s in slider:
            if not Slider.objects.filter(id = s['id']).exists() :
                Slider.objects.create(**s)
                print("Static sliders inserted successfully!")
            else:
                print(f"Duplicate slider found in ID : {s['id']}")


