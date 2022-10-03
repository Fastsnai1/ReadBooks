from gtts import gTTS
from art import tprint
from pathlib import Path


def text_to_mp3(file_path='test.txt', language='en'):
    if Path(file_path).is_file() and (file_path.endswith('.txt') or file_path.endswith('.doc')):

        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing.....')

        with (open(file=file_path, mode='r')) as txt:
            pages = txt.readlines()

        text = ''.join(pages)
        text = text.replace('\n', '')
        text = text.replace('-', ',')

        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully!'
    else:
        'File not exists, check the file path.'


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language, for example 'en' or 'ru': ")

    print(text_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
