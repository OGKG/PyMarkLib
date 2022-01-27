from base.builder import ModelBuilder
from base.models.graham import GrahamCenterPointCell, GrahamPiCompareCell, GrahamPoint, GrahamPointList, GrahamTable, GrahamTableRow, GrahamToAddCell, GrahamTrinityCell, PiCompare, ToAdd


class GrahamModelBuilder(ModelBuilder):
    
    @classmethod
    def _build_methods(cls):
        return [
            cls._build_internal_point,
            cls._build_ordered,
            cls._build_origin,
            cls._build_steps_table
        ]

    @staticmethod
    def _build_internal_point(answer):
        return GrahamPoint(x=answer.x, y=answer.y)
    
    @staticmethod
    def _build_ordered(answer):
        return GrahamPointList(points=[GrahamPoint(x=p.x, y=p.y) for p in answer])
    
    @staticmethod
    def _build_origin(answer):
        return GrahamPoint(x=answer.x, y=answer.y)

    @staticmethod
    def _build_steps_table(answer):
        pi_compare = lambda x: PiCompare.less if x else PiCompare.more
        to_add = lambda x: ToAdd.yes if x else ToAdd.no
        rows = [
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=tuple(GrahamPoint(x=p.x, y=p.y) for p in row[0])),
                GrahamPiCompareCell(content=pi_compare(row[1])),
                GrahamCenterPointCell(content=GrahamPoint(x=row[0][1].x, y=row[0][1].y)),
                GrahamToAddCell(content=to_add(row[1]))
            ))
            for row in answer
        ]
        
        return GrahamTable(rows=rows)
