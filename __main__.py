import argparse
import webbrowser

links = {
    'udemy': 'https://www.udemy.com/',
    'youtube': 'https://www.youtube.com/',
    'github': 'https://github.com/nhatkytran',
    'facebook': 'https://www.facebook.com/profile.php?id=100018031596666'
}

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--udemy', action='store_const', const='udemy')
parser.add_argument('-y', '--youtube', action='store_const', const='youtube')
parser.add_argument('-g', '--github', action='store_const', const='github')
parser.add_argument('-f', '--facebook', action='store_const', const='facebook')

args = parser.parse_args()

if args.udemy:
    webbrowser.open_new_tab(links[args.udemy])
if args.youtube:
    webbrowser.open_new_tab(links[args.youtube])
if args.facebook:
    webbrowser.open_new_tab(links[args.facebook])
if args.github:
    webbrowser.open_new_tab(links[args.github])
