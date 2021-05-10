import csv

# with open('workers.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for row in csv_reader:
#         print(row)


# with open('workers.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         print(dict(row))

# with open('employee_file.csv', mode='w', newline="") as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# fieldnames = ["href", "image", "title", "imdb_rating", "imdb_votes"]
# info = {'href': 'https://srulad.com/movie/2026-the-physician-mkurnali.html','image': 'https://srulad.com/assets/uploads/76905_Physician_german_poster.jpg','title': 'The Physician','imdb_rating': '7.2','imdb_votes': '27640'}
# with open('movies_info.csv', mode='w', newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()

#     writer.writerow(info)

# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(points, f, ensure_ascii=False, indent=4)
