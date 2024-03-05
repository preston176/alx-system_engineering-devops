[(https://www.holbertonschool.com/)

# 0x15. Web stack debugging #3



## Synopsis
This project applies concept of strace to web stack debugging.

### At the end of this project students should be able to explain to anyone, **without the help of Google**:

### Resources

### Project Requirements
-   Allowed editors: `vi`, `vim`, `emacs`
-   All your Bash script files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   Your Bash script must pass `shellcheck` without any error
-   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash` for instance is that it will make your script portable for different OS where Bash might be in a different location.

## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** | Use `strace` to find out why Apache returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).| [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp)
