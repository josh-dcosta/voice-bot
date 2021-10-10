from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', 'Atza|IwEBIJYitfo19N4Ho2PGdeEnIZEVr7hpnSnv9sA82ymM167ZSRGX4RKE9-Opxrmk_fLUelBnuvzT_YAJqK_nIsin5-u4KK6TM0029tvGaj3P83JrUlU_a8YJdj-BqSim3KRFJR-y4UXgrtrfzZ8MQGfsIKqMm-OOgZ_8Jlh2U82SgDLudCxDybtVgEzpaW0z-lYW9u4Fpr1juNpOmophBmGmFqQqZQF8llFLUMZqpCwhcTExq3gWzfm5CEtgyJRZRQokgRSlfyzlNyCFheYU3S0wmyKVjWZQ2ICGh6nDFF0Izk0tiC1GQ1QbBnleDpfjdtNas2G-pQV-9rN6_zFaMMlb2hiMxpSJBArXvjQRI4mm8Y8KYA',
        '--skillId', 'amzn1.ask.skill.05a0b6fc-2b2b-4ebe-8dcc-bb27d30a3527',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python/AlexaAssistant/Lenape/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
