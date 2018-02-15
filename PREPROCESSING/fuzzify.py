import csv
import re
import pandas as pd
import random
from test_for_uniqueness import *

access_granted = []
emergency = []
data_requested = []
time_of_access = []
previous_history = []
location_of_access = []

with open('generated_fuzzified_access_data.csv', 'w', newline='') as csv_write_file:

    # specify fieldnames
    fieldnames = ['data_requested', 'location_of_access', 'time_of_access', 'emergency', 'previous_history', 'access_granted']

    csv_writer = csv.DictWriter(csv_write_file, fieldnames=fieldnames)

    csv_writer.writeheader()

    csv_reader1 = pd.read_csv('generated_access_data.csv')

    csv_reader2 = pd.read_csv('generated_doctors_data.csv')

    emergency_column = csv_reader1.emergency
    access_granted_column = csv_reader1.access_granted
    data_requested_column = csv_reader1.data_requested
    time_of_access_column = csv_reader1.time_of_access
    d_id_column = csv_reader1.d_id
    location_of_access_column = csv_reader1.location_of_access
    specialization_column = csv_reader1.Specialization

    d_id2_column = csv_reader2.d_id
    accesses_column = csv_reader2.Accesses
    grants_column = csv_reader2.Grants
    location_of_access2_column = csv_reader2.Assigned_PC

    index = 0

    # normalize emergency
    for i in emergency_column:
        if i == "yes":
            emergency.append(1)
        else:
            emergency.append(0)

    # use sensitivity score along with data relevance
    # for this column
    for i, j in zip(data_requested_column, specialization_column):
        if i in spec_related_data[j][0]:
            data_requested.append(1)
        elif "+" in i:
            temp = i.split('+')
            # we have to find the spec where temp[1]
            # is and not the one where j is
            for k in specialization_column:
                if temp[1] in spec_related_data[k][0]:
                    score = spec_related_data[k][1]
                    # print(score)
                    break

            if float(score) < 0.5:
                data_requested.append(0.7)
            else:
                data_requested.append(0.3)
        else:
            data_requested.append(0)

        # normalize output lable
    for i in access_granted_column:
        if i == "yes":
            access_granted.append(1)
        else:
            access_granted.append(0)

    # fuzzify previous history as number of grants / accesses
    for i in d_id_column:
        val = int(doctors_grants[i][1]) / int(doctors_grants[i][0])
        val = round(val, 2)
        previous_history.append(val)

    # fuzzify location of access
    for i, j in list(zip(d_id_column, location_of_access_column)):
        if doctors_pc[i] == j:
            location_of_access.append(1)
        elif j in mac_addresses:
            location_of_access.append(0.5)
        else:
            location_of_access.append(0)

    # to fuzzify time of access
    for i in time_of_access_column:

        i = re.split('[:]', i)
        if (int)(i[0]) >= 9 and (int)(i[0]) < 22:
            time_of_access.append(1)
        elif ((int)(i[0]) >= 8 and (int)(i[0]) < 9) or ((int)(i[0]) >= 22 and (int)(i[0]) < 23):
            time_of_access.append(0.5)
        else:
            time_of_access.append(0)

        csv_writer.writerow({'data_requested': data_requested[index], 'location_of_access': location_of_access[index], 'time_of_access': time_of_access[index], 'emergency': emergency[index], 'previous_history': previous_history[index], 'access_granted': access_granted[index]})
        index = index + 1
