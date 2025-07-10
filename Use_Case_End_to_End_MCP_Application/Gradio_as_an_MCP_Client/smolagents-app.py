import gradio as gr

from smolagents import InferenceClientModel, CodeAgent, MCPClient
try:
    mcp_client = MCPClient(
        {"url": "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse"}
    )
    tools = mcp_client.get_tools()

    model = InferenceClientModel(token="your_token")
    agent = CodeAgent(tools=[*tools], model=model)

    demo = gr.ChatInterface(
        fn=lambda message, history: str(agent.run(message)),
        type='messages',
        examples=['Prime factorization of 68'],
        title='Agent with MCP Tools',
        description='This is a simple agent that uses MCP tools to answer questions.'
    )

    demo.launch()
finally:
    mcp_client.disconnect()