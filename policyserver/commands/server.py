from policyserver.core import http
import policyserver.config as conf
from policyserver.core.rules import RuleLoader
from policyserver.core.data import DataLoader
from policyserver import log


def server(args):
    log.info("loading rules.")
    data = DataLoader(args.rules).load_data()
    log.debug(f"data: {data}")
    rules = RuleLoader(args.rules)
    loaded_rules = rules.load_rules()
    routes = generate_routes(loaded_rules)
    log.info(f"generate_routes: {routes}")
    serve = http.HttpServer(routes, data, loaded_rules)
    serve.run(args.port, args.host)


def generate_routes(rules):
    routes = []
    for module_name, module in rules.items():
        view_function = RuleLoader.get_rules_func(module)
        for func in view_function:
            log.debug(f"func: {func}")
            if func[0].startswith("_"):
                continue
            routes.append(
                {
                    "rule": f"{conf.ROOT_PATH}/{module_name}/{func[0]}",
                    "endpoint": func[0],
                    "view_func": func[1],
                },
            )
    return routes
