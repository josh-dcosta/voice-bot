from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', 'Atza|IwEBIN-Q7jEz87mEyaNuQBZyfc67_e27Wc9hdBgeWYxUTygcTgIAj_YgPkVfZul4p8cnOCU_tyho9E4VCYMabNouLsg51vZpVmAE8Z5gQUdof8Gz8nf4a0sAgkquroHMS2P1LJWDQlEYHuQjPdKZNAFO3PhFsIRLJONEn1F3fbmKCbMMf7G9WUrmbxcQznHpP53n3DTLYFO9k8V4eivXSuUC0fDe8gXrArfwczwBW0bsfEDr5BJBNErWT3ETh-pzFKT5KpWhaEyZcSGqGLN8cA_NHYeZCTAEvpQ8gH703igKat6l_cIX30ZE-387rA1J-QFbc-uEGzN9Tjr1WXBzmUvIqGTJ',
        '--skillId', 'amzn1.ask.skill.3decc776-1378-4ecd-882f-bf60eb4df018',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python/AlexaAssistant/HelloWorld/demoskill/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
