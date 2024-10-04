# Python + Electron quick and dirty idea app

This is a simple application to keep track of project ideas in a list. The idea behind this implementation is to be used as a scratch pad to quickly jot down project ideas without specifying too much detail. Just 3 tags are allowed per idea and a short description and name. All ideas are stored in a database and retrieved and updated to the frontend.

### Context
I am trying to learn Django and I wanted to see how to hack something like this together without relying on a complete framework.
For this I chose to use a Python backend in combination with Electron using the [Eel](https://github.com/python-eel/Eel) library.
This was especially attractive to me since it makes it quite easy to export as an executable using PyInstaller.

The application can be run in two ways, directly from the terminal
```shell 
python app.py
```
or as the fully built executable found in the `./dist` folder.

### Possible expansions
- Tag management system
- Search through ideas
- Grouping similar ideas based on tags or content