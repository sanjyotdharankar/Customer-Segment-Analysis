import streamlit as st
import requests

def main():
    st.title("Customer Segmentation Analysis")
    st.write("Welcome to the Model App!")

    # Streamlit form input fields
    recency = st.number_input("Recency")
    total_expenses = st.number_input("Total Expenses")
    income = st.number_input("Income")
    total_acc_cmp = st.number_input("Total Acc Cmp")
    total_purchases = st.number_input("Total Purchases")

    # Submit button
    if st.button("Submit"):
        # Make a POST request to the Django server
        url = "http://127.0.0.1:8000/upload/"  # Replace with your Django server URL
        data = {
            "recency": recency,
            "total_expenses": total_expenses,
            "income": income,
            "total_acc_cmp": total_acc_cmp,
            "total_purchases": total_purchases
        }
        response = requests.post(url, data=data)

        if response.status_code == 200:
            # Display the predictions returned from Django
            predictions = response.json().get("predictions")
            st.write("Predictions:", predictions)

if __name__ == "__main__":
    main()
