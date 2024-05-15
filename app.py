import chainlit as cl


@cl.on_message
async def on_message():
    await cl.Message(content="Hi, I'm Social Robo and I'd like to help you find out more about the Social Map of Berlin.").send()

    