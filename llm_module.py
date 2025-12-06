# """
# LLM generation module using Google Gemini (Google GenAI SDK).
# Falls back to Hugging Face GPT-2 or DistilGPT-2 if Gemini is unavailable.
# """
# import os
# from dotenv import load_dotenv
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# # Gemini SDK
# try:
#     import google.generativeai as genai
#     GENAI_AVAILABLE = True
# except Exception:
#     GENAI_AVAILABLE = False

# # Fallback GPT-2
# FALLBACK = False
# generator = None
# if not GENAI_AVAILABLE:
#     try:
#         from transformers import pipeline as hf_pipeline
#         FALLBACK = True
#         generator = hf_pipeline("text-generation", model="distilgpt2")
#     except Exception:
#         FALLBACK = False

# DEFAULT_MODEL = "gemini-2.5-flash"

# DEFAULT_SYSTEM_PROMPT = """
# You are an empathetic emotional-support AI chatbot.
# Provide a clear explanation of the user's input.
# Respond in short, human-like, point-wise format if possible.
# """

# def configure_gemini():
#     if GENAI_AVAILABLE and GEMINI_API_KEY:
#         try:
#             genai.configure(api_key=GEMINI_API_KEY)
#             return True
#         except Exception as e:
#             print("Gemini configuration error:", e)
#     return False

# def generate_llm(prompt: str, model: str = DEFAULT_MODEL,
#                  max_output_tokens: int = 250, temperature: float = 0.7) -> str:

#     # --- Gemini ---
#     if GENAI_AVAILABLE and configure_gemini():
#         try:
#             llm = genai.GenerativeModel(model)
#             full_prompt = DEFAULT_SYSTEM_PROMPT + "\n\nUser Input:\n" + prompt + "\n\nAssistant:"

#             response = llm.generate_content(
#                 full_prompt,
#                 generation_config={
#                     "max_output_tokens": max_output_tokens,
#                     "temperature": temperature
#                 }
#             )

#             # Use response.text if available
#             if hasattr(response, "text") and response.text:
#                 return response.text.strip()
#             # Use first candidate if text missing
#             elif hasattr(response, "candidates") and response.candidates:
#                 for c in response.candidates:
#                     if hasattr(c, "content") and c.content:
#                         return c.content.strip()
#                 return "Gemini returned empty candidates."
#             else:
#                 return "Gemini returned no valid content."

#         except Exception as e:
#             print("Gemini Error:", e)

#     # --- GPT-2 fallback ---
#     if FALLBACK and generator:
#         try:
#             out = generator(prompt, max_new_tokens=max_output_tokens,
#                             temperature=temperature, truncation=True)
#             generated = out[0]["generated_text"]
#             if generated.startswith(prompt):
#                 generated = generated[len(prompt):]
#             return generated.strip()
#         except Exception as e:
#             print("GPT-2 Error:", e)
#             return f"GPT-2 Error: {e}"

#     return "Error: No LLM available. Check Gemini key or install HuggingFace transformers."


"""
LLM generation module using Google Gemini (GenAI SDK).
Falls back to Hugging Face GPT-2/DistilGPT-2 if Gemini unavailable.
"""
import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini SDK
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except Exception:
    GENAI_AVAILABLE = False

# Fallback GPT-2
FALLBACK = False
generator = None
if not GENAI_AVAILABLE:
    try:
        from transformers import pipeline as hf_pipeline
        FALLBACK = True
        generator = hf_pipeline("text-generation", model="distilgpt2")
    except Exception:
        FALLBACK = False

DEFAULT_MODEL = "gemini-2.5-flash"

DEFAULT_SYSTEM_PROMPT = """
You are an empathetic emotional-support AI chatbot.
Provide a clear explanation of the user's input.
Respond in short, human-like, point-wise format if possible.
"""

def configure_gemini():
    if GENAI_AVAILABLE and GEMINI_API_KEY:
        try:
            genai.configure(api_key=GEMINI_API_KEY)
            return True
        except Exception as e:
            print("Gemini configuration error:", e)
    return False

def generate_llm(prompt: str, model: str = DEFAULT_MODEL,
                 max_output_tokens: int = 250, temperature: float = 0.7,
                 user_need: str = None) -> str:

    # Build dynamic system prompt
    system_prompt = DEFAULT_SYSTEM_PROMPT
    if user_need and user_need.strip():
        system_prompt += f"\n\nAdditional context from user: {user_need.strip()}"

    full_prompt = system_prompt + "\n\nUser Input:\n" + prompt + "\n\nAssistant:"

    # --- Gemini ---
    if GENAI_AVAILABLE and configure_gemini():
        try:
            llm = genai.GenerativeModel(model)
            response = llm.generate_content(
                full_prompt,
                generation_config={
                    "max_output_tokens": max_output_tokens,
                    "temperature": temperature
                }
            )

            if hasattr(response, "text") and response.text:
                return response.text.strip()
            elif hasattr(response, "candidates") and response.candidates:
                for c in response.candidates:
                    if hasattr(c, "content") and c.content:
                        return c.content.strip()
                return "Gemini returned empty candidates."
            else:
                return "Gemini returned no valid content."

        except Exception as e:
            print("Gemini Error:", e)

    # --- GPT-2 fallback ---
    if FALLBACK and generator:
        try:
            out = generator(full_prompt, max_new_tokens=max_output_tokens,
                            temperature=temperature, truncation=True)
            generated = out[0]["generated_text"]
            if generated.startswith(full_prompt):
                generated = generated[len(full_prompt):]
            return generated.strip()
        except Exception as e:
            print("GPT-2 Error:", e)
            return f"GPT-2 Error: {e}"

    return "Error: No LLM available. Check Gemini key or install HuggingFace transformers."
