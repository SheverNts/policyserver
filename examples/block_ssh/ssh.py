#!/bin/python3
from policyserver.core.http import inputs
from policyserver.core.http import data

def _user_allow():
    return True if inputs.get("user") in data.get("users") else False

def user_allow():
    return  {"status": _user_allow()}

def _user_allow_network():
    return True if inputs.get("network") in data.get("allowed_network") else False

def user_allow_network():
    return  {"status": _user_allow_network()}

def allow():
    return  {"status": True if _user_allow() and _user_allow_network() else False}