import gradio as gr  # 导入Gradio库，并将其重命名为gr，以便于使用。

def greet(name, is_morning, temperature):  
    # 定义一个名为greet的函数，它接收三个参数：name（名字），is_morning（是否为早晨），temperature（温度）。

    salutation = "Good morning" if is_morning else "Good evening"  
    # 根据is_morning的布尔值选择合适的问候语，是早晨则为"Good morning"，否则为"Good evening"。

    greeting = f"{salutation} {name}. It is {temperature} degrees today"  
    # 构建一条包含问候语和当天温度的消息字符串。
    
    celsius = (temperature - 32) * 5 / 9  
    # 将华氏温度转换为摄氏温度。

    return greeting, round(celsius, 2)  
    # 返回构建的消息以及四舍五入到两位小数的摄氏温度。

demo = gr.Interface(  
    # 创建一个新的Gradio界面对象。
    
    fn=greet,  
    # 指定界面调用的函数为greet函数。

    inputs=["text", "checkbox", gr.Slider(0, 100)],  
    # 设置输入组件，分别为文本框、复选框和滑动条（温度范围从0到100）。

    outputs=["text", "number"],  
    # 设置输出组件，分别为文本和数字显示。
)
demo.launch()  # 启动Gradio界面，使其可以交互。