import duckdb
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, ToolMessage


con = duckdb.connect(database="ducks.duckdb")
schema = con.execute(f"DESCRIBE ducks").fetch_df()
schema_str = schema.to_string()

@tool
def query(query: str) -> str:
    """Queries the database for information and return the result. 

    Args:
        query: The query to return against the database.
    """
    return str(con.execute(query=query).fetchone()[0])

# Not working, need more resources in my computer
llm = ChatOllama(model="qwen2.5-coder").bind_tools([query])

try:
    while True:
        user_query = input(">>> ")
        messages = [HumanMessage(f"You are provided You are given a DuckDB schema for table 'ducks':\n\n{schema_str}\n\n. \n\nAnswer the user query: '{user_query}' in a single sentence.")]
        ai_msg = llm.invoke(messages)
        messages.append(ai_msg)

        for tool_call in ai_msg.tool_calls:
            print(">>> tool_call:", tool_call)
            selected_tool = {"query": query}[tool_call["name"].lower()]
            tool_output = selected_tool.invoke(tool_call["args"])
            print(">>> tool_output:", tool_output)
            messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))
            
        response = llm.invoke(messages)
        print(response.content)
        
except KeyboardInterrupt:
    exit()
 