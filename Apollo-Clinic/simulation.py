from datetime import datetime, timedelta

import random

from data import patients
from data import appointment_types
from communication import send_message



def simulate_clinic_operations(days=7):
    results = []
    for day in range(days):
        current_date = datetime.now() + timedelta(days=day)
        random.shuffle(patients)
        for patient in patients[:int(len(patients) * 0.3)]:
            sent = send_message(patient, "appointment_confirmation",
                                appt_type=random.choice(appointment_types),
                                date=current_date.strftime('%d/%m/%Y'),
                                time=random.choice(["9:00 AM", "11:30 AM", "2:00 PM", "4:30 PM"]))
            responded = sent and (random.random() < patient["response_rate"])
            results.append({"patient": patient, "responded": responded})
    return results
