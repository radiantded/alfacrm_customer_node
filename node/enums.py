from enum import Enum

URL_API_GENERAL_V2 = '/Api/V2/'
URL_CALL_API = '/Api/V1/'


class Api(str, Enum):
    api_general_v2 = 'api_general_v2'
    call_api_v1 = 'call_api_v1'


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
    get_offices = 'get_offices'
    get_lead_statuses = 'get_lead_statuses'
    get_leads = 'get_leads'
    get_history_modify_lead_status = 'get_history_modify_lead_status'
    get_students = 'get_students'
    on_ringing = 'on_ringing'
    on_answer = 'on_answer'


class Method(str, Enum):
    on_ringing = 'on_ringing'
    on_answer = 'on_answer'
    on_hangup = 'on_hangup'


class Path(str, Enum):
    default = ''
    get_offices = 'GetOffices'
    get_lead_statuses = 'GetLeadStatuses'
    get_leads = 'GetLeads'
    get_history_modify_lead_status = 'GetHistoryModifyLeadStatus'
    get_students = 'GetStudents'
    on_ringing = 'OnRinging'
    on_answer = 'OnAnswer'
    on_hangup = 'OnHangup'


class Parameters(str, Enum):
    office_id = 'office_id'
    office_location_id = 'office_location_id'
    office_name = 'office_name'
    office_license = 'office_license'
    lead_id = 'lead_id'
    lead_name = 'lead_name'
    lead_type = 'lead_type'
    lead_office_or_company_id = 'lead_office_or_company_id'
    lead_term = 'lead_term'
    lead_by_agents = 'lead_by_agents'
    lead_attached = 'lead_attached'
    lead_student_client_id = 'lead_student_client_id'
    lead_address_date_from = 'lead_address_date_from'
    lead_address_date_to = 'lead_address_date_to'
    lead_extra_field_name = 'lead_extra_field_name'
    lead_extra_field_value = 'lead_extra_field_value'
    lead_created_from = 'lead_created_from'
    lead_created_to = 'lead_created_to'
    lead_last_updated_from = 'lead_last_updated_from'
    lead_descending = 'lead_descending'
    lead_skip = 'lead_skip'
    lead_take = 'lead_take'
    lead_date_time_from = 'lead_date_time_from'
    lead_date_time_to = 'lead_date_time_to'
    lead_lead_id = 'lead_lead_id'
    student_client_id = 'student_client_id'
    student_id = 'student_id'
    student_office_or_company_id = 'student_office_or_company_id'
    student_term = 'student_term'
    student_by_agents = 'student_by_agents'
    student_address_date_from = 'student_address_date_from'
    student_address_date_to = 'student_address_date_to'
    student_statuses = 'student_statuses'
    student_extra_field_name = 'student_extra_field_name'
    student_extra_field_value = 'student_extra_field_value'
    student_query_study_requests = 'student_query_study_requests'
    student_descending = 'student_descending'
    student_skip = 'student_skip'
    student_take = 'student_take'
    on_ringing_call_id = 'on_ringing_call_id'
    on_ringing_from = 'on_ringing_from'
    on_ringing_to = 'on_ringing_to'
    on_ringing_trunk_number = 'on_ringing_trunk_number'
    on_ringing_continuable_call_ids = 'on_ringing_continuable_call_ids'
    on_ringing_utm = 'on_ringing_utm'
    on_answer_call_id = 'on_answer_call_id'
    on_hangup_call_id = 'on_hangup_call_id'
    on_hangup_cause = 'on_hangup_cause'
    on_hangup_audio_url = 'on_hangup_audio_url'
    on_hangup_continuing_call_ids = 'on_hangup_continuing_call_ids'
