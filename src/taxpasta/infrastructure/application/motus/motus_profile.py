# Copyright (c) 2022 Moritz E. Beber
# Copyright (c) 2022 Maxime Borry
# Copyright (c) 2022 James A. Fellows Yates
# Copyright (c) 2022 Sofia Stamouli.
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


"""Provide a description of the mOTUs profile format."""


import pandera as pa
from pandera.typing import Series


class MotusProfile(pa.SchemaModel):
    """Define the expected mOTUs profile format."""

    consensus_taxonomy: Series[str] = pa.Field()
    # Pandas cannot handle missing integer values. Thus, we read this column as string.
    ncbi_tax_id: Series[str] = pa.Field(nullable=True)
    read_count: Series[int] = pa.Field(ge=0)

    class Config:
        """Configure the schema model."""

        coerce = True
        ordered = True
        strict = True
