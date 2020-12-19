from datetime import datetime, timedelta
import const as ct
import os
from shutil import copytree
import wget
from bs4 import BeautifulSoup
import requests
import pickle

'''
Datetime Manipulation
'''
def getDateFromYYYYMMDD(in_YYYYMMDD):
    res = datetime.strptime(in_YYYYMMDD, '%Y%m%d').date()
    return res

def getYYYYMMDDFromDate(in_date):
    res = datetime.strftime(in_date, '%Y%m%d')
    return res

def firstValidateDate():
    return getDateFromYYYYMMDD(ct.FIRST_VALIDATE_DATE)

def getFirstDateInRange(in_date, in_date_freq):
    if in_date_freq == "daily":
        res = in_date
    elif in_date_freq == "weekly":
        res = in_date - timedelta(days=(in_date.isoweekday()-1))
    elif in_date_freq == "monthly":
        res = in_date.replace(day=1)
    elif in_date_freq == "yearly":
        res = in_date.replace(day=1, month=1)
    else:
        raise ValueError("|-> utils -> getFirstDateInRange: Invalid date frequency.")
    return res

def getPreviousDate(in_date, in_date_freq):
    res = getFirstDateInRange(in_date, in_date_freq)
    res = res - timedelta(days=1)
    return res

def getDateRange(in_date, in_date_freq):
    if in_date_freq == "daily":
        res = 1
    elif in_date_freq == "weekly":
        res = 7
    elif in_date_freq == "monthly":
        res = (in_date.replace(month = in_date.month % 12 +1, day = 1)-timedelta(days=1)).day
    elif in_date_freq == "yearly":
        year_begin = in_date.replace(month = 1, year = 1)
        res = (year_begin.replace(year = (year_begin.year + 1)) - year_begin).days
    else:
        raise ValueError("|-> utils -> getDateRange: Invalid date frequency.")
    return res

def getUrlOfDateTeam(in_date, in_team):
    return ct.URL_TO_DOWNLOAD + 'team-' + str(in_team) + '/' + str(in_date.year) + '/cycle-' + getYYYYMMDDFromDate(in_date) + '/'

def getValidateDate(in_date, in_date_freq, in_date_type):
    printMsgForTest("Current day: "  + msgOfDate(in_date))

    firstDayInRange = getFirstDateInRange(in_date, in_date_freq)

    printMsgForTest("First day in " + in_date_freq + " range: "  + msgOfDate(firstDayInRange))

    dayInRange = firstDayInRange

    for i in range(getDateRange(in_date, in_date_freq)):
        res = dayInRange
        if in_date_type == "none":
            res = dayInRange
        elif in_date_type == "weekday":
            if dayInRange.isoweekday() < 6:
                res = dayInRange
            # else:
            #     res = dayInRange + timedelta(days=((1 + 7 - dayInRange.isoweekday())%7))
        elif in_date_type == "weekend":
            if dayInRange.isoweekday() > 5:
                res = dayInRange
            # else:
            #     res = dayInRange + timedelta(days=((6 + 7 - dayInRange.isoweekday())%7))
        else:
            raise ValueError("|-> utils -> getValidateDate: Invalid date type.")

        printMsgForTest("Valid day: " + msgOfDate(res))

        for i_team in range(ct.NUM_TEAM):
            if (isUrlExist(getUrlOfDateTeam(res, i_team+1))):
                return res

        printMsgForTest("In Valid dURL: " + getUrlOfDateTeam(res, 1))

        dayInRange = dayInRange + timedelta(days=1)

    print("No date availble in this range")
    return None

def printMsgForTest(in_msg):
    MUTE = False
    if not MUTE:
        print(in_msg)

def msgOfDate(in_date):
    return str(in_date) + " is day " + str(in_date.isoweekday())

def getDirForTeam(i_team, dir_parent):
    return dir_parent + "team-" + str(i_team + 1) + "\\"

def getDirForYear(str_date, dir_parent):
    return dir_parent + str_date[0:4] + "\\"

def getDirForCycle(str_date, dir_parent):
    return dir_parent + "\\cycle-" + str_date + "\\"

