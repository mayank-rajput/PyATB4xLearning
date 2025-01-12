# Decorators

def add_before_ui_after_ui(func):
    # two parts
    # Wrapper & call
    def wrapper():
        print("1. Before Running UI TC")
        print("2. Start The Browser")
        func()
        print("3. Ending the Running UI TC")
        print("4. Quit The Browser")

    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print("I Will Test the UI.")

