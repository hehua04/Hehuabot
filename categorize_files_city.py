import pywikibot
from pywikibot import config

config.put_throttle = 5

site = pywikibot.Site()
keywords = ('市邮政管理局关于', '诉处理意见', '邮举告')
municipalities = ('北京', '天津', '上海', '重庆')
max_pages = 0
count = 0

for page in site.allpages(namespace=6, filterredir=False):
    if max_pages and count >= max_pages:
        break

    title = page.title()
    if not any(kw in title for kw in keywords):
        continue

    if any(m in title for m in municipalities):
        cat_title = '省级邮政管理部门的复函'
    else:
        cat_title = '地市级邮政管理部门的复函'
    cat_link = f'[[Category:{cat_title}]]'

    count += 1
    pywikibot.output(f'Processing: {page.title()} -> {cat_title}')

    text = page.text
    if cat_link in text:
        pywikibot.output(f'  Already has category, skipping')
        continue

    text = text.rstrip() + f'\n{cat_link}'
    page.text = text
    page.save(summary=f'bot:添加分类 [[Category:{cat_title}]]')
