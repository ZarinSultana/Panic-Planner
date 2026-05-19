import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'panicplanner.settings')
django.setup()

from resources.models import Resource

# Add sample resources
resources_data = [
    {
        'title': 'National Crisis Hotline',
        'description': 'Available 24/7 for mental health support',
        'url': 'https://www.crisishotline.org',
        'category': 'hotline',
        'is_emergency': True
    },
    {
        'title': 'Meditation Guide',
        'description': 'Learn basic meditation techniques to reduce stress',
        'category': 'self_help',
        'is_emergency': False
    },
    {
        'title': 'Mental Health Article',
        'description': 'Understanding anxiety and panic attacks',
        'url': 'https://www.example.com/mental-health',
        'category': 'articles',
        'is_emergency': False
    }
]

for data in resources_data:
    r, created = Resource.objects.get_or_create(title=data['title'], defaults=data)
    if created:
        print(f"Created: {data['title']}")
    else:
        print(f"Already exists: {data['title']}")

print(f"\nTotal resources: {Resource.objects.count()}")
