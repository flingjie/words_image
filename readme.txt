生成图形词云
==========

使用jieba和wordcloud生成图形词云

## 安装

    pip install -r requirements.txt

## 使用

    from words_image import generate_image
    import os

    base_dir = os.path.dirname(__file__)
    # 定义文本文件夹路径
    words_dir = os.path.join(base_dir, "data")
    # 定义图形的图片路径
    # 其中图片中白色的部分会被忽略
    image_name = os.path.join(base_dir, "nami.png")

    if __name__ == "__main__":
         # 获取文件夹下所有文本路径
         files = []
         for f in os.listdir(words_dir):
             full_f = os.path.join(words_dir, f)
             if os.path.isfile(full_f):
                 files.append(full_f)
         # 生成词云
         generate_image(files, image_name)

## 示例

*路飞*

_原图_
![luffy](luffy.png)
_词云图_
![luffy_word](luffy_result.png)

*乔巴*

_云图_
![tony](tony.png)

_词云图_
![tony_words](tony_result.png)
