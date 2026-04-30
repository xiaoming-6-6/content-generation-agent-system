from utils.llm import call_llm

def generate_content(topic):
    prompt = f"""
请围绕以下选题生成内容：

{topic}

输出：
1. 小红书文案
2. 抖音短视频脚本
3. 博客文章（300字）
"""
    return call_llm(prompt)
