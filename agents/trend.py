from utils.llm import call_llm

def get_trends(topic):
    prompt = f"""
你是内容运营专家，请围绕【{topic}】生成5个当前有潜力的内容选题。
"""
    return call_llm(prompt)
