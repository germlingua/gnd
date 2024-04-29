import csv

data_with_gnd = []
data_with_urls = {}

with open('outputs/pataky-test-29-4-24.csv', 'r', encoding='UTF-8') as file:
    for line in file:
        parts = line.strip().split(',')
        name = parts[0]
        if parts[1][2].isdigit():  # Entry with number
            data_with_gnd.append(parts)
        else:  # Entry with URLs
            urls = parts[1:]
            data_with_urls[name] = urls

with open('outputs/pataky-gnd-not-found-29-4-24.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'GND'])
    for name, gnd in data_with_urls.items():
        writer.writerow([name] + ([gnd] if isinstance(gnd, str) else gnd))

with open('outputs/pataky-gnd-found-29-4-24.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data_with_gnd)