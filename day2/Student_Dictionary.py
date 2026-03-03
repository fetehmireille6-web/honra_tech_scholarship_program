my_profile = {
    "name": "Mireille Lareine",
    "age" : 20,
    "country" : "Cameroon",
    "Favourite subject": "Machine Learning",
    "Goal" : "Becoming a Senior AI Engineer"
}

print("My Profile")
for key, value in my_profile.items():
    print(f"{key.title()}: {value}")