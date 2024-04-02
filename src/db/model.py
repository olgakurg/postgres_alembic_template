from __future__ import annotations

# import uuid
from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, func

# from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from typing import Optional


class Base(AsyncAttrs, DeclarativeBase):
    pass


class A(Base):
    __tablename__ = "a"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[Optional[str]]
    create_date: Mapped[datetime] = mapped_column(server_default=func.now())
    bs: Mapped[List[B]] = relationship()


class B(Base):
    __tablename__ = "b"
    id: Mapped[int] = mapped_column(primary_key=True)
    a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
    data: Mapped[Optional[str]]


# Base = declarative_base()
#
#
# class TimeStampMixin:
#     created_at: Mapped[datetime] = mapped_column(default=func.now())
#     updated_at: Mapped[datetime]
#
#
# #One-to-one in not-annotated mot-mapped style,
#
# class First(TimeStampMixin, Base):
#     __tablename__ = "firsts"
#
#     id = Column(
#         UUID(as_uuid=True), primary_key=True,
#         default=uuid.uuid4, unique=True,
#         nullable=False,
#     )
#     first_name = Column(String(255))
#     second = relationship("Second", back_populates="first", uselist=False)
#     firsts_idx = Index("firsts_idx", id, unique=True)
#
#
# class Second(TimeStampMixin, Base):
#     __tablename__ = "seconds"
#
#     id = Column(
#         UUID(as_uuid=True), primary_key=True,
#         default=uuid.uuid4, unique=True,
#         nullable=False,
#     )
#     second_name = Column(String(255))
#     first_id = Column(UUID(as_uuid=True), ForeignKey("firsts.id", ondelete="CASCADE"), nullable=True)
#     first = relationship("First", back_populates="second")

# One-to-many
# class Third(Base):
#     __tablename__ = "thirds"
#     id = Column(
#         UUID(as_uuid=True),
#         primary_key=True,
#         default=uuid.uuid4,
#         unique=True,
#         nullable=False,
#     )
#     third_name = Column(String(255))
#
#
# class Fourth(Base):
#     __tablename__ = "fourths"
#     id = Column(
#         UUID(as_uuid=True),
#         primary_key=True,
#         default=uuid.uuid4,
#         unique=True,
#         nullable=False,
#     )
#     third_id = Column(UUID(as_uuid=True), ForeignKey("thirds.id", ondelete="CASCADE"))
#     third = relationship(
#         "Third", back_populates="fourths")
#
#
# class Association(Base):
#     __tablename__ = "association_table"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     left_id: Mapped[int] = mapped_column(ForeignKey("left_table.id", ondelete="CASCADE"))
#     right_id: Mapped[int] = mapped_column(
#         ForeignKey("right_table.id", ondelete="CASCADE"
#     ))
#     extra_data: Mapped[str]
#     child: Mapped[List["Left"]] = relationship(back_populates="parents")
#     parent: Mapped[List["Right"]] = relationship(back_populates="children")
#
#
# class Left(Base):
#     __tablename__ = "left_table"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     children: Mapped[List["Association"]] = relationship(
#         back_populates="parent")
#
#
# class Right(Base):
#     __tablename__ = "right_table"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     parents: Mapped[List["Association"]] = relationship(
#         back_populates="child")
