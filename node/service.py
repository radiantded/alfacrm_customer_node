from sys import exc_info
from typing import Any, Dict, List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Credential, DisplayOptions,
    OptionValue, Property, RunState
)
from uc_http_requester.requester import Request

from node.credential_type import CredentialType
from node.enums import Api, Branch, Operation, Parameters, Resource


class NodeType(flow.NodeType):
    id: str = '002177ac-590c-44c9-bad9-b557934b97e5'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'RadiantAlfaCRM'
    displayName: str = 'RadiantAlfaCRM'
    icon: str = '<svg><text x="0" y="50" font-size="50">👽</text></svg>'
    description: str = 'RadiantAlfaCRM'
    inputs: List[str] = ['main']
    outputs: List[str] = ['main']
    properties: List[Property] = [
        Property(
            displayName='AlfaCRM token',
            name='token',
            type=Property.Type.CODE,
            noDataExpression=True,
        ),
        Property(
            displayName='Branch ID',
            name='branch_id',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Филиал 1',
                    value=Branch._id,
                    description='ID филиала',
                ),
            ]
        ),
        Property(
            displayName='Resource',
            name='resource',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Customer',
                    value=Resource.customer,
                    description='customer',
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'branch_id': [
                        Branch._id,
                    ],
                },
            )
        ),
        Property(
            displayName='Operation',
            name='operation',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Customer list',
                    value=Operation._index,
                    description='Список Customer',
                ),
                OptionValue(
                    name='Create customer',
                    value=Operation.create,
                    description='Создать Customer',
                ),
                OptionValue(
                    name='Update customer',
                    value=Operation.update,
                    description='Обновить Customer',
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resource.customer,
                    ],
                },
            ),
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            displayOptions=DisplayOptions(
                show={
                    'branch_id': [
                        Branch._id,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation._index,
                    ]
                }
            ),
            options=[
                Property(
                    displayName='Customer id',
                    name=Parameters._id,
                    type=Property.Type.NUMBER,
                    description='id клиента',
                ),
                Property(
                    displayName='Customer status',
                    name=Parameters.is_study,
                    type=Property.Type.NUMBER,
                    description='Состояние клиента (0-лид, 1-клиент)',
                ),
                Property(
                    displayName='Assigned id',
                    name=Parameters.assigned_id,
                    type=Property.Type.NUMBER,
                    description='id ответственного менеджера',
                ),
                Property(
                    displayName='Company id',
                    name=Parameters.company_id,
                    type=Property.Type.NUMBER,
                    description='id юр. лица',
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            displayOptions=DisplayOptions(
                show={
                    'branch_id': [
                        Branch._id,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.create,
                    ]
                }
            ),
            options=[
                Property(
                    displayName='Customer name',
                    name=Parameters.name,
                    type=Property.Type.STRING,
                    description='Имя клиента',
                ),
                Property(
                    displayName='Legal type',
                    name=Parameters.legal_type,
                    type=Property.Type.NUMBER,
                    description='Тип клиента (1-физ.л., 2-юр.л.)',
                ),
                Property(
                    displayName='Branch id',
                    name=Parameters.branch_ids,
                    type=Property.Type.NUMBER,
                    description='id филиала',
                ),
                Property(
                    displayName='Customer status',
                    name=Parameters.is_study,
                    type=Property.Type.NUMBER,
                    description='Состояние клиента (0-лид, 1-клиент)',
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            displayOptions=DisplayOptions(
                show={
                    'branch_id': [
                        Branch._id,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.update,
                    ]
                }
            ),
            options=[
                Property(
                    displayName='Customer id',
                    name=Parameters._id,
                    type=Property.Type.NUMBER,
                    description='id клиента',
                ),
                Property(
                    displayName='Customer name',
                    name=Parameters.name,
                    type=Property.Type.STRING,
                    description='Имя клиента',
                ),
                Property(
                    displayName='Legal type',
                    name=Parameters.legal_type,
                    type=Property.Type.NUMBER,
                    description='Тип клиента (1-физ.л., 2-юр.л.)',
                ),
                Property(
                    displayName='Branch id',
                    name=Parameters.branch_ids,
                    type=Property.Type.NUMBER,
                    description='id филиала',
                ),
                Property(
                    displayName='Customer status',
                    name=Parameters.is_study,
                    type=Property.Type.NUMBER,
                    description='Состояние клиента (0-лид, 1-клиент)',
                ),
            ],
        ),
    ]
    credentials: List[flow.NodeType.Credential] = [
        flow.NodeType.Credential(name="alfacrm_api_auth", required=True)
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType
        credential_types: Tuple[CredentialType] = (CredentialType(),)


class ExecuteView(execute.Execute):
    async def modify_params(self, parameters: Dict[str, Any]):
        result = {}
        try:
            for param in parameters:
                if parameters[param]:
                    result[param] = parameters[param][0][param]
        except TypeError:
            pass
        return result
    
    async def make_api_request(
        self,
        properties: Dict[str, Any],
        parameters: Dict[str, Any]
    ):
        url = (
            f"{Api.url}/"
            f"{Api.version}/"
            f"{properties.get('branch_id')}/"
            f"{properties.get('resource')}/"
            f"{properties.get('operation')}"
        )
        if properties.get('operation') == 'update':
            url += f"?id={parameters.get('id')}"
        headers = {'X-ALFACRM-TOKEN': properties['token']['token']}
        request = Request(
            url=url,
            method=Request.Method.post,
            headers=headers,
            json=parameters
        )
        return request

    async def make_auth_request(self, credentials: Credential):
        parameters = {
            "email": credentials.data['email'],
            "api_key": credentials.data['api_key']
        }
        hostname = credentials.data['hostname']
        url = f'https://{hostname}/v2api/auth/login'
        request = Request(
            url=url,
            method=Request.Method.post,
            json=parameters
        )
        return request

    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            try:
                credentials = await json.get_credentials()
            except RuntimeError:
                properties = json.node.data.properties
                parameters = await self.modify_params(
                    properties.get('parameters')
                )
                request = await self.make_api_request(
                    json.node.data.properties,
                    parameters
                )
                result = await request.execute()
                await json.save_result(
                    result.json()
                )
            else:
                request = await self.make_auth_request(credentials)
                
                result = await request.execute()
                await json.save_result(
                    result.json()
                )
            json.state = RunState.complete
        except Exception as e:
            exc_type, exc_obj, tb = exc_info()
            self.log.warning(exc_type, exc_obj, tb.tb_lineno)
            await json.save_error(str(e))
            json.state = RunState.error
        return json


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
