import json
import csv


def convert_json_to_csv(input_json_file, output_csv_file):
    with open(input_json_file, 'r') as json_file:
        data = json.load(json_file)

    with open(output_csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header based on the keys of the first JSON object
        header = list(data[0].keys())
        csv_writer.writerow(header)

        # Write the data
        for row in data:
            csv_writer.writerow(row.values())

convert_json_to_csv('input.json', 'output.csv')