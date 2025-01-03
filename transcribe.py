from markitdown import MarkItDown
import os
import argparse
import tracemalloc
tracemalloc.start()

def transcribe_audio(file_path, language='en-US'):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found")
        return
        
    try:
        md = MarkItDown()
        result = md.convert(file_path, language=language)
        print("Transcription Results:")
        print("-" * 50)
        print(result.text_content)
        
    except Exception as e:
        print(f"Error during transcription: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe audio files')
    parser.add_argument('file_path', help='Path to the audio file')
    parser.add_argument('--language', '-l', default='en-US', 
                      help='Language code (e.g., en-US, de-DE). Defaults to en-US')
    
    args = parser.parse_args()
    transcribe_audio(args.file_path, args.language)