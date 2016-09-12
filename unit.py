class Unit:
    """
    Unit class
    represents a unit and the encessary conversion logic.
    variables:
        - name      (string)  : the name of the unit (celsius, joule, etc...)
        - to_base   (function): function to convert this unit to the base unit
                                of the category. For example, this function will
                                convert any temperature to fahrenheit.
        - from_base (function): function to convert the base unit of this
                                category to this unit.
    """
    def __init__(self, name, category, to_base, from_base):
        self.name = name
        self.to_base = to_base
        self.from_base = from_base
        self.category = category

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def convert_to_base(self, value):
        return self.to_base(value)

    def convert_from_base(self, value):
        return self.from_base(value)
