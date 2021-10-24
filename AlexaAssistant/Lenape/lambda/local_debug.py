from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', 'Atza|IwEBIJ5TePUBMrgdKNtSVHdCo-4qktGl_88YKTXe87Qbg6MzUZEFngdFiO621dzn3qOygIWfIP4ZqTkbtXjwYJat5O-l6OyK5o3qoGKfTcatjgWSEFCKaht3VHzWcGLREwOaQd4YBp4hS0r6dZ5kD90OPGTdrL8iZJW7fRckc7Ppw5da3_TbcLuuAIUgqeZbM0y1Q2IAXWtP4LTdZ8opHLUPZnsFnmAT_MckKelBtSIzcxoIBZwRhuehgtShGDaUlCc-O4os2GJRU5N9DdfOOOPNKPrpia7rLn8Rv7UHL9ZI2mm25fvJ6IW55hj1mDu8qyhSbSYlrJNKbjb0hHQ2ACkAl7WE',
        '--skillId', 'amzn1.ask.skill.2c3c56f7-567b-4472-a934-4dec76db90fb',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python-2/AlexaAssistant/Lenape/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
