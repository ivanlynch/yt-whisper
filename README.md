# 🚨 READ
This is not the original repo, i forked it because the original is outdated. [THIS IS THE ORIGINAL REPO](https://openai.com/blog/whisper)

# Automatic YouTube subtitle generation

This repository uses `yt-dlp` and [OpenAI's Whisper](https://openai.com/blog/whisper) to generate subtitle files for any youtube video.

## Installation

To get started, you'll need Python 3.7 or newer. Install the binary by running the following command:

    python3 -m pip install git+https://github.com/ivanlynch/yt-whisper

You'll also need to install [`ffmpeg`](https://ffmpeg.org/), which is available from most package managers:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg
```

## Usage

The following command will generate a VTT file from the specified YouTube video

    sub "https://www.youtube.com/shorts/MAWYCl3jDb8"

The default setting (which selects the `small` model) works well for transcribing English. You can optionally use a bigger model for better results (especially with other languages). The available models are `tiny`, `tiny.en`, `base`, `base.en`, `small`, `small.en`, `medium`, `medium.en`, `large`.

    sub "https://www.youtube.com/shorts/MAWYCl3jDb8" --model medium

Adding `--task translate` will translate the subtitles into English:

    sub "https://www.youtube.com/shorts/MAWYCl3jDb8" --task translate

Run the following to view all available options:

    sub --help

## License

This script is open-source and licensed under the MIT License. For more details, check the [LICENSE](LICENSE) file.
