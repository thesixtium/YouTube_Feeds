'''
Feeds:

Store as a .txt file, looks like:
Feed Name 1,channel url 1,channel url 2,channel url 3
Feed Name 2,channel url 1

'''

from youtube_processing import get_channel_name_from_url


class Feeds:
    filename = "feed_information.txt"
    information = {}

    def __init__(self):
        with open(self.filename, "r+") as file:
            for line in file:
                try:
                    line_array = line.split(",")
                    self.information[line_array[0]] = line_array[1:]
                except Exception as e:
                    print("__init__")
                    print(e)
                    print()

    def remove_feed(self, feed_name):
        try:
            del self.information[feed_name]
            self.update_file()
            print(f"Deletion of {feed_name} worked")
        except Exception as e:
            print("remove_feed")
            print(e)
            print(f"Deletion of {feed_name} didn't work")
            print()

    def add_feed(self, feed_name):
        try:
            if feed_name in self.information.keys():
                print(f"{feed_name} already exists")
            else:
                self.information[feed_name] = []
                self.update_file()
                print(f"Adding {feed_name} worked")
        except Exception as e:
            print("add_feed")
            print(e)
            print(f"Adding {feed_name} didn't work")
            print()

    def add_to_feed(self, feed_name, url):
        try:
            if url in self.information[feed_name]:
                print(f"{url} already in {feed_name}")
            else:
                self.information[feed_name].append(url)
                self.update_file()
                print(f"Adding {url} to {feed_name} worked")
        except Exception as e:
            print("add_to_feed")
            print(e)
            print(f"Adding {url} to {feed_name} didn't work")
            print()

    def remove_from_feed(self, feed_name, url):
        try:
            if url not in self.information[feed_name]:
                print(f"{url} not in {feed_name}")
            else:
                self.information[feed_name].remove(url)
                self.update_file()
                print(f"Removing {url} from {feed_name} worked")
        except Exception as e:
            print("remove_from_feed")
            print(e)
            print(f"Removing {url} from {feed_name} didn't work")
            print()

    def list_feeds(self):
        return_array = []
        for key in self.information:
            return_array.append(key)

        return return_array

    def list_feed(self, feed):
        return_array = []
        try:
            for channel in self.information[feed]:
                return_array.append(get_channel_name_from_url(channel))
        except Exception as e:
            print("list_feed")
            print(e)
            print(f"Listing {feed} didn't work")
            print()

        return return_array

    def update_file(self):
        with open(self.filename, "w+") as file:
            for key in self.information:
                file.write(key)
                for channel in self.information[key]:
                    file.write(",")
                    file.write(channel)
