#!/usr/bin/python3

import sys, getpass

from utils.domains import domains
from utils.accounts import accounts
from utils.settings import settings
from utils.upload import upload
from utils.embeds import embeds

class main():
    # Main file that receives CLI arguments.

    args = sys.argv[1:] # Get the arguments, not including the actual file name.

    if "--domains" in args:
        domains().getAllDomains()
    if "--login" in args:
        loginPos = args.index("--login")
        try:
            username = args[loginPos + 1]
            password = args[loginPos + 2]
        except:
            print("[x] Couldn't find username or password in your arguments.")
            exit()
        accounts().addToken(username, password)
    if "--settings" in args:
        settings().viewAllSettings()
    if "--change" in args:
        loginPos = args.index("--change")
        try:
            setting = args[loginPos + 1]
            value = args[loginPos + 2]
        except:
            print("[x] Couldn't find setting or value in your arguments.")
            exit()

        settings().changeSetting(setting, value)
    if "--upload" in args:
        argPos = args.index("--upload")
        try:
            upload().uploadFile(args[argPos + 1])
        except:
            print("[x] You must specify the path to a file you want to upload!")
            exit()
    if "--regen-upkey" in args:
        accounts().regenUploadKey()
    if "--add-random-domain" in args:
        argPos = args.index("--add-random-domain")
        domains().addRandomDomain(args[argPos + 1])
    if "--del-random-domain" in args:
        argPos = args.index("--del-random-domain")
        domains().delRandomDomain(args[argPos + 1])
    if "--embeds" in args:
        embeds().getAllEmbeds()
    if "--new-embed" in args:
        embeds().createNewEmbed()
    if "--del-embed" in args:
        argPos = args.index("--del-embed")
        embeds().deleteEmbedPreset(args[argPos + 1])
    if "--edit-embed" in args:
        argPos = args.index("--edit-embed")
        embeds().editEmbedPreset(args[argPos + 1])
    if "--clear" in args:
        accounts().clearData()
    if "--encrypt" in args:
        userPass = getpass.getpass(prompt="New Encryption Password: ")
        userPassConfirmation = getpass.getpass(prompt="Confirm Encryption Password: ")
        if userPass == userPassConfirmation:
            accounts().encryptData(userPass)
        else:
            print("[x] Password mismatch.")
    if "--help" in args:
        print(
            """
AstralCLI is a command line interface for Astral.cool's API.


General Usage:
    --upload <file path>                Upload a file to Astral.
    --domains                           View all Astral domains.
        
Settings:
    --login <username> <password>       Login to Astral with your credentials.

    --settings                          View all of your settings.
    --change <setting> <value>          Change a specific setting.

    --embeds                            View current embed profiles.
    --new-embed                         Create a new embed profile.
    --del-embed <profile #>             Delete an embed profile.
    --edit-embed <profile #>            Edit an embed profile

    --add-random-domain <domain>        Add a random domain to your list.
    --del-random-domain <domain>        Delete a random domain from your list.

    --regen-upkey                       Regenerate your upload key.
    --clear                             Clear all local account data.

Are you a developer? Contribute to the AstralCLI project here: https://github.com/httpjamesm/astral-cli.
            """
        )