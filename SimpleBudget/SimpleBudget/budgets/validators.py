from django.core.exceptions import ValidationError

import re


def validate_budget_period(period):
    # return True
    failure_msg = f'{period} is not a valid Budget period.'
    regex = re.compile('^[0-9]{1,2}\-(daily|weekly|monthly|quarterly|annually|onetime)$')
    m = re.match(regex, period)

    if m is None:
        raise ValidationError(failure_msg)

    if int(period[:1]) == 0:
        raise ValidationError(failure_msg)

    if period.endswith('onetime'):
        split_loc = period.index('-')
        lside = period[:split_loc]
        v = int(lside)
        if v != 1:
            raise ValidationError(failure_msg)
