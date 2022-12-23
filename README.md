# whatsapp-chat-analyzer

# WhatsApp Chat Message Counter
This script calculates the number of messages sent by each contact in a WhatsApp chat export file.

**Requirements**
```python
Python 3.6 or higher

```Usage
Place the text files containing the WhatsApp chat exports in the chats folder.
Run the script:
Copy code
python message_counter.py
The script will scan the chats folder for text files and calculate the number of messages for each file separately. The results will be printed to the console.

**Example Output**
Copy code
Results for file chats/chat1.txt:
Number of messages sent by Emily: 4
Number of messages sent by Jake: 5

Results for file chats/chat2.txt:
Number of messages sent by James: 6
Number of messages sent by Jimmy: 3
Notes
The script expects the text files to be in the format exported by WhatsApp, with each message on a separate line and the sender's name followed by a colon and the message.
The script uses regular expressions to parse the text files and extract the messages and sender's name. It may not work correctly if the format of the text files is different from the expected format.