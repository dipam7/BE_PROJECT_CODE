# Databases included

* ### generated_doctors_data.csv

  * d_id:        a unique id assigned to every doctor.

  * d_name:      doctor's name.

  * Speciality:  doctor's field of mastery.

  * Assigned_pc: MAC address of the PC assigned to the doctor.

  * Accesses:    The total number of previous accesses requested by the doctor.

  * Grants:      The total number of successful accesses by the doctor.
  
  * Emergency_accesses_left: Every doctor only gets a fixed number of emergency accesses

* ### generated_patient_data (number of patients is a multiple of number of doctors)
 
  * p_id:         a unique id assigned to every patient.
 
  * Name:         patient's name
 
  * Gender:       patient's gender
  
  * Age:          patient's age
 
  * Email:        patient's email (name+age@gmail.com)

  * d_id:         id of the doctor assigned to the patient
  
  * d_name:       name of the doctor assigned to the patient
