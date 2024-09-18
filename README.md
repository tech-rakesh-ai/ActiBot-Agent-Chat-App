# ActiBot-Powered Liferay Agent Chat App

This **ActiBot-Powered Liferay Agent Chat App** enables users to interact with an intelligent agent to perform various tasks like creating websites, managing users, and retrieving user lists. The app leverages a large language model and custom tools to handle user queries and execute predefined tool-based actions seamlessly across multiple platforms via API integration.

## Features

### 1. **Interactive Conversational Agent**
- ActiBot allows users to interact conversationally and perform real-world tasks such as:
  - **Creating Websites**
  - **Creating Users**
  - **Fetching User Lists**

### 2. **Tool Integration**
- ActiBot integrates with powerful tools through Langchain to perform specific tasks:
  - `CreateWebsiteTool`: Assists in creating websites using user-defined parameters.
  - `CreateUserTool`: Creates users based on provided schemas.
  - `GetUserListTool`: Retrieves user lists from predefined data sources.

### 3. **Session-Based Chat History**
- Every conversation is tied to a unique session ID, which preserves the chat history. This enables users to resume conversations from where they left off in previous sessions.

### 4. **Customizable Prompts**
- The agent's interactions are managed by a flexible prompt template (`ChatPromptTemplate`), ensuring consistency and adaptability in responses and tool usage.

### 5. **Streamlit-Based UI**
- A clean and user-friendly web interface built with Streamlit, allowing users to input queries, receive responses, and visualize chat history.
- A sidebar provides additional functionality and application information.

### 6. **Dynamic Memory Management**
- The app uses the `RunnableWithMessageHistory` component from Langchain to dynamically manage and store chat histories, enabling the agent to retrieve past conversations and provide a more personalized experience.

## Installation and Setup

Follow these steps to install and run the **ActiBot-Powered Liferay Agent Chat App** on your local machine.

### Prerequisites
- Python 3.8 or higher
- API key for the required language model (configure in `.env` file)

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

Ensure your `requirements.txt` includes the following:

```text
streamlit
langchain
python-dotenv
```

### Step 4: Configure API Keys

Create a `.env` file in the root directory and add your API key:

```bash
API_KEY=your-api-key
```

Replace `your-api-key` with the actual API key for the language model.

### Step 5: Run the Application

To start the Streamlit app, use the following command:

```bash
streamlit run app.py
```

The app will open in your default web browser, and you can begin interacting with the agent.

## How to Use

1. **Start a Conversation**: Use the input box at the bottom of the page to submit a query or request.
2. **Tool Execution**: Ask ActiBot to perform tasks such as creating a website, managing users, or retrieving a user list.
3. **View Responses**: The agent will respond with relevant answers or perform requested actions.
4. **Session Continuity**: ActiBot retains chat history within the session, so you can review previous interactions or resume the conversation seamlessly.

### Example Queries:
- **Creating a website**: "Please create a website for my business."
- **Creating a user**: "Add a new user named John Doe."
- **Fetching user list**: "Can you retrieve the list of users?"

## Application Structure

```bash
actibot-agent-chat-app/
│
├── app.py                      # Main Streamlit app code
├── requirements.txt             # Python dependencies
├── tools_prompts.py             # Prompts for tools
├── tools_functions.py           # Tool function implementations
├── tools_schemas.py             # Schemas for tool inputs
├── display_sidebar.py           # Sidebar layout functions
├── display_conversation.py      # Functions to display chat history
└── .env                         # Environment variables (not included in repo)
```

### Key Components

- **ActiBot & Langchain**: Uses the language model integrated with Langchain for generating responses and handling queries.
- **Tool Calling Agent**: ActiBot can call specific tools like `CreateWebsiteTool`, `CreateUserTool`, and `GetUserListTool` based on user commands.
- **Chat History**: Chat sessions track and maintain conversation history using `ChatMessageHistory`.

## Future Enhancements

- **Additional Tool Integrations**: More advanced tools for automating complex workflows and actions.
- **Multi-Turn Conversation Handling**: Allow the agent to handle more nuanced conversations, retaining detailed memory across turns.
- **Enhanced UI**: Add customizable UI elements such as themes, settings, and widgets for richer user interactions.

## Developer

Developed by **Rakesh Kumar**.  
Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/tech-rakesh-ai/) for feedback or to discuss future improvements.

## License

MIT License © 2024 ActiBot-Powered Liferay Agent Chat App.
