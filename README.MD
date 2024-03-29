# Threadsnake

[![](https://img.shields.io/badge/Version-1.0.8-yellow.svg)](https://pypi.org/project/threadsnake/#history) 
[![](https://img.shields.io/badge/Repo-Pypi-blue.svg)](https://pypi.org/project/threadsnake/) 
[![](https://img.shields.io/badge/Repo-Github-purple.svg)](https://github.com/LostSavannah/threadsnake) 
![](https://img.shields.io/badge/Python_3.6-red.svg)

**Threadsnake** is an experimental server side library. It was created as an educational (self-educational) project in order to explain how does [HTTP/1.1](https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/Evolution_of_HTTP) works (I'm lying, it was to understand it).

```python
import asyncio
from threadsnake.turbo import Application, HttpRequest, HttpResponse

app = Application(8080)

@app.get('/')
def main(app:Application, req:HttpRequest, res:HttpResponse):
    res.end('Served by threadsnake!')

asyncio.run(app.run())
```
_The previous example sets a server wich listens at port 8080 and responds to every get resquest to the path /_

Threadsnake is designed to be lightweight and simple, yet able to serve hypertext and other resources sucessfully. Futhermore, as it was build over the [The Python Standard Library](https://docs.python.org/3/library/), it has no third party dependencies.

## Features

As I said, threadsnake is an academic project, not intended to be used as an fully production tool. However, it actually has some interesting capacities out of the box:

* [Static files](https://dev.moradev.dev/threadsnake/examples/static_files)

* [Session management](https://dev.moradev.dev/threadsnake/examples/session_management)

* [Files upload and download](https://dev.moradev.dev/threadsnake/examples/files)

* [Multipart-form data parsing](https://dev.moradev.dev/threadsnake/examples/body_parsing)

* [Authorization parameters parsing](https://dev.moradev.dev/threadsnake/examples/authorization)

...And much more. In fact, I'm compiling [a lot of examples](https://dev.moradev.dev/threadsnake/examples) in order to show how can you use all those options to make a feature-rich and fully functional web server.

## Installing threadsnake

### Installing through pip

The main way to get threadsnake is using [pip](https://pypi.org/project/pip/):

    pip install threadsnake

If you did it well, the [python package manager](https://pypi.org/project/pip/) will download and install threadsnake on your system. If not, well... That means something went wrong. Check [this link](https://dev.moradev.dev/threadsnake/installing_troubleshoot/pip) in order to solve the pip installation method. Those other links may be helpful:

* [Installing packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)
* [Installing Python Modules](https://docs.python.org/3/installing/index.html)

### Downloading from Pypi

Yes, i know it's redundant, but you always can go to [pypi](https://pypi.org/) and download the package [directly](https://pypi.org/project/threadsnake/#files) (The 'directly' part is the actual link to pypi. However, as all we know, we feel more comfortable by clicking the literal link, so, here you have it: [https://pypi.org/project/threadsnake/#files](https://pypi.org/project/threadsnake/#files)).

### Downloading from the repository ...if still here

If [Murphy](https://en.wikipedia.org/wiki/Murphy%27s_law) is obsessed with you (Seriously, if you're still reading, it have to be true) and all the above fails, then you have no option than going to the repository at [github](https://github.com/LostSavannah/threadsnake).

## Documentation and Issues 

Wow... You're still reading. You have to be some sort of... Anime Archetype. 

Well, as you can see right now we lack of a proper documentation. You have to understand, it's a new and small project. That said, once I finish uploading the examples, I'm planning to publish the [documentation in this link](https://dev.moradev.dev/threadsnake/documentation/) and the bugs tracking [to this other link](https://dev.moradev.dev/threadsnake/issues/). Till then... you know. Don't let your dreams be dreams. JU5T D0 1T (I don't know anything about trademarks, so i wrote the phrase that way cause i don't want that ancient-greek sneakers-maker goddess to get mad at me).