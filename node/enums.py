from enum import Enum


URL_API_GENERAL_V2 = '/Api/V2/'
URL_CALL_API = '/Api/V1/'


class Api(str, Enum):
    url = 'https://uiscom.s20.online'
    version = 'v2api'


class Branch(str, Enum):
    _id = '1'


class Resource(str, Enum):
    branch = 'branch'
    location = 'location'
    customer = 'customer'
    group = 'group'
    lesson = 'lesson'
    cgi = 'cgi'
    subject = 'subject'
    study_status = 'study_status'
    lead_status = 'lead_status'
    lead_source = 'lead_source'
    pay = 'pay'
    communication = 'communication'
    customer_tariff = 'customer_tariff'
    discount = 'discount'
    log = 'log'
    regular_session = 'regular_session'
    tariff = 'tariff'
    task = 'task'
    teacher = 'teacher'


class Operation(str, Enum):
    _index = 'index'
    create = 'create'
    update = 'update'


class Parameters(str, Enum):
    _id = 'id'
    is_study = 'is_study'
    assigned_id = 'assigned_id'
    company_id = 'company_id'
    name = 'name'
    legal_type = 'legal_type'
    branch_ids = 'branch_ids'
