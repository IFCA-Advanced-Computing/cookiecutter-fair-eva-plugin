# SPDX-FileCopyrightText: Copyright contributors to the FAIR eva project <https://github.com/IFCA-Advanced-Computing/FAIR_eva>
# SPDX-FileContributor: {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
#
# SPDX-License-Identifier: {{ cookiecutter.license }}

# coding: utf-8
from configparser import ConfigParser
import logging
import sys
from types import NotImplementedType
from typing import Union

from fair_eva.api.evaluator import EvaluatorBase
from pandas import DataFrame

logging.basicConfig(
    stream=sys.stdout, level=logging.DEBUG, format="'%(name)s:%(lineno)s' | %(message)s"
)
logger = logging.getLogger("api.plugin")


class Plugin(EvaluatorBase):
    """A class implements the RDA's FAIR indicators for the <{{ cookiecutter.plugin_name }}> plugin.

    Essential FAIR indicators are pre-implemented in the parent EvaluatorBase class. The remainder shall be coded as methods within this class.
    """

    def __init__(
        self,
        item_id: str,
        api_endpoint: str = "{{ cookiecutter.plugin_endpoint }}",
        lang: str = "en",
        config: ConfigParser = ConfigParser(),
        name: str = "{{ cookiecutter.plugin_name }}",
    ):
        """
        :param item_id: (persistent or not) identifier of the dataset, e.g. Digital Object identifier, Handle, or internal.
        :type item_id: str
        :param api_endpoint: Endpoint from which the metadata is collected.
        :type api_endpoint: str
        :param lang: Two-letter language code.
        :type lang: str
        :param config: ConfigParser's object containing both plugin's and main configuration.
        :type config: ConfigParser
        :param name: FAIR-EVA's plugin name.
        :type name: str
        """
        logger.debug(f"Initiating FAIR-EVA's <{name}> plugin")

        # Parent __init__ call
        super().__init__(item_id, api_endpoint, lang, config, name)

        # Metadata gathering
        self.metadata = self.get_metadata()
        if not self.metadata or len(self.metadata) == 0:
            error_message = f"Problem accessing (meta)data from repository <{api_endpoint}>"
            logger.error(error_message)
            raise Exception(error_message)
        logger.debug(f"Successfuly obtained metadata from repository: {self.metadata}")

    def get_metadata(self) -> Union[DataFrame, NotImplementedType]:
        return NotImplemented
