from openfisca_core.entities import SingleEntity

# A single “battery unit” entity
Unit = SingleEntity(
    key="unit",
    plural="units",
    label="Battery unit",
    doc="A BM-dispatchable battery unit",
)

# OpenFisca expects a list of entity *instances*
entities = [Unit]