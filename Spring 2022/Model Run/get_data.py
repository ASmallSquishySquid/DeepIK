import joblib
# from https://thispointer.com/python-add-a-column-to-an-existing-csv-file/
from csv import reader
from csv import writer

def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)

with open("Spring 2022\Tracking Data Check\Rerun\pos.pkl", "rb") as file:
	data = joblib.load(file)

endpoints_one = [k[-1][0] for k in data["default"].values()]
endpoints_two = [k[-1][1] for k in data["default"].values()]

add_column_in_csv('Spring 2022\Model Run\Data.csv', 'Spring 2022\Model Run\Data1.csv', lambda row, line_num: row.append(endpoints_one[line_num - 1]))
add_column_in_csv('Spring 2022\Model Run\Data1.csv', 'Spring 2022\Model Run\Data2.csv', lambda row, line_num: row.append(endpoints_two[line_num - 1]))