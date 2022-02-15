# S-So Fresh!

`ssofresh` is a small utility for refreshing your AWS Credentials when you're
using AWS SSO.

AWS SSO is the default mechanism for auth when you're using Landing Zone or
Control Tower, both of which tend to create a large proliferation of accounts.

If you're working across multiple accounts, you're going to find it incredibly
tedious to do the usual credentials workflow :

- Log into the SSO web portal
- Find the account you want to access
- Copy the creds out of it and paste them into your `~/.aws/credentials` file
  - Or into your current terminal environment

`ssofresh` will handle fetching the creds for multiple accounts and populating
your credentials file.

Paired with e.g. `ondir`, configured to change your `AWS_PROFILE` variable on
directory changes in the terminal, and a prompt program like 
[Starship](https://starship.rs/) that shows your selected AWS profile, and you
can have almost friction free switching of accounts as you switch folders.

## Prerequisites

**python3** <https://www.python.org/downloads/>

**boto3**

```
pip3 install boto3
```

## Installation

- Put or link `ssofresh` somewhere on your PATH (I like `~/.local/bin`)
- Configure your account/role groups in `~/.aws/ssofresh.ini`

## Usage

```
ssofresh my-account-group
```

A browser window will be spawned ; you'll either have to log in, or just click a confirm button if you already are.

## `ssoinit`

New, companion script. Needs running from a role that has at least read-only
access to Organizations in your root account.

```
ssoinit <account-group-name>
```

Prints the accounts section of an `ssofresh.ini` file *without* the default
section and *without* the start_url, so you'll have to add these.

It also lists **every** profile in your account group, which you may wish to
trim back for normal operational use.

## `assume-role`

Uses the ssofresh.ini file to allow you to assume a role.

e.g. in the template file, using the account-group-one-profile-one:
`./assume-role account-group-one-profile-one`

Will assume the role (`PhenomenalCosmicPower`, from the ini file) and fill the profile `AssumedRole` in your local credentials file, ready for use: `--profile AssumedRole`

## The Future

In the future, hopefully everything will natively support the AWS SDK 2.0
capabilties for working with SSO credentials and this will be unncessary.

### TODO

- Container mode : posts the link but doesn't try and open the browser
  - Useful for e.g. VSCode Remote Containers where you don't have a desktop
  - Auth outside the container to get creds inside the container
- Build for self-contained Windows exe version
  - Don't have to muck about with Python
