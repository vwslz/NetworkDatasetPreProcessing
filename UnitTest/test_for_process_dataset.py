import process_dataset as pd
import const as ct
import utils as ut
import pickle
import time

def testForGetRidOfSelfLoop():
    dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    dir_from = "D:\\dataset_monthly_weekday_with_loop\\"
    dir_to = "D:\\dataset_monthly_weekday\\"

    res = pd.getRidOfSelfLoop(dates, dir_from, dir_to)
    print(res)
    return res

def testForGetNodeFreq():
    dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    dir_from = "D:\\dataset_monthly_weekday\\"
    filename_to = "D:\\Cache\\node_freq.pkl"

    res = pd.getNodeFreq(dates, dir_from, filename_to)
    print(res)
    return res

def testForGetNodeSet():
    dir_from = "D:\\Cache\\"
    dir_to = "D:\\Cache\\"

    res = pd.getNodeSet(2, 2, 0.005, dir_from, dir_to)
    print(res)
    return res

def testForGetSubsetByNodes():
    dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    nodes = ut.pickleToFile("D:\\Cache\\nodeset_0.005.pkl").index
    dir_from = "D:\\dataset_monthly_weekday\\"
    dir_to = "D:\\dataset_monthly_weekday_sub\\"

    res = pd.getSubsetByNodes(dates, nodes, dir_from, dir_to)
    print(res)
    return res

def testForGetThresholdRTTForYear():
    dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    year = "2014"
    dir_from = "D:\\dataset_monthly_weekday_sub\\"
    dir_to = "D:\\Cache\\"
    pd.getThresholdRTTForYear(dates, year, dir_from, dir_to)

    # ------------------------------
    # Test Case 1
    # ------------------------------
    # @Input
    # dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    # year = "2014"
    # dir_from = "D:\\dataset_monthly_weekday_sub\\"
    # dir_to = "D:\\Cache\\"
    # ------------------------------
    # @Output
    # True
    # ------------------------------
    # Test Case 2
    # ------------------------------
    # @Input
    # dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    # year = "2018"
    # dir_from = "D:\\dataset_monthly_weekday_sub\\"
    # dir_to = "D:\\Cache\\"
    # ------------------------------
    # @Output
    # True
    # ------------------------------

def testForGetThresholdRTTFreqOfYear():
    dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    year = "2014"
    dir_from = "D:\\dataset_monthly_weekday_sub\\"
    dir_to = "D:\\Cache\\"
    pd.getThresholdRTTFreqOfYear(dates, year, dir_from, dir_to)

    # ------------------------------
    # Test Case 1
    # ------------------------------
    # @Input
    # dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    # year = "2014"
    # dir_from = "D:\\dataset_monthly_weekday_sub\\"
    # dir_to = "D:\\Cache\\"
    # ------------------------------
    # @Output
    # True
    # ------------------------------

def testForGetMedianWithinThreshhold():
    dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    dir_from = "D:\\dataset_monthly_weekday_sub\\"
    dir_to = "D:\\dataset_monthly_weekday_median_undirected_threshold\\"
    threshhold_timeout_lower = 200    # 10^2.3
    threshhold_timeout_upper = 200000    # 10^5.3
    threshhold_edge_freq = 30       # 10^1.5
    res = pd.getMedianWithinThreshhold(dates, dir_from, dir_to, threshhold_timeout_lower, threshhold_timeout_upper, threshhold_edge_freq)
    print(res)
    return res

def testForGetCSV():
    dates = ut.pickleToFile("D:\\Cache\\dates.pkl")
    dir_from = "D:\\dataset_monthly_weekday_median_undirected_threshold\\"
    dir_to = "D:\\Cache\\"
    filename_to = "network_monthly_weekday.csv"

    res = pd.getCSV(dates, dir_from, dir_to, filename_to)
    print(res)
    return res

