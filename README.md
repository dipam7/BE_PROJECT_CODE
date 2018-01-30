# Databases included

* ### generated_doctors_data.csv

  * d_id:        a unique id assigned to every doctor.

  * d_name:      doctor's name.

  * Speciality:  doctor's field of mastery.

  * Assigned_pc: MAC address of the PC assigned to the doctor.

  * Accesses:    The total number of previous accesses requested by the doctor.

  * Grants:      The total number of successful accesses by the doctor.
  

* ### generated_patient_data.csv (number of patients is a multiple of number of doctors)
 
  * p_id:         a unique id assigned to every patient.
 
  * Name:         patient's name
 
  * Gender:       patient's gender
  
  * Age:          patient's age
 
  * Email:        patient's email (name+age@gmail.com)

  * d_id:         id of the doctor assigned to the patient
  
  * d_name:       name of the doctor assigned to the patient

* ### generated_access_data.csv

  * p_id:               id of the patient whose data is being accessed
  
  * d_id:               id of the doctor accessing the data
  
  * location_of_access: pc used to access the data
  
  * time_of_access:     time at which data was accessed
  
  * data_requested:     kind of data requested (relevant, slightly-irrelevant, irrelevant)
  
  * emergency:          was the access made for an emergency case?
  
  * access_granted:     was access granted or denied?
  
  
* ### Histogram to show time distribution

  ![alt text](https://github.com/dipam7/BE_PROJECT_CODE/blob/master/time_histogram.jpg "Time distribution")
