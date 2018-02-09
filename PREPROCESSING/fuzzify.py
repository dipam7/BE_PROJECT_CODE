import csv
import re
import pandas as pd

access_granted = []
emergency = []
data_requested = []
time_of_access = []
previous_history = []
location_of_access = []

with open('generated_fuzzified_access_data.csv', 'w', newline='') as csv_write_file:

    # specify fieldnames
    fieldnames = ['data_requested','location_of_access','time_of_access','emergency','previous_history','access_granted']

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

    d_id2_column = csv_reader2.d_id
    accesses_column = csv_reader2.Accesses
    grants_column = csv_reader2.Grants
    location_of_access2_column = csv_reader2.Assigned_PC
    
    index=0
    
    for i in emergency_column:#emergency column
        
        if i=="yes":
            emergency.append(1)
            
        else:
            emergency.append(0)
            
    for i in data_requested_column:#data requested column
        
        if i=="relevant":
            data_requested.append(1)
            
        elif i == "slightly-irrelevant":
            data_requested.append(0.5)

        else:
            data_requested.append(0)
            
    for i in access_granted_column:#access granted column
        
        if i=="yes":
            access_granted.append(1)
            
        else:
            access_granted.append(0)
            
    indexOfi = 0#for navigating 1st csv file
    for i in d_id_column:#previous history & location
        index2 = 0#for navigating 2nd csv file
        for j in d_id2_column:
            if i == j:
                previous_history.append(grants_column[index2]/accesses_column[index2])
                if location_of_access_column[indexOfi]==location_of_access2_column[index2]:
                    location_of_access.append(1)
                    break
                else:
                    pc=re.split('[:]', location_of_access_column[indexOfi])
                    print(pc[0])
                    if pc[0] == "07":
                        location_of_access.append(0)
                        break
                    else:
                        location_of_access.append(0.5)
                        break
            index2 = index2 + 1
        indexOfi = indexOfi + 1

    for i in time_of_access_column:#time of access column
        
        i=re.split('[:]', i)
        if (int)(i[0])>=9 and (int)(i[0])<22:
            time_of_access.append(1)
            
        else:
            time_of_access.append(0)

        csv_writer.writerow({'data_requested': data_requested[index],'location_of_access': location_of_access[index], 'time_of_access': time_of_access[index], 'emergency': emergency[index], 'previous_history': previous_history[index],'access_granted': access_granted[index]})
        index=index+1
        



    
    
