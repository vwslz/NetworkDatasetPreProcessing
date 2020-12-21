import const as ct
import utils as ut

    # ------------------------------
    # Test Case
    # ------------------------------
    # @Input
    # ------------------------------
    # @Output
    # ------------------------------

def testForUnzip():
    # dict_dates = ut.pickleToFile("D:\\Cache\\dic_dates_monthly_weekday_62_updated.pkl")
    # dates = sorted(dict_dates.keys())
    # ut.fileToPickle("D:\\Cache\\dates.pkl", dates)

    dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    dir_from = "D:\\prob_monthly_weekday\\"
    dir_to = "D:\\dataset_monthly_weekday\\"
    res = ut.upzip(dates, dir_from, dir_to)
    print(res)

def testForIsUrlExist():
    id_team = 1
    str_YYYYMMDD = '20150121'
    in_url = ct.URL_TO_DOWNLOAD + 'team-' + str(id_team) + '/' + str_YYYYMMDD[0:4] + '/cycle-' + str_YYYYMMDD + '/'
    print(ut.isUrlExist(in_url))
    # ------------------------------
    # Test Case 1
    # ------------------------------
    # @Input
    # id_team = 1
    # str_YYYYMMDD = '20180819'
    # in_url = ct.DIR_DOWNLOADED + 'team-' + str(id_team) + '/' + str_YYYYMMDD[0:4] + '/cycle-' + str_YYYYMMDD + '/'
    # ------------------------------
    # @Output
    # True
    # ------------------------------
    # Test Case 2
    # ------------------------------
    # @Input
    # id_team = 1
    # str_YYYYMMDD = '20150121'
    # in_url = ct.URL_TO_DOWNLOAD + 'team-' + str(id_team) + '/' + str_YYYYMMDD[0:4] + '/cycle-' + str_YYYYMMDD + '/'
    # ------------------------------
    # @Output
    # False
    # ------------------------------
