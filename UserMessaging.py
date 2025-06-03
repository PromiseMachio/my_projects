class user:
    def __init__(self,name):
        self.name = name#This defines the name of the user.
        self.inbox = []# A list to store incoming messages.
    #Sending messages def function.
    def send_message(self, recipient,message): #Allows user1(self) to send a message to user2(recipient)
        print(f"{self.name} to {recipient.name}:{message}")# This is a print out message log like Mr Machio({self.name}) to Florence({recipient.name}):"Hey Florence it has been a while dear how have you bee?")({message}).
        recipient.inbox.append((self.name,message)) # Adds a message to recipient's inbox as a tuple(sender name, message)

        
    #Reading messages 
    def read_message(self):
        print(f"\n{self.name}'s Inbox:")# Print all the messages in the user's inbox
        if not self.inbox:
            print("No message.") # If the inbox is empty or no message has been inputed the if control flow.
        else:
            for sender.msg in self.inbox:
                print("From {sender}: {msg}")
                self.inbox.clear()# After reading it clears the inbox to simulate that messages have beed read.

#Create two users
user1 = user("Machio")
user2 = user("Florence")

#Sample conversation of the two
user1.send_message(user2, "Hello Mr Machio!")
user2.send_message(user1, "Hey Florence it has been a while dear how have you been?")
user1.send_message(user2, "I'm doing great Mr Machio just missed you and thought maybe I could say HI!")
user1.send_message(user1, "Ohh! Ohh! Ohh! This is sweet of you what do you say we go out on weekend maybe we have a chat?")
user2.send_message(user2, "Okay then Mr Machio am really looking forward for that?")
user1.send_message(user1, "Why don't you pick your favorite spot then we schedule a date.")
user2.send_message(user2, "Hmmm am blushing already! Okay let's go to Murigithi memorial gardens I find the place so serene and peaceful maybe we could have a lovely time there.")
user1.send_message(user2, "Murigithi memorial gardens really dear? Anyways it is what it is. See you then, we will talk later bye!")
user2.send_message(user2, "Ha! Ha! Ha! okay Mr Machia you have a great rest of the day, bye!")

#Reading message
user1.read_message()
user2.read_message()
