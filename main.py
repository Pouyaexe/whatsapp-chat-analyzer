import glob
import re

# Get a list of all the text files in the 'chats' folder
file_pattern = "chats/*.txt"
filenames = glob.glob(file_pattern)

# Iterate through the list of text files
for filename in filenames:
    # Open the file and read its contents into a string
    with open(filename, "r") as f:
        contents = f.read()

    # Parse the string to extract the messages and sender's name
    messages = []
    for line in contents.split("\n"):
        match = re.search(r"(\d+/\d+/\d+), (\d+:\d+) - ([^:]+): (.*)", line)
        if match:
            date, time, sender, message = match.groups()
            messages.append((date, time, sender, message))

    # Create a set to store the unique names of the contacts
    contacts = set()
    # contacts.add(messages[0][2])  # Add the first sender's name to the set

    # Iterate through the messages and add the sender's name to the set
    for date, time, sender, message in messages:
        contacts.add(sender)

    # Initialize the dictionary with the names in the set as keys
    message_counts = {name: 0 for name in contacts}

    # Iterate through the messages and increment the message count for each sender
    for date, time, sender, message in messages:
        message_counts[sender] += 1

    # Print the results for each file
    print(f"Results for file conversation with between {', '.join(contacts)}")
    for name in message_counts:
        print(f"Number of messages sent by {name}: {message_counts[name]}")
