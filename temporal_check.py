def temporal_check(conf_list, threshold=0.3):
    persistent = sum(c > threshold for c in conf_list)
    return persistent >= 3  # smoke in 3 frames
