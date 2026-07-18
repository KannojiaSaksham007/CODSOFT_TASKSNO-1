print("This is a basic rule based chat bot")
print("to eixt the chat bot type bye")
print("===============================")


while True:
    user=input("\nyou :").lower()

    if user=="hello" or user=="hi" or user=="namaste":
        print("Galvatron:Hello,i am Galvatron your virtual chatbot.how can i help you?")

    elif user=="how are you":
        print("Galvatron:everything is alright,what about you?")
    
    elif user=="i am fine too":
        print("Galvatron:thats great,what do u want to know?")

    elif user=="who created you":
        print("Galvatron:i am rule based chatbot created by predifned python rules")
        
    elif user=="what you can do":
        print("Galvatron:i can tell u date and time")
    
    elif user=="what is todays date and time":
        from datetime import datetime as dt
        today=dt.now().strftime("%d-%m-%y")
        time=dt.now().strftime("%H:%M:%S")
        print("Galvatron:todays date is ",today)
        print("Galvatron:the time now happens to be ",time)
    
    elif user=="bye":
        print("Galvatron:sure,have a nice day ahead!")
        break
    
    else:
        ("Galvatron:i can't understand what are you trying to say")