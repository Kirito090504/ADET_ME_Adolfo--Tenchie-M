from webexteamssdk import WebexTeamsAPI

#Question 1
# Initialize the Webex API
api = WebexTeamsAPI(access_token="YTlhZmVhNTItOTM4Ni00MGQ2LWEyNDYtMDU5MWFmMWNhZWVmZDYzNDgxZmQtN2Vm_P0A1_856a32b6-339b-4d3d-89fb-dabbd25aff7b")

# Get user input for room name and message
room_name = input("Enter the room name: ")
message = input("Enter the welcome message: ")

# Create a new room
room = api.rooms.create(title=room_name)

# Send a message to the room
api.messages.create(roomId=room.id, text=message)

print(f"Room '{room_name}' created and welcome message sent.")

# Question 2
# List of participant email addresses
participants = ["mattandrewinovero@baliuagu.edu.ph", "christopherandreitayao@baliuagu.edu.ph", "arabelaramos@baliuagu.edu.ph"]
# Add participants to the room
for participant in participants:
    api.memberships.create(roomId=room.id, personEmail=participant)

print("Participants added to the room.")

#Question 3
# List all messages in the room
messages = api.messages.list(roomId=room.id)
# Print messages with their IDs
for message in messages:
    print(f"Message ID: {message.id}, Text: {message.text}")

# Prompt user to input a message ID to delete
message_id = input("Enter the message ID to delete: ")

# Delete the selected message
api.messages.delete(message_id)

print("Message deleted.")
