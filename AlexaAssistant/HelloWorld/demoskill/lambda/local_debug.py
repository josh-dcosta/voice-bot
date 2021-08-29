from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', 'Atza|IwEBIOCr-pZ9DEPtCNaXq9LhcYvJP_DTm3htrTGA9PAc29p5uUbu0DqhUN2d-H-LAi10zUDeMsEKRHyoOtZwChVmMuA3bPGhWvxd8CLZn8TTzaIjVF9qaE3xHpT9E8fIbIeOgsmUvGhW5V8knw5BqYAoyiSEjASrHg8FmYOzR0ndxbjpuuCuRe51pykNVBIPPUFdJpor24pztICZcZDTgzV6a811rfzsqtJn7i5RPsC9Y9oDqRarJQOm1U0dorsR-4FxZPGPO_uYL2fZexsw0V5F6gOkDGCJcs2tq5U9xl23_020wtK2U1pZCVEvbdgxOkKvNk5cRk_ye4Kg3bW_fguzXEo8WO5WvTlfn4NQrw7EMGj5_A',
        '--skillId', 'amzn1.ask.skill.3decc776-1378-4ecd-882f-bf60eb4df018',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', '/Users/joshuadcosta/Documents/projects/Python/AlexaAssistant/HelloWorld/demoskill/lambda/lambda_function.py',
        "--region", "NA" # Optional argument. Region defaults to NA.
        ]
    ).invoke()
