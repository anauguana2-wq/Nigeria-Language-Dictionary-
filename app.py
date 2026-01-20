import streamlit as st

# 1. Dictionary with 5 Nigerian languages and expanded vocabulary
nigerian_languages = {
    "Hausa": {
        "Hello": "Sannu",
        "Thank You": "Na gode",
        "Welcome": "Barka da zuwa",
        "Good Morning": "Ina kwana",
        "Goodbye": "Sai an jima"
    },
    "Yoruba": {
        "Hello": "Pẹlẹ o",
        "Thank You": "E ṣe",
        "Welcome": "E ku abo",
        "Good Morning": "E kaaro",
        "Goodbye": "O dabọ"
    },
    "Igbo": {
        "Hello": "Ndewo",
        "Thank You": "Imela",
        "Welcome": "Nnoo",
        "Good Morning": "Ututu oma",
        "Goodbye": "Ka omesia"
    },
    "Fulfulde": {
        "Hello": "Jam waali",
        "Thank You": "A balti",
        "Welcome": "Bismilla",
        "Good Morning": "Jam weeti",
        "Goodbye": "Sihir am"
    },
    "Kanuri": {
        "Hello": "Lale",
        "Thank You": "Wushir",
        "Welcome": "Lale kowo",
        "Good Morning": "Wandé njiaro",
        "Goodbye": "Sabuwa dâwa"
    }
}

# 2. Streamlit UI
st.set_page_config(page_title="Nigerian Dictionary", page_icon="🇳🇬")

st.title("🇳🇬 Nigerian Multi-Language Dictionary")

# 3. Selection Dropdown
selection = st.selectbox("Select a Language:", list(nigerian_languages.keys()))

# 4. Display words using a simple loop (No Pandas)
st.subheader(f"Vocabulary: {selection}")
lang_data = nigerian_languages[selection]

for label, word in lang_data.items():
    st.write(f"**{label}:** {word}")

st.divider()

# 5. Full Overview using st.data_editor (Native Streamlit, No Pandas)
st.subheader("All Languages Overview")
st.data_editor(nigerian_languages, use_container_width=True)


