import pdfplumber
from gtts import gTTS


def get_text():
    with pdfplumber.open("text.pdf") as file:
        pages = [page.extract_text() for page in file.pages]
        text = " ".join(pages).replace("\n"," ")
    return text


def get_audio_file(text):
    language = "ru"
    phrase = gTTS(text = text,lang = language,slow = False)
    phrase.save("Welcome.mp3")


def main():
    text = get_text()
    print(text)
    get_audio_file(text)


if __name__ == "__main__":
    main()
