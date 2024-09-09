# Function to display chat history
def display_chat_history(st):
    for message in st.session_state['conversation']:
        if message['role'] == 'user':
            st.markdown(f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <span style="font-size: 20px; margin-right: 10px;">👤</span>
                    <div style="background-color: #f0f0f0; border-radius: 10px; padding: 10px;">
                        {message['content']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        elif message['role'] == 'assistant':
            st.markdown(f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <span style="font-size: 20px; margin-right: 10px;">🤖</span>
                    <div style="background-color: #e8f4f8; border-radius: 10px; padding: 10px;">
                        {message['content']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
