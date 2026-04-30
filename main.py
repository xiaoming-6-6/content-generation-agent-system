import os
from agents.trend import get_trends
from agents.content import generate_content
from agents.style import rewrite_style

OUTPUT_DIR = "outputs"

def save_file(name, content):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(f"{OUTPUT_DIR}/{name}.txt", "w", encoding="utf-8") as f:
        f.write(content)

def run_pipeline(topic):
    print("🔥 获取热点选题...")
    trends = get_trends(topic)
    print(trends)

    first_topic = trends.split("\n")[0]

    print("\n✍️ 生成内容...")
    content = generate_content(first_topic)
    print(content)

    print("\n🎨 风格优化...")
    styled = rewrite_style(content, "更有网感、适合年轻人")
    print(styled)

    save_file("final_content", styled)
    print("\n✅ 内容已保存到 outputs/final_content.txt")

if __name__ == "__main__":
    run_pipeline("AI工具")
