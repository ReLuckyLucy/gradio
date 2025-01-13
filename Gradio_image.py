# 导入numpy库，并重命名为np，以便于后续使用。
import numpy as np

# 导入gradio库，并重命名为gr，以便于后续使用。
import gradio as gr

# 定义一个名为sepia的函数，接收一个参数input_img，即输入的图像。
def sepia(input_img):

    # 创建一个3x3的数组，作为棕褐色调的滤镜矩阵。
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],  # 滤镜的第一行，对应红色通道的权重。
        [0.349, 0.686, 0.168],  # 滤镜的第二行，对应绿色通道的权重。
        [0.272, 0.534, 0.131]   # 滤镜的第三行，对应蓝色通道的权重。
    ])

    # 对输入图像的每个像素点与滤镜矩阵进行点乘运算，实现棕褐色调效果。
    sepia_img = input_img.dot(sepia_filter.T)

    # 将图像归一化，使得所有像素值位于0和1之间，防止溢出。
    sepia_img /= sepia_img.max()

    # 返回经过棕褐色调处理后的图像。
    return sepia_img

# 创建一个新的Gradio界面对象。
demo = gr.Interface(
    sepia,  # 指定界面调用的函数为上面定义的sepia函数。
    gr.Image(),  # 设置输入组件为图像上传控件。
    "image"  # 设置输出组件类型为图像显示。
)

# 启动Gradio界面，使其可以交互。
demo.launch()