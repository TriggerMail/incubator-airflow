#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Create LastDeployedTime table

Revision ID: 53bee4c621a1
Revises: c2091a80ac70
Create Date: 2020-05-03 23:18:22.731457

"""

# revision identifiers, used by Alembic.
revision = '53bee4c621a1'
down_revision = 'c2091a80ac70'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'last_deployed_time',
        sa.Column('last_deployed', sa.DateTime(), primary_key=True)
    )

def downgrade():
    op.drop_table("last_deployed_time")
