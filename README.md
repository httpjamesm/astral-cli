# astral-cli

Astral CLI is a command line client for uploading media to Astral, a private image host.

# Features

## Speedy

Change a setting, add a random domain and create a new embed profile within *seconds*. Account credentials are already stored, so no need to login every time or launch a web browser. All it takes is a keyboard and fingers.

## Lightweight

Astral CLI is an easy-to-use and lightweight (in size and memory usage) command line interface to interact with Astral's API. You could install this on a toaster if you really wanted to!

## Automatic Access Token Generation

No need to constantly send POST requests to generate access tokens every 5 minutes because Astral CLI does it for you seamlessly. On every request, whether it's to change a setting or create a new embed profile, Astral CLI conveniently fetches a new access token in the background.

## Linux Compatible

Are you using a Linux distro? No problemo. Astral CLI is independent of screenshot apps, like ShareX, so you can keep on uploading without Windows spyware.

## Open-Source

Since Astral CLI is open-source, you can audit its code to verify that I am not doing anything malicious or even contribute to the project! If have an idea to make it even better, fork it and make a pull request.

## Endorsed

Aspect, the founder of Astral, has shouted out Astral CLI in the [official astralcool Github organization](https://github.com/astralcool/cli).

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