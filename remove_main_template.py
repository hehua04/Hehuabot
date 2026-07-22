import pywikibot
from pywikibot import config
config.put_throttle = 10
import re

site = pywikibot.Site()
template = '{{main|中国大陆现行邮政相关规章制度的目录列表}}'

for page in site.allpages(namespace=0, filterredir=False):
    if '变迁史' not in page.title():
        continue

    pywikibot.output(f'Processing: {page.title()}')
    text = page.text

    if template not in text:
        continue

    new_text = text.replace(template, '')
    if new_text == text:
        continue

    page.text = new_text
    page.save(summary='移除 {{main|中国大陆现行邮政相关规章制度的目录列表}}')
