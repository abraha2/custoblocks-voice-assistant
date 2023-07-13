"""
Welcome to the Media Archive.
This is the library for song entries
each dictionary key is the name of the song,
and the definition is the song's filesystem path.
"""

#defining variables
#this is the filepath dictionary, it contains music filepaths.
filepath_dict = {"": ""}

def media_archive(title):
    if title != "":
        if title in filepath_dict:
            path = filepath_dict[title]
            return path
        else:
                return f"song {title} not known"
    else:
        return "please provide song title"

if __name__ == '__main__':
    while True:
        path = commands_checkA(input("Type here: "))
        print(path)
