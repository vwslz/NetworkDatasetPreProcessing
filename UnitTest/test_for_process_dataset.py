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
