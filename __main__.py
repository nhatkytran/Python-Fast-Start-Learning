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
    'facebook_mike': 'https://www.facebook.com/profile.php?id=100018031596666',
    'facebook_mike_avatar': 'https://scontent.fsgn17-1.fna.fbcdn.net/v/t39.30808-1/296869480_1088823018395408_1339029068878044395_n.jpg?stp=dst-jpg_p480x480&_nc_cat=105&ccb=1-7&_nc_sid=7206a8&_nc_ohc=PYjri-4sgIgAX9Q0MYF&_nc_oc=AQm9TJEnt-BMLyz0zUTXTZ39d8YWpr5ZMxcTexhJFK9rnn_WaOlyow5KTuvtKpt0AuljGiQm2Uh_RW6DiHhdul0a&_nc_ht=scontent.fsgn17-1.fna&oh=00_AT-sVQ-yggHksJzYj-6xxv9uHmHOtoqdEAhuJw8qC_vjzw&oe=62EC33C3'
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
    if site_namespace[key] is not None:
        webbrowser.open_new_tab(links[site_namespace[key]])
