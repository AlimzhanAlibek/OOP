def prefix_message(message, prefix="Info"):
    return f"[{prefix}]: {message}"

def suffix_message(message, suffix="DONE"):
    return f"{message} [{suffix}]"
