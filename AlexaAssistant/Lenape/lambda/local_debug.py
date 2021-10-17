from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', 'Atza|IwEBIIlYoo2WqNfc9i1wUeMI3vKqaa6dugmwc5-60M_zanXcShO-X1AAWw40sSevKYgRGtBBtCgWxwU8GIehf2FLDNhHmaRLWS9baq-PorwhzB4tA5pyAJY0Y8-I8XCU782QR5SH467Axr_vVkqDbTw5ugytNR9dDgYmDOUU0plSvjXAJU8WHiYOvN0bDtfdaRf-fP-ViLridaZCXk-CtnAQJHsT_tVUYh9qWq0xyZKKJ5o9J1f2KO0uCCxO9QeePmFG0Ce2qSJf7QUpHS5AnmEHW0QwaPqsHqLksPEGr7rVemyf1JfONWnrfAcNApMXnnjvSinByDk98R8yXTGWsNK99-2T',
        '--skillId', 'amzn1.ask.skill.2c3c56f7-567b-4472-a934-4dec76db90fb',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python-2/AlexaAssistant/Lenape/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
