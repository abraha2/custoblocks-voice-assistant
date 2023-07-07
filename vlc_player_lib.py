#pafy is for YT music stream usage
#import pafy
import vlc
from media_archive import media_archive

instance = vlc.Instance()
mediaplayer = None

action_dict = {"play media": lambda title: (
        media := media_archive(title),
        str(media) if (not (media[0] == "/")) else None,
        media_instance := instance.media_new(media),
        mediaplayer.set_media(media_instance),
        mediaplayer.play()
        )[1],
               "pause media": lambda placeholder: mediaplayer.pause() if mediaplayer else None,
               "resume playback": lambda placeholder: mediaplayer.play() if mediaplayer else None,
               "stop playback": lambda placeholder: mediaplayer.stop() if mediaplayer else None,
               "set volume": lambda volume: mediaplayer.audio_set_volume(int(volume)) if mediaplayer else None,
               }

def vlc_player(action):
    global mediaplayer
    if mediaplayer is None:
        mediaplayer = instance.media_player_new()
    for each_key in action_dict.keys():
        if each_key in action:
            args = action.replace(each_key + " ", "")
            output = action_dict[each_key](args) #if args else None
            if isinstance(output, str):
                return output
            break
    else:
        return f"\033[31mSorry, action '{action}' is not currently supported.\033[0m"

if __name__ == '__main__':
    while True:
        try:
            output = vlc_player(input("Type an action: "))
            if output:
                print(output)
        except Exception as e:
            print(f"\033[31m--ERROR--\n{e}\033[0m")