# Test Guideline:
### Module download_dataset:
1. get valid dates
2. update dict_dates
3. collect dataset
4. Unzip
5. ReadWarts
6. MapKey

### Module process_dataset:
1. get rid of self-loop
2. get node freqency
3. get node set
4. get subset by given node set
5. get plots for t
6. get dataset of median within threshhold
7. get CSV file to feed in model
8. check connectivity
## To run selected method
Uncomment and run **unit_test.py** -> Module -> Step

Note:
- You can uncomment the required module in line 77 and 78.
- The numbered steps for each module is listed in *testForDownloadDataset* and *testForProcessDataset* with description of each method. You can uncomment the required step which is *tdd/tpd*.*()

## To feed the parameters for given function
**UnitTest** folder -> **testfor_download_dataset.py** and **testfor_process_dataset.py** -> *testForSomething()*
