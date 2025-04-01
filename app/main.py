import streamlit as st

import streamlit as st

def main():
    st.title("Mad Libs Game")
    st.subheader("Fill in the blanks and create your own story!")

    noun = st.text_input("Enter a noun:")
    verb = st.text_input("Enter a verb:")
    adjective = st.text_input("Enter an adjective:")
    place = st.text_input("Enter a place:")
    
    if st.button("Generate Story"):
        if noun and verb and adjective and place:
            story = f"One day, a {adjective} {noun} decided to {verb} at {place}. It was an unforgettable experience!"
            st.success(story)
        else:
            st.warning("Please fill in all the blanks!")

if __name__ == "__main__":
    main()