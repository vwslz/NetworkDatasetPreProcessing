import utils as ut
import os
import warts
from warts.traceroute import Traceroute
import pandas as pd

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
def getActionsForDates(in_dates_dict, dir_from):
    res = {}
    for str_date in in_dates_dict:
        if ut.isDirExist(str_date, dir_from):
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
list of string: sorted dates
'''
def collectDatasetByDates(in_dates_dict, dir_from, dir_to):
    for str_date in in_dates_dict:
        for i_team in range(3):
            dir_from_date = ut.getDirForCycle(str_date, ut.getDirForYear(str_date, ut.getDirForTeam(i_team, dir_from)))
            if in_dates_dict[str_date] == "C":
                ut.copyOfDateIteam(str_date, i_team, dir_from_date, dir_to)
            elif in_dates_dict[str_date] == "D":
                ut.downloadOfDateTeam(str_date, i_team, dir_to)
    return sorted(in_dates_dict.keys())

'''
Unzip the raw dataset.
@In:
list dates: sorted dictionary in_dates_with_action's key
str dir_from: directory to unzip from
str dir_to: directory to unzip to
@Out:
boolean indicates whether success or not
'''
def unzip(in_dates, dir_from, dir_to):
    # Create directories
    for str_date in in_dates:
        for i_team in range(3):
            dir_to_date = ut.getDirForCycle(str_date, ut.getDirForYear(str_date, ut.getDirForTeam(i_team, dir_from)))

            if os.path.isdir(dir_to_date):
                dir_to_for_team = ut.getDirForTeam(i_team, dir_to)
                ut.mkdir(dir_to_for_team)
                dir_to_for_year = ut.getDirForYear(str_date, dir_to_for_team)
                ut.mkdir(dir_to_for_year)
                dir_to_for_cycle = ut.getDirForCycle(str_date, dir_to_for_year)
                ut.mkdir(dir_to_for_cycle)

                for filename in os.listdir(dir_to_date):
                    dir_from_upzip = os.path.join(dir_to_date, filename)
                    dir_to_unzip = os.path.join(dir_to_for_cycle, filename)
                    if os.path.isfile(dir_from_upzip) and (str_date in filename):
                        ut.upzipFile(dir_from_upzip, dir_to_unzip)

    return True

'''
Read Warts file and save required data in data of "IP_SRC", "IP_DST", and RTT
@In:
list dates: sorted dictionary in_dates_with_action's key
str dir_from: directory to read dataset
str dir_to: directory to save dataframe
@Out: 
dictionary of ip address to map to indexes.
'''
def readWarts(in_dates, dir_from, dir_to):
    set_ip = set()
    df_columns = ["IP_SRC", "IP_DST", "RTT"]
    for str_date in in_dates:
        for i_team in range(3):
            dir_from_file = dir_from + "\\team-" + str(i_team+1) + "\\" + str_date[0:4] + "\\cycle-" + str_date
            dir_to_file = dir_to + "\\" + str_date + "_" + str(i_team+1) +".pkl"

            df_data = []

            if not os.path.isfile(dir_to_file):
                if os.path.isdir(dir_from_file):
                    for filename in os.listdir(dir_from_file):
                        filename = os.path.join(dir_from_file, filename)
                        with open(filename, 'rb') as f:
                            record = warts.parse_record(f)
                            while record:
                                if isinstance(record, Traceroute):
                                    pre = record.src_address
                                    for hop in record.hops:
                                        df_data.append([pre, str(hop.address), hop.rtt])
                                record = warts.parse_record(f)
                if len(df_data) > 0:
                    df = pd.DataFrame(df_data, columns = df_columns)
                    df.to_pickle(dir_to_file)

                    set_ip_sub = set(df.IP_SRC.unique()).union(df.IP_DST.unique())
                    set_ip = set_ip.union(set_ip_sub)
                    ut.printMsgForTest(dir_from_file + " -> " + dir_to_file + ": " + str(len(df_data)))

    indexes = [i for i in range(len(set_ip))]
    dict_ip = dict(zip(set_ip, indexes))

    return dict_ip

'''
Map IP address to unique int ID.
@In:
str dir_from: directory to read dataset
str dir_to: directory to save dataframe
@Out: 
boolean indicates whether success or not
'''
def mapKey(dict_ip, dir_from, dir_to):
    for filename in os.listdir(dir_from):
        filename_to = os.path.join(dir_to, filename)
        filename_from = os.path.join(dir_from, filename)
        df = pd.read_pickle(filename_from)
        df['IP_SRC'] = df['IP_SRC'].map(dict_ip)
        df['IP_DST'] = df['IP_DST'].map(dict_ip)
        if df['IP_SRC'].isnull().sum() > 0:
            print("NAN exist for SRC")
        if df['IP_DST'].isnull().sum() > 0:
            print("NAN exist for DST")
        df.to_pickle(filename_to)
    return True
