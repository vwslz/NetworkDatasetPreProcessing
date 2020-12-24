import download_dataset as dd
import const as ct
import utils as ut
import pickle

    # ------------------------------
    # Test Case
    # ------------------------------
    # @Input
    # ------------------------------
    # @Output
    # ------------------------------

def testForMapKey():
    dict_ip = ut.pickleToFile("D:\\Cache\\dict_ip.pkl")

    dir_from = "D:\\dataset_monthly_weekday_ip\\"
    dir_to = "D:\\dataset_monthly_weekday_with_loop\\"

    res = dd.mapKey(dict_ip, dir_from, dir_to)
    print(res)
    return res

def testForReadWarts():
    dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    dir_from = "D:\\dataset_monthly_weekday_raw\\"
    dir_to = "D:\\dataset_monthly_weekday_ip\\"

    res = dd.readWarts(dates, dir_from, dir_to)
    print(len(res))
    return res
    # ------------------------------
    # Test Case 1
    # ------------------------------
    # @Input
    # datesWithActions = ut.pickleToFile("D:\\Cache\\dic_dates_monthly_weekday_62.pkl")
    # dir_from = "D:\\prob_weekday_raw\\"
    # dd.getActionsForDates(datesWithActions, dir_from)
    # ------------------------------
    # @Output
    # {'20180801': 'C', '20180702': 'C', '20180601': 'C', '20180501': 'C', '20180402': 'C', '20180301': 'C', '20180201': 'C', '20180101': 'C', '20171201': 'C', '20171101': 'C', '20171002': 'C', '20170904': 'C', '20170801': 'C', '20170703': 'C', '20170601': 'C', '20170501': 'C', '20170403': 'C', '20170301': 'C', '20170201': 'C', '20170102': 'C', '20161201': 'C', '20161101': 'C', '20161003': 'C', '20160901': 'C', '20160801': 'C', '20160704': 'C', '20160601': 'C', '20160502': 'C', '20160401': 'C', '20160301': 'C', '20160201': 'C', '20160101': 'C', '20151201': 'C', '20151102': 'C', '20151001': 'C', '20150901': 'C', '20150803': 'C', '20150701': 'C', '20150601': 'C', '20150501': 'C', '20150401': 'C', '20150302': 'C', '20150202': 'C', '20150101': 'C', '20141201': 'C', '20141103': 'C', '20141001': 'C', '20140912': 'C', '20140801': 'C', '20140701': 'C', '20140602': 'C', '20140501': 'C', '20140402': 'C', '20140303': 'C', '20140203': 'C', '20140101': 'C', '20131202': 'C', '20131101': 'C', '20131001': 'C', '20130902': 'C', '20130801': 'C', '20130701': 'C'}
    # ------------------------------


def testForUnzip():
    # dict_dates = ut.pickleToFile("D:\\Cache\\dic_dates_monthly_weekday_62_updated.pkl")
    # dates = sorted(dict_dates.keys())
    # ut.fileToPickle("D:\\Cache\\dates.pkl", dates)

    dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    dir_from = "D:\\prob_monthly_weekday\\"
    dir_to = "D:\\dataset_monthly_weekday_raw\\"
    res = dd.unzip(dates, dir_from, dir_to)
    print(res)

def testForGetActionsForDates():
    datesWithActions = ut.pickleToFile("D:\\Cache\\dic_dates_monthly_weekday_62.pkl")
    dir_from = "D:\\prob_weekday_raw\\"

    res = dd.getActionsForDates(datesWithActions, dir_from)
    print(res)
    return res
    # ------------------------------
    # Test Case 1
    # ------------------------------
    # @Input
    # datesWithActions = ut.pickleToFile("D:\\Cache\\dic_dates_monthly_weekday_62.pkl")
    # dir_from = "D:\\prob_weekday_raw\\"
    # dd.getActionsForDates(datesWithActions, dir_from)
    # ------------------------------
    # @Output
    # {'20180801': 'C', '20180702': 'C', '20180601': 'C', '20180501': 'C', '20180402': 'C', '20180301': 'C', '20180201': 'C', '20180101': 'C', '20171201': 'C', '20171101': 'C', '20171002': 'C', '20170904': 'C', '20170801': 'C', '20170703': 'C', '20170601': 'C', '20170501': 'C', '20170403': 'C', '20170301': 'C', '20170201': 'C', '20170102': 'C', '20161201': 'C', '20161101': 'C', '20161003': 'C', '20160901': 'C', '20160801': 'C', '20160704': 'C', '20160601': 'C', '20160502': 'C', '20160401': 'C', '20160301': 'C', '20160201': 'C', '20160101': 'C', '20151201': 'C', '20151102': 'C', '20151001': 'C', '20150901': 'C', '20150803': 'C', '20150701': 'C', '20150601': 'C', '20150501': 'C', '20150401': 'C', '20150302': 'C', '20150202': 'C', '20150101': 'C', '20141201': 'C', '20141103': 'C', '20141001': 'C', '20140912': 'C', '20140801': 'C', '20140701': 'C', '20140602': 'C', '20140501': 'C', '20140402': 'C', '20140303': 'C', '20140203': 'C', '20140101': 'C', '20131202': 'C', '20131101': 'C', '20131001': 'C', '20130902': 'C', '20130801': 'C', '20130701': 'C'}
    # ------------------------------

