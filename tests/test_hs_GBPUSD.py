import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tradingpatterns.tradingpatterns import detect_head_shoulder

def test_detect_head_shoulder():
    data = pd.read_csv('GBPUSD_5M_7_days.csv')

    data['Date'] = data['Date'].astype('datetime64[s]')
    data = data.set_index('Date')
    
    df_with_detection = detect_head_shoulder(data)

    # write the value of the dataframe to a csv file
    df_with_detection.to_csv('df_with_detection_GBPUSD_3.csv')

    assert "Head and Shoulder" in df_with_detection['head_shoulder_pattern'].values

test_detect_head_shoulder()
