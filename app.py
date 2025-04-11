import streamlit as st
st.title("Tester votre categorie")


st.write('Bonjour')

age = st.number_input("Entrer votre age")


if st.button("Envoyer"):
    if age > 16:
        st.success("Majeur")
    else: 
        st.success("Vous etes mineur")
