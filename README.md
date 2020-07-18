# m3u8-dl

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/05b08dc62b29405a934ee673be94d78d)](https://app.codacy.com/manual/excalibur.krv/m3u8-dl?utm_source=github.com&utm_medium=referral&utm_content=excalibur-kvrv/m3u8-dl&utm_campaign=Badge_Grade_Settings)

a CLI program to download videos in a m3u8 playlist, write it to a single video file and convert it to mp4 using ffmpeg 

## Dependencies
- Install python external modules using `pip install -r requirements.txt` after activating virtualenv.
- FFMPEG for video conversion, visit https://www.ffmpeg.org/download.html.
- Visit https://www.wikihow.com/Install-FFmpeg-on-Windows for FFMPEG setup on windows.
- Visit https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment for instructions on how to use virtualenv. 

## Usage
- clone the repository using `git clone "ssh/https url"`.
- create a virtual environment using `virtualenv -p python3.6 venv` in linux terminal, see 'Dependecies' for platform specific instructions.
- activate virtual environment using `source venv/bin/activate` in linux terminal, see 'Dependecies' for platform specific instructions.
- install dependencies using `pip install -r requirements.txt`.
- compile shared libraries using ` python setup.py build_ext --inplace`.
- insert the url request headers in headers.txt.
- start the script using `python main.py <url of playlist>`.

## Installing/Uninstalling
for installation in ubuntu using PyInstaller:-
- activate virtualenv using `source venv/bin/activate`
- run `pyinstaller main.py --name m3u8-dl --onefile -p venv/lib/python3.6/site-packages/
` in terminal.
- run `sudo mv dist/m3u8-dl /usr/local/bin/` in terminal window.
- now that the program is installed globally you can start the program using `m3u8-dl` in the terminal

for uninstalling in ubuntu:-
- run `sudo rm /usr/local/bin/m3u8-dl`

## CLI Options
    --help, -h:- display how to use the script
    --convert, -c:- specify this flag to convert the video to mp4 using ffmpeg`
    --name, -n:- specify the name by which to save the downloaded video, ele 'video' is chosen as default name`
    --header-path, -p:- specify the path of header file`
    --retry, -r:- specify number of retries, by default 5 retries will be initiated
    --debug, -d:- print helpful messages to console to understand program flow
