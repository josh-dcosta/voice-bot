from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', 'Atza|IwEBIIZzKzYZJ8AhqAeAy6PjYUBAjIFNjOS1qxwhHk1RbqiVXG1BVChZbVXKlbdpQGzObuuREsos8HOUjnz2wfWIckx8sdJebK2z-83R3XQCgrdDaoR1vZqolGnrWq0Nfooxgmm5CrduGvYaS9gzqPmJ1aGsAz8IxwCwvuPTJWqqBNtHKqPiX3m3DLoYkkKfOV_PLmyDJgdRiyz5oENX55_EGgt03NTHz90eBhZWnNpkBDJdzBGO3MFm4HpWhsHv9-DijIhQfdE0t-m9PYIcLypvA3stMXi3U40sj_EFdprp4mzgMQEpcpU9Fm985npYJoEuMXc_3G9Gb5GzJBijR9l1H0AY',
        '--skillId', 'amzn1.ask.skill.2c3c56f7-567b-4472-a934-4dec76db90fb',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python-2/AlexaAssistant/Lenape/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
