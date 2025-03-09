import os
import pytube
from moviepy.editor import AudioFileClip

def download_youtube_audio(youtube_url: str, output_folder: str = ".", output_filename: str = "audio.mp3") -> str:
    """
    Скачивает аудио с YouTube и сохраняет в MP3.
    
    :param youtube_url: Ссылка на YouTube-видео.
    :param output_folder: Папка для сохранения MP3-файла.
    :param output_filename: Имя MP3-файла.
    :return: Путь к сохранённому файлу.
    """
    print("🔄 Загружаем аудио с YouTube...")

    # Получаем аудиопоток
    yt = pytube.YouTube('https://youtu.be/o37_Leu6-3I?si=iP_zxg84LDccjl8i')
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Скачиваем временный файл
    temp_file = audio_stream.download(output_path=r'C:\Users\Public\Music')
    
    # Преобразуем в MP3
    audio_clip = AudioFileClip(temp_file)
    mp3_file = os.path.join(output_folder, 'test')
    audio_clip.write_audiofile(mp3_file)
    
    # Удаляем временный файл
    os.remove(temp_file)

    print(f"✅ Аудио успешно сохранено: {mp3_file}")
    return mp3_file

if __name__ == "__main__":
    youtube_url = input("Введите ссылку на YouTube-видео: ").strip()
    output_folder = input("Введите папку для сохранения (Enter для текущей): ").strip() or "."
    output_filename = input("Введите имя файла (Enter для 'audio.mp3'): ").strip() or "audio.mp3"

    download_youtube_audio(youtube_url, output_folder, output_filename)
