# ucs-core

ucs-core/
├── data/                       # Data layer: Hub-and-Spoke definitions
│   ├── mappings.json           # The translation bridge table
│   ├── lbc_taxonomy.json       # LBC/BBK hierarchical definitions
│   ├── udc_taxonomy.json       # UDC hierarchical definitions
│   └── niem_subset.xml         # Relevant NIEM exchange schema subset
├── src/                        # The Engine & Logic layer
│   ├── engine.py               # Core Hub translation controller
│   ├── validators.py           # Schema-wide gatekeeper (JSON Schema)
│   ├── utils.py                # Linter for bridge table integrity
│   └── transformers/           # Specialized Transformer Factory
│       ├── __init__.py
│       ├── base.py             # Abstract base class for all transformers
│       ├── lbc.py              # LBC transformation and validation logic
│       ├── udc.py              # UDC transformation and validation logic
│       └── niem.py             # NIEM transformation and validation logic
├── tests/                      # Testing layer
│   ├── test_engine.py          # Verifies Hub-to-Spoke translation
│   ├── test_validation.py      # Verifies input schema compliance
│   └── test_transformers.py    # Verifies standard-specific validation rules
├── docs/                       # Docs-as-Code layer
│   ├── 01_architecture.md      # Hub-and-Spoke design documentation
│   ├── 02_cataloging_guide.md  # How-to for catalog manifestation
│   └── CHANGELOG.md            # Versioning and modification history
└── main.py                     # Primary entry point for catalog processing
