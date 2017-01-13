"""This file should have our order classes in it."""

import random


class AbstractMelonOrder(object):
    """A melon order in an ideal world with no taxes."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        self.shipped = False
        self.species = species
        self.qty = qty

        if qty > 100:
            raise TooManyMelonsError
            # raise Exception

    def __repr__(self):
        total = self.get_total()
        return "{} melons of the {} species for {:.2f}".format(self.qty, self.species, total)

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        if self.species == "christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_base_price(self):
        base_price = random.randint(5, 9)
        return base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    tax = 0.08
    order_type = "domestic"

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        subtotal = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            flat_fee = 3
            subtotal += flat_fee

        return subtotal


class GovernmentMelonOrder(AbstractMelonOrder):
    """Melon orders under government program"""

    tax = 0
    order_type = 'government'

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(passed):
        self.passed_inspection = passed


class TooManyMelonsError(ValueError):

    def __init__(self):
        message = "Orders may not have more than 100 melons."
        super(TooManyMelonsError, self).__init__(message)


order0 = GovernmentMelonOrder("watermelon", 105)