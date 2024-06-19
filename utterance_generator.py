import pandas as pd

# Data for training utterances
data = {
    "Intent": ["Greeting"] * 10 + ["Sign off"] * 10 + ["Empathy"] * 10 + ["Professionalism"] * 10,
    "Utterance": [
        "Welcome to Samsung Contact Center, how may I help you?", "Hello! How can I assist you today?",
        "Good day! What can I do for you?", "Hi there! How can I help you?",
        "Welcome! What service do you need?", "Greetings! How may I assist you?",
        "Hello! How can I support you today?", "Hi! What assistance do you require?",
        "Welcome to our service center, how can I be of service?", "Good to see you! How can I help?",
        "Thanks for contacting Samsung, have a great day!", "Thank you for reaching out. Goodbye!",
        "We appreciate your contact, farewell!", "Thanks and goodbye!",
        "Thank you, have a nice day!", "Thanks for your time, bye!",
        "Thank you for choosing Samsung. Bye!", "Goodbye, take care!",
        "Thanks for contacting us, see you!", "Thank you, goodbye!",
        "I'm sorry to hear that you're having trouble.", "I understand how frustrating that must be.",
        "I'm here to help you with this issue.", "I can see how that would be upsetting.",
        "I'm really sorry that this happened.", "I understand your concern.",
        "That sounds difficult, let me assist you.", "I empathize with your situation.",
        "I can understand why you're upset.", "I'm here to help you through this.",
        "Please provide me with the details of your issue.", "Could you please elaborate on the problem?",
        "I will ensure this is resolved promptly.", "Let me get the necessary information for you.",
        "I will handle your request with priority.", "Allow me to assist you with that.",
        "I will address your concern immediately.", "Could you please give me more information?",
        "I will make sure to follow up on this.", "Let's get this sorted out for you."
    ],
    "ID": [
        "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10",
        "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10",
        "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10",
        "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"
    ]
}

# Data for testing utterances
test_data = {
    "Intent": ["Greeting", "Sign off", "Empathy", "Professionalism", "Greeting", "Sign off", "Empathy", "Professionalism", "Greeting", "Sign off"],
    "Utterance": [
        "Hello, how can I assist you today?", "Thank you for contacting us, goodbye!",
        "I'm sorry for the inconvenience caused.", "Please describe your problem in detail.",
        "Welcome, how may I help you today?", "Thanks for reaching out, take care!",
        "I understand your frustration, let's resolve this.", "Could you please specify the issue?",
        "Hi, how can I help you today?", "Thanks for your call, goodbye!"
    ],
    "ID": ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10"]
}

# Create DataFrames
df_train = pd.DataFrame(data)
df_test = pd.DataFrame(test_data)

# Create a Pandas Excel writer using XlsxWriter as the engine.
with pd.ExcelWriter("/utterances.xlsx", engine="xlsxwriter") as writer:
    df_train.to_excel(writer, sheet_name="Training Utterances", index=False)
    df_test.to_excel(writer, sheet_name="Testing Utterances", index=False)
