import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Hi, I'm Social Robo and I'd like to help you find out more about the Social Map of Berlin.").send()

    