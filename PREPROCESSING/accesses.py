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

    # average case 1:
    # doctors will not access data from their own pc but
    # everything else will be proper
    # the first 70% doctors will get access because they have
    # a good previous history record
    # in the other 30% doctors, the doctors with large differences
    # in previous history will not get access
    # and the doctors with small difference will randomly get access or no
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # 9 am to 9 pm
        hours = random.randint(9, 21)
        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours) + ":" + str(minutes).zfill(2)

        accesses = int(doctors_grants[doctor][0])
        grants = int(doctors_grants[doctor][1])
        # print(accesses)
        # print(grants)

        # result is initially set to yes for the doctors with good prev history
        result = 'yes'

        # if the grants are less than 75% then choose on random whether to
        # give access or no
        if grants < int(0.75 * accesses):
            result = random.choice(['yes', 'no'])

        # but if the grants are less than 50% of accesses
        # don't give access
        if grants < int(0.5 * accesses):
            result = 'no'

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': random.choice(d_ids), 'time_of_access': time, 'data_requested': 'relevant', 'emergency': 'no', 'access_granted': result})

    # average case 2:
    # same as average case 1 but instead of wrong computer
    # doctors will access data at the wrong time
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

        accesses = int(doctors_grants[doctor][0])
        grants = int(doctors_grants[doctor][1])
        # print(accesses)
        # print(grants)

        # result is initially set to yes for the doctors with good prev history
        result = 'yes'

        # if the grants are less than 75% then choose on random whether to
        # give access or no
        if grants < int(0.75 * accesses):
            result = random.choice(['yes', 'no'])

        # but if the grants are less than 50% of accesses
        # don't give access
        if grants < int(0.5 * accesses):
            result = 'no'

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[doctor], 'time_of_access': time, 'data_requested': 'relevant', 'emergency': 'no', 'access_granted': result})

    # average case 3:
    # doctors will access data from wrong pc at the wrong time
    # think about how to give accesses
    # include emergency in some cases and then
    # try to deduct the emergency value in the doctors database

    # average case 4:
    # doctors will access data from the wrong pc
    # during hospital hours
    # data will be slightly irrelevant
    # use prev history and emergency to make decisions
    # try to deduct the emergency value in the doctors database

    # average case 5:
    # same as average case 4 only instead of wrong pc
    # the doctor will access data at the wrong time

    # average case 6:
    # wrong pc and highly irrelevant data

    # average case 7:
    # wrong time and highly irrelevant data

    # average case 8:
    # wrong pc, wrong, time and highly irrelevant data
    # only check emergency to give access
    # but don't include too many emergency cases
    # try to deduct emergency value in the doctors database

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