def testForCheckConnectivity():
    filename_from = "C:\\Users\\vwslz\\Documents\\GitHub\\tgn_rtt\\data\\ml_network_monthly_weekday.csv"
    res = pd.checkConnectivity(filename_from)
    return res

    # ------------------------------
    # Test Case 1
    # ------------------------------
    # @Input
    # filename_from = "C:\\Users\\vwslz\\Documents\\GitHub\\tgn_rtt\\data\\ml_network_monthly_weekday.csv"
    # ------------------------------
    # @Output
    # --- 0 ---
    # 3087:	100.00%
    # --- 1 ---
    # 3342:	100.00%
    # --- 2 ---
    # 3584:	100.00%
    # --- 3 ---
    # 3879:	100.00%
    # --- 4 ---
    # 3265:	100.00%
    # --- 5 ---
    # 2577:	100.00%
    # --- 6 ---
    # 2550:	100.00%
    # --- 7 ---
    # 3098:	100.00%
    # --- 8 ---
    # 4170:	100.00%
    # --- 9 ---
    # 4566:	100.00%
    # --- 10 ---
    # 4732:	100.00%
    # --- 11 ---
    # 3652:	100.00%
    # --- 12 ---
    # 3794:	100.00%
    # --- 13 ---
    # 4832:	100.00%
    # --- 14 ---
    # 4576:	100.00%
    # --- 15 ---
    # 3566:	100.00%
    # --- 16 ---
    # 4181:	100.00%
    # --- 17 ---
    # 4368:	100.00%
    # --- 18 ---
    # 3837:	100.00%
    # --- 19 ---
    # 3049:	100.00%
    # --- 20 ---
    # 2679:	100.00%
    # --- 21 ---
    # 4530:	100.00%
    # --- 22 ---
    # 3866:	100.00%
    # --- 23 ---
    # 4905:	100.00%
    # --- 24 ---
    # 5419:	100.00%
    # --- 25 ---
    # 4477:	100.00%
    # --- 26 ---
    # 5018:	100.00%
    # --- 27 ---
    # 5571:	100.00%
    # --- 28 ---
    # 5298:	100.00%
    # --- 29 ---
    # 5297:	100.00%
    # --- 30 ---
    # 5340:	100.00%
    # --- 31 ---
    # 5825:	100.00%
    # --- 32 ---
    # 4264:	100.00%
    # --- 33 ---
    # 5354:	100.00%
    # --- 34 ---
    # 4052:	100.00%
    # --- 35 ---
    # 6160:	100.00%
    # --- 36 ---
    # 6032:	99.88%
    # 7:	0.12%
    # --- 37 ---
    # 6226:	100.00%
    # --- 38 ---
    # 6146:	100.00%
    # --- 39 ---
    # 3896:	100.00%
    # --- 40 ---
    # 5947:	100.00%
    # --- 41 ---
    # 6056:	100.00%
    # --- 42 ---
    # 6089:	100.00%
    # --- 43 ---
    # 6182:	100.00%
    # --- 44 ---
    # 6013:	100.00%
    # --- 45 ---
    # 6207:	100.00%
    # --- 46 ---
    # 6013:	100.00%
    # --- 47 ---
    # 5908:	100.00%
    # --- 48 ---
    # 6005:	100.00%
    # --- 49 ---
    # 5362:	100.00%
    # --- 50 ---
    # 4253:	100.00%
    # --- 51 ---
    # 5623:	100.00%
    # --- 52 ---
    # 5001:	100.00%
    # --- 53 ---
    # 5719:	100.00%
    # --- 54 ---
    # 5540:	100.00%
    # --- 55 ---
    # 5465:	100.00%
    # --- 56 ---
    # 5604:	100.00%
    # --- 57 ---
    # 5534:	100.00%
    # --- 58 ---
    # 5168:	100.00%
    # --- 59 ---
    # 5136:	100.00%
    # --- 60 ---
    # 4421:	99.89%
    # 5:	0.11%
    # --- 61 ---
    # 4493:	100.00%
