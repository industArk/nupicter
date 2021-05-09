#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com


try:
    import filehandler
except (ImportError, IOError):
    filehandler = MissingModule("filehandler", urgent=1)
