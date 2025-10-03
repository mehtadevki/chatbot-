print("===================================")
print("     ✈️ AIRPLANE TRAVEL CHATBOT ✈️   ")
print("===================================")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("🤖 Chatbot: Hello! Welcome to the Airplane Travel Helpdesk. How can I assist you today?")
    elif "ticket" in user or "book" in user:
        print("🤖 Chatbot: You can book flight tickets online, through airline apps, or at the airport counter.")
    elif "price" in user or "cost" in user or "fare" in user:
        print("🤖 Chatbot: Ticket prices depend on destination, class, and booking time. Booking early usually gives cheaper rates.")
    elif "luggage" in user or "baggage" in user:
        print("🤖 Chatbot: Most airlines allow 15-20kg check-in luggage and 7kg cabin luggage. Extra baggage may cost more.")
    elif "check in" in user:
        print("🤖 Chatbot: Online check-in usually opens 24 hours before departure. Airport check-in closes 45 minutes before domestic flights.")
    elif "passport" in user or "visa" in user:
        print("🤖 Chatbot: For international travel, you need a valid passport and sometimes a visa, depending on your destination country.")
    elif "id" in user:
        print("🤖 Chatbot: For domestic flights in India, you can carry Aadhaar card, Voter ID, Driving License, or Passport as valid ID proof.")
    elif "boarding pass" in user:
        print("🤖 Chatbot: You can download the boarding pass after check-in or collect it from the airline counter at the airport.")
    elif "food" in user or "meal" in user:
        print("🤖 Chatbot: Some airlines provide complimentary meals, while budget airlines may charge extra for food.")
    elif "wifi" in user or "internet" in user:
        print("🤖 Chatbot: Few airlines provide in-flight WiFi, but it may be paid and speed can be limited.")
    elif "delay" in user or "cancel" in user:
        print("🤖 Chatbot: If your flight is delayed or cancelled, airlines usually offer refunds or rescheduling options.")
    elif "time" in user or "schedule" in user:
        print("🤖 Chatbot: You can check real-time flight status on the airline website or mobile apps.")
    elif "safety" in user:
        print("🤖 Chatbot: Air travel is one of the safest modes of transport. Always follow crew instructions for safety.")
    elif "bye" in user or "exit" in user:
        print("🤖 Chatbot: Goodbye! Have a pleasant and safe journey! ✈️")
        break
    else:
        print("🤖 Chatbot: Sorry, I didn't understand that. Can you ask something related to flights?")
