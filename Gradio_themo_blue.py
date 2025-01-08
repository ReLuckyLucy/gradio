import gradio as gr

def greet(你的名字, intensity):
    return "你好, " + 你的名字 + ",你的名字真好听" +"!"* int(intensity)

# 使用预设主题创建 Blocks 应用
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    # 创建文本输入框
    name_input = gr.Textbox(label="你的名字")
    
    # 创建滑动条输入
    intensity_slider = gr.Slider(minimum=1, maximum=10, step=1, label="强度", value=5)
    
    # 创建文本输出框
    output_text = gr.Textbox(label="问候信息")
    
    # 绑定 greet 函数到输入控件上，并将结果输出到文本框
    name_input.change(greet, inputs=[name_input, intensity_slider], outputs=output_text)
    intensity_slider.change(greet, inputs=[name_input, intensity_slider], outputs=output_text)

# 启动应用，并设置 share 参数为 True 以允许公网访问
demo.launch(share=True)