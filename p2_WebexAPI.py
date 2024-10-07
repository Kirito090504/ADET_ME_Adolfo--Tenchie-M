from faker import Faker

# Initialize the Faker library
fake = Faker()

# Question 4
# Generate 10 fake user profiles
profiles = []
for _ in range(10):
    profile = {
        "Full Name": fake.name(),
        "Email Address": fake.email(),
        "Job Title": fake.job(),
        "Company": fake.company()
    }
    profiles.append(profile)

# Print each profile
for profile in profiles:
    print(profile)

# Question 5
# Generate 10 fake transaction records
transactions = []
for _ in range(10):
    transaction = {
        "Transaction ID": fake.uuid4(),
        "Transaction Date": fake.date(),
        "Amount": round(fake.random.uniform(100.00, 5000.00), 2)
    }
    transactions.append(transaction)

# Print each transaction
for transaction in transactions:
    print(transaction)