生成图形词云
==========

使用jieba和wordcloud生成图形词云

## 安装

    pip install -r requirements.txt

## 使用

*简单显示*

    from words_image import get_content, show_image
    import os

    BASE_DIR = os.path.dirname(__file__)
    # 文本文件夹路径
    DATA_DIR = os.path.join(BASE_DIR, "data")
    # 图片文件夹路径
    IMAGE_DIR = os.path.join(BASE_DIR, "images")
    # 源图片路径
    # 其中图片中白色的部分会被忽略
    IMAGE_PATH = os.path.join(IMAGE_DIR, "tony.png")

    if __name__ == "__main__":
        content = get_content(DATA_DIR)
        ＃ 显示生成的词图
        show_image(content, IMAGE_PATH)

*批量处理并保存*
    from words_image import get_content, save_image
    import os

    BASE_DIR = os.path.dirname(__file__)
    # 文本文件夹路径
    DATA_DIR = os.path.join(BASE_DIR, "data")
    # 图片文件夹路径
    IMAGE_DIR = os.path.join(BASE_DIR, "images")
    # 结果保存路径
    OUTPUT_DIR = os.path.join(BASE_DIR, "output")

    if __name__ == "__main__":
        content = get_content(DATA_DIR)
        for image in os.listdir(IMAGE_DIR):
            image_name = os.path.join(IMAGE_DIR, image)
            save_image(content, image_name, OUTPUT_DIR)


## 示例

*路飞*

![luffy_word](output/luffy.png)

*乔巴*

![tony_words](output/tony.png)
