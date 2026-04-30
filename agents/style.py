from utils.llm import call_llm

def rewrite_style(content, style="幽默风格"):
    prompt = f"""
请将以下内容改写为【{style}】：

{content}
"""
    return call_llm(prompt)
