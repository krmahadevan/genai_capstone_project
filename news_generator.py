import streamlit as st

from personas import Editor, Reporter, Reviewer


def news_room(news_topic: str, in_temperature: float) -> None:
    if 'persona' not in st.session_state:
        st.session_state.persona = {
            'reporter': Reporter(temperature=in_temperature),
            'editor': Editor(temperature=0.5),
            'reviewer': Reviewer(temperature=0.5)
        }

    st.info(f"Topic: {news_topic}, Temperature: {in_temperature}", icon="ℹ️")

    draft = st.session_state.persona['reporter'].call_llm(news_topic)
    if draft:
        edited = st.session_state.persona['editor'].call_llm(draft)
        if edited:
            reviewed = st.session_state.persona['reviewer'].call_llm(edited)
            with st.container():
                st.title("Draft")
                st.write(draft)
            with st.container():
                st.title("After Editing")
                st.write(edited)
            with st.container():
                st.title("After Review")
                st.write(reviewed)


st.title("News-Room: where all _Fake News_ stays Fake")
with st.form("news_form"):
    input_topic = st.text_input("What topic would you like the news to be related to: ")
    input_temperature = st.select_slider("How hilarious would you like it to be",
                                         ["realistic", "somewhat-hilarious", "extremely-hilarious"]
                                         )
    match input_temperature:
        case "realistic":
            temperature = 0.25
        case "extremely-hilarious":
            temperature = 0.75
        case _:
            temperature = 0.5

    submitted = st.form_submit_button("Submit")
    if input_topic:
        if submitted:
            news_room(input_topic, temperature)
