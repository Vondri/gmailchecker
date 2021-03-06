<div align="center">
  <img src="ss.png" alt="ScreenShot">
  <h3>
    π§Gmail checkerπ§<br>
    β v1.0.0 β<br>
    Created by <a href="https://gtihub.com/vondri">Vondri</a>
  </h3>
</div>

<div align="center">
  <img src="https://img.shields.io/github/repo-size/vondri/gmailchecker" alt="Repo size">
  <img src="https://img.shields.io/github/last-commit/vondri/gmailchecker" alt="Last commit">
  <img src="https://img.shields.io/github/v/tag/vondri/gmailchecker" alt="Last tag">
  <img src="https://img.shields.io/github/downloads/vondri/gmailchecker/total" alt="Downloads">
  <img src="https://img.shields.io/github/languages/top/vondri/gmailchecker" alt="Top">
  <img src="https://img.shields.io/github/license/vondri/gmailchecker" alt="License">
</div>

* * * * * * * * *
## Features
- [x] π Script work with params e.g `-h` π
- [x] π Silent mode (run without banner) π
- [x] β Writing valid and invalid users to another files β
- [x] β Timeout beetwen checks β
- [x] π Possibility to check single email π

## Requirements
  ![](https://img.shields.io/pypi/v/requests?label=requests)
  ![](https://img.shields.io/pypi/v/requests?label=argparse)
  ![](https://img.shields.io/pypi/v/requests?label=os)
  ![](https://img.shields.io/pypi/v/requests?label=sys)
  ![](https://img.shields.io/pypi/v/requests?label=time)

## Usage
* #### Linux
    ```
    git clone https://github.com/Vondri/admin-panel-finder.git
    cd gmailchecker
    chmod +x GmailChecker.py
    python GmailChecker.py -e <email>
    ```
* #### Windows
Download, extract zip and run script by `python GmailChecker.py -e <email>`

## Usage
```
python GmailChecker.py -u <userlist.txt> -o -i -t1
```
It will check all users in `userlist.txt` and print to another files valid and invalid users. Timout equal one second between checks.

* * * 

```
python GmailChecker.py -e <email>
``` 
It will check one user.
* * *
```
python GmailChecker.py -s -u <userlist.txt>
```
It will run script without banner and print result of scan.
