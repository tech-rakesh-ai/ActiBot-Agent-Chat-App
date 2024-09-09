def display_sidebar(st):
    # Streamlit app
    st.sidebar.title("Liferay AI Chat Bot")

    st.sidebar.divider()

    st.sidebar.write("""
    This Liferay AI Chat Bot is an intelligent assistant powered by AI-LLM. 
    It can help you with various tasks related to Liferay in conversational way, such as creating websites 
    and providing information.
    """)

    st.sidebar.divider()
    st.sidebar.text('© 2024 Liferay AI Chat Bot.')
