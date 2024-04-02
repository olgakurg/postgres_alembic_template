"""
This is not an example of repository realisation, This module is created for increasing cohesion"
"""

from sqlalchemy import select
from sqlalchemy.orm import selectinload
from .model import A, B
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


async def proto_add(value, async_session):
    async with async_session() as session:
        async with session.begin():
            session.add_all(
                [
                    A(bs=[B(data=value), B(data="b2")], data="a1"),
                    A(bs=[], data="a2"),
                    A(bs=[B(data="b3"), B(data="b4")], data="a3"),
                ]
            )


async def proto_selectin(value, async_session):
    async with async_session() as session:
        async with session.begin():
            # eager loading of relationship with selectinload
            stmt = (
                select(A)
                .where(A.data == value)
                .order_by(A.id)
                .options(selectinload(A.bs))
            )

            result = await session.execute(stmt)
            # buffered result (allocates memory)
            for a in result.scalars():
                print(a, a.data)

            print(f"created at: {a.create_date}")
            for b in a.bs:
                print(b, b.data)

            # exceptions should be handled - it's one() method
            result = await session.execute(select(A).order_by(A.id).limit(1))
            try:
                a1 = result.scalars().one()
            except NoResultFound as e:
                print("No results", e)
                return None

            except MultipleResultsFound as e:
                print("Too much results", e)

            a1.data = "new data"
            await session.commit()
            # expire_on_commit magic
            print("expire_on_commit magic", a1.data)


async def proto_streaming_selectin(value, async_session):
    async with async_session() as session:
        async with session.begin():
            # eager loading of relationship with selectinload
            stmt = (
                select(A)
                .where(A.data == value)
                .order_by(A.id)
                .options(selectinload(A.bs))
            )
            # streaming results (one-by-one)
            result = await session.stream(stmt)
            async for a1 in result.scalars():
                print(f"streaming a.data={a1.data}")
                # lazy loading attrs
                for b1 in await a1.awaitable_attrs.bs:
                    print(b1, b1.data)
