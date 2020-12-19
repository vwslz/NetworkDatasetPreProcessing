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

def testForGetActionsForDates():
    datesWithActions = {}
    dir_downloaded = ct.DIR_DOWNLOADED
    dd.getActionsForDates(datesWithActions, dir_downloaded)


def testForCollectDatasetByDates():
    in_YYYYMMDD = "20180831"
    in_num_dates = 62
    in_date_freq = "monthly"
    in_date_type = "weekday"

    in_dates_with_action = dd.getValidDates(in_YYYYMMDD, in_num_dates, in_date_freq, in_date_type)


    dir_from = ct.DIR_DOWNLOADED
    dir_to = ct.DIR_TO

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
