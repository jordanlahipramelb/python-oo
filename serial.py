"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a new generator starting at start.

        Args:
            start (int, optional): Defaults to 0 if no number inputed.
        """
        # defines all variables from 1 initial argument
        self.start = self.next = start

    def __repr__(self):
        """Shows represenation of arguments"""

        return f"<SerialGenerator start = {self.start}, next = {self.next}>"

    def generate(self):
        """Returns next serial number."""

        # increases number by 1 each time function is ran
        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets generator to original start inputed."""

        self.next = self.start