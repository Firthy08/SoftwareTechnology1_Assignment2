# A simple list to store all appointments
appointments = []


def add_appointment(patient_name, practitioner_name, appointment_time):
    """Store a single appointment using basic Python data structures."""

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    return appointment


# Example usage
add_appointment("Alice Smith", "Dr Brown", "2026-10-03 10:30")
add_appointment("John Lee", "Dr Patel", "2026-10-03 11:00")

print(appointments)