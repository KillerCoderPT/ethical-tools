# Ethical Tools

## Brute Force Program

This script is a tool to find the correct password for the user provided.

The script will ask for a URL, a username, a password list file and the string when the users login fails.

| Field              | Description                                                          |
| ------------------ | -------------------------------------------------------------------- |
| URL                | Target Link.                                                         |
| Username           | User to match the password.                                          |
| Password List      | File with password list.                                             |
| Login String Fails | The string used by the server on the response, when the login fails. |


During my tests I found this github repo very usefully, https://github.com/berzerk0/Probable-Wordlists it contains a very large passwords list texts that you can use.

#### Note

Before using, you need to check that the name of the HTML fields match the names of the code.

The fiels are `username` and `password`, you need to change this or sometimes this will not work. If you don't know what I'm talking about. This tool is not for you.

## Port Scanner

This script is a tool to find open ports on the target provided.

You can used multiple targets, split them by a comma `,`.


| Field              | Description                                                             |
| ------------------ | ----------------------------------------------------------------------- |
| Targets            | Target IP, you can use more than one, just split them by a comma.       |
| Ports Range        | Specifies the number of ports to scan. This will always starts on the 1 |
