import wordcloud   # 导入词云模块
import imageio
back_color = imageio.imread('background.jpg')  # 解析该图片
w = wordcloud.WordCloud(
    font_path="C:/WINDOWS/Fonts/SIMYOU.TTF",  # 字体
    background_color="white",  # 白色背景
    mask = back_color,  # 设置背景的形状
                        ) # 创建词云对象
w.generate('梦想 Python 创新 青春 Java Android 人生 苦短 我用Python 敬业 爱国 富强 民主 和谐')  # 指定加载文本
w.to_file('picture.png')  # 保存图片


