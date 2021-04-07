# astral-cli

Astral CLI is a command line client for uploading media to Astral, a private image host.

# Installation Instructions

Clone this git onto your computer. Run the following commands in order.

```
python3 -m pip install requests
```
If you're on Linux, run the above AND the following:
```
sudo apt install tkinter
```
You may need to use another package manager depending on your distro.

Once requests and Tkinter are installed, run the following:
```
python3 astralcli.py --login <username> <password>
```


This will install the required dependency and store your account credentials for Astral CLI.

# Usage Help

```
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
```