from tempelates import messages

import random

def select_channel(patient, message_type):
    if message_type == "wait_time_update" and patient["age_group"] in ["18-25", "25-40"]:
        return "WhatsApp"
    return "WhatsApp" if patient["response_rate"] < 0.6 else patient["channel"]

def generate_message(patient, message_type, **kwargs):
    return messages[message_type][patient["language"]].format(**kwargs)

def send_message(patient, message_type, **kwargs):
    channel = select_channel(patient, message_type)
    message = generate_message(patient, message_type, **kwargs)
    success = random.random() < 0.9
    print(f"\U0001F4E9 [{channel}] to {patient['name']} ({patient['language']}): {message}\n") if success else print(f"❌ Failed to send to {patient['name']} via {channel}\n")
    return success
