"""
Various model fields that mostly provide default field sizes to ensure
these are consistant when used across multiple models.
"""

from future.builtins import super

from locale import localeconv

from django.db.models import CharField, DecimalField
# from django.utils.translation import ugettext_lazy as _



class PercentageField(DecimalField):
    """
    A field for representing a percentage. Sets restrictions on admin
    form fields to ensure it is between 0-100.
    """
    def formfield(self, *args, **kwargs):
        defaults = {'min_value': 0, 'max_value': 100}
        kwargs.update(**defaults)
        return super(PercentageField, self).formfield(*args, **kwargs)


class MoneyField(DecimalField):
    """
    A field for a monetary amount. Provide the default size and
    precision.
    """
    def __init__(self, *args, **kwargs):
        defaults = {"null": True, "blank": True, "max_digits": 10,
                    "decimal_places": localeconv()["frac_digits"]}
        defaults.update(kwargs)
        super(MoneyField, self).__init__(*args, **defaults)


class DiscountCodeField(CharField):
    """
    A field for Discount Codes. Provide the default field size.
    """
    def __init__(self, *args, **kwargs):
        defaults = {"max_length": 20}
        defaults.update(kwargs)
        super(DiscountCodeField, self).__init__(*args, **defaults)
