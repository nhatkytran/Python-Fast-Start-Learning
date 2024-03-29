import argparse
import webbrowser
import requests

r = requests.get(
    'https://nhatkytran-serverless-learning.netlify.app/api/airtable')

data = r.json()


def load_mike_images():
    for item in data:
        image_url = item['image']
        webbrowser.open_new_tab(image_url)


links = {
    'udemy': 'https://www.udemy.com/',
    'youtube': 'https://www.youtube.com/',
    'github': 'https://github.com/nhatkytran',
    'gmail1': 'https://mail.google.com/mail/u/0/#inbox',
    'gmail2': 'https://mail.google.com/mail/u/2/#inbox',
    'gmail3': 'https://mail.google.com/mail/u/3/#inbox',
    'facebook': 'https://www.facebook.com/',
    'facebook_mike': 'https://www.facebook.com/profile.php?id=100018031596666',
    'facebook_mike_avatar': ''
}

site_names = ('u', 'udemy', 'y', 'youtube', 'g',
              'github', 'g1', 'gmail1', 'g2', 'gmail2', 'g3', 'gmail3', 'f', 'facebook', 'fm', 'facebook_mike', 'fma', 'facebook_mike_avatar')


def add_argument_helper(short, long):
    parser.add_argument(f'-{short}', f'--{long}',
                        action='store_const', const=f'{long}')


parser = argparse.ArgumentParser()

for i in range(0, len(site_names), 2):
    add_argument_helper(site_names[i], site_names[i + 1])

args = parser.parse_args()


site_namespace = args.__dict__
site_namespace_keys = site_namespace.keys()

for key in site_namespace_keys:
    if site_namespace[key] == 'facebook_mike_avatar':
        load_mike_images()
    elif site_namespace[key] is not None:
        webbrowser.open_new_tab(links[site_namespace[key]])
