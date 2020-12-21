import pandas as pd
import numpy as np
import networkx as nx
import os
import csv
import const as ct
import utils as ut

'''
Read dataset and remove the self loop which is that IIP_SRC equals to IP_DST.
@In:
list in_dates: sorted dictionary in_dates_with_action's key
str dir_from: directory to read dataset
str dir_to: directory to save dataset without self loop
@Out: 
boolean: whether success or not
'''
def getRidOfSelfLoop(in_dates, dir_from, dir_to):
    for str_date in in_dates:
        for id_team in range(3):
            filename_from = dir_from + str_date + "_" + str(id_team + 1) + ".pkl"
            filename_to = dir_to + str_date + "_" + str(id_team + 1) + ".pkl"

            ut.printMsgForTest(filename_from)

            if os.path.isfile(filename_from):
                df = pd.read_pickle(filename_from)
                msg = str(len(df))
                df = df[df.IP_SRC != df.IP_DST]
                msg = msg + " -> " + str(len(df))
                df.to_pickle(filename_to)
                print(msg)
    return True

'''
Get node frequencies
@In:
list in_dates: sorted dictionary in_dates_with_action's key
str dir_from: directory to read dataset
str filename_to: file to save the node frequency
@Out: 
dataframe: column node, timestamp, frequency
'''
def getNodeFreq(in_dates, dir_from, filename_to):
    list_of_df = []

    for str_date in in_dates:
        nodes_freq = pd.Series([], name='freq')
        for id_team in range(3):
            filename_from = dir_from + str_date + "_" + str(id_team + 1) + ".pkl"

            ut.printMsgForTest(filename_from)

            if os.path.isfile(filename_from):
                df_temp = pd.read_pickle(filename_from)
                nodes_freq = nodes_freq.add(df_temp.IP_SRC.value_counts(), fill_value=0)
                nodes_freq = nodes_freq.add(df_temp.IP_DST.value_counts(), fill_value=0)

        df = pd.DataFrame({'node':nodes_freq.index, 'freq':nodes_freq.values})
        df['timestamp'] = str_date
        list_of_df.append(df)

    res = pd.concat(list_of_df, ignore_index=True)
    res.to_pickle(filename_to)
    return res

'''
Get node set with filters for min frequency and top percentage
@In:
list in_dates: sorted dictionary in_dates_with_action's key
int in_min_month: minimum frequency to exist in month for a node
int in_min_freq: minimum frequency to exist for a node
int in_proportion: the proportion to select top nodes, 0.05 means 5 percentage
str dir_from: directory to read dataset
str dir_to: directory to save the filtered node set
@Out: 
serie: nodes
'''
def getNodeSet(in_min_freq, in_min_month, in_proportion, dir_from, dir_to):
    filename_to = os.path.join(dir_to, "nodeset_" + str(in_proportion) + ".pkl")

    nodes_freq = pd.read_pickle(os.path.join(dir_from, "node_freq.pkl"))
    msg_threshold = "Filter with threshold: " + str(len(nodes_freq))
    nodes_freq = nodes_freq.groupby('node').filter(lambda x: x.freq.sum() > in_min_freq and len(x) > in_min_month)
    msg_threshold = msg_threshold + " -> " + str(len(nodes_freq))
    nodes_freq.to_pickle(os.path.join(dir_to, "nodeset_" + str(in_proportion) + "_filtered.pkl"))
    ut.printMsgForTest(msg_threshold)

    nodes_top = nodes_freq.groupby(['node'])['freq'].agg('sum') # Return a serie
    nodes_top = nodes_top.sort_values(ascending=False)
    msg_proportion = "Filter with percentage: " + str(len(nodes_top))
    nodes_top = nodes_top[:int(in_proportion * (len(nodes_top)))]
    msg_proportion = msg_proportion + str(len(msg_proportion))
    nodes_top.to_pickle(filename_to)

    ut.printMsgForTest(msg_proportion)

    return nodes_top

