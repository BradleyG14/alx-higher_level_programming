#!/usr/bin/bash
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_lisy[idx]
    return my_list
