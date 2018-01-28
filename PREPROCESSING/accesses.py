import random
from test_for_uniqueness import *

with open('generated_access_data.csv', 'w') as csv_write_file:

    # specify fieldnames
    fieldnames = ['p_id', 'd_id', 'location_of_access', 'time_of_access', 'data_requested', 'emergency', 'access_granted']

    csv_writer = csv.DictWriter(csv_write_file, fieldnames=fieldnames)

    csv_writer.writeheader()

    # this loop is for the best case in our training set
    # all doctors will access data from their assigned pcs
    # during hospital hours (24 hours time format)
    # they will access data relevant to their specialization
    # there will be no emergency cases
    # and access will always be granted
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # 9 am to 9 pm
        hours = random.randint(9, 21)
        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours) + ":" + str(minutes).zfill(2)

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[doctor], 'time_of_access': time, 'data_requested': 'relevant', 'emergency': 'no', 'access_granted': 'yes'})

    # In between there will be many loops for different combinations
    # of average cases
    # where access will either be granted or denied
    # use the previous history and emergency left columns for decision making
    # we will also include some cases
    # where all values are random (noisy data)
    # so that the data is not very obvious

    # this loop is for the worst case in our training set
    # no doctor will access data from his assigned pcs
    # outside hospital hours (24 hours time format)
    # they will access irrelevant data
    # there will be no emergency cases
    # and access will always be denied
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # before hospital hours
        hours_before = random.randint(0, 8)

        # after hostpial hours
        hours_after = random.randint(22, 24)

        available_hours = [hours_before, hours_after]

        hours = random.choice(available_hours)

        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours) + ":" + str(minutes).zfill(2)

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': random.choice(d_ids), 'time_of_access': time, 'data_requested': 'irrelevant', 'emergency': 'no', 'access_granted': 'no'})
