from configparser import ConfigParser


# read basic info provide on the config.ini file
def read_configuration(category, key):
    config = ConfigParser()
    config.read("./config.ini")
    return config.get(category, key)


# read settings option provide on the config.ini file
def read_headless_mode(settings, key):
    config = ConfigParser()
    config.read("./config.ini")
    return config.getboolean(settings, key)

