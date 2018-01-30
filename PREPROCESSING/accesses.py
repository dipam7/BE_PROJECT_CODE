import random
from test_for_uniqueness import *

emergency = ''

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
        time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[doctor], 'time_of_access': time, 'data_requested': 'relevant', 'emergency': 'no', 'access_granted': 'yes'})

    # average case 1:
    # doctors will not access data from their own pc but
    # everything else will be proper
    # the first 70% doctors will get access because they have
    # a good previous history record
    # in the other 30% doctors, the doctors with large differences
    # in previous history will not get access
    # and the doctors with small difference will randomly get access or no
    # result is initially set to yes for the doctors with good prev history
    result = 'yes'
    emergency = 'no'
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # 9 am to 9 pm
        hours = random.randint(9, 21)
        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)

        accesses = int(doctors_grants[doctor][0])
        grants = int(doctors_grants[doctor][1])
        # print(accesses)
        # print(grants)

        # if the grants are less than 75% then choose on random whether to
        # give access or no
        if grants < int(0.75 * accesses):
            result = random.choice(['yes', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        # but if the grants are less than 30% of accesses
        # give less accesses
        if grants < int(0.3 * accesses):
            # probability of no is greater
            result = random.choice(['yes', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        random_pc = random.choice(list(doctors_pc.keys()))

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[random_pc], 'time_of_access': time, 'data_requested': 'relevant', 'emergency': emergency, 'access_granted': result})

    # average case 2:
    # same as average case 1 but instead of wrong computer
    # doctors will access data at the wrong time
    # result is initially set to yes for the doctors with good prev history
    result = 'yes'
    emergency = 'no'
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # before hospital hours
        hours_before = random.randint(0, 8)

        # after hostpial hours
        hours_after = random.randint(22, 23)

        available_hours = [hours_before, hours_after]

        hours = random.choice(available_hours)

        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)

        accesses = int(doctors_grants[doctor][0])
        grants = int(doctors_grants[doctor][1])
        # print(accesses)
        # print(grants)

        # if the grants are less than 75% then choose on random whether to
        # give access or no
        if grants < int(0.75 * accesses):
            result = random.choice(['yes', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        # but if the grants are less than 30% of accesses
        # give less accesses
        if grants < int(0.3 * accesses):
            # probability of no is greater
            result = random.choice(['yes', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[doctor], 'time_of_access': time, 'data_requested': 'relevant', 'emergency': emergency, 'access_granted': result})

    # average case 3:
    # doctors will access data from wrong pc at the wrong time
    # think about how to give accesses
    # include emergency in some cases and then
    # try to deduct the emergency value in the doctors database
    # result is initially set to yes for the doctors with good prev history
    result = 'yes'
    emergency = 'no'
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # before hospital hours
        hours_before = random.randint(0, 8)

        # after hostpial hours
        hours_after = random.randint(22, 23)

        available_hours = [hours_before, hours_after]

        hours = random.choice(available_hours)

        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)

        accesses = int(doctors_grants[doctor][0])
        grants = int(doctors_grants[doctor][1])
        # print(accesses)
        # print(grants)

        # if the grants are less than 80% then choose on random whether to
        # give access or no
        if grants < int(0.8 * accesses):
            result = random.choice(['yes', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        # but if the grants are less than 40% of accesses
        # never give access
        if grants < int(0.4 * accesses):
            # probability of no is greater
            result = random.choice(['yes', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        random_pc = random.choice(list(doctors_pc.keys()))

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[random_pc], 'time_of_access': time, 'data_requested': 'relevant', 'emergency': emergency, 'access_granted': result})

    # average case 4:
    # doctor will access from his own pc
    # during hospital hours
    # but slightly irrelevant data
    # past history > 90% give access
    # 90 - 50% based on emergency
    result = 'yes'
    emergency = 'no'
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # 9 am to 9 pm
        hours = random.randint(9, 21)
        # random minutes
        minutes = random.randint(0, 59)

        accesses = int(doctors_grants[doctor][0])
        grants = int(doctors_grants[doctor][1])
        # print(accesses)
        # print(grants)

        # if the grants are less than 90% then choose on random whether to
        # give access or no
        if grants < int(0.9 * accesses):
            result = random.choice(['yes', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        # but if the grants are less than 30% of accesses
        # give less number of accesses
        if grants < int(0.3 * accesses):
            # probability of no is greater
            result = random.choice(['yes', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[doctor], 'time_of_access': time, 'data_requested': 'slightly-irrelevant', 'emergency': emergency, 'access_granted': result})

    # average case 5:
    # doctors will access data from the wrong pc
    # during hospital hours
    # data will be slightly irrelevant
    # be strict in this case when giving access
    result = 'yes'
    emergency = 'no'
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # 9 am to 9 pm
        hours = random.randint(9, 21)
        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)

        accesses = int(doctors_grants[doctor][0])
        grants = int(doctors_grants[doctor][1])
        # print(accesses)
        # print(grants)

        # if the grants are less than 95% then choose on random whether to
        # give access or no
        if grants < int(0.95 * accesses):
            result = random.choice(['yes', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        # but if the grants are less than 40% of accesses
        # never give access
        if grants < int(0.4 * accesses):
            # probability of no is greater
            result = random.choice(['yes', 'no', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        random_pc = random.choice(list(doctors_pc.keys()))

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[random_pc], 'time_of_access': time, 'data_requested': 'slightly-irrelevant', 'emergency': emergency, 'access_granted': result})

    # average case 6:
    # same as average case 4 only instead of wrong pc
    # the doctor will access data at the wrong time
    result = 'yes'
    emergency = 'no'
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # before hospital hours
        hours_before = random.randint(0, 8)

        # after hostpial hours
        hours_after = random.randint(22, 23)

        available_hours = [hours_before, hours_after]

        hours = random.choice(available_hours)

        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)

        accesses = int(doctors_grants[doctor][0])
        grants = int(doctors_grants[doctor][1])
        # print(accesses)
        # print(grants)

        # if the grants are less than 95% then choose on random whether to
        # give access or no
        if grants < int(0.95 * accesses):
            result = random.choice(['yes', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        # but if the grants are less than 40% of accesses
        # never give access
        if grants < int(0.4 * accesses):
            # probability of no is greater
            result = random.choice(['yes', 'no', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[doctor], 'time_of_access': time, 'data_requested': 'slightly-irrelevant', 'emergency': emergency, 'access_granted': result})

    # average case 7:
    # own pc
    # during hospital hours
    # but data is highly irrelevant
    # prev history greater than 90% get 50-50 choice
    # 90 - 50 have greater chance of no
    # less than 50 no access
    result = 'yes'
    emergency = 'no'
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # 9 am to 9 pm
        hours = random.randint(9, 21)
        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)

        accesses = int(doctors_grants[doctor][0])
        grants = int(doctors_grants[doctor][1])
        # print(accesses)
        # print(grants)

        # if the grants are less than 95% then choose on random whether to
        # give access or no
        if grants < int(0.95 * accesses):
            result = random.choice(['yes', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        # but if the grants are less than 30% of accesses
        # never give access
        if grants < int(0.4 * accesses):
            # probability of no is greater
            result = random.choice(['yes', 'no', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[doctor], 'time_of_access': time, 'data_requested': 'irrelevant', 'emergency': emergency, 'access_granted': result})

    # average case 8:
    # wrong pc and highly irrelevant data
    # only great prev history and emergency get access
    result = 'yes'
    emergency = 'no'
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # 9 am to 9 pm
        hours = random.randint(9, 21)
        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)

        accesses = int(doctors_grants[doctor][0])
        grants = int(doctors_grants[doctor][1])
        # print(accesses)
        # print(grants)

        # if the grants are less than 75% then choose on random whether to
        # give access or no
        if grants < int(0.95 * accesses):
            result = random.choice(['yes', 'no', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        # but if the grants are less than 30% of accesses
        # never give access
        if grants < int(0.3 * accesses):
            # probability of no is greater
            result = random.choice(['yes', 'no', 'no', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        random_pc = random.choice(list(doctors_pc.keys()))

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[random_pc], 'time_of_access': time, 'data_requested': 'irrelevant', 'emergency': emergency, 'access_granted': result})

    # average case 9:
    # wrong time and highly irrelevant data
    # only great prev history and emergency get access
    result = 'yes'
    emergency = 'no'
    for key in patients_doctor:

        doctor = patients_doctor[key]

        # before hospital hours
        hours_before = random.randint(0, 8)

        # after hostpial hours
        hours_after = random.randint(22, 23)

        available_hours = [hours_before, hours_after]

        hours = random.choice(available_hours)

        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)

        accesses = int(doctors_grants[doctor][0])
        grants = int(doctors_grants[doctor][1])
        # print(accesses)
        # print(grants)

        # if the grants are less than 75% then choose on random whether to
        # give access or no
        if grants < int(0.95 * accesses):
            result = random.choice(['yes', 'no', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        # but if the grants are less than 30% of accesses
        # never give access
        if grants < int(0.3 * accesses):
            # probability of no is greater
            result = random.choice(['yes', 'no', 'no', 'no', 'no'])
            if result == 'yes':
                emergency = 'yes'
            else:
                emergency = 'no'

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[doctor], 'time_of_access': time, 'data_requested': 'irrelevant', 'emergency': emergency, 'access_granted': result})

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
        hours_after = random.randint(22, 23)

        available_hours = [hours_before, hours_after]

        hours = random.choice(available_hours)

        # random minutes
        minutes = random.randint(0, 59)

        # zfill is used because if minutes is in single digits
        # a zero must be appended before it
        time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)

        random_pc = random.choice(list(doctors_pc.keys()))

        csv_writer.writerow({'p_id': key, 'd_id': doctor, 'location_of_access': doctors_pc[random_pc], 'time_of_access': time, 'data_requested': 'irrelevant', 'emergency': 'no', 'access_granted': 'no'})