'''
Get subset according to given node set
@In:
list in_dates: sorted dictionary in_dates_with_action's key
list in_nodes: given node set which is series of nodes with frequencies
str dir_from: directory to read original dataset
str dir_to: directory to save the subset
@Out: 
boolean: whether success or not
'''
def getSubsetByNodes(in_dates, in_nodes, dir_from, dir_to):
    for str_date in in_dates:
        list_of_df = []
        filename_to = dir_to + str_date + ".pkl"
        for id_team in range(3):
            filename_from = dir_from + str_date + "_" + str(id_team + 1) + ".pkl"
            if os.path.isfile(filename_from):
                df = pd.read_pickle(filename_from)
                df['IP_SRC'] = pd.to_numeric(df.IP_SRC)
                df['IP_DST'] = pd.to_numeric(df.IP_DST)
                df = df.loc[df['IP_SRC'].isin(in_nodes) & df['IP_DST'].isin(in_nodes)]
                list_of_df.append(df)
        res = pd.concat(list_of_df, ignore_index=True)
        res.to_pickle(filename_to)
        ut.printMsgForTest(filename_to + ": " + str(len(res)))
    return True

'''
Get plot of edge distribution to determine the lower and upper threshold for given year
@In:
list in_dates: sorted dates
int in_year: the year to plot
str dir_from: directory to read original dataset
str dir_to: directory to save the plot
@Out:
int list: [lower threshold, upper threshold]
'''
def getThresholdRTTForYear(in_dates, in_year, dir_from, dir_to):
    filename_to = os.path.join(dir_to, "rtts_" + in_year + ".pkl")
    # list_of_rtt = []
    #
    # for str_date in in_dates:
    #     if str_date[0:4] == in_year:
    #         df = pd.read_pickle(os.path.join(dir_from, str_date)+".pkl")
    #         list_of_rtt.append(df.RTT)
    #         ut.printMsgForTest(str_date)
    #
    # rtts = pd.concat(list_of_rtt)
    # # log 10
    # rtts.to_pickle(filename_to)

    rtts = pd.read_pickle(filename_to)

    ut.drawHist(np.log10(rtts), "RTT(log 10)", "Frequency", "RTT distribution", os.path. join(dir_to, "distribution_rtt_" + in_year + ".pdf"))
    return True

'''
Get plot of monthly edge frequency distribution to determine the lower and upper threshold
@In:
list in_dates: sorted dates
int in_year: the year to plot
str dir_from: directory to read original dataset
str dir_to: directory to save the plot
@Out:
int: threshold of edge frequency
'''
def getThresholdRTTFreqOfYear(in_dates, in_year, dir_from, dir_to):
    filename_to = os.path.join(dir_to, "rtts_freq_" + in_year + ".pkl")
    edges_freq_of_month = []
    for str_date in in_dates:
        if str_date[0:4] == in_year:
            df = pd.read_pickle(os.path.join(dir_from, str_date)+".pkl")
            edges_freq_of_month.append(df.groupby(by=['IP_SRC', 'IP_DST']).size())
            ut.printMsgForTest(str_date)

    ut.fileToPickle(filename_to, edges_freq_of_month)

    # edges_freq_of_month = ut.pickleToFile(filename_to)

    ut.drawHists(edges_freq_of_month, 'Frequency of edge', 'Frequency of edge frequency', "Edge Frequency distribution", os.path. join(dir_to, "distribution_edge_frequency_" + in_year + ".pdf"))

    return True

