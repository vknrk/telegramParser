import asyncio
import os
import random
import string

from TeleParser import TeleParser
from statbot import TGBot

urls_filename = 'urls.txt'
filters_filename = 'filters.txt'
api_id = 1103463
api_hash = '91971674d49ac402c515c2a85957c032'
id_file = 'id_file.txt'
REGISTER_CODE = ''
REGISTER_PHRASE = ''.join(
                random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(25))
def load_filters(filter_file):
    if os.path.isfile(filter_file):
        with open(filter_file, encoding='utf-8') as inf:
            filters = [x.strip() for x in inf.readlines()]
    else:
        with open(filter_file, mode='w', encoding='utf-8') as ouf:
            pass
        filters = []
    return set(filters)


def load_urls(urls_file):
    if os.path.isfile(urls_file):
        with open(urls_file, encoding='utf-8') as inf:
            urls = []
            for x in inf.readlines():
                if x.startswith('t.me/') or x.startswith('t.me/joinchat/'):
                    urls.append(x.strip())
                else:
                    raise ValueError(f'{x} не отформатирована по виду t.me/link или t.me/joinchat/link')
    else:
        with open(urls_file, mode='w', encoding='utf-8') as ouf:
            pass
        urls = []
    return set(urls)


loop = asyncio.new_event_loop()
filters = load_filters(filters_filename)
users = load_urls(urls_filename)
tp = TeleParser(loop, api_id, api_hash, filters, users, id_file,REGISTER_PHRASE)
tp.switch_mode('bot')
TGBot(filters,users,REGISTER_PHRASE).start()
print('here')