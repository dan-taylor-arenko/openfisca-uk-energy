from openfisca_core.model_api import *
from openfisca_uk_energy.entities import Unit

class unit__target_output_mw(Variable):
    value_type = float
    entity = Unit
    definition_period = DAY
    label = "BM target setpoint for the unit (MW)"

class unit__metered_output_mw(Variable):
    value_type = float
    entity = Unit
    definition_period = DAY
    label = "Metered output for the unit (MW)"

class bm__compliant_delivery(Variable):
    value_type = bool
    entity = Unit
    definition_period = DAY
    label = "Delivery within tolerance"

    def formula(unit, period, parameters):
        target = unit('unit__target_output_mw', period)
        metered = unit('unit__metered_output_mw', period)
        tol = parameters(period).bm.delivery_tolerance
        return abs(metered - target) <= tol
