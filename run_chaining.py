from Generator import *
from chaining import *
from Utils import *
import time
import csv

gen = Generator(100000, 20, 20, 500)

print("Sample List Added")
#print("Length", len(gen.samples))
with open('chaining.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    telemetry_start = time.time()

    # Running Insertions
    index = 0
    for i in range(gen.data_points):
        sum = 0
        for trial in range(gen.num_of_trials):
            table = ChainingHashTable(gen.max_strings)
            # Paths
            cur_path = os.path.dirname(__file__)
            sample_path = os.path.relpath(f"samples/sample_{(i+1)*gen.increment}_strings_{trial}", cur_path)
            case_path = os.path.relpath(f"search_cases/case_{(i+1)*gen.increment}_strings_{trial}", cur_path)

            # Running Insertions
            with open(sample_path, 'r') as file:
                for j in range((i+1)*gen.increment):
                    table.insert(file.readline(), j)

            print("Data point inserted", i+1, "of", gen.data_points, "|")
            # Running Searches

            search_list = []
            
            with open(case_path, 'r') as file:
                for j in range(gen.num_cases):
                    search_list.append(file.readline())
                file.close()

            start = time.time()

            for j in search_list:
                table.contains(j)
            
            end = time.time()

            sum += end - start

            # Telemetry Update
            telemetry_time = time.time()
            print("Trial searched", trial, "of", gen.num_of_trials, "for", (i+1) * gen.increment, "|", Utils.convert(telemetry_time-telemetry_start), "elapsed")
            
            index += 1

        avg = sum / (gen.num_of_trials * gen.num_cases)
        csv_writer.writerow([(i+1)*gen.increment, avg])

        # Telemetry Update
        telemetry_time = time.time()
        print("Data point inserted", i+1, "of", gen.data_points, "|", Utils.convert(telemetry_time-telemetry_start), "elapsed")


    