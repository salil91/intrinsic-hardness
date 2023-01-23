"""
Structure Maker module:

This module contains functions for returning pymatgen Structure objects from one or more files. Supported formats
include cif, POSCAR/CONTCAR, CHGCAR, LOCPOT, vasprun.xml, CSSR, Netcdf and pymatgen's JSON-serialized structures. """

from pymatgen.core import IStructure


def structure_from_file(filename):
    """
    Returns a structure from a single file.

    :param filename: The filename to read from.
    :return: Pymatgen IStructure object.
    """
    structure = IStructure.from_file(filename)

    return structure


def structures_in_dir(dirname):
    """
    Returns structures from all supported files in a directory.

    :param dirname: The directory to search in.
    :return: List of pymatgen IStructure objects.
    """
    from glob import glob

    ftypes = (
        "*.cif",
        "*.mcif",
        "*POSCAR*",
        "*CONTCAR*",
        "*CHGCAR*",
        "*LOCPOT*",
        "vasprun*.xml",
        "*.cssr",
        "*.json",
        "*.mson",
        "*.yaml",
        "*.yml",
        "*.xsf",
    )
    files_globbed = []
    for ftype in ftypes:
        files_globbed.extend(glob(ftype, root_dir=dirname))

    structures = []
    for filename in files_globbed:
        structures.extend(IStructure.from_file(filename))

    return structures


def structures_from_list(filename):
    """
    Returns structures from a list containing the paths to the files.

    :param filename: The list to read from.
    :return: List of pymatgen IStructure objects.
    """
    with open(filename, "r") as f:
        text = f.read()
        files = text.split("\n")
    structures = []
    for filename in files:
        structures.extend(IStructure.from_file(filename))

    return structures
