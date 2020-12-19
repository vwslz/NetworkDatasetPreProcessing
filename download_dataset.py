import utils as ut
import os

'''
Get the validates date before (including) given date.
@Note: could be less than number of requested.
@In:
str in_YYYYMMDD: the last date
int in_num_dates: number of required dates
int in_date_freq: frequency of required dates, daily/monthly/yearly
int in_date_type: type of required dates, none/weekday/weekend
@Out:
dictionary {date, action}: 
    date: YYYYMMDD
    action: "D" - Download, "C" - Copy
'''
def getValidDates(in_YYYYMMDD, in_num_dates, in_date_freq, in_date_type):
    res = {}

    date = ut.getDateFromYYYYMMDD(in_YYYYMMDD)

    while (in_num_dates > 0):
        validDate = ut.getValidateDate(date, in_date_freq, in_date_type)

        if not validDate is None:
            if validDate < ut.firstValidateDate():
                print("Required dates out of valid range.")
                break

            if validDate <= date:
                res[ut.getYYYYMMDDFromDate(validDate)] = "D"
                in_num_dates = in_num_dates - 1

        date = ut.getPreviousDate(date, in_date_freq)

    return res

'''
Check if a date is downloaded. Change action from D to C if True.
@In:
dict in_dates_with_action {date, action}: diction with keys of required dates and value of action.
str in_dir_downloaded: local address of downloaded dates. 
'''
def getActionsForDates(in_dates_with_action, in_dir_downloaded):
    res = {}
    for str_date in in_dates_with_action:
        dir_downloaded_date = ut.getDirForCycle(str_date, ut.getDirForYear(str_date, ut.getDirForTeam(in_dir_downloaded)))
        if os.path.isdir(dir_downloaded_date):
            res[str_date] = "C"
        else:
            res[str_date] = "D"
    return res

'''
Collect dataset of given dates and dicide whether to copy or download.
@In:
dict in_dates_with_action {date, action}: diction with keys of required dates and value of action
str dir_from: directory to copy from
str dir_to: directory to copy to
@Out:
boolean indicates whether success or not.
'''
def collectDatasetByDates(in_dates_with_action, dir_from, dir_to):
    res = {}
    for str_date in in_dates_with_action:
        for i_team in range(3):
            dir_downloaded_date = ut.getDirForCycle(str_date, ut.getDirForYear(str_date, ut.getDirForTeam(i_team, dir_from)))
            if res[str_date] == "C":
                ut.copyOfDateIteam(dir_from, dir_to)
            elif res[str_date] == "D":
                ut.downloadOfDateTeam(str_date, i_team, dir_to)
    return res


