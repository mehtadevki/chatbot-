import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
  try:
        user_msg = request.get_json().get("message", "").lower()
  except:
        return jsonify({"message": "Error: could not read message."})
 

    # Python chatbot logic
    if "hello" in user_msg or "hi" in user_msg:
        bot_msg = "Hello! Welcome to the Airplane Travel Helpdesk. How can I assist you today?"
    elif "ticket" in user_msg or "book" in user_msg:
        bot_msg = "You can book flight tickets online, through airline apps, or at the airport counter."
    elif "price" in user_msg or "cost" in user_msg or "fare" in user_msg:
        bot_msg = "Ticket prices depend on destination, class, and booking time. Booking early usually gives cheaper rates."
    elif "luggage" in user_msg or "baggage" in user_msg:
        bot_msg = "Most airlines allow 15-20kg check-in luggage and 7kg cabin luggage. Extra baggage may cost more."
    elif "check in" in user_msg:
        bot_msg = "Online check-in usually opens 24 hours before departure. Airport check-in closes 45 minutes before domestic flights."
    elif "passport" in user_msg or "visa" in user_msg:
        bot_msg = "For international travel, you need a valid passport and sometimes a visa, depending on your destination country."
    elif "id" in user_msg:
        bot_msg = "For domestic flights in India, you can carry Aadhaar card, Voter ID, Driving License, or Passport as valid ID proof."
    elif "boarding pass" in user_msg:
        bot_msg = "You can download the boarding pass after check-in or collect it from the airline counter at the airport."
    elif "food" in user_msg or "meal" in user_msg:
        bot_msg = "Some airlines provide complimentary meals, while budget airlines may charge extra for food."
    elif "wifi" in user_msg or "internet" in user_msg:
        bot_msg = "Few airlines provide in-flight WiFi, but it may be paid and speed can be limited."
    elif "delay" in user_msg or "cancel" in user_msg:
        bot_msg = "If your flight is delayed or cancelled, airlines usually offer refunds or rescheduling options."
    elif "time" in user_msg or "schedule" in user_msg:
        bot_msg = "You can check real-time flight status on the airline website or mobile apps."
    elif "safety" in user_msg:
        bot_msg = "Air travel is one of the safest modes of transport. Always follow crew instructions for safety."
    elif "bye" in user_msg or "exit" in user_msg:
        bot_msg = "Goodbye! Have a pleasant and safe journey! ✈️"
    else:
        bot_msg = "Sorry, I didn't understand that. Can you ask something related to flights?"

    return jsonify({"message": bot_msg})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



