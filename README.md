TURN YOUR VIDEO INTO A DREAM


This program takes your video, splits it into its frames, sends it to an AI to have special effects applied, and puts the video back together.


Install required libraries with:

> pip3 install -r requirements.txt


Usage:

<ul><b><i>Put your video in the same folder as main.py </i></b></ul>

<ul><b><i><pre>python main.py  'name.mp4 '  'apikey' </pre></i></b></ul>

<ul><b><i>Run the program and wait </i></b></ul>

using_docker:

```bash
docker build -t ai .
```
```bash
docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp ai main.py test.mp4  apikey
```