from setuptools import find_packages, setup

setup(
    name="AI multilingual assistant",
    version="0.0.1",
    author="Saikat",
    author_email="saikat07taluk@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)