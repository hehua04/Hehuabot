import pywikibot
from pywikibot import config

config.put_throttle = 5

site = pywikibot.Site()
cat_title = '省级邮政管理部门的复函'
cat_link = f'[[Category:{cat_title}]]'
include_kw = ('省邮政管理局关于', '区邮政管理局', '邮管信访', '邮信处')
exclude_kw = '市邮政管理局'
max_pages = 0
count = 0

for page in site.allpages(namespace=6, filterredir=False):
    if max_pages and count >= max_pages:
        break

    title = page.title()
    if exclude_kw in title:
        continue
    if not any(kw in title for kw in include_kw):
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
