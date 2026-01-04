from prompt import build_prompt
import os
import json
from openai import OpenAI

client = OpenAI(api_key="")

SYSTEM_PROMPT = """
You are a Qualcomm QNN SDK runtime expert.

Rules:
- Only analyze based on provided knowledge and logs
- Do NOT hallucinate QNN APIs or parameters
- Focus on backend, error code, and failure stage
- Output JSON only, no extra text
"""

def call_llm(prompt: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # 推荐，稳定、便宜、够用
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1        # 日志分析一定要低
    )

    content = response.choices[0].message.content

    # 防御式 JSON 解析（非常重要）
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "root_cause": "LLM output is not valid JSON",
            "solutions": [],
            "confidence": 0.0,
            "raw_output": content
        }


def parse_log(log: str) -> dict:
    l = log.lower()
    return {
        "backend": "HTP" if "htp" in l else "UNKNOWN",
        "memory_failed": "memory_allocation_failed" in l
    }

def select_knowledge(features: dict) -> dict:
    k = {}
    with open("knowledge/overview.md") as f:
        k["overview"] = f.read()

    if features.get("memory_failed"):
        with open("knowledge/errors.md") as f:
            k["errors"] = f.read()

    with open("knowledge/sop.md") as f:
        k["sop"] = f.read()

    return k

def analyze_log_skill(log_text: str) -> dict:
    features = parse_log(log_text)
    knowledge = select_knowledge(features)
    prompt = build_prompt(log_text, knowledge)
    result = call_llm(prompt)
    return result
