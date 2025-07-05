contacts = {
    "name": "Bob",
    "lastname": "Ibaza",
    "address": "Fredericksburg",
    "state": "VA",
}

print(contacts.get("name", "Uknown"))

print(contacts.get("school", "Uknown"))


print(contacts.keys())


contacts["phone"] = "777-33-455-45"
print(contacts.items())

# Un pack and iterate ove dictionary
contact_emails = {"bob": "papeguirassy@gmail.com", "ken": "ken@gmail.com"}

for name, email in contact_emails.items():
    print(f"My name is : {name} and this is my email {email}")
