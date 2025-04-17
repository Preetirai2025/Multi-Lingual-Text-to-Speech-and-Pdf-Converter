import streamlit as st
from gtts import gTTS
from io import BytesIO
from googletrans import Translator
from PyPDF2 import PdfReader

# Streamlit App
st.title("Multilingual Text-to-Speech and PDF Converter")

# Language Options
languages = {
    'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian',
    'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian',
    'bg': 'Bulgarian', 'ca': 'Catalan', 'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)', 'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish',
    'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish',
    'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek',
    'gu': 'Gujarati', 'ht': 'Haitian Creole', 'ha': 'Hausa', 'haw': 'Hawaiian', 'iw': 'Hebrew',
    'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo', 'id': 'Indonesian',
    'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh',
    'km': 'Khmer', 'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz', 'lo': 'Lao',
    'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian',
    'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi',
    'mn': 'Mongolian', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian',
    'ps': 'Pashto', 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian',
    'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic', 'sr': 'Serbian', 'st': 'Sesotho',
    'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali',
    'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil',
    'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'ug': 'Uyghur',
    'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba',
    'zu': 'Zulu'
}

# Input Options
input_option = st.radio("Select Input Type", ["Text", "PDF File"])

# Select Language
target_language = st.selectbox("Select the language for Text-to-Speech", options=languages.keys(), format_func=lambda x: languages[x])

translator = Translator()

if input_option == "Text":
    user_text = st.text_area("Enter the text you want to convert to speech")
    if st.button("Convert Text to Speech"):
        if user_text:
            translated_text = translator.translate(user_text, dest=target_language).text
            tts = gTTS(translated_text, lang=target_language)
            audio_file = BytesIO()
            tts.write_to_fp(audio_file)
            audio_file.seek(0)
            st.audio(audio_file, format="audio/mp3", start_time=0)
            st.success("Conversion Successful! Audio is ready to play.")
        else:
            st.error("Please enter some text.")

elif input_option == "PDF File":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        reader = PdfReader(uploaded_file)
        pdf_text = ""
        for page in reader.pages:
            pdf_text += page.extract_text() + "\n"

        if st.button("Convert PDF to Speech"):
            if pdf_text.strip():
                translated_text = translator.translate(pdf_text, dest=target_language).text
                tts = gTTS(translated_text, lang=target_language)
                audio_file = BytesIO()
                tts.write_to_fp(audio_file)
                audio_file.seek(0)
                st.audio(audio_file, format="audio/mp3", start_time=0)
                st.success("Conversion Successful! Audio is ready to play.")
            else:
                st.error("The PDF seems to be empty. Please upload a valid file.")
