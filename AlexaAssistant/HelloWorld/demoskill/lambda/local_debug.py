from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', 'Atza|IwEBIG5XQuAW1z60qrr1wEemdV2wvSvhJzcm-Il_NDOj8k5o5kGcfJAXYr-kYMoZNc1LOhFi81upVN-2i3Ws6ABXZ6IcKvHMJHZyAnWCcZNCoYAnD_Pxw4lLCYD7-XtbGjOaBWP0ZIxwebp6sHdI7tLIKBS1MkR0Tspanfur9z-8ZTSzkh6ATowQzF-Tw8SjOPKFonofSoL_CzTLYoTBvwseLTo6GsKVHodCurUxrUVJdnJs4n9v6foAvaCOy_VQCIiSnJq8QRPP-vZxR_PJwTywWineZiAnWZTcDxBMwlb2_an7h-XT5F16dCpKvAA4q6P60i6ZGzGz15pIbJreTMDZy82v',
        '--skillId', 'amzn1.ask.skill.3decc776-1378-4ecd-882f-bf60eb4df018',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python/AlexaAssistant/HelloWorld/demoskill/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
