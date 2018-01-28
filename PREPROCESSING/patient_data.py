import csv
import uuid
import mac_test
# we can also use
# from mac_test import *
# this imports all the objects and methods from mac_test
# and they can be used directly instead of the dot notation
# but this also wastes a lot of space since we don't need everything

patient_names = []
patient_genders = []
patient_ages = []
patient_emails = []
d_ids = []

with open('patient_data.csv', 'r', encoding="utf8") as csv_read_file:

    # reader object
    csv_reader = csv.DictReader(csv_read_file)

    for line in csv_reader:
        # ignore everything after space
        name, sep, tail = line['name'].partition(' ')
        patient_names.append(name)

        patient_genders.append(line['gender'])

        patient_ages.append(line['Age'])

        email = name + line['Age'] + "@gmail.com"
        patient_emails.append(email)

    with open('generated_doctors_data.csv', 'r', encoding="utf8") as csv_r_file:

        # reader object
        csv_r = csv.DictReader(csv_r_file)

        for line in csv_r:
            d_ids.append(line['d_id'])

        with open('generated_patient_data.csv', 'w', encoding="utf8") as csv_write_file:

            fieldnames = ['p_id', 'Name', 'Gender', 'Age', 'Email', 'd_id', 'd_name']
            csv_writer = csv.DictWriter(csv_write_file, fieldnames=fieldnames)

            csv_writer.writeheader()

            # subtracted 627 to get number of entries in patient data
            # as a multiple of number of entries in doctor data
            number_of_patients = len(patient_names) - 627
            # print(number_of_patients)

            # subtracted one because the first value is not a real value
            number_of_doctors = len(mac_test.doctors) - 1

            patients_per_doctor = int(number_of_patients / number_of_doctors)

            print(patients_per_doctor)

            start = 0
            stop = start + patients_per_doctor

            for j in range(number_of_doctors + 1):

                for i in range(start, stop):
                    csv_writer.writerow({'p_id': uuid.uuid4(), 'Name': patient_names[i], 'Gender': patient_genders[i], 'Age': patient_ages[i], 'Email': patient_emails[i], 'd_id': d_ids[j], 'd_name': mac_test.doctors[j]})

                start = start + patients_per_doctor
                stop = start + patients_per_doctor
