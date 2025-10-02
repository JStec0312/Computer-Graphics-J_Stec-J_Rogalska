def cmd_help(kv: dict) -> int:
    print("Available commands:")
    print("--help : Show this help message")
    print("--brightness --input=<input_path> --output=<output_path> --delta=<value> : Adjust image brightness by <value> (-255 to 255)")
    return 0