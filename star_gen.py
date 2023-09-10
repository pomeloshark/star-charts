# importing the csv module
import csv
import random



def get_right_ascension():
    return round(random.uniform(0, 24), 10)

def get_declination():
    return round(random.uniform(-90, 90), 10)

def get_magnitude():
    return round(random.uniform(-1.47, 6.5), 10)

def generate_stardata():
    return [get_right_ascension(), get_declination(), get_magnitude()]

rows = [generate_stardata()]



# writing to csv file
with open('stardata.csv', 'w') as csvfile:
    # creating a csv writer object
    writer = csv.writer(csvfile)

    # writing the data rows
    for n in range(1, 4550):
        row = generate_stardata()
        writer.writerow(row)
