from flask import Flask
from area.area_entity import Area
from construction_technologies.construction_technology_entity import ConstructionTechnology
from developers.developer_entity import Developer
from heating.heating_entity import Heating
from installment_plan.installment_plan_entity import InstallmentPlan
from installment_plan_term.installment_plan_term_entity import InstallmentPlanTerm
from insulation.insulation_entity import Insulation
from parking.parking_entity import Parking
from protected_area.protected_area_entity import ProtectedArea
from renovation.renovation_entity import Renovation
from residence_classes.residence_class_entity import ResidenceClass
from rooms.room_entity import Room
from walls.wall_entity import Wall
from residences.residence_entity import Residence
from dataset import real_estate

app = Flask(__name__)


@app.route('/residences')
def get_residences():
    residence = Residence(real_estate)
    return list(residence.get_all())


@app.route('/construction_technologies')
def get_construction_technologies():
    construction_technologies = ConstructionTechnology(real_estate)
    return list(construction_technologies.get_all())


@app.route('/developers')
def get_developers():
    developers = Developer(real_estate)
    return list(developers.get_all())


@app.route('/heating')
def get_heating():
    heating = Heating(real_estate)
    return list(heating.get_all())


@app.route('/installment_plan')
def get_installment_plan():
    installment_plan = InstallmentPlan(real_estate)
    return list(filter(None, list(installment_plan.get_all())))


@app.route('/installment_plan_term')
def get_installment_plan_term():
    installment_plan_term = InstallmentPlanTerm(real_estate)
    return list(filter(None, list(installment_plan_term.get_all())))


@app.route('/insulation')
def get_insulation():
    insulation = Insulation(real_estate)
    return list(insulation.get_all())


@app.route('/parking')
def get_parking():
    parking = Parking(real_estate)
    return list(parking.get_all())


@app.route('/protected_area')
def get_protected_area():
    protected_area = ProtectedArea(real_estate)
    return list(filter(None, list(protected_area.get_all())))


@app.route('/renovation')
def get_renovation():
    renovation = Renovation(real_estate)
    return list(renovation.get_all())


@app.route('/residence_classes')
def get_residence_classes():
    residence_classes = ResidenceClass(real_estate)
    return list(filter(None, list(residence_classes.get_all())))


@app.route('/rooms')
def get_rooms():
    rooms = Room(real_estate)
    return list(rooms.get_all())


@app.route('/walls')
def get_walls():
    walls = Wall(real_estate)
    return list(walls.get_all())


if __name__ == '__main__':
    app.run()
