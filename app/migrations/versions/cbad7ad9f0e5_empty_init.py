"""Empty Init

Revision ID: cbad7ad9f0e5
Revises: b4806548dda0
Create Date: 2024-01-09 00:17:14.652920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbad7ad9f0e5'
down_revision: Union[str, None] = 'b4806548dda0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
