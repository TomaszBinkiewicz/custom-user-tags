import csv
from custom_user_tags_app.templatetags.custom_tags import pg_13, bizz_fuzz
from custom_user_tags.settings import BASE_DIR
from os import path


def create_csv_file(users):
    file_path = path.join(BASE_DIR, 'custom_user_tags_app/static/csv/users.csv')
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Username', 'Birthday', 'Eligible', 'Random number', 'BuzzFizz'])
        for user in users:
            writer.writerow([user.username, user.birthday, pg_13(user), user.random_number, bizz_fuzz(user)])
