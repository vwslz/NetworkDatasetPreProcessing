import UnitTest.test_for_download_dataset as tdd
import UnitTest.test_for_utils as tut
import utils as ut

def testForDownloadDataset():
    # --- Checked ---
    dict_dates = tdd.testForDownloadDatasetGetValidDates()
    ut.fileToPickle("D:\\Cache\\dic_dates.pkl", dict_dates)
    # tdd.testForCollectDatasetByDates()

    # --- To be checked ---
    TODO = True

def testForMethods():
    # --- Checked ---
    # id_team = 1
    # str_YYYYMMDD = '20150121'
    # in_url = ct.URL_TO_DOWNLOAD + 'team-' + str(id_team) + '/' + str_YYYYMMDD[0:4] + '/cycle-' + str_YYYYMMDD + '/'
    # tut.testForIsUrlExist(in_url)


    # --- To be checked ---
    TODO = True

if __name__ == "__main__":
    testForDownloadDataset()
    # testForMethods()
