import sys
from commands.cmd_brigthness import cmd_brightness
from commands.cmd_help import cmd_help
from commands.cmd_contrast import cmd_contrast
from commands.cmd_negative import cmd_negative
from commands.cmd_horizontal_flip import cmd_horizontal_flip
from commands.cmd_vertical_flip import cmd_vertical_flip


COMMANDS = {
        "--help" : cmd_help,
        "--brightness" : cmd_brightness,
        "--contrast" : cmd_contrast,
        "--negative" : cmd_negative,
        "--horizontal" : cmd_horizontal_flip,
        "--vertical" : cmd_vertical_flip,
    }

def usage() -> None:
    print("Usage: main.py --command [-argument=value ...]")

def parse(argv: list[str]) -> tuple[str, dict]:
    if not argv or not argv[0].startswith("--"): # must start with --
        usage()
        raise SystemExit(2)
    command = argv[0] #command is the first token
    kv = {} # dictionary to hold key-value pairs
    for token in argv[1:]:
        token = token.lstrip("-")
        if "=" in token:
            k, v = token.split("=", 1) #argument - value pair
            kv[k] = v
        else:
            kv[token] = True #else it's a flag
    return command, kv

def main() -> int:
    command, kv = parse(sys.argv[1:])
    if command  in COMMANDS:
        return COMMANDS[command](kv)
    else:
        print(f"Unknown command: {command}, use --help for usage information.")
        return 0



if __name__ == "__main__":
    sys.exit(main())