'''
Get subset with median of filtered edges
@In:
list in_dates: sorted dictionary in_dates_with_action's key
str dir_from: directory to read subset with nodes filtered
str dir_to: directory to save the subset with median of filtered edges
threshhold_timeout_lower, threshhold_timeout_upper, threshhold_edge_freq
@Out: 
boolean: whether success or not
'''
def getMedianWithinThreshhold(in_dates, dir_from, dir_to, threshhold_timeout_lower, threshhold_timeout_upper, threshhold_edge_freq):
    for str_date in in_dates:
        filename_from = os.path.join(dir_from, str_date + ".pkl")
        filename_to = os.path.join(dir_to, str_date + ".pkl")
        if os.path.isfile(filename_from) and not os.path.isfile(filename_to):
            msg = ""
            df_ori = pd.read_pickle(filename_from)

            msg = msg + str(len(df_ori)) + " -> "
            df_ordered = df_ori[['RTT']].copy()
            df_ordered['IP_SRC'] = df_ori[['IP_SRC', 'IP_DST']].min(axis=1)
            df_ordered['IP_DST'] = df_ori[['IP_SRC', 'IP_DST']].max(axis=1)

            df_ordered['size'] = df_ordered.groupby(['IP_SRC', 'IP_DST']).transform(np.size)
            df_ordered = df_ordered[(df_ordered['size'] > threshhold_edge_freq) & (df_ordered.RTT > threshhold_timeout_lower) & (df_ordered.RTT < threshhold_timeout_upper)]
            msg = msg + str(len(df_ordered)) + " -> "

            df_ordered_m = df_ordered.groupby(['IP_SRC', 'IP_DST'], as_index=False).median()
            df_ordered_m.drop(columns=['size'])

            df_ordered_m.to_pickle(filename_to)
            msg = msg + str(len(df_ordered_m))

            ut.printMsgForTest(filename_to)
            ut.printMsgForTest(msg)
    return True

'''
Get dataframe of whole subset
@In:
list in_dates: sorted dictionary in_dates_with_action's key
str dir_from: directory to read whole subset
@Out:
dataframe: whole subset
'''
def getWholeDF(in_dates, dir_from):
    list_of_df = []
    for str_date in in_dates:
        filename_from = os.path.join(dir_from, str_date + ".pkl")
        if os.path.isfile(filename_from):
            df_ori = pd.read_pickle(filename_from)
            df = pd.DataFrame()
            df['user_id'] = df_ori['IP_SRC']
            df['item_id'] = df_ori['IP_DST']
            df['timestamp'] = in_dates.index(str_date)
            df['state_label'] = 0
            df['rtt'] = df_ori.RTT
            df['comma_separated_list_of_features'] = df_ori.RTT
            list_of_df.append(df)

            ut.printMsgForTest(str_date)

    return pd.concat(list_of_df, ignore_index=True)

'''
Reindex given dataframe
@In:
list in_df: dataframe to be reindexed
@Out:
boolean: whether success or not
'''
def getReindexedDF(in_df):
    in_df_id_values = in_df[["user_id", "item_id"]].values.ravel()
    dict_id_keys = pd.unique(in_df_id_values)
    dict_id = dict(zip(dict_id_keys, [i for i in range(len(dict_id_keys))]))
    in_df['user_id'] = in_df['user_id'].map(dict_id)
    in_df['item_id'] = in_df['item_id'].map(dict_id)
    return in_df

'''
Get CSV from processed dataste:
@In:
list in_dates: sorted dated
str dir_from: directory to read whole subset
str dir_to: directory to save csv file
in_filename: name of csv file
@Out:
boolean: whether success or not
'''
def getCSV(in_dates, dir_from, dir_to, in_filename):
    df = getWholeDF(in_dates, dir_from)
    df = getReindexedDF(df)
    filename_to = os.path.join(dir_to, in_filename)
    df.to_csv(filename_to, encoding='utf-8', index=False)

'''
Print connectivity of given dataset
@In:
filename_from: the file of given dataset
@Out:
print the connectivity.
'''
def checkConnectivity(filename_from):
    df = pd.read_csv(filename_from)
    gs = ut.get_G(df)
    for i in range(int(df.ts.max() + 1)):
        l_g = [len(c) for c in sorted(nx.connected_components(gs[i]), key=len, reverse=True)]
        print("--- " + str(i) + " ---")
        s = sum(l_g)

        for l in l_g:
            print(str(l) + ":\t" + "{:.2f}".format(l/s*100) + "%")

    return True
