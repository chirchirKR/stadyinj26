from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="Derick_Chirchir",
        email="kimutaichirchir16@gmail.com",
        password="P@$$word!_1611"
    )
    print("Superuser created.")
else:
    print("Superuser already exists.")
