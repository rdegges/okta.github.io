"""
This script transform jekyll blog posts in markdown to hugo specific
It's specific to Okta blog

Unfortunately all available tools doesn't work with images
https://gohugo.io/commands/hugo_import_jekyll/#hugo-import-jekyll

TODO:
- may be create PR for hugo-import-jekyll
"""

import argparse
import logging

import os

import re
from time import strptime, time, strftime

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

JEKYLL_FILENAME = re.compile(r'(\d+-\d+-\d+)-(.+)\..*')

# {% img blog/ultimate-pwa-guide/hnpwa.png alt:"Hacker News PWA" width:"800" %}{: .center-image }
IMG_TAG = re.compile(r'{% img ([\w/\-.]+) (.*) %}(.*)')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", help="dir with jekyll blog posts",
                        default='_source/_posts/')
    parser.add_argument("--output", help="dir with hugo blog posts",
                        default='hugo/content/blog')
    args = parser.parse_args()
    if args.target:
        if not os.path.exists(args.target):
            log.error('Please use correct folder')
            raise SystemExit
        for file in os.listdir(args.target):
            if file.endswith(".md"):
                f = os.path.join(args.target, file)
                m = re.match(JEKYLL_FILENAME, file)
                file_date = strptime(m.group(1), "%Y-%m-%d")
                new_file = '{}.md'.format(m.group(2))
                new_file_path = os.path.join(args.output, new_file)
                with open(f) as orig, open(new_file_path, 'w') as new:
                    data = orig.read()
                    data = re.sub(
                        r'author: ([\w\-]+)',
                        r'author: \1\ndate: ' + strftime('%Y-%m-%dT%H:%M:%SZ',
                                                         file_date),
                        data)
                    new_lines = []
                    for line in data.splitlines():
                        if line.startswith('{% img'):
                            m = re.match(IMG_TAG, line)
                            center_img = ''
                            if m.group(3):
                                center_img = ' class="center-image"'
                            new_line = '<img src="/img/{}" {}{}>'.format(
                                m.group(1), m.group(2).replace(':', '='),
                            center_img)
                            new_lines.append(new_line)
                        else:
                            new_lines.append(line)
                    new.write('\n'.join(new_lines))

if __name__ == '__main__':
    main()
