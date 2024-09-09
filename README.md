# Groq-Powered Liferay Agent Chat App

This **Groq-Powered Liferay Agent Chat App** allows users to interact with an intelligent agent, leveraging Groq's large language model and custom tools to perform various tasks like creating websites, managing users, and retrieving user lists. This app is built using Streamlit, Langchain, and Groq's powerful AI infrastructure to handle user queries and execute predefined tool-based actions.

## Features

### 1. **Interactive Conversational Agent**
- The app allows users to have a conversation with an AI agent that can not only respond to text inputs but also execute specific tools, like:
  - **Creating Websites**
  - **Creating Users**
  - **Getting User Lists**

### 2. **Tool Integration**
- The agent has built-in tools powered by Langchain, which allow it to perform real-world tasks:
  - `CreateWebsiteTool`: Helps create websites using user-defined parameters.
  - `CreateUserTool`: Allows creating users based on a schema.
  - `GetUserListTool`: Retrieves a list of users from a predefined data source.
  
### 3. **Session-Based Chat History**
- The app maintains chat history using a unique session ID, allowing users to track their past conversations.
- Each session has its own chat message history, so users can resume conversations from where they left off.

### 4. **Customizable Prompts**
- The agent uses a prompt template (`ChatPromptTemplate`) to manage how it interacts with users and tools, ensuring consistency in the responses generated.

### 5. **Streamlit-Based UI**
- A clean, easy-to-use web interface built with Streamlit, allowing users to type in queries, receive responses, and visualize their interaction history.
- Sidebar includes additional functionality and app information.

### 6. **Dynamic Memory**
- The app uses memory management with the `RunnableWithMessageHistory` component from Langchain, enabling the agent to store and access chat history dynamically during conversations.

## Installation and Setup

Follow the steps below to install and run the **Groq-Powered Liferay Agent Chat App** on your local machine.

### Prerequisites
- Python 3.8 or higher
- [Groq API Key](https://groq.com/)

### Step 1: Clone the Repository

```bash
git clone https://github.com/tech-rakesh-ai/ConversationChatBot.git
cd ConversationChatBot
```

### Step 2: Create and Activate a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Make sure your `requirements.txt` includes the following:

```text
streamlit
langchain
langchain_groq
langchain_openai
python-dotenv
```

### Step 4: Configure API Keys

Create a `.env` file in the root directory and add your Groq API key:

```bash
GROQ_API_KEY=your-groq-api-key
```

Replace `your-groq-api-key` with the actual API key.

### Step 5: Run the Application

To run the Streamlit app, use the following command:

```bash
streamlit run app.py
```

The app will open in your default web browser, and you can begin interacting with the agent.

## How to Use

1. **Start a Conversation**: Use the text input box at the bottom of the page to type in a query or request.
2. **Tool Execution**: Ask the agent to perform tasks like creating a website, managing users, or retrieving a user list.
3. **View Responses**: The agent will respond with appropriate answers or actions, depending on the task.
4. **Session Management**: The chat history is preserved across your session. You can review past interactions or continue the conversation seamlessly.

### Example Queries:
- **Creating a website**: "Can you create a website for my business?"
- **Creating a user**: "Create a new user with the name John Doe."
- **Fetching user list**: "Get me the list of users."

## Application Structure

```bash
groq-agent-chat-app/
│
├── app.py                      # Main Streamlit app code
├── requirements.txt             # Python dependencies
├── tools_prompts.py             # Prompts for tools
├── tools_functions.py           # Tool functions implementations
├── tools_schemas.py             # Schemas for tool inputs
├── display_sidebar.py           # Sidebar layout functions
├── display_conversation.py      # Functions to display chat history
└── .env                         # Environment variables (not included in repo)
```

### Key Components

- **ChatGroq & Langchain**: Uses `ChatGroq` as the main LLM for generating text and handling queries. Langchain is used to integrate tools that allow the agent to perform tasks.
- **Tool Calling Agent**: The agent can call tools like `CreateWebsiteTool`, `CreateUserTool`, and `GetUserListTool` based on user requests.
- **Chat History**: Tracks the conversation history in each session using `ChatMessageHistory`.

## Future Enhancements

- Integration with more complex tools for automating additional workflows.
- Add multi-turn conversation handling where the agent remembers past interactions in detail.
- Enhance UI with more customizable features like theming and additional interaction widgets.

## Developer

Developed by **Rakesh Kumar**.  
Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/tech-rakesh-ai/) to provide feedback or discuss improvements.

## License

MIT License © 2024 Groq-Powered Liferay Agent Chat App.
