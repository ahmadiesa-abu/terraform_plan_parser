"""Setup for Terraplanfeed."""

from setuptools import setup, find_packages
import pathlib

setup(
    name="terraform-plan-parser",
    version='0.0.1',
    description="Parse Terraform plan in json format and give feedback.",
    keywords=["terraform-plan-parser", "Python", "Terraform", "Terraform Plan"],
    packages=["terraform_plan_parser"],
    install_requires=[],
)
