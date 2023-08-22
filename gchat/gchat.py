#!/usr/bin/env python3.10

# Standard library
import sys

# Local
import gchat.utilities.chatgpt as gpt
import gchat.utilities.parsers as parsers
import gchat.utilities.printers as printers
import gchat.utilities.code_execution as code_exec


######
# MAIN
######


def main():
    args = sys.argv
    if len(args) == 1 or args[1].lower() in ("-h", "--help"):
        printers.print_help_message()
        return

    if len(args) == 1 or args[1].lower() in ("-v3"):
        if not gpt.is_user_registered_v3():
            gpt.register_openai_credentials_v3()
        print()
        with printers.LoadingMessage():
            explanation = gpt.get_chatgpt_res_v3(args)
    else:
        if not gpt.is_user_registered():
            gpt.register_openai_credentials()
        print()
        with printers.LoadingMessage():
            explanation = gpt.get_chatgpt_res(args)

    printers.print_error_explanation(explanation)
