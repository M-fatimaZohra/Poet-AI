import chainlit as cl
from agents import Runner
from my_agents.poet import poet

# Store conversation history globally or in session
poetAI_history = []

@cl.on_message
async def main(message: cl.Message):
    input_prompt = message.content.strip()

    if input_prompt == "":
        await cl.Message(content="Empty prompt. Please say something!").send()
        return

    # Add user message to history
    poetAI_history.append({"role": "user", "content": input_prompt})

    # Run agent and get result
    result = await Runner.run(poet, poetAI_history)

    # Add assistant response to history
    poetAI_history.append({"role": "assistant", "content": result.final_output})

    # Send response
    await cl.Message(content=result.final_output).send()
