# main_module.py
from dao.hospital_service_impl import HospitalServiceImpl
from entity.patient import Patient
from entity.doctor import Doctor
from entity.appointment import Appointment
from exception.custom_exceptions import PatientNumberNotFoundException


def main():
    service = HospitalServiceImpl()

    while True:
        print("\nHospital Management System")
        print("1. Get Appointment by ID")
        print("2. Get Appointments for Patient")
        print("3. Get Appointments for Doctor")
        print("4. Schedule Appointment")
        print("5. Update Appointment")
        print("6. Cancel Appointment")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            appointment_id = int(input("Enter Appointment ID: "))
            try:
                appointment = service.get_appointment_by_id(appointment_id)
                print(appointment)
            except Exception as e:
                print(f"Error: {e}")


        elif choice == '2':
            patient_id = input("Enter patient ID: ")
            try:
                appointments = service.get_appointments_for_patient(patient_id)
                if not appointments:
                    raise PatientNumberNotFoundException(patient_id)
                for appointment in appointments:
                    print(appointment)
            except Exception as e:
                print(e)


        elif choice == "3":
            doctor_id = int(input("Enter Doctor ID: "))
            appointments = service.get_appointments_for_doctor(doctor_id)
            for appointment in appointments:
                print(appointment)


        elif choice == "4":  # already there was appointment for 10 datas so here creating new schedule where the appointment id generated automatically after 10
            # Updated this section to no longer ask for the appointment ID
            patient_id = int(input("Enter Patient ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
            description = input("Enter Description: ")
            # Create an Appointment object without specifying appointment_id (it will be generated automatically)
            appointment = Appointment(None, patient_id, doctor_id, appointment_date, description)
            try:
                success = service.schedule_appointment(appointment)
                if success:
                    print("Appointment scheduled successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            appointment_id = int(input("Enter Appointment ID: "))
            patient_id = int(input("Enter Patient ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
            description = input("Enter Description: ")
            appointment = Appointment(appointment_id, patient_id, doctor_id, appointment_date, description)
            success = service.update_appointment(appointment) # it may be date/patient_id/description
            if success:
                print("Appointment updated successfully.")

        elif choice == "6":
            appointment_id = int(input("Enter Appointment ID: "))
            success = service.cancel_appointment(appointment_id)
            if success:
                print("Appointment cancelled successfully.")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
