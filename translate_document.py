#!/usr/bin/env python3
"""
AI Translation Service — Sovereign Optics
Workflow: document → DeepL API → human review notes → formatted output
Usage: python3 translate_document.py <input_file> <source_lang> <target_lang>
"""
import sys, os, json, subprocess
from pathlib import Path

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY", "")  # Set when user signs up

def translate_text(text, source_lang, target_lang):
    """Use DeepL API to translate text."""
    if not DEEPL_API_KEY:
        # Fallback: use local LLM via zai proxy
        print("No DEEPL_API_KEY set — using local LLM fallback")
        result = subprocess.run([
            "curl", "-s", "http://localhost:9099/chat/completions",
            "-H", "Content-Type: application/json",
            "-d", json.dumps({
                "model": "glm-4-flash",
                "messages": [
                    {"role": "system", "content": f"You are a professional translator. Translate the following text from {source_lang} to {target_lang}. Maintain formatting, preserve technical terms, and ensure natural fluency. Output ONLY the translation."},
                    {"role": "user", "content": text[:5000]}
                ],
                "temperature": 0.3
            })
        ], capture_output=True, text=True)
        resp = json.loads(result.stdout)
        return resp.get("choices", [{}])[0].get("message", {}).get("content", text)
    
    # DeepL API
    result = subprocess.run([
        "curl", "-s", "https://api-free.deepl.com/v2/translate",
        "-d", f"auth_key={DEEPL_API_KEY}",
        "-d", f"text={text[:5000]}",
        "-d", f"source_lang={source_lang}",
        "-d", f"target_lang={target_lang}"
    ], capture_output=True, text=True)
    resp = json.loads(result.stdout)
    return resp.get("translations", [{}])[0].get("text", text)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: translate_document.py <input_file> <source_lang> <target_lang>")
        print("Example: translate_document.py document.pdf DE EN")
        sys.exit(1)
    
    input_file = sys.argv[1]
    source_lang = sys.argv[2].upper()
    target_lang = sys.argv[3].upper()
    
    # Read input (works with txt, md; for PDF use pdftotext first)
    text = Path(input_file).read_text()
    
    # Split into chunks if long
    chunks = [text[i:i+5000] for i in range(0, len(text), 5000)]
    translated = []
    for i, chunk in enumerate(chunks):
        print(f"Translating chunk {i+1}/{len(chunks)}...")
        translated.append(translate_text(chunk, source_lang, target_lang))
    
    result = "\n".join(translated)
    
    # Write output
    output_file = input_file.rsplit(".", 1)[0] + f"_translated_{target_lang.lower()}.txt"
    Path(output_file).write_text(result)
    print(f"\nTranslation saved to: {output_file}")
    print(f"Characters: {len(result)}")
    print(f"Estimated cost: €{max(0.10, len(result)/1500 * 0.50):.2f}")
