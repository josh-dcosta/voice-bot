from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', 'Atza|IwEBIOr0VWHOc8x5fsplZNe-XsKQ14ex0mL1Gsy4ILYh6dzjhjB9G0kI1Dv0C4uwSOMRSjJuyK23V6FwlsCXjnHoZ5zaI-Pz_2ba9qTePH7SCWk117QoSpw6Ih5pw1EX5P1eGOwVTm6yr6r4b3ou-uV0vLnUWTZw53ASq4vJHHvU7UmNlePdCTwlbsx6Ppc70Na_QlH7wfAx_Ht2a8hYtyHzNcB_pxb0Icze6OusYiSQy3XCGZpP4SvIDKv00ozkEZMY1y2_lZQpHtCeoED8-EEiMoUoNpuxPLAVtYZ4Dr1pWhH1Do64WApOl2DscuSh5lPcWHgSk3S-1lFUdEFXjE37tpZkYFtVqq6iXs2Zhgz9E2oDGg',
        '--skillId', 'amzn1.ask.skill.2c3c56f7-567b-4472-a934-4dec76db90fb',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python-2/AlexaAssistant/Lenape/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
