from enum import Enum, auto

from pydantic import BaseModel
from base.models.base import BinTree, HeaderTable, Point, Region, TableCell, TableRow


class KdTreePoint(Point):
    pass


class KdTreeOrderedLists(BaseModel):
    ordered_x: list[KdTreePoint]
    ordered_y: list[KdTreePoint]


class KdTree(BinTree):
    region: Region


class Partition(Enum):
    vertical = auto()
    horizontal = auto()


class ToAddKdTree(Enum):
    yes = auto()
    no = auto()


class Intersection(Enum):
    yes = auto()
    no = auto()


class KdTreePointCell(TableCell):
    content: KdTreePoint


class KdTreePartitionCell(TableCell):
    content: Partition


class KdTreeToAddCell(TableCell):
    content: ToAddKdTree


class KdTreeInterscetionCell(TableCell):
    content: Intersection


class KdTreePartitionTableRow(TableRow):
    cells: tuple[KdTreePointCell, KdTreePartitionCell]


class KdTreeSearchTableRow(TableRow):
    cells: tuple[KdTreePointCell, KdTreeToAddCell, KdTreeInterscetionCell]


class KdTreePartitionTable(HeaderTable):
    rows: list[KdTreePartitionTableRow]
    headers: tuple[str, str] = ('', '')


class KdTreeSearchTable(HeaderTable):
    rows: list[KdTreeSearchTableRow]
    headers: tuple[str, str, str] = ('', '', '')