import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Farm as FarmModel, Crop as CropModel, Weather as WeatherModel, Equipment as EquipmentModel


class Farm(SQLAlchemyObjectType):
    class Meta:
        model = FarmModel


class Crop(SQLAlchemyObjectType):
    class Meta:
        model = CropModel


class Weather(SQLAlchemyObjectType):
    class Meta:
        model = WeatherModel


class Equipment(SQLAlchemyObjectType):
    class Meta:
        model = EquipmentModel


class Query(graphene.ObjectType):
    farms = graphene.List(Farm)
    crops = graphene.List(Crop)
    weathers = graphene.List(Weather)
    equipments = graphene.List(Equipment)

    def resolve_farms(self, info):
        return FarmModel.query.all()

    def resolve_crops(self, info):
        return CropModel.query.all()

    def resolve_weathers(self, info):
        return WeatherModel.query.all()

    def resolve_equipments(self, info):
        return EquipmentModel.query.all()


schema = graphene.Schema(query=Query)