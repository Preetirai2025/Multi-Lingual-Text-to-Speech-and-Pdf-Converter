# 🌐 Multilingual Text Converter

A powerful and lightweight Python tool to detect, convert, and translate text between multiple languages and scripts. Ideal for NLP pipelines, multilingual applications, and AI-based localization engines.

---

## 🚀 Features

- 🔍 **Language Detection** (e.g., English, Hindi, Bengali, etc.)
- 🔤 **Script Detection and Conversion** (e.g., Roman to Devanagari)
- 🌎 **Translation Support** (via Google Translate or offline models)
- 💬 **Transliteration Engine** (Supports Indic and Latin scripts)
- ⚡ Easy CLI and API support

---

## 🛠️ Technologies Used

- Python 3.x
- `langdetect` or `fastText` for language detection
- `indic-transliteration` for script conversion
- `googletrans` or `transformers` for translation


---

## 🧪 Example

```python
from multilingual_converter import convert_text

text = "mera naam Rahul hai"
converted = convert_text(text, target_script="Devanagari")
print(converted)
# Output: मेरा नाम राहुल है

git clone https://github.com/Preetirai2025/Multi-Lingual-Text-to-Speech-and-Pdf-Converter
cd multilingual-converter
pip install -r requirements.txt

