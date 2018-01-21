import random
import csv
import uuid


RANGE_OF_ACCESSES = 50000

doctors = []
specialities = ['Gynec', 'Dentist', 'Pediatrician', 'Neuro', 'Cardio']


def randomMAC():
    return [0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)]


def MACprettyprint(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))


# The file was saved from libre office as csv and wasn't opening normally
# so the encoding had to be mentioned
with open('doctors_data.csv', 'r', encoding="utf8") as csv_read_file:

    # using DictReader instead of the normal reader because
    # in normal reader we have to always access the first row
    # i.e the row of column names along with any other row to identify what the
    # values are
    # in DictReader the values are saved in the form of a dictionary
    # i.e key value pairs hence it makes it more intuitive and easy to use

    # reader object
    csv_reader = csv.DictReader(csv_read_file)

    for line in csv_reader:

        doctors.append(line['Doctor Name'])
        # speciality will be edited later to suport only 4 or 5 specialities
        # speciality.append(line['Speciality'])

    with open('generated_doctors_data.csv', 'w') as csv_write_file:

        # specify field names
        fieldnames = ['d_id', 'd_name', 'Speciality', 'Assigned_PC', 'Accesses', 'Grants']

        # writer object
        csv_writer = csv.DictWriter(csv_write_file, fieldnames=fieldnames)

        # write column names at the top of the file
        csv_writer.writeheader()

        number_of_doctors = len(doctors)

        # for 70% of the doctors
        # total grants will be greater than 80% of total accesses
        # for the rest of the doctors it'll be less
        first_half = int(number_of_doctors * 0.7)

        for i in range(first_half):

            # total number of accesses from a predefined range
            total_accesses = random.randrange(RANGE_OF_ACCESSES)

            # total number of grants should be random
            # but in the range of 80-100%
            total_grants = random.randrange(int(total_accesses * 0.8), total_accesses)

            csv_writer.writerow({'d_id': uuid.uuid4(), 'd_name': doctors[i], 'Speciality': random.choice(specialities), 'Assigned_PC': MACprettyprint(randomMAC()), 'Accesses': total_accesses, 'Grants': total_grants})

        for i in range(first_half, number_of_doctors):

            # total number of accesses from a predefined range
            total_accesses = random.randrange(RANGE_OF_ACCESSES)

            # total number of grants should be random
            # but less than 80%
            total_grants = random.randrange(int(total_accesses * 0.8))

            csv_writer.writerow({'d_id': uuid.uuid4(), 'd_name': doctors[i], 'Speciality': random.choice(specialities), 'Assigned_PC': MACprettyprint(randomMAC()), 'Accesses': total_accesses, 'Grants': total_grants})
