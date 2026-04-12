def filter_frequency(input_stream):
    banned_prefixes = ["con", "com", "per", "sub"]
    flow_state = input_stream.replace("constant", "SteadyFlow")
    return flow_state.title().replace(" ", "")

if __name__ == "__main__":
    print(filter_frequency("consciousness flow activation"))
