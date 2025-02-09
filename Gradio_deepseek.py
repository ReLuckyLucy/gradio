# 导入所需库
import gradio as gr  # 用于构建Web界面
import requests  # 用于发送HTTP请求
import json  # 用于处理JSON数据

# DeepSeek API配置（需要替换为你的真实API密钥）
DEEPSEEK_API_KEY = "sk-aee59f45296f42d9b12306e100fa3fbd"  # 从DeepSeek平台获取的API密钥
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"  # API端点地址

# 定义处理AI回复的函数
def get_ai_response(user_input):
    """
    调用DeepSeek API获取AI回复
    参数：user_input - 用户输入的文本
    返回：AI生成的回复内容
    """
    # 设置请求头
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }

    # 构建请求体（根据DeepSeek API文档要求）
    payload = {
        "model": "deepseek-chat",  # 使用的模型名称
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ],
        "temperature": 0.7  # 控制生成文本的随机性（0-2之间）
    }

    try:
        # 发送POST请求
        response = requests.post(
            url=DEEPSEEK_API_URL,
            headers=headers,
            data=json.dumps(payload)
        )

        # 检查响应状态
        response.raise_for_status()

        # 解析响应内容
        response_data = response.json()
        
        # 提取AI回复内容（根据实际API返回结构调整）
        ai_response = response_data["choices"][0]["message"]["content"]
        
        return ai_response

    except Exception as e:
        # 错误处理
        return f"发生错误：{str(e)}"

# 创建Gradio界面
with gr.Blocks() as demo:  # 使用Blocks API创建更灵活的布局
    gr.Markdown("## DeepSeek AI对话接口")  # 标题
    
    with gr.Row():  # 创建水平排列的布局
        # 左侧输入区域
        with gr.Column():
            input_text = gr.Textbox(
                label="输入你的消息",
                placeholder="在这里输入你想说的话...",
                lines=5  # 设置输入框高度为5行
            )
            submit_btn = gr.Button("发送", variant="primary")  # 主要样式按钮
        
        # 右侧输出区域
        with gr.Column():
            output_text = gr.Textbox(
                label="AI回复",
                lines=10,  # 设置输出框高度为10行
                interactive=False  # 设置为不可编辑
            )

    # 设置按钮点击事件和输入框回车事件
    submit_btn.click(
        fn=get_ai_response,  # 绑定的处理函数
        inputs=input_text,  # 输入组件
        outputs=output_text  # 输出组件
    )
    input_text.submit(
        fn=get_ai_response,
        inputs=input_text,
        outputs=output_text
    )

    # 添加示例
    gr.Examples(
        examples=[
            ["请用Python写一个快速排序算法"],
            ["解释量子计算的基本原理"],
            ["写一首关于春天的诗"]
        ],
        inputs=input_text
    )

# 启动Web服务
if __name__ == "__main__":
    demo.launch(server_port=7860)  # 指定端口号启动服务