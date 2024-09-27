import csv
from openpyxl import Workbook
from datetime import datetime


def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def generate_xlsx_from_csv(csv_file, xlsx_file):
    try:

        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)


            all_data = []
            for row in reader:
                all_data.append(row)


            workbook = Workbook()
            all_sheet = workbook.active
            all_sheet.title = "all"

            all_sheet.append(["№", "Прізвище", "Ім’я", "По батькові", "Дата народження", "Вік"])


            for index, row in enumerate(all_data, start=1):
                last_name = row[0]
                first_name = row[1]
                middle_name = row[2]
                birth_date = datetime.strptime(row[4], '%Y-%m-%d')
                age = calculate_age(birth_date)

                all_sheet.append([index, last_name, first_name, middle_name, birth_date.strftime('%Y-%m-%d'), age])


            categories = {
                "younger_18": [],
                "18-45": [],
                "45-70": [],
                "older_70": []
            }

            for row in all_data:
                birth_date = datetime.strptime(row[4], '%Y-%m-%d')
                age = calculate_age(birth_date)

                if age < 18:
                    categories["younger_18"].append(row)
                elif 18 <= age < 45:
                    categories["18-45"].append(row)
                elif 45 <= age < 70:
                    categories["45-70"].append(row)
                else:
                    categories["older_70"].append(row)


            for category, data in categories.items():
                sheet = workbook.create_sheet(title=category)
                sheet.append(["№", "Прізвище", "Ім’я", "По батькові", "Дата народження", "Вік"])
                for index, row in enumerate(data, start=1):
                    birth_date = datetime.strptime(row[4], '%Y-%m-%d')
                    age = calculate_age(birth_date)
                    sheet.append([index, row[0], row[1], row[2], birth_date.strftime('%Y-%m-%d'), age])

            workbook.save(xlsx_file)
            print("Ok, файл XLSX успішно створено.")
    except FileNotFoundError:
        print("Помилка: CSV файл не знайдено!")
    except Exception as e:
        print(f"Помилка: {e}")

generate_xlsx_from_csv('employees.csv', 'employees.xlsx')
