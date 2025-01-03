# ToneItDown


A quick and dirty evening project to transcribe voice recordings and turn them into markdown notes.

Audio transcription tool powered by Google Speech-to-Text API which is embedded in Microsoft's [markitdown](https://github.com/microsoft/markitdown) library. Supports MP3 and WAV files with multiple language options. 

## State of the project

Transcription of a short english test file works very well. German translation is not working.

## Requirements

- Anaconda or Miniconda
- Python 3.10+

## Setup

1. Install Anaconda/Miniconda from [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

3. Clone & open repository:
   ```shell
   git clone https://github.com/yourusername/toneitdown.git
   cd toneitdown
   ```

4. Open Anaconda Prompt (not regular CMD) and create environment:
   ```shell
   conda env create -f environment.yml
   conda activate toneitdown
   ```

## Usage

In Anaconda Prompt:

```shell
# English transcription (default)
python transcribe.py "path/to/audio.mp3"

# German transcription
python transcribe.py "path/to/audio.mp3" --language de-DE
```

The output is printed to the terminal.
