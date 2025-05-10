# transcription.py
import os
from openai import OpenAI

def transcribe_audio(audio_file_path, openai_client=None):
    """
    Transcribes an audio file using OpenAI's Whisper API.

    Args:
        audio_file_path (str): The path to the audio file.
        openai_client (openai.OpenAI, optional): An OpenAI client instance.
                                                  If None, a new client will be created.

    Returns:
        str: The transcribed text.
    """
    if openai_client is None:
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    else:
        client = openai_client

    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return transcript.text
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

if __name__ == '__main__':
    # Example usage (for testing the transcription function)
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        print("OPENAI_API_KEY not found in .env file.")
    else:
        audio_path = r"C:\Users\dell\Downloads\newMeeting.mp3"  # Replace with your audio file
        if os.path.exists(audio_path):
            transcription_text = transcribe_audio(audio_path)
            if transcription_text:
                print("Transcription:")
                print(transcription_text)
        else:
            print(f"Audio file not found at: {audio_path}")