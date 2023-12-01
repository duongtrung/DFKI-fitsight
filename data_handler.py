import csv

def save_angles_to_csv(filename, angles):
    # Open CSV file for writing
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['angleLH', 'angleRH', 'angleLL', 'angleRL'])
        writer.writerows(angles)

def save_percentage_to_csv(filename, percentages):
    # Open CSV file for writing
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['percentage'])
        writer.writerows([[percentage] for percentage in percentages])

def save_bar_to_csv(filename, bars):
    # Open CSV file for writing
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['bar'])
        writer.writerows([[bar] for bar in bars])
