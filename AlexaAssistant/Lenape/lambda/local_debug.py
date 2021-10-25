from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', 'Atza|IwEBIBlrV1iHxeOTciDXmi4-Md1xtctC1x5BcpEWk_ZOqBuhtguTH4sszZXNUpRqpW1eVe8yfK-2xDqY__53UC36sWOT9aMcDLgU8MG0v_PP66C2876RSJtJt80Flb5B2Lj9DArAhmdvv140KpUxu_O4UA0c1C8UaZ0_OYARi9I3aSOwW5byejxvtS4J6MCdSS_07VvkdgANxPbA3Fe7dI_nJTULzPgovZyDPEhzki3_HkLYz5bvmGgLu3qGA7dCbA8lDBnvdEcmxEeBn8HhjdtQeUAS7mwe-Ra2dpqRlzdOJdG1xfMAVPLpkW-7CndEA5T8NapNBPSzSFlP_zew3ZrxRC4w',
        '--skillId', 'amzn1.ask.skill.2c3c56f7-567b-4472-a934-4dec76db90fb',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python-2/AlexaAssistant/Lenape/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
