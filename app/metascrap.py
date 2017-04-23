'''
Does not work on rated games that have not been released yet
'''
from __future__ import print_function
from lxml import html
import requests

#checks if xpath is valid
def pcheck(p):
    ''' checks if xpath exists '''
    if p:
        return (p[0].text).strip()
    else: 
        return 'N/A'
#input meta('xbox-one', 'mass-effect-andromeda')
def meta(system, gname):
    '''
    Input: system (ex. switch, xbox-one, playstation-4), gname (ex. horizon-zero-dawn)
    Action: crawls and scrapes metacritic.com game reviews
    Returns: dictionary (None on FAIL)
        ({game: str}, {release_date: str}, {metascore: str}, 
         {numcritics: str}, {User_Score: str}, {numratings: str})
    '''
    keys = ("name", "date", "metascore", "numcritics", "userscore", "numratings")
    url = "http://www.metacritic.com/game/"
    #request headers: copied User-Agent of the GET request (network tab of developer tools in browser)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}
    system = system.lower().replace(' ', '-')
    gname = gname.lower().replace(' ', '-').replace(':', '')
    opsys = system
    game = gname
    game = (game.lower()).replace(' ', '-')
    page = requests.get(url+opsys+"/"+game, headers=headers)
    if page.status_code == 200:
        tree = html.fromstring(page.content)
        #xpath for game cover in jpg format
        #//*[@id="main"]/div/div[3]/div/div/div[1]/div/img
        path = tree.xpath('//div/div[1]/h1/a/span')
        game = pcheck(path)
        path = tree.xpath('//div/div[1]/div[2]/ul/li[2]/span[2]')
        date = pcheck(path)
        path = tree.xpath('//div/div/a/div/span')
        m_score = pcheck(path)
        path = tree.xpath('//div[3]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/p/span[2]/a/span')
        critics = pcheck(path)
        path = tree.xpath('//div[3]/div/div/div[2]/div[1]/div[2]/div[1]/div/a/div')
        u_score = pcheck(path)
        path = tree.xpath('//div[3]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/p/span[2]/a')
        num_ratings = pcheck(path)
        return dict(zip(keys, (game, date, m_score, critics, u_score, (num_ratings.split())[0])))
    else:
        return None
