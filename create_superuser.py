# create_superuser.py
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("neferuz", "notferuz@gmail.com", "1235804679f")
    print("✅ Superuser created")
else:
    print("ℹ️ Superuser already exists")
