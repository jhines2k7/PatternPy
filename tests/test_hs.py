import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tradingpatterns.hard_data import generate_sample_df_with_pattern
from tradingpatterns.tradingpatterns import detect_head_shoulder

def test_detect_head_shoulder():
    # Generate data with head and shoulder pattern
    df_head_shoulder = generate_sample_df_with_pattern("Head and Shoulder")
    df_inv_shoulder = generate_sample_df_with_pattern("Inverse Head and Shoulder")
    df_with_detection = detect_head_shoulder(df_head_shoulder)
    df_with_inv_detection = detect_head_shoulder(df_inv_shoulder)

    # write the value of the dataframe to a csv file
    df_with_detection.to_csv('df_with_detection.csv')
    df_with_inv_detection.to_csv('df_with_inv_detection.csv')

    assert "Head and Shoulder" in df_with_detection['head_shoulder_pattern'].values
    assert "Inverse Head and Shoulder" in df_with_inv_detection['head_shoulder_pattern'].values

test_detect_head_shoulder()
