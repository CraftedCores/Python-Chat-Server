## Overview

**Project Title**:
Python Chat Server

**Project Description**:
A basic python chat server and client program with a GUI, The server is ran on a local IP and can connect up to 5 clients.

**Project Goals**:
The server (or peer) listens for connections on an ip address (localhost is okay) and a port number you select

The client (or peer) connects to an already waiting server (or peer)

The client (or peer) sends at least one type of request message to the server (or peer)

The server (or peer) processes the request and sends a response back to the client (or peer)

The server (or peer) can handle a client disconnecting allowing another client to connect

## Instructions for Build and Use

Steps to build and/or run the software:

1. Make sure you are running a virtual python environment in Visual Studio
2. once you have the environment properly setup you will need to run instance of the server script and up to 5 of the client script.

Instructions for using the software:

1. Run Server Script
2. Run a chat script
3. A window should pop up for the client where you must enter a username, once that is put in you can chat with any other clients connected.

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Visual Studio
* Socket, threading, Tkinter, Libraries
* Virtual Environment: If you don't have this the Tkinter GUI has issues.

## Useful Websites to Learn More

I found these websites useful in developing this software:

* https://docs.python.org/3/library/socket.html
* https://docs.python.org/3/library/tk.html
* https://stackoverflow.com/questions/13060263/python-tkinter-module-not-showing-output

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Better Interface.
* [ ] Notification sound.
* [ ] Ability to run the server over the internet.
