import argparse
import webbrowser

links = {
    'udemy': 'https://www.udemy.com/',
    'youtube': 'https://www.youtube.com/',
    'github': 'https://github.com/nhatkytran',
    'gmail1': 'https://mail.google.com/mail/u/0/#inbox',
    'gmail2': 'https://mail.google.com/mail/u/2/#inbox',
    'gmail3': 'https://mail.google.com/mail/u/3/#inbox',
    'facebook': 'https://www.facebook.com/',
    'facebook_mike': 'https://www.facebook.com/profile.php?id=100018031596666'
}

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--udemy', action='store_const', const='udemy')
parser.add_argument('-y', '--youtube', action='store_const', const='youtube')
parser.add_argument('-g', '--github', action='store_const', const='github')
parser.add_argument('-g1', '--gmail1', action='store_const', const='gmail1')
parser.add_argument('-g2', '--gmail2', action='store_const', const='gmail2')
parser.add_argument('-g3', '--gmail3', action='store_const', const='gmail3')
parser.add_argument('-f', '--facebook', action='store_const', const='facebook')
parser.add_argument('-fm', '--facebook_mike',
                    action='store_const', const='facebook_mike')

args = parser.parse_args()

if args.udemy:
    webbrowser.open_new_tab(links[args.udemy])
if args.youtube:
    webbrowser.open_new_tab(links[args.youtube])
if args.github:
    webbrowser.open_new_tab(links[args.github])
if args.gmail1:
    webbrowser.open_new_tab(links[args.gmail1])
if args.gmail2:
    webbrowser.open_new_tab(links[args.gmail2])
if args.gmail3:
    webbrowser.open_new_tab(links[args.gmail3])
if args.facebook:
    webbrowser.open_new_tab(links[args.facebook])
if args.facebook_mike:
    webbrowser.open_new_tab(links[args.facebook_mike])
