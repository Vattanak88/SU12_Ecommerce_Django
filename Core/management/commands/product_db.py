from django.core.management.base import BaseCommand
from Home.models import Product

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        products = [
            {
                "name": "Cropped Fitted T-Shirts",
                "description": "Cropped fitted t-shirt featuring short sleeves with embroidery design printed at left chest and crew-neck.",
                "price": 0.025,
                "image": "ZANDO30.06.20250663.jpg",
                "rate": 3.7,
                "discount_price": 3.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Wide Leg Denim Jean",
                "description": "Wide leg denim jean featuring side pockets with front button and zipper-up fastening.",
                "price": 0.025,
                "image": "Untitled Session0045.jpg",
                "rate": 3.7,
                "discount_price": 7.49,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Midi Skirt",
                "description": "Midi skirt featuring tie detail with zipper-up fastening at left waist.",
                "price": 0.025,
                "image": "ZD__3937.jpg",
                "rate": 3.7,
                "discount_price": 21.59,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Regular Stripped Shirt",
                "description": "Regular stripped shirt featuring long sleeves with pockets at left chest, shirt collar and front button fastening.",
                "price": 0.025,
                "image": "ZD__4559.jpg",
                "rate": 3.7,
                "discount_price": 15.95,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Oversized T-Shirts",
                "description": "Oversized t-shirt featuring short sleeves design with printed and round neck.",
                "price": 0.025,
                "image": "ZD__3874.jpg",
                "rate": 3.7,
                "discount_price": 8.37,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Long Sleeves Shirt",
                "description": "Cropped shirt featuring long sleeves, no design printed shirt collar and front button fastening.",
                "price": 0.025,
                "image": "ZD__3852.jpg",
                "rate": 3.7,
                "discount_price": 11.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Regular T-Shirts",
                "description": "Regular t-shirts featuring short sleeves and round neck.",
                "price": 0.025,
                "image": "ZD__4045.jpg",
                "rate": 3.7,
                "discount_price": 8.96,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Knitted Polo Shirt",
                "description": "Regular knitted polo shirt featuring short sleeves, shirt collar and front button fastening.",
                "price": 0.025,
                "image": "ZD__3592.jpg",
                "rate": 3.7,
                "discount_price": 13.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Wide Leg Trousers",
                "description": "Wide leg trousers featuring side pockets with front tie adjustable and zipper-up fastening.",
                "price": 0.025,
                "image": "ZD__3504.jpg",
                "rate": 3.7,
                "discount_price": 3.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Mini Polo Dresses",
                "description": "Mini polo dresses featuring short sleeves, do design printed shirt collar and front button fastening.",
                "price": 0.025,
                "image": "ZD__3880.jpg",
                "rate": 3.7,
                "discount_price": 3.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Cropped Long Sleeves Shirt",
                "description": "Cropped shirt featuring long sleeves with front pockets, shirt collar and front buttom fastening.",
                "price": 0.025,
                "image": "ZD__4278.jpg",
                "rate": 3.7,
                "discount_price": 21.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Poizen Ragen Top",
                "description": "Poizen reagen top featuring sleeveless with front zipper-up fastening and side tie adjustable.",
                "price": 0.025,
                "image": "TAKK0646-Edit.jpg",
                "rate": 3.7,
                "discount_price": 3.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Tank Top",
                "description": "Tank top featuring sleeveless.",
                "price": 0.025,
                "image": "ZD__2297.jpg",
                "rate": 3.7,
                "discount_price": 5.12,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Off-Shoulder T-Shirts",
                "description": "Off-shoulder t-shirts featuring short sleeves and front printed.",
                "price": 0.025,
                "image": "ZD__1662.jpg",
                "rate": 3.7,
                "discount_price": 33.18,
                "quantity": 10,
                "category_id": 1
            },
            {
                "name": "Textured T-Shirts",
                "description": "Cropped textured t-shirts featuring short sleeves and round neck.",
                "price": 0.025,
                "image": "ZD__1725.jpg",
                "rate": 3.7,
                "discount_price": 8.95,
                "quantity": 10,
                "category_id": 1
            },












    {
        "name": "Classic Cotton T-Shirt",
        "description": "A timeless and comfortable t-shirt made from 100% premium cotton. Perfect for everyday wear.",
        "price": 0.025,
        "image": "LEAD_569ZE10_600copy.webp",
        "rate": 3.7,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 1
    },
    {
        "name": "Slim-Fit Denim Jeans",
        "description": "Modern and stylish slim-fit jeans crafted from high-quality denim. A versatile addition to any wardrobe.",
        "price": 0.045,
        "image": "BEST-MENS-JEANS-2048px-9811.webp",
        "rate": 4.1,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 2
    },
    {
        "name": "Cozy Wool Sweater",
        "description": "Stay warm and fashionable with this cozy sweater made from a soft wool blend. Ideal for chilly days.",
        "price": 0.035,
        "image": "coosh9-222186-min__preview.jpg",
        "rate": 3.9,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 3
    },
    {
        "name": "Leather Biker Jacket",
        "description": "A classic biker jacket made from genuine leather. Adds a touch of edge to any outfit.",
        "price": 0.050,
        "image": "WEASLEY-BLCK-0047h-scaled.jpg",
        "rate": 4.6,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 4
    },
    {
        "name": "Casual Linen Shirt",
        "description": "A lightweight and breathable linen shirt, perfect for a relaxed and casual look.",
        "price": 0.045,
        "image": "untitled-session3537.webp",
        "rate": 4.6,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 5
    },
    {
        "name": "Tailored Chino Pants",
        "description": "Versatile and stylish chino pants that can be dressed up or down for any occasion.",
        "price": 0.050,
        "image": "chino-page-man-wearing-light-khaki-chino-steps-down-the-stairs-3-e1649749357223-975x1300.jpg",
        "rate": 3.1,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 6
    },
    {
        "name": "Graphic Print Hoodie",
        "description": "A comfortable and stylish hoodie with a unique graphic print. Perfect for a streetwear look.",
        "price": 0.045,
        "image": "Hustle_1.webp",
        "rate": 4.7,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 7
    },
    {
        "name": "Formal Dress Shirt",
        "description": "A crisp and elegant dress shirt, perfect for formal events and business meetings.",
        "price": 0.050,
        "image": "s7-1390091_alternate4.avif",
        "rate": 4.2,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 5
    },
    {
        "name": "Cargo Shorts",
        "description": "Comfortable and practical cargo shorts with multiple pockets. Ideal for outdoor activities.",
        "price": 0.045,
        "image": "1098935.jpg",
        "rate": 3.8,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 8
    },
    {
        "name": "V-Neck Sweater",
        "description": "A classic v-neck sweater made from a soft and comfortable merino wool.",
        "price": 0.045,
        "image": "il_fullxfull.2663518508_odxm.webp",
        "rate": 4.7,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 3
    },
    {
        "name": "Polo Shirt",
        "description": "A classic polo shirt for a smart-casual look.",
        "price": 0.040,
        "image": "mens-blue-mercerised-jersey-polo-shirt-mtpomeblu_1.webp",
        "rate": 4.2,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 5
    },
    {
        "name": "Bomber Jacket",
        "description": "A stylish and versatile bomber jacket.",
        "price": 0.050,
        "image": "best-bomber-jackets-654a645c613dd.avif",
        "rate": 3.8,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 4
    },
    {
        "name": "Turtleneck Sweater",
        "description": "A warm and stylish turtleneck sweater.",
        "price": 0.050,
        "image": "87010605_08.avif",
        "rate": 3.6,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 3
    },
    {
        "name": "Denim Jacket",
        "description": "A timeless denim jacket for a casual look.",
        "price": 0.050,
        "image": "87080596_TM.avif",
        "rate": 4.1,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 4
    },
    {
        "name": "Flannel Shirt",
        "description": "A comfortable and warm flannel shirt.",
        "price": 0.045,
        "image": "MERGED_0073_Layer130.webp",
        "rate": 4.8,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 5
    },
    {
        "name": "Pea Coat",
        "description": "A classic and warm pea coat for cold weather.",
        "price": 0.050,
        "image": "PeacoatBoardwalkLSMOBILE1_e399cef2-e10a-4a7d-8c62-3f7ab7f1e6e5.webp",
        "rate": 3.0,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 4
    },
    {
        "name": "Henley Shirt",
        "description": "A stylish and comfortable henley shirt.",
        "price": 0.045,
        "image": "Ms-LS-Henley-Fog-WOOLLY_4673.webp",
        "rate": 3.9,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 5
    },
    {
        "name": "Cardigan Sweater",
        "description": "A versatile and stylish cardigan sweater.",
        "price": 0.045,
        "image": "71m5o8kBjaL._UY350_.jpg",
        "rate": 3.7,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 3
    },
    {
        "name": "Windbreaker Jacket",
        "description": "A lightweight and water-resistant windbreaker jacket.",
        "price": 0.045,
        "image": "womens-windbreaker-jacket-neon-coral-jacket-aviator-nation-684000.webp",
        "rate": 3.4,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 4
    },
    {
        "name": "Straight-Leg Jeans",
        "description": "Classic straight-leg jeans for a timeless look.",
        "price": 0.045,
        "image": "JORDYN_HIGH_WAISTED_STRAIGHT_LEG_JEANS_16.01.24_05.webp",
        "rate": 3.8,
        "discount_price": 1000.00,
        "quantity": 10,
        "category_id": 2
    }
]


        for p in products:
            if not Product.objects.filter(name = "dksjf").exists():
                Product.objects.create(**p)
            else :
                print("Duplicate product found")

        print("Static products inserted successfully!")