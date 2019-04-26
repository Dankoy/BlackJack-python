# Take argument from clipboard, open browser in google maps and let it find route to the place copied from clipboard

import webbrowser, sys, pyperclip


if len(sys.argv) > 1:
    # Get address from the command line.
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)
