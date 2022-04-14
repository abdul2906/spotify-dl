import sys

class parsed_args:
    link = None
    audio_format = None
    path = None
    version = False

    def __init__(self):
        skip_next_arg = False
        for i, arg in enumerate(sys.argv):
            if skip_next_arg:
                skip_next_arg = False
                continue
            if arg == 'spotify-dl':
                continue
            if 'python' in arg:
                continue
            if arg.startswith('https'):
                self.link = arg
                continue

            if arg == '-f':
                skip_next_arg = True
                self.audio_format = sys.argv[i + 1]
            elif arg == '-o':
                skip_next_arg = True
                self.path = sys.argv[i + 1]
            elif arg == '-v':
                self.version = True
