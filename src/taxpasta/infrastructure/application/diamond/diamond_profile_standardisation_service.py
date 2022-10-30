# Copyright (c) 2022, Moritz E. Beber, Maxime Borry, Jianhong Ou, Sofia Stamouli.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Provide a standardisation service for diamond profiles."""


import pandas as pd
import pandera as pa
from pandera.typing import DataFrame

from taxpasta.application.service import ProfileStandardisationService
from taxpasta.domain.model import StandardProfile

from .diamond_profile import DiamondProfile


class DiamondProfileStandardisationService(ProfileStandardisationService):
    """Define a standardisation service for diamond profiles."""

    @classmethod
    @pa.check_types(lazy=True)
    def transform(
        cls, profile: DataFrame[DiamondProfile]
    ) -> DataFrame[StandardProfile]:
        """
        Tidy up and standardize a given diamond profile.

        Args:
            profile: A taxonomic profile generated by diamond.

        Returns:
            A standardized profile.

        """

        result = profile[[DiamondProfile.query_id, DiamondProfile.taxonomy_id]].copy()
        result = (
            result.groupby(DiamondProfile.taxonomy_id)
            .count()
            .reset_index()
            .rename(columns={DiamondProfile.query_id: StandardProfile.count})
        )
        return pd.DataFrame(
            {
                StandardProfile.taxonomy_id: result[DiamondProfile.taxonomy_id].astype(
                    str
                ),
                StandardProfile.count: result[StandardProfile.count],
            }
        )
