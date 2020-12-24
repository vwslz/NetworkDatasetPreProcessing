import UnitTest.test_for_download_dataset as tdd
import UnitTest.test_for_process_dataset as tpd
import UnitTest.test_for_utils as tut
import utils as ut
import time
import pandas as pd


def testForDownloadDataset():
    # --- Checked ---
    # 1. monthly weekday 62 ✓
    # dict_dates = tdd.testForDownloadDatasetGetValidDates()
    # ut.fileToPickle("D:\\Cache\\dic_dates_monthly_weekday_62.pkl", dict_dates)
    # 2. update dict_dates ✓ Note that it becomes all "C" in this case
    # dict_dates = tdd.testForGetActionsForDates()
    # ut.fileToPickle("D:\\Cache\\dic_dates_monthly_weekday_62_updated.pkl", dict_dates)
    # 3. collect dataset ✓ D not checked here
    # tdd.testForCollectDatasetByDates()
    # 4. Unzip
    # tut.testForUnzip() ✓
    # 5. ReadWarts
    # dict_ip = tdd.testForReadWarts()
    # ut.fileToPickle("D:\\Cache\\dict_ip.pkl", dict_ip)
    # --- 47702.79011631012 seconds ---
    # Run time:
    # 6. MapKey
    # tdd.testForMapKey()
    # --- 12858.215857982635 seconds ---

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

def testForProcessDataset():
    # 1. GetRidOfSelfLoop
    # tpd.testForGetRidOfSelfLoop()
    # --- 1556.6258471012115 seconds ---
    # 2. GetNodeFreq
    # tpd.testForGetNodeFreq()
    # --- 966.4730834960938 seconds ---
    # 3. GetNodeSet
    # tpd.testForGetNodeSet()
    # --- 3336.1672472953796 seconds for get node set ---
    # 4. GetSubsetByNodes
    # tpd.testForGetSubsetByNodes()
    # --- 1713.6620967388153 seconds ---
    # 5. GetThreshold
    # tpd.testForGetThresholdRTTForYear()
    # --- 1600.9689016342163 seconds ---
    # tpd.testForGetThresholdRTTFreqOfYear()
    # --- 16.802095890045166 seconds ---
    # 6. GetMedianWithinThreshhold
    # tpd.testForGetMedianWithinThreshhold()
    # --- 2897.753428209853235 seconds ---
    # 7. GetCSV
    # tpd.testForGetCSV()
    # --- 11.078333616256714 seconds ---
    # 8. CheckConnectivity
    # tpd.testForCheckConnectivity()
    # --- 98.04251027107239 seconds ---

    # --- To be checked ---
    TODO = True

if __name__ == "__main__":
    start_time = time.time()

    # testForDownloadDataset()
    testForProcessDataset()

    # testForMethods()

    print("--- %s seconds ---" % (time.time() - start_time))
