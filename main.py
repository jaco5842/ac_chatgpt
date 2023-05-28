import streamlit as st
from gpt_api import generate_email_recommendations

st.title("Create email using ChatGPT")

options = ["TM", "TMX", "MG", "NO"]
selected_option = st.selectbox("Mail type", options)
selected_date = st.date_input("Dato emailen skal afsendes")
email_name = st.text_input("Indtast email navn", placeholder="f.eks. TMX Castel del Lago 45")
email_content = st.text_area("Forklar hvad emailen handler om", placeholder="F.eks. Kun 48 timer kan du spare 50% på Castel del lago")
uploaded_file = st.file_uploader("Upload grafik")
button_clicked = st.button("Opret email forslag")

if button_clicked:
    # Remove the initial input fields
    st.empty()
    
    # Display the loading spinner
    with st.spinner("Generating recommendations..."):
        emne, preheader, tekst = generate_email_recommendations(email_name, email_content)
    
    # Display the recommendations
    st.success("Recommendations generated!")
    st.write("Emne:", emne)
    st.write("Preheader:", preheader)
    st.write("Tekst:", tekst)
