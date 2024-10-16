class Patient:
    def __init__(self, patient_id, name, age, ailment):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.ailment = ailment

    def __repr__(self):
        return f"Patient({self.patient_id}, {self.name}, {self.age}, {self.ailment})"


class PatientManagementSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient_id, name, age, ailment):
        if patient_id in self.patients:
            print("Patient ID already exists.")
        else:
            self.patients[patient_id] = Patient(patient_id, name, age, ailment)
            print(f"Patient {name} added successfully.")

    def view_patients(self):
        if not self.patients:
            print("No patients in the system.")
            return
        for patient in self.patients.values():
            print(patient)

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            print(f"Patient ID {patient_id} deleted successfully.")
        else:
            print("Patient ID not found.")


if __name__ == "__main__":
    pms = PatientManagementSystem()
    
    while True:
        print("\n1. Add Patient")
        print("2. View Patients")
        print("3. Delete Patient")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            ailment = input("Enter Ailment: ")
            pms.add_patient(patient_id, name, age, ailment)

        elif choice == '2':
            pms.view_patients()

        elif choice == '3':
            patient_id = input("Enter Patient ID to delete: ")
            pms.delete_patient(patient_id)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")
