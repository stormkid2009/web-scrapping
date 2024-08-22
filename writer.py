import csv

def write_to_csv(all_matches, filename='matches.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["التاريخ", "البطولة", "الفريق الاول", "الفريق الثانى"])
        writer.writeheader()
        writer.writerows(all_matches)
    print(f"Data written to {filename}")