def testForCollectDatasetByDates():
    dict_dates = ut.pickleToFile("D:\\Cache\\dic_dates_monthly_weekday_62_updated.pkl")
    dir_from = "D:\\prob_weekday_raw\\"
    dir_to = "D:\\prob_monthly_weekday\\"
    res = dd.collectDatasetByDates(dict_dates, dir_from, dir_to)
    print(res)
    # ------------------------------
    # Test Case 1
    # ------------------------------
    # @Input
    # dict_dates = ut.pickleToFile("D:\\Cache\\dic_dates_monthly_weekday_62_updated.pkl")\
    # dir_from = "D:\\prob_weekday_raw\\"
    # dir_to = "D:\\prob_monthly_weekday\\"
    # ------------------------------
    # @Output
    #
    # ------------------------------

def testForDownloadDatasetGetValidDates():
    in_YYYYMMDD = "20180831"
    in_num_dates = 62
    in_date_freq = "monthly"
    in_date_type = "weekday"
    res = dd.getValidDates(in_YYYYMMDD, in_num_dates, in_date_freq, in_date_type)
    # print(sorted(res.keys()))
    return res

    # ------------------------------
    # Test Case 1
    # ------------------------------
    # @Input
    # in_YYYYMMDD = "20180831"
    # in_num_dates = 3
    # in_date_freq = "daily"
    # in_date_type = "none"
    # ------------------------------
    # @Output
    # Current day: 2018-08-31 is day 5
    # First day in daily range: 2018-08-31 is day 5
    # Valid day: 2018-08-31 is day 5
    # Current day: 2018-08-30 is day 4
    # First day in daily range: 2018-08-30 is day 4
    # Valid day: 2018-08-30 is day 4
    # Current day: 2018-08-29 is day 3
    # First day in daily range: 2018-08-29 is day 3
    # Valid day: 2018-08-29 is day 3
    # {'20180831': 'D', '20180830': 'D', '20180829': 'D'}
    # ------------------------------
    # Test Case 2
    # ------------------------------
    # @Input
    # in_YYYYMMDD = "20180731"
    # in_num_dates = 3
    # in_date_freq = "weekly"
    # in_date_type = "weekday"
    # ------------------------------
    # @Output
    # Current day: 2018-07-31 is day 2
    # First day in weekly range: 2018-07-30 is day 1
    # Valid day: 2018-07-30 is day 1
    # Current day: 2018-07-29 is day 7
    # First day in weekly range: 2018-07-23 is day 1
    # Valid day: 2018-07-23 is day 1
    # Current day: 2018-07-22 is day 7
    # First day in weekly range: 2018-07-16 is day 1
    # Valid day: 2018-07-16 is day 1
    # {'20180730': 'D', '20180723': 'D', '20180716': 'D'}
    # ------------------------------
    # Test Case 3
    # ------------------------------
    # @Input
    # in_YYYYMMDD = "20180731"
    # in_num_dates = 3
    # in_date_freq = "weekly"
    # in_date_type = "weekend"
    # ------------------------------
    # @Output
    # Current day: 2018-07-31 is day 2
    # First day in weekly range: 2018-07-30 is day 1
    # Valid day: 2018-08-04 is day 6
    # Current day: 2018-07-29 is day 7
    # First day in weekly range: 2018-07-23 is day 1
    # Valid day: 2018-07-28 is day 6
    # Current day: 2018-07-22 is day 7
    # First day in weekly range: 2018-07-16 is day 1
    # Valid day: 2018-07-21 is day 6
    # Current day: 2018-07-15 is day 7
    # First day in weekly range: 2018-07-09 is day 1
    # Valid day: 2018-07-14 is day 6
    # {'20180728': 'D', '20180721': 'D', '20180714': 'D'}
    # ------------------------------
    # Test Case 4
    # ------------------------------
    # @Input
    # in_YYYYMMDD = "20180630"
    # in_num_dates = 3
    # in_date_freq = "yearly"
    # in_date_type = "weekend"
    # res = download_dataset.getValidDates(in_YYYYMMDD, in_num_dates, in_date_freq, in_date_type)
    # print(res)
    # ------------------------------
    # @Output
    # Current day: 2018-06-30 is day 6
    # First day in yearly range: 2018-01-01 is day 1
    # Valid day: 2018-01-06 is day 6
    # Current day: 2017-12-31 is day 7
    # First day in yearly range: 2017-01-01 is day 7
    # Valid day: 2017-01-01 is day 7
    # Current day: 2016-12-31 is day 6
    # First day in yearly range: 2016-01-01 is day 5
    # Valid day: 2016-01-02 is day 6
    # {'20180106': 'D', '20170101': 'D', '20160102': 'D'}
    # ------------------------------
    # Test Case 5
    # ------------------------------
    # @Input
    # in_YYYYMMDD = "20180524"
    # in_num_dates = 3
    # in_date_freq = "monthly"
    # in_date_type = "none"
    # ------------------------------
    # @Output
    # Current day: 2018-05-24 is day 4
    # First day in monthly range: 2018-05-01 is day 2
    # Valid day: 2018-05-01 is day 2
    # Current day: 2018-04-30 is day 1
    # First day in monthly range: 2018-04-01 is day 7
    # Valid day: 2018-04-01 is day 7
    # Current day: 2018-03-31 is day 6
    # First day in monthly range: 2018-03-01 is day 4
    # Valid day: 2018-03-01 is day 4
    # {'20180501': 'D', '20180401': 'D', '20180301': 'D'}
    # ------------------------------
