#!/usr/bin/env python
"""Usage: main.py [OPTIONS]

Options:
  --single-structure TEXT  Location of structure file  [required]
  --model [ML|CAS|EN|BS]   Hardness model to use  [default: CAS]
  --help                   Show this message and exit.
"""
import logging
import warnings
from pathlib import Path

import click

from intrinsic_hardness import bond_detectors, hardness_calculators, structure_makers


@click.command()
@click.option(
    "--single-structure",
    help="Location of structure file",
    required=True,
)
@click.option(
    "--model",
    help="Hardness model to use",
    type=click.Choice(["ML", "CAS", "EN", "BS"], case_sensitive=False),
    default="CAS",
    show_default=True,
)
def main(single_structure, model):
    warnings.filterwarnings("ignore")
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        filename=f"intrinsic_hardness.log",
        filemode="a",
        level=logging.INFO,
    )

    structure = structure_makers.structure_from_file(Path.cwd() / single_structure)
    bonds = bond_detectors.detect_bonds(structure)
    hardness = hardness_calculators.calculate_hardness(
        structure, bonds, model=model.upper()
    )

    print(f"{model.upper()} Model Hardness = {hardness}")


if __name__ == "__main__":
    main()
