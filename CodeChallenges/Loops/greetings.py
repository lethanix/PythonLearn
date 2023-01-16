def add_greetings(names: list[str]):
    greetings = []
    for name in names:
        greetings.append("Hello, {}".format(name))
    return greetings


if __name__ == "__main__":
    print(add_greetings(["Louis", "Lethani", "Neovide"]))
