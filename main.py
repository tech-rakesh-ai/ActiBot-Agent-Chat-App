# import getpass
import os
import uuid
import streamlit as st
from langchain_core.tools import StructuredTool
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import tools_prompts
from display_sidebar import display_sidebar
from display_conversation import display_chat_history
from tools_functions import create_website_func, create_user_func, get_user_list_func
from tools_schemas import CreateWebsiteSchema, CreateUserSchemas, GetUserListSchema
from streamlit_extras.let_it_rain import rain
from langchain.globals import set_verbose

load_dotenv()

st.set_page_config(page_title="ActiBot-Agent-Chat-App", page_icon=":robot_face:")

rain(
    emoji="🎈",
    font_size=54,
    falling_speed=5,
    animation_length=5,
)

# Load the GROQ API KEY
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
# if not GROQ_API_KEY:
#     os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

# Initialize the language model of Groq
llm = ChatGroq(
    model_name="llama3-70b-8192",
    temperature=0.3,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

MEMORY_KEY = "chat_history"

liferay_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", tools_prompts.assistant_prompt),
        MessagesPlaceholder(variable_name=MEMORY_KEY),
        ("user", "{content}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# Create website tool
create_website_tool = StructuredTool.from_function(
    func=create_website_func,
    name="CreateWebsiteTool",
    description=tools_prompts.create_website_tool_prompt,
    args_schema=CreateWebsiteSchema,
    handle_tool_error=True,
)

# create user tool
create_user_tool = StructuredTool.from_function(
    func=create_user_func,
    name="CreateUserTool",
    description=tools_prompts.create_user_tool_prompt,
    args_schema=CreateUserSchemas,
    handle_tool_error=True,
)

# get user list  tool
get_user_list_tool = StructuredTool.from_function(
    func=get_user_list_func,
    name="GetUserListTool",
    description=tools_prompts.get_user_list_tool_prompt,
    args_schema=GetUserListSchema,
    handle_tool_error=True,
)

# List of tools
tools = [create_website_tool, create_user_tool, get_user_list_tool]

# Bind tools to the language model
llm_with_tools = llm.bind_tools(tools)

# Create the agent
agent = create_tool_calling_agent(llm, tools, liferay_prompt_template)

# Initialize the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Store for session history
store = {}


# Function to get session history
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


# Runnable with message history
agent_with_chat_history = RunnableWithMessageHistory(
    agent_executor,
    get_session_history,
    input_messages_key="content",
    history_messages_key=MEMORY_KEY,
)

# Calling function to display sidebar
display_sidebar(st)


# Function to get or create a session_id
def get_session_id():
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = str(uuid.uuid4())
    return st.session_state["session_id"]


if 'conversation' not in st.session_state:
    st.session_state.conversation = []

if user_input := st.chat_input("Enter Your Query!"):
    st.session_state.conversation.append({"role": "user", "content": user_input})

    res = agent_with_chat_history.invoke(
        {"content": user_input},
        config={"configurable": {"session_id": get_session_id()}},
    )

    st.session_state.conversation.append({"role": "assistant", "content": res['output']})

    print("Store Message--------------------", store)

# Display conversation
display_chat_history(st)
