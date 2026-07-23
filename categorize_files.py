import pywikibot
from pywikibot import config

config.put_throttle = 5

site = pywikibot.Site()
cat_title = '国家邮政局的复函'
cat_link = f'[[Category:{cat_title}]]'
keywords = ('国家邮政局', '国邮信复', '2026年第')
max_pages = 0
count = 0

for page in site.allpages(namespace=6, filterredir=False):
    if max_pages and count >= max_pages:
        break
    if not any(kw in page.title() for kw in keywords):
        continue

    count += 1
    pywikibot.output(f'Processing: {page.title()}')

    text = page.text
    if cat_link in text:
        pywikibot.output(f'  Already has category, skipping')
        continue

    text = text.rstrip() + f'\n{cat_link}'
    page.text = text
    page.save(summary=f'bot:添加分类 [[Category:{cat_title}]]')
