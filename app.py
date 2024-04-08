import streamlit as st
from factorial import fact


def main():
    st.title("Factorial Calculator")
    number = st.number_input("Enter a number", min_value=0, max_value=9000)
    result = None
    if st.button("Calculate"):
        result = fact(number)
        st.write(f"Key đây: {number}!={result}")
        st.balloons()

if __name__ == "__main__":
    main()
