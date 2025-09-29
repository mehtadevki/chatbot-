def clothing_store_chatbot():
    print("Welcome to Trendy Threads Clothing Store!")
    print("You can ask about our 'catalog', 'place order', 'order status', or type 'exit' to quit.")
   
    while True:
        user_input = input("You: ").lower()
       
        if user_input == "exit":
            print("Bot: Thanks for visiting Trendy Threads. Have a stylish day!")
            break
       
        elif "catalog" in user_input or "show" in user_input:
            print("Bot: Here's our latest catalog:")
            print("- T-Shirts\n- Jeans\n- Jackets\n- Dresses\n- Sneakers")
            print("Would you like to place an order? (yes/no)")
            response = input("You: ").lower()
            if response == "yes":
                print("Bot: Great! Please type the item you want to order.")
            else:
                print("Bot: No worries! Let me know if you need anything else.")
       
        elif "place order" in user_input or user_input in ["t-shirts", "t-shirt", "jeans", "jacket", "jackets", "dress", "dresses", "sneakers"]:
            if user_input in ["t-shirts", "t-shirt", "jeans", "jacket", "jackets", "dress", "dresses", "sneakers"]:
                # Normalize item names
                if "t-shirt" in user_input or "t-shirts" in user_input:
                    order_item = "T-Shirt"
                elif "jeans" in user_input:
                    order_item = "Jeans"
                elif "jacket" in user_input or "jackets" in user_input:
                    order_item = "Jacket"
                elif "dress" in user_input or "dresses" in user_input:
                    order_item = "Dress"
                elif "sneakers" in user_input:
                    order_item = "Sneakers"
                else:
                    order_item = user_input.title()
            else:
                print("Bot: Please type the item you want to order from the catalog.")
                order_item = input("You: ").lower().title()
           
            catalog = ["T-Shirt", "Jeans", "Jacket", "Dress", "Sneakers"]
            if order_item in catalog:
                print(f"Bot: Your order for {order_item} has been placed successfully!")
                print("Bot: Would you like to check your order status? (yes/no)")
                status = input("You: ").lower()
                if status == "yes":
                    print("Bot: Your order is being processed and will be shipped soon.")
                else:
                    print("Bot: Thank you for shopping with Trendy Threads!")
            else:
                print("Bot: Sorry, we don't have that item. Please choose from the catalog.")
       
        elif "order status" in user_input or "status" in user_input:
            print("Bot: Please enter your order number:")
            order_number = input("You: ")
            # Assume all order numbers are valid for simplicity
            print(f"Bot: Order #{order_number} is being packed and will be shipped shortly.")
       
        else:
            print("Bot: Sorry, I didn't get that. Please ask about 'catalog', 'place order', or 'order status'.")
           
# Run the chatbot
clothing_store_chatbot()
