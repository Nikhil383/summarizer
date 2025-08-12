import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage
from schema import BookSummary
import json

# Load environment variables
load_dotenv()

SYSTEM_PROMPT = f"""
You are a professional book summarizer.

1. Read the input and extract keypoints.
2. Condense ideas in plain English.
3. Highlight themes, key events, or arguments.

Return JSON only in this format:

{json.dumps(BookSummary.model_json_schema(), indent=2).replace("{", "{{").replace("}", "}}")}
"""

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.4)
parser = PydanticOutputParser(pydantic_object=BookSummary)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())

# Since we're not using file saving, we remove save_summary tool
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=[])
executor = AgentExecutor(agent=agent, tools=[], verbose=True)

st.set_page_config(page_title="📚 Book Summarizer", layout="wide")
st.title("📚 Book Summarizer Agent")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.form("book_summary_form", clear_on_submit=False):
    user_text = st.text_area("Paste book content here:", height=200)
    submit_btn = st.form_submit_button("Summarize")

if submit_btn and user_text.strip():
    st.session_state.chat_history.append(HumanMessage(content=user_text))

    with st.spinner("Summarizing..."):
        response = executor.invoke({
            "query": user_text,
            "chat_history": st.session_state.chat_history
        })

    try:
        result = parser.parse(response["output"])
        st.session_state.chat_history.append(AIMessage(content=result.summary))

        st.success("✅ Summary generated successfully!")
        st.subheader(f"📖 {result.title}")
        st.write(result.summary)

        # Prepare JSON for download (in memory)
        json_output = {
            "title": result.title,
            "summary": result.summary
        }

        st.download_button(
            label="📥 Download Summary as JSON",
            data=json.dumps(json_output, indent=4),
            file_name=f"{result.title.replace(' ', '_')}.json",
            mime="application/json"
        )

    except Exception as e:
        st.error(f"Error parsing response: {e}")

# Show chat history below
if st.session_state.chat_history:
    st.divider()
    st.subheader("💬 Conversation History")
    for msg in st.session_state.chat_history:
        if isinstance(msg, HumanMessage):
            st.markdown(f"**You:** {msg.content}")
        elif isinstance(msg, AIMessage):
            st.markdown(f"**AI:** {msg.content}")
