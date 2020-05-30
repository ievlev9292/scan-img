"""
This module is used for some complementary tasks
such as reporting progress

History:
2020.05.26 created
"""

import time

def report_progress_time_simple(current_iter, tot_iter, start_time, prefix=''):
    """
    Report how much work was done and estimate remaining time
    current_iter is supposed to start from zero
    :param current_iter: current iteration counter value
    :param tot_iter: total number of iterations
    :param start_time: starting time, result of time.time()
    :param prefix: this is written before the main message
    :return: None
    """
    if current_iter != 0:
        done_ratio = current_iter / tot_iter
        elapsed_time = (time.time() - start_time) / 60
        estimated_time_left = elapsed_time * (1 / done_ratio - 1)
        print(prefix + "Done {:.2f} percent ({:d} out of {:d}), elapsed time {:.2f} minutes, estimated time left {:.2f} minutes ...".format(100 * done_ratio, current_iter, tot_iter, elapsed_time, estimated_time_left))
    return None

