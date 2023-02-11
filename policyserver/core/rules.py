import policyserver.config as conf
import os
import sys
import json
import inspect
from policyserver import log


class RuleLoader(object):
    def __init__(self, rules_root):
        sys.path.append(rules_root)
        self.rules_root = rules_root

    def get_rules(self):
        return [
            rule.replace(".py", "")
            for rule in os.listdir(self.rules_root)
            if rule.endswith(".py")
        ]

    def load_rules(self):
        """
        loading modules
        """
        modules = {}
        for x in self.get_rules():
            try:
                modules[x] = __import__(x)
                log.info("Successfully imported")
                log.debug(x)
            except ImportError:
                log.error("Error importing ")
                log.error(x)
        return modules

    def get_rules_func(loaded_rules):
        return inspect.getmembers(loaded_rules, inspect.isfunction)
