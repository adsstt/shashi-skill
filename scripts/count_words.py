"""
一个简单的示例脚本：统计文本中的字数。

这是 Skill 文件夹中 scripts/ 的示例——
展示 Skill 除了 skill.md，还能打包可执行脚本让 AI 调用。

用法：python count_words.py <文件路径>
"""

import sys


def count_words(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    return len(words)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python count_words.py <文件路径>")
        sys.exit(1)

    path = sys.argv[1]
    count = count_words(path)
    print(f"文件 '{path}' 共 {count} 个字")
