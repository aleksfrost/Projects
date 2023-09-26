class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


to_check = input().split()
for attr in to_check:
    if attr.lower() in Person.__dict__:
        print(f'{attr}-YES')
    else:
        print(f'{attr}-NO')
