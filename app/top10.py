
'''
    ----------------------------------------------------------------------
    Name: 
        Nicholas Voran
    FSUID: 
        NJV11C
    Class: 
        CIS4930 - Python Programming
    Assignment: Group Project - Game Review Compiler
        
    ---------------------------------------------------------------------- 
''' 
import requests
import re

def get_platform(_input):
    '''
    ----------------------------------------------------------------------
    Prompt user for game title to use.
    ---------------------------------------------------------------------- 
    '''
    
    platform = []
    platform.append(('Playstation 4', 'ps4'))
    platform.append(('Xbox One', 'xboxone'))
    platform.append(('Switch', 'switch'))
    platform.append(('PC', 'pc'))
    platform.append(('Wii U', 'wii-u'))
    platform.append(('3DS', '3ds'))
    platform.append(('PS Vita', 'vita'))
    platform.append(('iOS', 'ios'))

    output = 'all'
    for item in platform:
        if _input == item[0]:
            output = item[1]
    return output

def get_timeframe(_input):
    '''
    ----------------------------------------------------------------------
    Prompt user for timeframe
    ---------------------------------------------------------------------- 
    '''

    timeFrames = []
    timeFrames.append(('All Time','all'))
    timeFrames.append(('Last 90 Days','90day'))
    timeFrames.append(('2017','2017'))
    timeFrames.append(('2016','2016'))
    timeFrames.append(('2015','2015'))
    timeFrames.append(('2014','2014'))
    timeFrames.append(('2013','2013'))
    timeFrames.append(('2012','2012'))
    timeFrames.append(('2011','2011'))
    timeFrames.append(('2010','2010'))
    timeFrames.append(('2009','2009'))
    timeFrames.append(('2008','2008'))
    timeFrames.append(('2007','2007'))
    timeFrames.append(('2006','2006'))
    timeFrames.append(('2005','2005'))
    timeFrames.append(('2004','2004'))
    timeFrames.append(('2003','2003'))
    timeFrames.append(('2002','2002'))
    timeFrames.append(('2001','2001'))
    timeFrames.append(('2000','2000'))
    timeFrames.append(('1999','1999'))
    timeFrames.append(('1998','1998'))
    timeFrames.append(('1997','1997'))
    timeFrames.append(('1996','1996'))
    timeFrames.append(('1995','1995'))

    output = ('All Time','all')
    for item in timeFrames:
        if _input == item[0]:
            output = item
    return output

def get_top10(platform, timeFrame):
    '''
    ----------------------------------------------------------------------
    
    ---------------------------------------------------------------------- 
    ''' 
    _platform = get_platform(platform)
    _timeFrame = get_timeframe(timeFrame)

    baseURL = 'http://www.metacritic.com/browse/games/score/metascore/'
    if _timeFrame[0] == 'All Time':
        timeType = _timeFrame[1]
    elif _timeFrame[0] == 'Last 90 Days':
        timeType = _timeFrame[1]
    else:
        timeType = 'year'
    
    url = baseURL + timeType + '/' + str(_platform) + '/filtered'
    if timeType == 'year':
        url = url + '?sort=desc&year_selected=' + _timeFrame[1]

    data = [] 
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}
    page = requests.get(url, headers=headers)
    
    data = re.findall(r'<div class="product_item row_num">\s*(\d*).\s*</div>\s*<div class="product_item product_score">\s*<div class="metascore_w small game positive">(\d*)</div>\s*</div>\s*<div class="product_item product_title">\s*<a href=".*?">\s*(.*?)\s*(.*?)\s*</a>\s*</div>\s*<div class="product_item product_userscore_txt">\s*<span class="label">User:</span>\s*<span class="data textscore textscore_.*?">(.*?)</span>\s*</div>', page.text)
    top10 = []
    for i in range(0,10):
        top10.append(data[i])

    
    return top10