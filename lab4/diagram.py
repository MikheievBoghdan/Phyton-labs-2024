import csv
from datetime import datetime
import matplotlib.pyplot as plt


def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def read_csv_file(csv_file):
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = [row for row in reader]
            print("Ok, файл успішно відкрито.")
            return data
    except FileNotFoundError:
        print("Помилка: CSV файл не знайдено!")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None

def analyze_employee_data(data):
    if not data:
        return

    male_count = 0
    female_count = 0
    age_categories = {
        "молодше_18": {"male": 0, "female": 0},
        "між_18-45": {"male": 0, "female": 0},
        "між_45-70": {"male": 0, "female": 0},
        "старше_70": {"male": 0, "female": 0}
    }

    for row in data:
        gender = row[3]
        birth_date = datetime.strptime(row[4], '%Y-%m-%d')
        age = calculate_age(birth_date)

        if gender == "Чоловіча":
            male_count += 1
            if age < 18:
                age_categories["молодше_18"]["male"] += 1
            elif 18 <= age <= 45:
                age_categories["між_18-45"]["male"] += 1
            elif 45 < age <= 70:
                age_categories["між_45-70"]["male"] += 1
            else:
                age_categories["старше_70"]["male"] += 1

        elif gender == "Жіноча":
            female_count += 1
            if age < 18:
                age_categories["молодше_18"]["female"] += 1
            elif 18 <= age <= 45:
                age_categories["між_18-45"]["female"] += 1
            elif 45 < age <= 70:
                age_categories["між_45-70"]["female"] += 1
            else:
                age_categories["старше_70"]["female"] += 1


    print(f"Кількість співробітників чоловічої статі: {male_count}")
    print(f"Кількість співробітників жіночої статі: {female_count}")
    print("Кількість співробітників у вікових категоріях:")
    for category, counts in age_categories.items():
        print(f"{category}: Чоловіків - {counts['male']}, Жінок - {counts['female']}")


    plot_gender_age_distribution(male_count, female_count, age_categories)

def plot_gender_age_distribution(male_count, female_count, age_categories):
    categories = list(age_categories.keys())
    male_counts = [age_categories[cat]["male"] for cat in categories]
    female_counts = [age_categories[cat]["female"] for cat in categories]


    fig, axs = plt.subplots(1, 2, figsize=(15, 5))

    # Графік 1: Кількість співробітників за статтю
    labels = ['Чоловіки', 'Жінки']
    counts = [male_count, female_count]
    axs[0].bar(labels, counts, color=['blue', 'pink'])
    axs[0].set_xlabel('Стать')
    axs[0].set_ylabel('Кількість співробітників')
    axs[0].set_title('Кількість співробітників за статтю')

    # Графік 2: Кількість співробітників за віковими категоріями
    x = range(len(categories))
    axs[1].bar(x, male_counts, width=0.4, label='Чоловіки', color='blue', align='center')
    axs[1].bar(x, female_counts, width=0.4, label='Жінки', color='pink', align='edge')
    axs[1].set_xlabel('Вікові категорії')
    axs[1].set_ylabel('Кількість співробітників')
    axs[1].set_title('Кількість співробітників за віковими категоріями')
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(categories)
    axs[1].legend()

    plt.tight_layout()
    plt.show()


csv_file = 'employees.csv'
employee_data = read_csv_file(csv_file)
analyze_employee_data(employee_data)
