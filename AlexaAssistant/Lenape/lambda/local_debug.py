from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', "Atza|IwEBILUf5l2Bn7ZFro2OcfAIg0LoUvjirF8l0ualkZJBjWTQWTN-Iwixmuu-y4gOVK8fo41Tb1-dHtfDuna_QyK3k1ijDiR_qhmNorpiPPG05ryoeXdcCkrt_BmdQpV4IH0uLumJaXd1K_Q31TVkyhcWz-ybVqVE2lO_kPB7Y95PonSWFmd5N5kVpC7MPkSRJs2CblrFJTVgdBJ4OH34BPGydM-4lhOZEHwPPc6YepMGiS72-zsO_Pw76uTAV3OxCv_CNhfTJlffUg95ufejp9x2Csmx_0APPYIllt8DFtqAJo0RlCw9GwuCm2allgWPfw3Tv1YehxH6a5RYMlopuFOnWSl4hYuQu8TRIVeYZt6ee3MfxA",
        '--skillId', 'amzn1.ask.skill.2c3c56f7-567b-4472-a934-4dec76db90fb',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python-2/AlexaAssistant/Lenape/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
