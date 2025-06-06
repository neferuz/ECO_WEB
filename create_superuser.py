import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mylanding.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("neferuz", "admin@example.com", "admin123")
    print("✅ Superuser created")
else:
    print("ℹ️ Superuser already exists")
