from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', 'Atza|IwEBID8DJQCpk-qsv2zoqadij6Dk1eWsUGPunxgVhJmVRVmVEJb1MMLFdBo74S8NV93c9ONfInQK4HeskEDKOq-U2oypo472J_o-LkN67_OmtyVHbWyAV2HZ4J_kicvHdvBcB8enpDDblyZuhP7iP3AkdkVNppvsvVhXqPgnnKeSLjRf56NWPRq4rD1xGn0D3aA0RcFxQ8YEdXAYc9889WKXs3vo6wl2p8dlqYpb8BqLnfXbbckUOMoK_7RkDtX4gZo-vU5D9uRsSDFyllJx2DmLeiT-9cP5xbHcoBdNp2NPfHAvPWsKRlWbrqZL0rou4X5n4Z9fD7VcoDGSlvlse1-UGe39',
        '--skillId', 'amzn1.ask.skill.1740aeac-90a1-4f40-b742-b10e96bb77fd',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python/AlexaAssistant/HelloWorld/demoskill/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
