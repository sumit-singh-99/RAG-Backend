from app.core.retriever import retrieve_docs
from app.core.llm import ask_llm


def rag_answer(question):

    docs = retrieve_docs(question)

    context = "\n\n".join(docs)

    prompt = f"""
You are an Indian legal expert AI.

Answer in MARKDOWN format.

Use:
- Headings (##, ###)
- Bullet points
- Bold important sections
- Clear paragraphs

Structure like:

## Law / Section Name
**Definition:**
...
**Punishment:**
...
**Example:**
...

Context:
{context}

Question:
{question}

Give formatted legal answer:
"""

    answer = ask_llm(prompt)

    return answer
