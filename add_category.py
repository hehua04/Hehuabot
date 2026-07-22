import re
import pywikibot
from pywikibot import config

config.put_throttle = 5

site = pywikibot.Site()
category_ns = site.namespaces[14]  # 分类 namespace

seen_categories = set()
max_pages = 0  # 试运行数量，改为 0 则不限
count = 0

for page in site.allpages(namespace=0, filterredir=False):
    if max_pages and count >= max_pages:
        break
    if not page.title().startswith('国家邮政局'):
        continue

    cat_title = '国家邮政局的复函'
    cat_page = pywikibot.Page(site, cat_title, ns=category_ns)

    count += 1
    pywikibot.output(f'Processing: {page.title()} -> [[Category:{cat_title}]]')

    # 添加分类到条目
    text = page.text
    cat_link = f'[[Category:{cat_title}]]'
    if cat_link not in text:
        text = text.rstrip() + f'\n{cat_link}'
        page.text = text
        page.save(summary=f'bot:添加分类 [[Category:{cat_title}]]')
    else:
        pywikibot.output(f'  Already has category, skipping')

    # 创建分类页（如果不存在）
    if cat_title not in seen_categories:
        seen_categories.add(cat_title)
        if not cat_page.exists():
            cat_page.text = f'[[Category:复函]]\n{cat_title}。'
            cat_page.save(summary=f'bot:创建分类页 [[Category:{cat_title}]]')
        else:
            pywikibot.output(f'  Category page already exists')
