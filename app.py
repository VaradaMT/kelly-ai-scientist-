import gradio as gr
from kelly import make_poem

INTRO = """\
I’m Kelly, the AI-Scientist Poet.
Ask me anything about AI—I'll answer only in skeptical, analytical verse with practical, evidence-based tips.
"""

def chat_fn(message, history):
    if history is None:
        history = []

    reply = make_poem(message or "")

    # Append messages in dict format for type="messages"
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})

    return history, gr.Textbox(value="")

with gr.Blocks(title="Kelly — AI Scientist Poet", fill_height=True) as demo:
    gr.Markdown("# Kelly — AI Scientist Poet\n" + INTRO)

    chatbot = gr.Chatbot(type="messages", label="Chat", height=480)
    with gr.Row():
        msg = gr.Textbox(
            placeholder="e.g., Can AI replace radiologists? What are the limits?",
            scale=5
        )
        send = gr.Button("Send", variant="primary", scale=1)

    send.click(chat_fn, [msg, chatbot], [chatbot, msg])
    msg.submit(chat_fn, [msg, chatbot], [chatbot, msg])

if _name_ == "_main_":
    demo.launch()
