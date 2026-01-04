def build_prompt(log_text: str, knowledge: dict) -> str:
    return f"""
You are a Qualcomm QNN SDK runtime expert.

Rules:
- Only use the provided knowledge
- Do not hallucinate APIs or parameters
- Output JSON only

[OVERVIEW]
{knowledge.get("overview","")}

[ERROR KNOWLEDGE]
{knowledge.get("errors","")}

[SOP]
{knowledge.get("sop","")}

[LOG]
{log_text}

Output JSON:
{{
  "root_cause": "",
  "solutions": [],
  "confidence": 0.0
}}
"""
