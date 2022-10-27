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


"""Provide an arrow reader."""


import pandas as pd

from taxpasta.application import BinaryBufferOrFilepath, TableReader


class ArrowTableReader(TableReader):
    """Define the arrow reader."""

    @classmethod
    def read(cls, source: BinaryBufferOrFilepath, **kwargs) -> pd.DataFrame:
        """Read arrow from the given source."""
        return pd.read_feather(source, **kwargs)
