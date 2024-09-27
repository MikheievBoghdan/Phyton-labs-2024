from faker import Faker
import csv
import random

fake = Faker(locale='uk_UA')

male_middle_name = [
    'Олександрович', 'Іванович', 'Сергійович', 'Миколайович', 'Андрійович',
    'Володимирович', 'Петрович', 'Дмитрович', 'Федорович', 'Богданович',
    'Юрійович', 'Михайлович', 'Віталійович', 'Романович', 'Євгенович',
    'Олегович', 'Васильович', 'Валентинович', 'Борисович', 'Григорович'
]

female_middle_name = [
    'Олександрівна', 'Іванівна', 'Сергіївна', 'Миколаївна', 'Андріївна',
    'Володимирівна', 'Петрівна', 'Дмитрівна', 'Федорівна', 'Богданівна',
    'Юріївна', 'Михайлівна', 'Віталіївна', 'Романівна', 'Євгенівна',
    'Олегівна', 'Василівна', 'Валентинівна', 'Борисівна', 'Григорівна'
]

def generate_employees(filename, count=2000):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

        for _ in range(count):
            gender = random.choices(['M', 'F'], [0.6, 0.4])[0]

            if gender == 'M':
                first_name = fake.first_name_male()
                last_name = fake.last_name_male()
                middle_name = random.choice(male_middle_name)
            else:
                first_name = fake.first_name_female()
                last_name = fake.last_name_female()
                middle_name = random.choice(female_middle_name)

            birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
            position = fake.job()
            city = fake.city()
            address = fake.address()
            phone = fake.phone_number()
            email = fake.email()

            writer.writerow([last_name, first_name, middle_name, 'Чоловіча' if gender == 'M' else 'Жіноча', birth_date, position, city, address, phone, email])

generate_employees('employees.csv')
print("тест")