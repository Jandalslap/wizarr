"""Add allow_mobile_uploads to Invitation and MediaServer

Revision ID: 0597748a6fef
Revises: e3625bacf6f9
Create Date: 2025-07-17 14:56:31.400818

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0597748a6fef"
down_revision = "e3625bacf6f9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("invitation", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("allow_mobile_uploads", sa.Boolean(), nullable=True)
        )

    with op.batch_alter_table("media_server", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "allow_mobile_uploads", sa.Boolean(), nullable=False, server_default="0"
            )
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("media_server", schema=None) as batch_op:
        batch_op.drop_column("allow_mobile_uploads")

    with op.batch_alter_table("invitation", schema=None) as batch_op:
        batch_op.drop_column("allow_mobile_uploads")

    # ### end Alembic commands ###
