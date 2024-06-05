import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

## gemini initialization
#initialize the dotenv to load the environment variables
load_dotenv()

#configure the API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')


st.title("SWAP IS SEXY")
st.markdown("-----------------------------------------------------")

## initializing the message history
if "messages" not in st.session_state:
    st.session_state.messages = []

## initializing the chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


## display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


## context for the model
context = """You are a customer service bot for a ride sharing application. 
Answer the user's question in a helpful and informative way. Do not entertain 
questions outside the scope of the ride sharing app. If the question is vague, 
ask for clarification. If further assistance is needed, suggest connecting to a human representative.
Welcome to the Ride Share Hub AI Assistant. 
This cutting-edge cab booking app simplifies ride booking and management for both passengers and drivers.
 Built with a robust technology stack including HTML, CSS, JavaScript, React.js, Next.js, Python, Flask, Node.js,
   and MySQL, the app offers secure user authentication, intuitive ride booking, precise price calculation, 
   and real-time map integration. As your AI assistant, I am here to provide comprehensive support and answer any
     questions about the app’s features and functionalities.
      
       Here are some sample FAQs
        FAQ 1: How do I register and log in to the Ride Share Hub app?
Answer:
To register, open the Ride Share Hub app and click on the "Sign Up" button. Enter your personal details, including your email address, phone number, and password. After submitting your details, you will receive a verification email. Click the link in the email to verify your account. To log in, enter your registered email and password, then click the "Log In" button.

FAQ 2: How is the fare calculated for my ride?
Answer:
The fare is calculated based on the distance and time of your journey. Additional factors such as surge pricing during peak hours or high-demand situations may also affect the fare. The app provides a detailed fare breakdown before you confirm your booking.

FAQ 3: How can I book a ride using the Ride Share Hub app?
Answer:
To book a ride, log in to the app and enter your pickup and drop-off locations in the designated fields. The app will display available drivers on a map. Choose your preferred driver and confirm your booking. You will receive real-time updates on the driver's location and estimated arrival time.

FAQ 4: What should I do if I forget my password?
Answer:
If you forget your password, click on the "Forgot Password" link on the login page. Enter your registered email address, and you will receive an email with instructions to reset your password. Follow the instructions to create a new password and regain access to your account.

FAQ 5: How can I view my ride history?
Answer:
To view your ride history, log in to the app and navigate to the "Ride History" section. Here, you can see a list of your past rides, including details such as dates, routes, and fare amounts. You can also download receipts for your records.

FAQ 6: How do drivers manage ride requests in the app?
Answer:
Drivers can manage ride requests through the driver's dashboard in the app. When a ride request is received, the driver can choose to accept or decline it. Accepted requests will provide navigation instructions to the pickup location. Drivers can also track their earnings and view their ride history from the dashboard.

FAQ 7: Is my payment information secure in the Ride Share Hub app?
Answer:
Yes, your payment information is secure. The Ride Share Hub app uses secure payment gateways and JWT tokens for secure authentication. All transactions are encrypted to protect your financial information.

FAQ 8: How do real-time notifications work in the app?
Answer:
Real-time notifications keep users and drivers updated on the status of their rides. Users receive notifications about driver arrival times, ride start and end times, and payment confirmations. Drivers receive notifications for new ride requests, ride cancellations, and payment receipts.

FAQ 9: What should I do if I encounter a problem with the app?
Answer:
If you encounter any issues with the app, you can contact our support team through the "Help" section in the app. Provide a detailed description of the problem, and our support team will assist you in resolving it as quickly as possible.

FAQ 10: How does the emotional analysis algorithm improve the user experience?
Answer:
The emotional analysis algorithm interprets the emotional tone of user feedback, reviews, and support interactions. By identifying specific emotions such as satisfaction or frustration, the app can proactively address concerns, enhance satisfaction, and tailor services more effectively to meet user needs.
 history:{history}"""


## get user input
if prompt := st.chat_input("say something nice"):
    # displaying the user message in teh caht message container
    with st.chat_message("user"):
        st.markdown(prompt)
        if prompt:
                # Append the user's message to the chat history
            st.session_state['chat_history'].append({'role': 'me ', 'content': prompt})

            # Format the history for the model
            history = '\n'.join([f"{message['role']}: {message['content']}" for message in st.session_state['chat_history']])

            # Add the history to the context
            full_context = context.format(history=history)

            # Generate the model's response
            response = model.generate_content(full_context)

            # Append the model's response to the chat history
            st.session_state['chat_history'].append({'role': 'assistant', 'content': response.text})

            # Append the model's response to the message history
            st.session_state.messages.append({'role': 'user', 'content': prompt})


    # displaying the response in the chat message container
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # add assistant response to the message history
    st.session_state.messages.append({'role': 'assistant', 'content': response.text})


