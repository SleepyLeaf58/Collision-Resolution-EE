from Generator import *
from chaining import *
from Utils import *
import time
import csv

gen = Generator(100000, 20, 10)
gen.add_sample_list() # Adds existing test case file paths to the list of filepaths
table = ChainingHashTable(gen.max_strings)

#print("Length", len(gen.samples))
with open('chaining.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    telemetry_start = time.time()

    # Running Tests
    index = 0
    for i in range(gen.data_points):
        sum = 0

        for trial in range(gen.num_of_trials):
            start = time.time()
            with open(gen.samples[index], 'r') as file:
                for j in range(i*gen.increment):
                    table.insert(file.read(), j)
            end = time.time()

            sum += end - start

            index += 1

        avg = sum / gen.num_of_trials
        
        csv_writer.writerow([(i+1)*gen.increment, avg])

        # Telemetry Update
        telemetry_time = time.time()
        print("Data point", i+1, "of", gen.data_points, "|", Utils.convert(telemetry_time-telemetry_start), "elapsed")


    