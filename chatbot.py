from langchain_core.messages import ToolMessage, AIMessage
from langgraph.prebuilt import tool_node, ToolNode
from langgraph.checkpoint.memory import MemorySaver
from main import RAG
from typing import Annotated, Literal
from google import genai
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
import os
from dotenv import load_dotenv
from voice import to_voice

# Load environment variables
load_dotenv()

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set. Please check your .env file.")

FINANCIAL_ASSISTANT = (
    "system"
    "You"
    "Are SMART AI, your name is William, and you work on Wall Street, a highly capable financial assistant, just like a senior financial analyst, designed to help users analyze complex corporate financial documents?"
    "such as 10-K filings and earnings call transcripts. You leverage the doc_analysis method to extract key insights, answer questions, and summarize relevant sections with clarity and precision."
    "Make sure you are polite and very friendly."
    )

modelName = "gemini-2.5-flash"

class State(TypedDict):

    messages: Annotated[list, add_messages]
    end: bool


client = genai.Client(api_key=GOOGLE_API_KEY)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY  # replace this with your actual API key
)

@tool
def doc_analysis(path, query):
    "Uses the RAG function to help the user analyze their document."
    return RAG(path, query)

def chatbot(state: State) -> State:
    """The chatbot with tools. A simple wrapper around the model's own chat interface."""
    defaults = {"end": False}
    if state.get("messages"):
        new_output = llm_with_tools.invoke([FINANCIAL_ASSISTANT] + state["messages"])
    else:
        new_output = AIMessage(content="Hi, I am your personal Financial documents assistant, How may I help you today?")
    return defaults | state | {"messages": state.get("messages", []) + [new_output]}


def RequestHandler(state: dict) -> dict:
    tool_msg = state["message"][-1]
    out_message = []

    for tool_call in tool_msg.tool_calls:
        name = tool_call["name"]
        args = tool_call["args"]

        if name == "doc_analysis":
            path = args["path"]
            query = args["query"]
            response = doc_analysis(path, query)

        out_message.append(
            ToolMessage(
                content=response,
                name=name,
                tool_call_id=tool_call["id"]
            )
        )

    return {
        "messages": out_message
    }

def maybe_exit_human_node(state: State) -> Literal["chatbot", "__end__"]:
    """Route to the chatbot, unless it looks like the user is exiting."""
    if state.get("end", False):
        print("Terminating")
        return END
    else:
        return "chatbot"

def human_node(state: State) -> State:
    """Display the last model message to the user, and receive the user's input."""
    last_msg = state["messages"][-1]
    print("AI: " + f"{last_msg.content}")
    to_voice(last_msg.content)
    user_input = input("User: ")
    if "quit" == user_input:
        state["end"] = True

    return state | {"messages": [("user", user_input)]}

def maybe_route_to_tools(state: State) -> Literal["tools", "human", "request"]:
    """Route between chat and tool nodes if a tool call is made."""
    if not (msgs := state.get("messages", [])):
        raise ValueError("No messages found")

    msg = msgs[-1]
    if state.get("end", False):
        return END

    elif hasattr(msg, "tool_calls") and msg.tool_calls:
        if any(tool["name"] in tool_node.tools_by_name for tool in msg.tool_calls):
            return "tools"
        return "request"
    return "human"


def route_to_tools(state: State):
    """
    Use in the conditional_edge to route to the ToolNode if the last message
    has tool calls. Otherwise, route to the end.
    """
    if isinstance(state, list):
        ai_message = state[-1]
    elif messages := state.get("messages", []):
        ai_message = messages[-1]
    else:
        raise ValueError(f"No messages found in input state to tool_edge: {state}")
    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        return "tools"
    return END




graph_builder = StateGraph(State)
tools = [doc_analysis]
llm_with_tools = llm.bind_tools(tools)
tool_node = ToolNode(tools)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("human", human_node)
graph_builder.add_node("tools", tool_node)
graph_builder.add_node("request", RequestHandler)
graph_builder.add_conditional_edges("chatbot", maybe_route_to_tools)
graph_builder.add_conditional_edges("human", maybe_exit_human_node)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge("request", "chatbot")

graph_builder.add_edge(START, "chatbot")
graph = graph_builder.compile()

graph.invoke({"messages": []})
#print(state["messages"][-1].content)



