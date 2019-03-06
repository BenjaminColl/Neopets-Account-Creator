import requests, os, random, sys

class NAC(object):
    def __init__(self):
        self.s = requests.session()
        self.s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9'})
        self.base = 'http://www.neopets.com/'

    def signup(self):
        username = input('Username: ')
        password = input('Password: ')
        email = input('Email: ')
        gender = input('Gender: ')
        day = int(input('Day: '))
        month = int(input('Month: '))
        year = int(input('Year: '))
        country = input('Country: ')
        neoname = input('Pet Name: ')
        selpet = input('Pet: ')
        neogen = input('Pet Gender: ')
        colour = input('Pet Colour: ')
        url = self.base
        self.s.get(url)
        self.s.headers.update({'Referer': url})
        url = self.base + 'login/index.phtml'
        self.s.get(url)
        self.s.headers.update({'Referer': url})
        url = self.base + 'signup/index.phtml'
        self.s.get(url)
        signup_data = {'method':'step1','username':username,'password1':password,'password2':password,'terms':'true','destination':''}
        self.s.headers.update({'Referer': url, 'Content-Type':'application/x-www-form-urlencoded','X-Requested-With':'XMLHttpRequest','Accept':'*/*'})
        url = self.base + 'signup/ajax.phtml'
        r = self.s.post(url, data=signup_data)
        if 'true' in r.text:
            print('Submitted our username and password successfully, onto the next step.')
            url = self.base + 'signup/index.phtml?cookieCheck=1'
            self.s.get(url)
        if 'unavailable' in r.text:
            print('This username is unavailable.')
            sys.exit()
        if 'profane' in r.text:
            print('This username contains a profane word.')
            sys.exit()
        if '6 and 20' in r.text:
            print('This username is too short.')
            sys.exit()
        signup_data2 = {'method':'step2','gender':gender,'month':month,'day':day,'year':year,'country':country,'usState':''}
        url = self.base + 'signup/ajax.phtml'
        r = self.s.post(url, data=signup_data2)
        if 'true' in r.text:
            print('Submitted location information successfully.')
            url = self.base + 'signup/index.phtml?cookieCheck=1'
            self.s.get(url)
        else:
            print('Failed to submit location information.')
            sys.exit()
        signup_data3 = {'method':'step3','email1':email,'email2':email,'optinNeopets':'false','optinEmail':''}
        url = self.base + 'signup/ajax.phtml'
        r = self.s.post(url, data=signup_data3)
        if 'true' in r.text:
            print('Submitted our email successfully')
            url = self.base + 'reg/page4.phtml'
            self.s.get(url)
        else:
            print('Failed to submit our email.')
            sys.exit()
        signup_data4 = {'neopet_name':neoname,'selected_pet':selpet,'selected_pet_colour':colour,'gender':neogen,'terrain':6,'likes':4,'meetothers':6,'pet_stats_set':'2'}
        url = self.base + 'reg/process_page6.phtml'
        r = self.s.post(url, data=signup_data4)
        if 'pet_success' in r.text:
            print('Submitted pet information successfully.')
            url = 'reg/launch.phtml'
            self.s.get(url)
        else:
            print('Failed to submit pet information')
            sys.exit()

if __name__ == '__main__':
    a=NAC()
    a.signup()