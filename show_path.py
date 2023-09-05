"""Write the function show_path() to print output like this (on Mac/Linux):

   Your PATH contains:
   /usr/local/bin      <----  print PATH environment variable, 
   /usr/sbin                  one directory per line.
   /usr/bin
   /bin
   ~/bin

   How to Program:
   1. use os.getenv(envvar) to get the value of an environment variable
   2. use str.split(sep=char) to split a string
   3. use os.path.pathsep as the separater char to split the string

   Windows - os.path.pathsep returns ";" (semi-colon)
             The Windows PATH variable looks like:
             PATH=C:\Windows\System32;C:\Windows;C:\Programs;etc.

   Linux & MacOS - os.path.pathsep returns ":" (colon)
             and the Linux/MacOS path looks like:
             PATH=/usr/local/bin:/usr/bin:/usr/sbin:/bin:~/bin
"""
import os

def show_path():
    """Print all directories on a user's PATH, one per line.

    Enhancement: if a directory in the PATH does not exist,
    print a warning on the same line, such as "(Not a Directory)".  
    Hint: os.path.isdir(pathname)
    """
    pass

if __name__ == "__main__":
    show_path()

