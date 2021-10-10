from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', 'Atza|IwEBIJ-g-YYHxLqsFm201xIn08_mQ2fXP-PFi5FFryr9IymL9R_TnOwistdOku600tmabYkc0Y_d8WkErCT7XkWzV7nMOkEqinJUBJmjQtU2tlUGEzyJlFotVcrpVdQGAudimgwqVUsG-A4JmWz5PKzl4SQmq3Ox1pSRGz8QIkt3kzu6eaCEppj7Zeb63Ic_rCFoEMw-IiYcgMn_0ipiNFSymDYQh7LfP1udi9GUKL9yH7EHy9JEwz03Yo-UGejhBhzL9AvVKDrj4qTg9wKUCa3QoeP4NUSnTjxlms5q0FJVdNqJv17DAtbi2z-hE0YQRPiS7yIp8APSzMqsn_FiQ12OoaCb',
        '--skillId', 'amzn1.ask.skill.2c3c56f7-567b-4472-a934-4dec76db90fb',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python/AlexaAssistant/Lenape/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
