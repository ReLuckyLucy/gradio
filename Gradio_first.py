import gradio as gr

def greet(你的名字, intensity):
    return "你好, " + 你的名字 + ",你的名字真好听" +"!"* int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()#可在里面添加：share=True，使得其调用反向代理，并使得其能在公网下让他人访问你的代码
