from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', "Atza|IwEBIAAfv9Q-krH83BrmcV9b1ojj9WiIv677ZaiJGtcSuXcBC5s0zVScWxcWwIvMn8royS5djrluPfTGM-caRSY1SB-EitKf_Zq1RnqUauv0BTks5HRSTaz8wRi-5kDP1H5lRJy5r0zRBqWA32VUYmQ6RfCPA7KVG43TFHcS1-kD23kpjfjRZ_TfVDVx7hDmh_pTTjUObaQH1xuzZyY6d9QHL-quYZUn4vHLAmQLtMXD2Fn1zeIbv1g15OKtp16FGQpP5ZKIrcvbl0myHo4GqP8n2Y4vnkLFlV0Fa8NcKe-ewNwbe77AXajfyn5skVw3yomorcUHOddXC9DB5xwBvkqmc0XA5_Hd-FTgPAGuiMi-oIwvfg",
        '--skillId', 'amzn1.ask.skill.2c3c56f7-567b-4472-a934-4dec76db90fb',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python-2/AlexaAssistant/Lenape/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