def mkdir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def copyDirectory(dir_from, dir_to):
    if not os.path.isdir(dir_to):
        copytree(dir_from, dir_to)

def isUrlExist(in_url):
    request = requests.get(in_url)
    if request.status_code == 200:
        return True
    else:
        return False

'''
Download dataset for a specific date with corresponding team id.
@In:
str in_YYYYMMDD: given date
int in_team: 0, 1, 2
str dir_to: the directory to save the dateset
@Out:
boolean: return true after succeed
'''
def downloadOfDateTeam(in_YYYYMMDD, in_team, dir_to):
    res = False
    folder_for_team = 'team-' + str(in_team) + '/'
    url_for_team = ct.URL_TO_DOWNLOAD + folder_for_team
    path_for_team = dir_to + folder_for_team

    page_for_team = requests.get(url_for_team)
    data_for_team = page_for_team.text
    soup_for_team = BeautifulSoup(data_for_team)
    links_for_year = []

    for link in soup_for_team.find_all('a'):
        links_for_year.append(link.get('href'))

    links_for_year = links_for_year[5:]

    if len(links_for_year) > 0:
        if not os.path.exists(path_for_team):
            os.mkdir(path_for_team)

    printMsgForTest("team is: " + str(in_team))

    for folder_for_year in links_for_year:

        if folder_for_year[:-1] != in_YYYYMMDD[0:4]:
            continue

        url_for_year = url_for_team + folder_for_year
        path_for_year = path_for_team + folder_for_year

        page_for_year = requests.get(url_for_year)
        data_for_year = page_for_year.text
        soup_for_year = BeautifulSoup(data_for_year)
        links_for_cycle = []

        for link in soup_for_year.find_all('a'):
            links_for_cycle.append(link.get('href'))

        links_for_cycle = links_for_cycle[5:]

        if len(links_for_cycle) > 0:
            if not os.path.exists(path_for_year):
                os.mkdir(path_for_year)

        for folder_for_cycle in links_for_cycle:
            if folder_for_cycle[-9:-1] != in_YYYYMMDD[0:4]:
                continue
            else:
                printMsgForTest("date is: " + in_YYYYMMDD[0:4])

            url_for_cycle = url_for_year + folder_for_cycle
            path_for_cycle = path_for_year + folder_for_cycle

            page_for_cycle = requests.get(url_for_cycle)
            data_for_cycle = page_for_cycle.text
            soup_for_cycle = BeautifulSoup(data_for_cycle)
            links_for_file = []

            for link in soup_for_cycle.find_all('a'):
                links_for_file.append(link.get('href'))

            links_for_file = links_for_file[5:-1]

            if len(links_for_file) > 0:
                if not os.path.exists(path_for_cycle):
                    os.mkdir(path_for_cycle)

            for file in links_for_file:
                url_for_file = url_for_cycle + file
                if '-us' in file:
                    if not os.path.exists(path_for_cycle + file):
                        filename = wget.download(url_for_file, path_for_cycle)
                    res = True
    return res

'''
Copy dataset for a specific date with corresponding team id.
@In:
str in_YYYYMMDD: given date
int in_team: 0, 1, 2
str dir_to: the directory to save the dateset
@Out:
boolean: return true after succeed
'''
def copyOfDateIteam(in_YYYYMMDD, in_team, dir_from, dir_to):
    dir_to_for_team = getDirForTeam(in_team, dir_to)
    mkdir(dir_to_for_team)
    dir_to_for_year = getDirForYear(in_YYYYMMDD, dir_to_for_team)
    mkdir(dir_to_for_year)
    dir_to_for_cycle = getDirForYear(in_YYYYMMDD, dir_to_for_year)
    copyDirectory(dir_from, dir_to_for_cycle)

'''
File Manipulation
'''
def fileToPickle(filename, obj):
    outfile = open(filename,'wb')
    pickle.dump(obj, outfile)
    outfile.close()

def pickleToFile(filename):
    infile = open(filename,'rb')
    res = pickle.load(infile)
    infile.close()
    return res
