"""add item model

Revision ID: 405cb080963b
Revises:
Create Date: 2023-07-25 19:55:30.035069

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "405cb080963b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "items",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("(gen_random_uuid())"),
            nullable=False,
        ),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("completed", sa.Boolean(), nullable=True),
        sa.Column("deleted", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_items_id"), "items", ["id"])
    op.create_index(op.f("ix_items_title"), "items", ["title"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_items_title"), table_name="items")
    op.drop_index(op.f("ix_items_id"), table_name="items")
    op.drop_table("items")
    # ### end Alembic commands ###
