# openfisca_uk_energy/__init__.py
import os
from openfisca_core.taxbenefitsystems import TaxBenefitSystem

from .entities import entities  # list of Entity classes, e.g. [Unit]
from .variables import *        # ensures your Variable classes are registered

class CountryTaxBenefitSystem(TaxBenefitSystem):
    """
    Minimal OpenFisca system for UK energy.
    Exposed here because the OpenFisca CLI imports this symbol.
    """

    def __init__(self):
        super().__init__(entities)

        package_dir = os.path.dirname(__file__)
        # Load YAML parameters
        self.load_parameters(os.path.join(package_dir, "parameters"))
        # Load all Variable classes from your variables/ dir
        self.add_variables_from_directory(os.path.join(package_dir, "variables"))
