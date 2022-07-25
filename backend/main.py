from gui import Gui

# https://developers.google.com/youtube/v3/getting-started
# https://github.com/youtube/api-samples/tree/master/python
'''
get_all_video_in_channel("https://www.youtube.com/channel/UC6V2iQ7cHA-r9f3iSu3mXoQ")
'''


def main():
    '''info = Feeds()
    print(info.list_feeds())
    info.add_feed("test1")
    info.add_to_feed("test1", "https://www.youtube.com/channel/UC6V2iQ7cHA-r9f3iSu3mXoQ")

    info2 = Feeds()
    print(info2.list_feeds())
    print(info2.list_feed("test1"))
    info2.remove_feed("test1")
    info2.remove_feed("test1")
    print(info2.list_feeds())
    print(info2.list_feed("test1"))'''
    gui = Gui()


if __name__ == '__main__':
    main()
