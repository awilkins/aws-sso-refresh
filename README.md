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

## Installation

- Put or link `ssofresh` somewhere on your PATH (I like `~/.local/bin`)
- Configure your account/role groups in `~/.aws/ssofresh.ini`

## Usage

```
ssofresh my-account-group
```

A browser window will be spawned ; you'll either have to log in, or just click a confirm button if you already are.

## The Future

In the future, hopefully everything will natively support the AWS SDK 2.0
capabilties for working with SSO credentials and this will be unncessary.

## Caveats

- This script was written for Linux ; Mac guys might need to change `xdg-open`
  for `open` ; or do me a PR that makes it work on either platform!
