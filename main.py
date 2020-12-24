import download_dataset as dd
import process_dataset as pd
import utils as ut
import time

if __name__ == "__main__":
    in_YYYYMMDD = "20180831"
    in_num_dates = 60
    in_date_freq = "daily"
    in_date_type = "weekday"
    name_dataset = in_date_freq + "_" + in_date_type + "_"+ str(in_num_dates)
    dir_root = "D:\\" + name_dataset + "\\"
    ut.mkdir(dir_root)
    dirs={}
    # Change prob_weekday_raw to prob_raw, so all datasets can check from here.
    dirs["prob_raw"] = "D:\\prob_raw\\"
    dirs["prob"] = dir_root + "prob_" + name_dataset + "\\"
    dirs["dataset_raw"] = dir_root + "dataset_" + name_dataset + "_raw\\"
    dirs["dataset_ip"] = dir_root + "dataset_" + name_dataset + "_ip\\"
    dirs["dataset_with_loop"] = dir_root + "dataset_" + name_dataset + "_with_loop\\"
    dirs["dataset"] = dir_root + "dataset_" + name_dataset + "\\"
    dirs["dataset_sub"] = dir_root + "dataset_" + name_dataset + "_sub\\"
    dirs["cache"] = dir_root + "cache_" + name_dataset + "\\"
    dirs["dataset_median_undirected_threshold"] = dir_root + "dataset_" + name_dataset + "_median_undirected_threshold\\"
    for key in dirs:
        ut.mkdir(dirs[key])

    filename_csv = "network_monthly_weekday.csv"
    threshold_timeout_lower = 200  # 10^2.3
    threshold_timeout_upper = 200000  # 10^5.3
    threshold_edge_freq = 30  # 10^1.5

    start_time = time.time()
    dict_date = dd.getValidDates(in_YYYYMMDD=in_YYYYMMDD, in_num_dates=in_num_dates, in_date_freq=in_date_freq, in_date_type=in_date_type)
    dict_dates = dd.getActionsForDates(in_dates_dict=dict_date, dir_from= dirs["prob_raw"])
    dates = dd.collectDatasetByDates(in_dates_dict=dict_date , dir_from=dirs["prob_raw"], dir_to=dirs["prob"])
    dd.unzip(in_dates=dates, dir_from=dirs["prob"], dir_to=dirs["dataset_raw"])    
    dict_ip = dd.readWarts(in_dates=dates, dir_from="dataset_raw", dir_to=dirs["dataset_ip"])
    dd.mapKey(dict_ip=dict_ip, dir_from=dirs["dataset_ip"], dir_to=dirs["dataset_with_loop"])
    print("--- %s seconds for Module: download dataset---" % (time.time() - start_time))

    start_time = time.time()
    pd.getRidOfSelfLoop(in_dates=dates, dir_from=dirs["dataset_with_loop"], dir_to=dirs["dataset"])
    node_freq = pd.getNodeFreq(in_dates=dates, dir_from=dirs["dataset"], dir_to=dirs["cache"])
    nodes_top = pd.getNodeSet(in_min_freq=2, in_min_month=2, in_proportion=0.005, dir_from=dirs["cache"], dir_to=dirs["cache"])
    pd.getSubsetByNodes(in_dates=dates, in_nodes=nodes_top, dir_from=dirs["dataset"], dir_to=dirs["dataset_sub"])
    pd.getThresholdRTTForYear(in_dates=dates, in_year=2014, dir_from=dirs["dataset_sub"], dir_to=dirs["cache"])
    pd.getThresholdRTTFreqOfYear(in_dates=dates, in_year=2014, dir_from=dirs["dataset_sub"], dir_to=dirs["cache"])
    pd.getMedianWithinThreshhold(in_dates=dates, dir_from=dirs["dataset_sub"], dir_to=dirs["dataset_median_undirected_threshold"], threshold_timeout_lower=threshold_timeout_lower, threshold_timeout_upper=threshold_timeout_upper,  threshold_edge_freq=threshold_edge_freq)
    pd.getCSV(in_dates=dates, dir_from=dirs["dataset_median_undirected_threshold"], dir_to=dirs["cache"], in_filename=filename_csv)
    pd.checkConnectivity(dirs["cache"]+filename_csv)
    
    print("--- %s seconds for Module: process dataset---" % (time.time() - start_time))