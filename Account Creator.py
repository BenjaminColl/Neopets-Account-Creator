import requests, os, random, sys
from random import randint

class NAC(object):
    def __init__(self):
        self.s = requests.session()
        self.s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9'})
        self.base = 'http://www.neopets.com/'

    def signup(self):
        self.username = input('Username: ')
        self.password = input('Password: ')
        self.email = input('Email: ')
        neoname = input('Pet Name: ')
        self.day = randint(1,25)
        self.month = randint(1,12)
        self.year = randint(1910,2000)
        url = self.base
        self.s.get(url)
        self.s.headers.update({'Referer': url})
        url = self.base + 'login/index.phtml'
        self.s.get(url)
        self.s.headers.update({'Referer': url})
        url = self.base + 'signup/index.phtml'
        self.s.get(url)
        signup_data = {'method':'step1','username':self.username,'password1':self.password,'password2':self.password,'terms':'true','destination':''}
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
        gender = ['M', 'F']
        country = ['AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI']
        self.s.headers.update({'Referer': url, 'Content-Type': 'application/x-www-form-urlencoded', 'X-Requested-With': 'XMLHttpRequest','Accept': '*/*'})
        signup_data2 = {'method':'step2','gender':random.choice(gender),'month':self.month,'day':self.day,'year':self.year,'country':random.choice(country),'usState':''}
        url = self.base + 'signup/ajax.phtml'
        r = self.s.post(url, data=signup_data2)
        if 'true' in r.text:
            print('Submitted location information successfully.')
            url = self.base + 'signup/index.phtml?cookieCheck=1'
            self.s.get(url)
        else:
            print('Failed to submit location information.')
            sys.exit()
        self.s.headers.update({'Referer': url, 'Content-Type': 'application/x-www-form-urlencoded', 'X-Requested-With': 'XMLHttpRequest','Accept': '*/*'})
        signup_data3 = {'method':'step3','email1':self.email,'email2':self.email,'optinNeopets':'false','optinEmail':''}
        url = self.base + 'signup/ajax.phtml'
        r = self.s.post(url, data=signup_data3)
        if 'true' in r.text:
            print('Submitted our email successfully')
            url = self.base + 'reg/page4.phtml'
            self.s.get(url)
        else:
            print('Failed to submit our email.')
            sys.exit()
        pet_gender = ['male', 'female']
        selpet = ['Quiggle', 'Acara', 'Meerca', 'Pteri', 'JubJub',' Gelert', 'Nimmo', 'Mynci', 'Blumaroo', 'Kau', 'Yurble', 'Gnorbu', 'Uni', 'Flotsam', 'Scorchio', 'Ixi', 'Skeith', 'Vandagyre', 'Buzz', 'Kougra', 'Peophin', 'Chia', 'Xweetok', 'Elephante', 'Bori', 'Usul', 'Wocky', 'Kacheek', 'Eyrie', 'Aisha', 'Ogrin', 'Korbat',' Shoyru', 'Bruce', 'Kyrii', 'Lupe', 'Lenny', 'Moehog']
        colour = ['blue', 'yellow']
        self.s.headers.update({'Referer': 'http://www.neopets.com/signup/index.phtml?cookieCheck=1','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'})
        signup_data4 = {'neopet_name':neoname,'selected_pet':random.choice(selpet),'selected_pet_colour':random.choice(colour),'gender':random.choice(pet_gender),'terrain':6,'likes':4,'meetothers':6,'pet_stats_set':'2'}
        url = self.base + 'reg/process_page6.phtml'
        r = self.s.post(url, data=signup_data4)
        if 'pet_success' in r.text:
            print('Submitted pet information successfully.')
            url = self.base + 'reg/launch.phtml'
            self.s.get(url)
        else:
            print('Failed to submit pet information')
            sys.exit()

    def savedata(self):
        f = open(os.path.join('Accounts', 'Output.txt'), 'a')
        f.write(self.username + ':' + self.password + ':' + self.email + ':' + str(self.month) + '/' + str(self.day) + '/' + str(self.year) + '\n')
        f.close()
        print('Saved account information to: Accounts\\Output.txt')

    def dosignup(self):
        self.signup()
        self.savedata()

if __name__ == '__main__':
    a=NAC()
    a.dosignup()
    input()
